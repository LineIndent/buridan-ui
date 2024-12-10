import reflex as rx

from buridan_ui.pages.landing.style import LandingPageStyle
from buridan_ui.pantry.logins.v1 import LoginStyle
from buridan_ui.templates.navigation.navigation import landing_page_navigation

from .components.editor import ace_editor
from .scripts import callback, dynamics
from .state import Editor


@rx.dynamic
def rendered_component(state: Editor):
    # Create a dictionary to capture the context (globals) where the code is executed
    context = {
        "rx": rx,
        "LoginStyle": LoginStyle,
    }

    try:
        # Execute the code in the given context
        exec(state.code, context)

        # Check for a defined component in the context, either directly or from a function call
        component = None

        # Look for any variable in the context that is a valid component
        for _name, value in context.items():
            if isinstance(value, rx.Component):
                component = value
                break

        # If no component found, check if there's any function to call (e.g., first function in context)
        if component is None:
            for _name, value in context.items():
                if callable(value):  # If it's callable (a function)
                    component = value()  # Call the function and return its result
                    break

    except Exception as e:
        # If there's an error executing the code, return an error message
        return rx.text(f"Error: {e}")

    # Check if 'component' is a valid rx.Component
    if not isinstance(component, rx.Component):
        return rx.text("Invalid component")

    return component


def buridan_sandbox():
    return rx.vstack(
        rx.script(callback),
        rx.script(dynamics),
        rx.vstack(
            landing_page_navigation(),
            rx.hstack(
                rx.select(
                    ["Login V1", "Login V2"],
                    placeholder="Select Component",
                    on_change=Editor.handle_selection,
                    size="1",
                ),
                width="100%",
                justify="end",
            ),
            rx.hstack(
                ace_editor(),
                rx.vstack(
                    rendered_component(),
                    height="100%",
                    align="center",
                    justify="center",
                    flex=["100%" if i <= 3 else "30%" for i in range(6)],
                ),
                width="100%",
                height="100%",
                wrap="wrap",
                align="center",
            ),
            **LandingPageStyle.content,
        ),
        **LandingPageStyle.base,
    )
