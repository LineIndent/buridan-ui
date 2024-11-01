import asyncio

import reflex as rx

from typing import Callable, List
from functools import wraps

from reflex.components.datadisplay.code import Theme
from reflex.constants.colors import Color

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
    font_size="12px",
    language="markup",
    wrap_long_lines=True,
    scrollbar_width="none",
    code_tag_props={"pre": "transparent"},
    custom_style={
        "backgroundColor": "transparent",
        "color": rx.color("gray", 12),
    },
)

INNER_CODE = dict(**SHARED, align_items="start", position="relative")


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
                rx.icon(tag="proportions", size=18, color=rx.color("slate", 11)),
                size="1",
                color=rx.color("slate", 11),
                width="32px",
                height="32px",
                outline="none",
                cursor="pointer",
                variant="soft",
                color_scheme="gray",
                border_radius="0px 10px 10px 0px",
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
            rx.icon(tag="github", size=18, color=rx.color("slate", 11)),
            href=path,
            is_external=True,
        ),
        size="1",
        color=rx.color("slate", 11),
        width="32px",
        height="32px",
        outline="none",
        cursor="pointer",
        variant="soft",
        color_scheme="gray",
        border_radius=[
            "10px",
            "10px",
            "10px",
            "10px",
            "10px 0px 0px 10px",
            "10px 0px 0px 10px",
        ],
        display=["none" if i <= 1 else "flex" for i in range(6)],
    )


def create_color_box(color: str, name: str = "test"):
    common_box_props = {
        "width": "15px",
        "height": "15px",
    }

    name_map = {
        "blue": "Fayrouz فَيْرُوز",
        "ruby": "Yaqout يَاقُوت",
        "jade": "Zumurud زُمُرُّد",
        "gray": "Hematite هَيْمَاتِيت",
    }

    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 5),
                        border_radius="7.5px 0 0 0",
                    ),
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 6),
                        border_radius="0 7.5px 0 0",
                    ),
                    spacing="0",
                ),
                rx.hstack(
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 7),
                        border_radius="0 0 0 7.5px",
                    ),
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 8),
                        border_radius="0 0 7.5px 0",
                    ),
                    spacing="0",
                ),
                spacing="0",
                padding="2.5px",
                width="32px",
                height="32px",
                cursor="pointer",
                opacity="0.71",
                _hover={
                    "opacity": "1",
                    "filter": rx.color_mode_cond(
                        "brightness(0.95)", "brightness(1.25)"
                    ),
                },
                on_click=lambda: Item.toggle_theme(color),
            )
        ),
        rx.hover_card.content(
            rx.text(
                f"{name_map[color]}",
                size="1",
                color=rx.color("slate", 12),
                weight="bold",
            ),
            padding="10px",
            border_radius="6px",
        ),
    )


def toggle_chart_theme():
    return rx.hstack(
        *[create_color_box(color) for color in ["blue", "ruby", "jade", "gray"]],
        spacing="1",
        align="center",
        padding=["0px 0px" if i <= 1 else "0px 24px" for i in range(6)],
    )


start: int = 8
color_map = {
    "blue": {i: rx.color("blue", i + start) for i in range(4)},
    "ruby": {i: rx.color("ruby", i + start) for i in range(4)},
    "jade": {i: rx.color("jade", i + start) for i in range(4)},
    "gray": {i: rx.color("gray", i + start) for i in range(4)},
}


class Item(rx.State):
    uuid: dict[int, str]

    default_icon: bool = True

    default_theme: dict[int, Color] = color_map["blue"]
    selected_theme: str = "blue"

    async def toggle_theme(self, color: str):
        self.selected_theme = color
        self.default_theme = color_map[color]

    async def toggle_icon(self):
        self.default_icon = False
        yield
        await asyncio.sleep(1)
        self.default_icon = True

    def resize(self, uuid: int, size: str):
        self.uuid[uuid] = size


def item(path: str, has_theme: bool = False):
    def decorator(func: Callable[[], List[rx.Component]]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            components = func(*args, **kwargs)
            return rx.vstack(
                rx.tabs.root(
                    rx.hstack(
                        create_tabs_list(),
                        rx.hstack(
                            toggle_chart_theme() if has_theme else rx.spacer(),
                            view_source_code(path),
                            rx.box(
                                resize_menu(components[2]),
                                display=[
                                    "none" if i <= 3 else "flex" for i in range(6)
                                ],
                                border_radius="0px 10px 10px 0px",
                            ),
                            spacing="0",
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
                            rx.code_block(
                                components[1],
                                theme=Theme.vs_dark,
                                **CODE,
                            ),
                            rx.button(
                                rx.cond(
                                    Item.default_icon,
                                    rx.icon(tag="clipboard-list", size=15),
                                    rx.icon(
                                        tag="check", size=15, color=rx.color("grass")
                                    ),
                                ),
                                color_scheme="gray",
                                variant="ghost",
                                size="1",
                                on_click=[
                                    Item.toggle_icon,
                                    rx.set_clipboard(components[1]),
                                ],
                                cursor="pointer",
                                position="absolute",
                                top="24px",
                                right="24px",
                            ),
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
                padding=[f"12px {i}px" for i in [12, 12, 16, 18, 22, 24]],
            )

        return wrapper

    return decorator
