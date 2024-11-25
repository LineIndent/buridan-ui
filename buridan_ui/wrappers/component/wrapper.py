import reflex as rx

from typing import Callable, List
from functools import wraps

from reflex.components.datadisplay.code import Theme

from buridan_ui.wrappers.state import ComponentWrapperState
from .style import ComponentWrapperStyle, InnerCode

from buridan_ui.wrappers.shared.tabs import component_wrapper_tab_menu
from buridan_ui.wrappers.shared.responsive import component_wrapper_responsive_menu
from buridan_ui.wrappers.shared.source import component_wrapper_source_code
from buridan_ui.wrappers.shared.scheme import component_wrapper_color_scheme


def component_wrapper_menu_bar(has_theme: bool, component_id: int, path: str):
    return rx.hstack(
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
        justify="end",
        width="100%",
    )


def component_wrapper_menu_bar_no_code(path: str):
    return rx.hstack(
        rx.badge("Responsive UI", size="1", variant="surface"),
        component_wrapper_source_code(path),
        align="center",
        justify="end",
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


def component_wrapper(path: str, has_theme: bool = False):
    def decorator(func: Callable[[], List[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, component_code, component_id = func()

            return rx.vstack(
                component_wrapper_menu_bar(has_theme, component_id, path),
                rx.tabs.root(
                    component_wrapper_tab_menu(),
                    component_wrapper_preview_content(component, component_id),
                    component_wrapper_code_base(component_code),
                    **ComponentWrapperStyle.root,
                ),
                width="100%",
            )

        return wrapper

    return decorator
