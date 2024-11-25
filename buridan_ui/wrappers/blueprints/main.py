import reflex as rx
from functools import wraps
from typing import Callable, List

from .style import BlueprintWrapperStyle

from ..shared.source import component_wrapper_source_code

blueprintAppWrapperMenu: Callable[[str], rx.Component] = lambda path: rx.hstack(
    rx.badge("Responsive UI", size="1", variant="surface"),
    component_wrapper_source_code(path),
    align="center",
    justify="end",
    width="100%",
)

blueprintAppPreview: Callable[[rx.Component], rx.Component] = (
    lambda component: rx.tabs.content(
        rx.vstack(component, **BlueprintWrapperStyle.preview),
        value="1",
    )
)


blueprintAppCode: Callable[[dict], rx.Component] = lambda struct: rx.tabs.content(
    value="2",
)


def blueprint_app_wrapper(url: str):
    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component = func()
            if not isinstance(component, List):
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
