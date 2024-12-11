from __future__ import annotations

from functools import wraps
from typing import Callable

import reflex as rx

from buridan_ui.wrappers.shared.source import component_wrapper_source_code

from .style import BlueprintWrapperStyle


def blueprintAppWrapperMenu(path: str) -> rx.Component:
    return rx.hstack(
        rx.badge("Responsive UI", size="1", variant="surface"),
        component_wrapper_source_code(path),
        align="center",
        justify="end",
        width="100%",
    )


def blueprintAppPreview(component: rx.Component) -> rx.Component:
    return rx.tabs.content(
        rx.vstack(component, **BlueprintWrapperStyle.preview),
        value="1",
    )


def blueprintAppCode(struct: dict) -> rx.Component:
    return rx.tabs.content(value="2")


def blueprint_app_wrapper(url: str):
    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component = func()
            if not isinstance(component, list):
                raise TypeError("The wrapped blueprint item is not a list.")

            return rx.vstack(
                blueprintAppWrapperMenu(url),
                rx.tabs.root(
                    blueprintAppPreview(component[0]),
                    **BlueprintWrapperStyle.root,
                ),
                width="100%",
            )

        return wrapper

    return decorator
