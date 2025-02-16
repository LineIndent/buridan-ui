from __future__ import annotations

from functools import wraps
from typing import Callable

import reflex as rx
from reflex.components.datadisplay.code import Theme

from buridan_ui.wrappers.shared.responsive import component_wrapper_responsive_menu
from buridan_ui.wrappers.shared.scheme import component_wrapper_color_scheme
from buridan_ui.wrappers.shared.source import component_wrapper_source_code
from buridan_ui.wrappers.shared.tabs import component_wrapper_tab_menu
from buridan_ui.wrappers.state import ComponentWrapperState

from .style import ComponentWrapperStyle, InnerCode
from .view_code import view_code
from ...pages.landing.hero_grid_layout import create_grid_item


def component_wrapper_menu_bar(has_theme: bool, component_id: int, path: str, lab):
    return rx.hstack(
        lab,
        rx.hstack(
            (component_wrapper_color_scheme() if has_theme else rx.spacer()),
            (
                rx.divider(
                    width="0.75px",
                    height="25px",
                    orientation="vertical",
                    display=["none" if i <= 1 else "flex" for i in range(6)],
                )
                if has_theme
                else rx.spacer()
            ),
            component_wrapper_responsive_menu(component_id),
            rx.divider(
                width="0.75px",
                height="25px",
                orientation="vertical",
                display=["none" if i <= 3 else "flex" for i in range(6)],
            ),
            component_wrapper_source_code(path),
            align="center",
        ),
        align="center",
        justify="between",
        width="100%",
    )


def component_wrapper_preview_content(component: rx.Component, component_id: int):
    return rx.tabs.content(
        rx.vstack(
            component,
            width=[
                ("100%" if i <= 3 else ComponentWrapperState.uuid[component_id])
                for i in range(6)
            ],
            **ComponentWrapperStyle.preview,
        ),
        value="1",
    )


def component_wrapper_code_base(
    component_code: str,
    value: str = "2",
) -> rx.tabs.content:
    return rx.tabs.content(
        rx.hstack(
            rx.code_block(
                component_code,
                theme=Theme.darcula,
                **ComponentWrapperStyle.code,
            ),
            rx.button(
                rx.cond(
                    ComponentWrapperState.default_icon,
                    rx.icon(tag="clipboard-list", size=14),
                    rx.icon(tag="check", size=14, color=rx.color("grass")),
                ),
                on_click=[
                    ComponentWrapperState.toggle_icon,
                    rx.set_clipboard(component_code),
                ],
                **ComponentWrapperStyle.copy_button,
            ),
            **InnerCode,
        ),
        value=value,
    )


def chart_wrapper(path: str):
    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, component_code, chart_icon = func()

            return rx.box(
                rx.box(
                    rx.box(
                        rx.icon(
                            tag=chart_icon,
                            size=15,
                        ),
                        rx.el.span("Chart UI", class_name="text-sm font-bold"),
                        class_name="flex align-center gap-2 py-1",
                    ),
                    rx.box(
                        rx.box(
                            rx.icon(
                                tag="clipboard",
                                size=13,
                                color=rx.color("slate", 11),
                                _hover={"color": rx.color("slate", 12)},
                            ),
                            on_click=[
                                rx.set_clipboard(component_code),
                                rx.toast(
                                    "Copied to clipboard!",
                                    position="top-center",
                                ),
                            ],
                            _hover={"background": rx.color("gray", 3)},
                            border=f"1px solid {rx.color('gray', 5)}",
                            class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
                        ),
                        view_code(component, component_code),
                        rx.box(
                            rx.link(
                                rx.icon(
                                    tag="github",
                                    size=13,
                                ),
                                href=path,
                                is_external=True,
                                text_cdecoration="none",
                                color=rx.color("slate", 11),
                                _hover={"color": rx.color("slate", 12)},
                            ),
                            _hover={"background": rx.color("gray", 3)},
                            border=f"1px solid {rx.color('gray', 5)}",
                            class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
                        ),
                        class_name="flex align-center gap-2",
                    ),
                    border_bottom=f"1px solid {rx.color('gray', 5)}",
                    class_name="px-4 py-3 w-full flex align-center justify-between shadow-sm",
                ),
                rx.box(
                    component,
                    class_name=f"p-4 rounded-xl h-full",
                ),
                border=f"1px solid {rx.color('gray', 5)}",
                class_name=f"rounded-xl shadow-md h-full w-full",
            )

            # return rx.vstack(
            #     component_wrapper_menu_bar(has_theme, component_id, path, lab),
            #     rx.tabs.root(
            #         component_wrapper_tab_menu(),
            #         component_wrapper_preview_content(component, component_id),
            #         component_wrapper_code_base(component_code),
            #         **ComponentWrapperStyle.root,
            #     ),
            #     width="100%",
            # )

        return wrapper

    return decorator


def component_wrapper(path: str):
    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            lab = rx.spacer()
            component, component_code = func()

            return rx.box(
                rx.box(
                    rx.box(
                        rx.icon(
                            tag="component",
                            size=15,
                        ),
                        rx.el.span("Pantry UI", class_name="text-sm font-bold"),
                        class_name="flex align-center gap-2 py-1",
                    ),
                    rx.box(
                        rx.box(
                            rx.icon(
                                tag="clipboard",
                                size=13,
                                color=rx.color("slate", 11),
                                _hover={"color": rx.color("slate", 12)},
                            ),
                            _hover={"background": rx.color("gray", 3)},
                            border=f"1px solid {rx.color('gray', 5)}",
                            class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
                            on_click=[
                                rx.set_clipboard(component_code),
                                rx.toast(
                                    "Copied to clipboard!",
                                    position="top-center",
                                ),
                            ],
                        ),
                        view_code(component, component_code),
                        rx.box(
                            rx.link(
                                rx.icon(
                                    tag="github",
                                    size=13,
                                ),
                                href=path,
                                is_external=True,
                                text_cdecoration="none",
                                color=rx.color("slate", 11),
                                _hover={"color": rx.color("slate", 12)},
                            ),
                            _hover={"background": rx.color("gray", 3)},
                            border=f"1px solid {rx.color('gray', 5)}",
                            class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
                        ),
                        class_name="flex align-center gap-2",
                    ),
                    border_bottom=f"1px solid {rx.color('gray', 5)}",
                    class_name="px-4 py-3 w-full flex align-center justify-between shadow-sm",
                ),
                rx.box(
                    component,
                    class_name="rounded-xl h-full w-full flex align-center justify-center items-center py-6 px-4",
                ),
                border=f"1px solid {rx.color('gray', 5)}",
                class_name=f"rounded-xl shadow-md size-full flex flex-col",
            )

        return wrapper

    return decorator


#
