import reflex as rx

from typing import Callable, List
from functools import wraps

ROOT = dict(
    width="100%",
    padding="10px",
    overflow="hidden",
    default_value="1",
)

SHARED = dict(
    margin_top="24px",
    border_radius="8px",
    display="flex",
    background=rx.color("gray", 2),
)

PREVIEW = dict(
    transition="all 550ms ease",
    padding="24px 12px",
    align_items="center",
    justify_content="center",
    overflow="hidden",
    **SHARED,
)

CODE = dict(
    width="100%",
    theme="vs-dark",
    font_size="12px",
    language="python",
    wrap_long_lines=True,
    scrollbar_width="none",
    code_tag_props={"pre": "transparent"},
    custom_style={"background_color": "transparent"},
)

INNER_CODE = dict(**SHARED, align_items="start")


def create_wrapper_tab(name: str, value: str):
    return rx.tabs.trigger(
        rx.text(name), value=value, cursor="pointer", color=rx.color("slate", 12)
    )


def create_tabs_list():
    return rx.tabs.list(
        create_wrapper_tab("Preview", "1"),
        create_wrapper_tab("Code", "2"),
        justify_content="start",
        align_items="center",
        gap="12px",
    )


def resize_menu(component_id: int):
    size_name = ["Mobile", "Small", "Medium", "Large", "Full Width"]
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon(tag="proportions", size=18, color=rx.color("slate", 12)),
                size="1",
                color=rx.color("slate", 12),
                width="32px",
                height="32px",
                outline="none",
                cursor="pointer",
                variant="soft",
                color_scheme="gray",
            )
        ),
        rx.menu.content(
            *[
                rx.menu.item(
                    rx.text(
                        size_name[i],
                        on_click=Item.resize(component_id, size),
                        cursor="pointer",
                    )
                )
                for i, size in enumerate(["30%", "40%", "60%", "80%", "100%"])
            ],
            size="1",
            side="left",
            width="100px",
        ),
    )


def view_source_code(path: str):
    return rx.button(
        rx.link(
            rx.icon(tag="github", size=18, color=rx.color("slate", 12)),
            href=path,
            is_external=True,
        ),
        size="1",
        color=rx.color("slate", 12),
        width="32px",
        height="32px",
        outline="none",
        cursor="pointer",
        variant="soft",
        color_scheme="gray",
    )


class Item(rx.State):
    uuid: dict[int, str]

    def resize(self, uuid: int, size: str):
        self.uuid[uuid] = size


def item(path):
    def decorator(func: Callable[[], List[rx.Component]]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            components = func(*args, **kwargs)
            return rx.vstack(
                rx.tabs.root(
                    rx.hstack(
                        create_tabs_list(),
                        rx.hstack(
                            view_source_code(path),
                            rx.box(
                                resize_menu(components[2]),
                                display=[
                                    "none" if i <= 3 else "flex" for i in range(6)
                                ],
                            ),
                            spacing="2",
                            align="center",
                        ),
                        align="center",
                        justify="between",
                        width="100%",
                    ),
                    rx.tabs.content(
                        rx.vstack(
                            components[0],
                            width=[
                                "100%" if i <= 4 else Item.uuid[components[2]]
                                for i in range(6)
                            ],
                            **PREVIEW,
                        ),
                        background_size="24px 24px",
                        background_image="radial-gradient(circle, hsl(0, 0%, 30%) 1px, transparent 1px)",
                        value="1",
                    ),
                    rx.tabs.content(
                        rx.hstack(
                            rx.code_block(components[1], **CODE),
                            # copy_button(ui),
                            padding_right="12px",
                            padding_top="12px",
                            width="100%",
                            **INNER_CODE,
                        ),
                        value="2",
                    ),
                    **ROOT,
                ),
                width="100%",
                padding="12px 22px",
            )

        return wrapper

    return decorator
