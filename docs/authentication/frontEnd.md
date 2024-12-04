
### Frontend Components

In this section, we define key frontend components that will be used to build the authentication UI.

#### Text Display

We define `lambda` functions to set the **title** and **subtitle** of both the `Create` and `Login` UI components.

```python
authTitle: Callable[[str], rx.text] = lambda name: rx.text(
    name, size="5", weight="bold", color=rx.color("slate", 12)
)

authSubtitle: Callable[[str], rx.text] = lambda name: rx.text(
    name, size="2", weight="regular", color=rx.color("slate", 11)
)
```

We create another component that allows inter-page navigation, that is, linkage between the ``create`` and `Login` pages of the app.

```python
authInterPageLinking: Callable[[str, str, str, str], rx.text] = (
    lambda start, link, path, end: rx.text(
        start,
        rx.link(f"{link}", href=path),
        end,
        size="1",
        max_width="18em",
        z_index="4",
    )
)
```

An alert text is displayed to inform the user that the account number should be stored securely.

```python
authAlertText: Callable[[], rx.text] = lambda: rx.hstack(
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
```

`authAlertText` This text component informs the user to copy and securely store the generated account number. It is styled with a red (ruby) color scheme and custom transitions for appearance changes.


#### Buttons

We define buttons that will interact with state variables, triggering the action of generating an account number, with loading and disabled states controlled by the `SandboxAuthState`.

```python
authLoginButton: Callable[[str], rx.button] = lambda name: rx.button(
    name,
    width="100%",
    size="2",
    variant="surface",
    cursor="pointer",
    padding="1.5em",
)

authNumberButton: Callable[[str], rx.button] = lambda name: rx.button(
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
```

#### Input Field

An input field is created for users to enter their account number during the login phase.

```python
authLoginEntry: Callable[[], rx.button] = lambda: rx.input(
    width="100%",
    variant="surface",
    height="3em",
    text_align="center",
    font_size="18px",
)
```
`authLoginEntry`: This input field is used for the user to enter their account number. It’s styled with a surface variant, and the text is centered.

#### Account Number Display

The account number is displayed in groups, and each group is clickable for copying. The `createAuthAccountNumber` function helps create these groups.

```python
createAuthAccountNumber: Callable[[list[str]], rx.hstack] = (
    lambda numberList: rx.hstack(
        *[
            rx.text(getattr(SandboxAuthState, number), size="5")
            for number in numberList
        ],
        spacing="1",
        align="center",
    )
)

authAccountNumber: Callable[[], rx.hstack] = lambda: rx.hstack(
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
```

`createAuthAccountNumber` Displays a part of the account number using a horizontal stack (hstack). Each number is rendered as a separate text element.

`authAccountNumber` Displays the full account number in groups, styled with padding, hover effects, and a click action that triggers the copy functionality.

#### UI Layouts 

Now that we have our core components, we can assemble them into the layout for the authentication UI. This includes both the "Create Account" and "Login" sections.

The **Create Account UI** is assembled using the various components, including titles, subtitles, a button for generating account numbers, the account number display, and alert text.

```python
sandboxAuthCreateAccount: Callable[[], rx.center] = lambda: rx.center(
    rx.box(
        *[top, bottom, left, right],
        rx.vstack(
            authTitle("Create Account"),
            authSubtitle("Click the button below to generate a unique account number."),
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
```

`sandboxAuthCreateAccount` The layout for creating a new account, which combines the title, subtitle, button, account number, and alert text into a vertically stacked layout (vstack). This layout also includes inter-page linking to switch to the login page.

Next, the **Account Login UI** allows users to input their account number to log in.

```python
sandboxAuthAccountLogin: Callable[[], rx.center] = lambda: rx.center(
    rx.box(
        *[top, bottom, left, right],
        rx.vstack(
            authTitle("Account Login"),
            authSubtitle(
                "Enter your account number below to access your account dashboards."
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
```