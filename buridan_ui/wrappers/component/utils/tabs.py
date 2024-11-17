import reflex as rx


def tab_menu_wrapper(name: str, value: str):
    return rx.tabs.trigger(
        rx.text(name),
        value=value,
        cursor="pointer",
        color=rx.color("slate", 12),
        flex="1",
    )


def component_wrapper_tab_menu() -> rx.tabs.list:
    return rx.tabs.list(
        tab_menu_wrapper("Preview", "1"),
        tab_menu_wrapper("Code", "2"),
        justify_content="start",
        align_items="center",
        width=["100%", "100%", "25%", "25%", "15%", "15%"],
    )
