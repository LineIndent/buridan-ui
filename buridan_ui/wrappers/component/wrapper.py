import reflex as rx

from typing import Callable, List
from functools import wraps

from reflex.components.datadisplay.code import Theme

from .state import ComponentWrapperState
from .style import ComponentWrapperStyle, InnerCode

from .utils.tabs import (
    component_wrapper_tab_menu,
    component_wrapper_tab_menu_blueprints,
)
from .utils.responsive import component_wrapper_responsive_menu
from .utils.source import component_wrapper_source_code
from .utils.scheme import component_wrapper_color_scheme


def component_wrapper_menu_bar(has_theme: bool, component_id: int, path: str):
    return rx.hstack(
        component_wrapper_tab_menu(),
        rx.hstack(
            (component_wrapper_color_scheme() if has_theme else rx.spacer()),
            component_wrapper_responsive_menu(component_id),
            component_wrapper_source_code(path),
            spacing="0",
            align="center",
        ),
        align="center",
        justify="between",
        width="100%",
        padding="0.5em",
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


def component_wrapper_code_content(component_code: str):
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
        value="2",
    )


def component_wrapper(path: str, has_theme: bool = False):
    def decorator(func: Callable[[], List[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, component_code, component_id = func()

            return rx.vstack(
                rx.tabs.root(
                    component_wrapper_menu_bar(has_theme, component_id, path),
                    component_wrapper_preview_content(component, component_id),
                    component_wrapper_code_base(component_code),
                    **ComponentWrapperStyle.root,
                ),
                width="100%",
            )

        return wrapper

    return decorator


blueprintFrontEndContent: Callable[[str], rx.tabs.content] = (
    lambda code: component_wrapper_code_base(code, value="2")
)

blueprintStyleContent: Callable[[str], rx.tabs.content] = (
    lambda code: component_wrapper_code_base(code, value="3")
)

blueprintStateContent: Callable[[str], rx.tabs.content] = (
    lambda code: component_wrapper_code_base(code, value="4")
)


def blueprint_wrapper():
    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, preview, style, state, _ = func()

            return rx.vstack(
                rx.tabs.root(
                    component_wrapper_tab_menu_blueprints(),
                    component_wrapper_preview_content(component, 0),
                    component_wrapper_code_base(preview, "2"),
                    component_wrapper_code_base(style, "3"),
                    component_wrapper_code_base(state, "4"),
                    **ComponentWrapperStyle.root,
                ),
                width="100%",
            )

        return wrapper

    return decorator
