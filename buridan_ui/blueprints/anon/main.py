import reflex as rx

from .components.borders import createAuthBorders
from .state import SandboxAuthState, numberList
from .style import SandboxAuthStyle


def authTitle(name: str) -> rx.text:
    return rx.text(name, size="5", weight="bold", color=rx.color("slate", 12))


def authSubtitle(name: str) -> rx.text:
    return rx.text(name, size="2", weight="regular", color=rx.color("slate", 11))


def authNumberButton(name: str) -> rx.button:
    return rx.button(
        name,
        width="100%",
        size="2",
        variant="surface",
        cursor="pointer",
        padding="1.5em",
        loading=SandboxAuthState.authGenButton["loading"],
        disabled=SandboxAuthState.authGenButton["disabled"],
        on_click=SandboxAuthState.run_animation_task,
    )


def authLoginButton(name: str) -> rx.button:
    return rx.button(
        name,
        width="100%",
        size="2",
        variant="surface",
        cursor="pointer",
        padding="1.5em",
    )


def authLoginEntry() -> rx.button:
    return rx.input(
        width="100%",
        variant="surface",
        height="3em",
        text_align="center",
        font_size="18px",
    )


def authInterPageLinking(start: str, link: str, path: str, end: str) -> rx.text:
    return rx.text(
        start,
        rx.link(f"{link}", href=path),
        end,
        size="1",
        max_width="18em",
        z_index="4",
    )


def createAuthAccountNumber(numberList: list[str]) -> rx.hstack:
    return rx.hstack(
        *[
            rx.text(getattr(SandboxAuthState, number), size="5")
            for number in numberList
        ],
        spacing="1",
        align="center",
    )


def authAccountNumber() -> rx.hstack:
    return rx.hstack(
        createAuthAccountNumber(numberList[:4]),
        createAuthAccountNumber(numberList[4:8]),
        createAuthAccountNumber(numberList[8:12]),
        createAuthAccountNumber(numberList[12:16]),
        spacing="5",
        padding="0.35em",
        align="center",
        border_radius="8px",
        _hover={"bg": rx.color("gray", 3), "cursor": "pointer"},
        on_click=SandboxAuthState.can_copy_account_number,
    )


def authAlertText() -> rx.text:
    return rx.hstack(
        rx.text(
            "Copy the ",
            rx.text.strong("account number"),
            " above and store it in a safe place. It's the ",
            rx.text.strong("ONLY"),
            " identifier you have to access our services.",
            size="1",
            color_scheme="ruby",
        ),
        background=rx.color("ruby", 3),
        border=f"1.5px solid {rx.color('ruby')}",
        padding="0.5em",
        transition="filter 300ms ease 200ms, transform 300ms ease 200ms, opacity 300ms ease 200ms",
        height=SandboxAuthState.authAlert["height"],
        filter=SandboxAuthState.authAlert["filter"],
        transform=SandboxAuthState.authAlert["transform"],
        opacity=SandboxAuthState.authAlert["opacity"],
    )


top = createAuthBorders("top", "left")
bottom = createAuthBorders("bottom", "left")
left = createAuthBorders("left", "bottom")
right = createAuthBorders("right", "bottom")


def sandboxAuthCreateAccount() -> rx.center:
    return rx.center(
        rx.box(
            *[top, bottom, left, right],
            rx.vstack(
                authTitle("Create Account"),
                authSubtitle(
                    "Click the button below to generate a unique account number.",
                ),
                rx.divider(height="0.5em", opacity="0"),
                authNumberButton("Generate Account Number"),
                rx.divider(height="0.5em", opacity="0"),
                authAccountNumber(),
                rx.divider(height="0.5em", opacity="0"),
                authAlertText(),
                rx.divider(height="0.5em", opacity="0"),
                authInterPageLinking(
                    "Already have an account number? Click ",
                    "here",
                    "#",
                    " to get started.",
                ),
                **SandboxAuthStyle.content,
            ),
            position="relative",
        ),
        **SandboxAuthStyle.base,
    )


def sandboxAuthAccountLogin() -> rx.center:
    return rx.center(
        rx.box(
            *[top, bottom, left, right],
            rx.vstack(
                authTitle("Account Login"),
                authSubtitle(
                    "Enter your account number below to access your account dashboards.",
                ),
                rx.divider(height="0.5em", opacity="0"),
                authLoginEntry(),
                rx.divider(height="0.5em", opacity="0"),
                authLoginButton("Account Login"),
                rx.divider(height="0.5em", opacity="0"),
                authInterPageLinking(
                    "Looking for your account number? Click ",
                    "here",
                    "#",
                    " to get one.",
                ),
                **SandboxAuthStyle.content,
            ),
            position="relative",
        ),
        **SandboxAuthStyle.base,
    )


def sandboxAuth() -> rx.vstack:
    return rx.vstack(
        sandboxAuthCreateAccount(),
        sandboxAuthAccountLogin(),
        width="100%",
        align="center",
    )
