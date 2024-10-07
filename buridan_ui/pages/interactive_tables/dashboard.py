import reflex as rx

from ...wrappers.base import base

import reflex as rx

from .data import DATA, COLORS
from copy import deepcopy
import asyncio

# for this beta version, using only two compoenents with limited props ...
# can extend this easily by adding the prop here and making a MENU item for it...
badge_props: dict[str, str] = {"color": "", "variant": ""}
button_props: dict[str, str] = {"variant": "", "size": ""}

schema = {"badge": badge_props, "button": button_props}


class State(rx.State):
    source: str = (
        "https://jsonplaceholder.typicode.com/todos"  # source is a placeholder ... data coming from data.py...
    )
    data: list[dict[str, str]]
    headers: list[str]
    columns: list[str]
    key_set: dict[str, list[str]]
    key_map: dict[str, str]
    ui_map: dict[str, dict[str, dict[str, dict[str, str]]]]

    is_loading: bool = False
    is_header: dict[str, str] = {"display": "none", "opacity": "0"}
    is_table: dict[str, str] = {"display": "none", "opacity": "0"}
    is_export: dict[str, str] = {"display": "none", "opacity": "0"}

    async def update_ui_element(self, element, delay=0.5):
        """Helper function to update display and opacity with delays."""
        await asyncio.sleep(delay)
        element["display"] = "flex"

        await asyncio.sleep(delay)
        element["opacity"] = "1"

    async def process_data_set(self):
        self.reset()
        self.data = DATA
        self.is_loading = True
        yield
        await asyncio.sleep(2)

        # Process headers and key mappings
        for header in list(self.data[0].keys()):
            # can catch extra keys here ... ex: avatar or any common key varr
            if header == "avatar":
                self.key_map[header] = "avatar"
            else:
                self.key_map[header] = "text"
            self.headers.append(header)

        self.key_set, column_set, self.columns = await self.find_repetitive_keys(
            self.data
        )

        for col in self.columns:
            self.ui_map[col] = {}
            for element in column_set[col]:
                self.ui_map[col][element] = deepcopy(schema)

        # Sequentially update UI elements with display and opacity
        await self.update_ui_element(self.is_header)
        yield
        await self.update_ui_element(self.is_table)
        yield
        await self.update_ui_element(self.is_export)
        yield

        self.is_loading = False

    async def find_repetitive_keys(self, data):
        repetitive_keys = {}

        # look for repeated keys that function as descriptors...
        # can add more cases here to catch other datatypes ...
        for key in data[0].keys():
            values = [item[key] for item in data]
            unique_values = set(values)

            if len(values) > len(unique_values) > 1:
                repetitive_keys[key] = unique_values

        string_keys = {
            key: list(map(str, value)) for key, value in repetitive_keys.items()
        }

        return string_keys, repetitive_keys, list(repetitive_keys.keys())

    def change_table_ui(
        self,
        column_name: str,
        column_item: str,
        component: str,
        prop_name: str,
        prop_value: str,
    ):
        self.key_map[column_name] = component
        self.ui_map[column_name][column_item][component][prop_name] = prop_value


def blip():
    return rx.box(
        width="10px",
        height="10px",
        border_radius="10px",
        background=rx.color("gray", 9),
        position="absolute",
        left="-4.5px",
    )


def wrapper(
    title: str, instructions: str, components: list[rx.Component] = [], **kwargs
):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(
                        title, size="3", weight="bold", color=rx.color("slate", 12)
                    ),
                    align="center",
                ),
                rx.text(instructions, size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            *components,
            spacing="5",
            width="100%",
        ),
        width="100%",
        align="start",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
        border_left=f"1px solid {rx.color('gray', 10)}",
        **kwargs,
    )


def menu(column_name: str, column_item: str):
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                "...",
                size="1",
                color_scheme="gray",
                variant="soft",
                width="21px",
                height="21px",
                cursor="pointer",
            )
        ),
        rx.menu.content(
            rx.menu.item(
                rx.text(
                    "Badge Component",
                    font_size="10px",
                    weight="medium",
                    color=rx.color("slate", 11),
                )
            ),
            *[
                rx.menu.item(
                    rx.hstack(
                        rx.text(
                            var.upper(),
                            font_size="10px",
                            color=rx.color("slate", 12),
                            weight="bold",
                        ),
                        rx.text(
                            "variant", font_size="10px", color=rx.color("slate", 11)
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        on_click=State.change_table_ui(
                            column_name, column_item, "badge", "variant", var
                        ),
                    ),
                )
                for var in ["soft", "surface", "solid", "outline"]
            ],
            rx.menu.item(
                rx.hstack(
                    rx.text(
                        "color".upper(),
                        font_size="10px",
                        color=rx.color("slate", 12),
                        weight="bold",
                    ),
                    rx.text(
                        "color_scheme", font_size="10px", color=rx.color("slate", 11)
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
            ),
            rx.hstack(
                *[
                    rx.badge(
                        width="12px",
                        height="12px",
                        radius="full",
                        size="1",
                        variant="solid",
                        color_scheme=color,
                        cursor="pointer",
                        on_click=State.change_table_ui(
                            column_name, column_item, "badge", "color", color
                        ),
                    )
                    for color in COLORS
                ],
                align="center",
                flex_wrap="wrap",
                spacing="2",
                padding="10px",
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.text(
                    "Button Component",
                    font_size="10px",
                    weight="medium",
                    color=rx.color("slate", 11),
                )
            ),
            *[
                rx.menu.item(
                    rx.hstack(
                        rx.text(
                            var.upper(),
                            font_size="10px",
                            color=rx.color("slate", 12),
                            weight="bold",
                        ),
                        rx.text(
                            "variant", font_size="10px", color=rx.color("slate", 11)
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        on_click=State.change_table_ui(
                            column_name, column_item, "button", "variant", var
                        ),
                    ),
                )
                for var in ["classic", "solid", "soft", "surface", "outline", "ghost"]
            ],
            *[
                rx.menu.item(
                    rx.hstack(
                        rx.text(
                            var,
                            font_size="13px",
                            color=rx.color("slate", 12),
                            weight="medium",
                        ),
                        rx.text("size", font_size="10px", color=rx.color("slate", 11)),
                        justify="between",
                        align="center",
                        width="100%",
                        on_click=State.change_table_ui(
                            column_name, column_item, "button", "size", var
                        ),
                    ),
                )
                for var in ["1", "2", "3", "4"]
            ],
            size="1",
            width="200px",
        ),
    )


def header_items(col_name: str):
    return rx.hstack(
        rx.foreach(
            State.key_set[col_name],
            lambda item: rx.hstack(
                rx.text(
                    item,
                    size="1",
                    weight="medium",
                    color=rx.color("slate", 12),
                    width="100px",
                ),
                menu(col_name, item),
                background=rx.color("gray", 1),
                align="center",
                justify="between",
                border_radius="8px",
                padding="6px 12px",
            ),
        ),
        align="center",
        flex_wrap="wrap",
    )


def headers():
    return wrapper(
        "Changeable Headers",
        "Select a component from the menu to change data-specific UI.",
        [
            rx.foreach(
                State.columns,
                lambda col: rx.vstack(
                    rx.hstack(
                        rx.text(
                            col, size="1", weight="bold", color=rx.color("slate", 11)
                        ),
                        align="center",
                        justify="between",
                        width="100%",
                    ),
                    header_items(col),
                    width="100%",
                ),
            )
        ],
        display=State.is_header["display"],
        opacity=State.is_header["opacity"],
        transition="all 850ms ease",
    )


def process_rows(data: dict[str, str]):
    def process_cell(item):
        return rx.table.cell(
            rx.match(
                # ... item[0] is the column name
                State.key_map[item[0]],
                ("text", rx.text(f"{item[1]}")),
                ("avatar", rx.avatar(src=item[1], size="2", radius="full")),
                (
                    "badge",
                    rx.badge(
                        item[1],
                        variant=State.ui_map[item[0]][item[1]]["badge"]["variant"],
                        color_scheme=State.ui_map[item[0]][item[1]]["badge"]["color"],
                    ),
                ),
                (
                    "button",
                    rx.button(
                        item[1],
                        variant=State.ui_map[item[0]][item[1]]["button"]["variant"],
                        size=State.ui_map[item[0]][item[1]]["button"]["size"],
                    ),
                ),
            )
        )

    return rx.table.row(
        rx.foreach(data, process_cell),
        align="center",
        white_space="nowrap",
    )


def table():
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.foreach(
                        State.headers,
                        lambda title: rx.table.column_header_cell(
                            rx.hstack(rx.text(title, font_size="12px", weight="bold")),
                        ),
                    )
                ),
            ),
            rx.table.body(
                rx.foreach(State.data, process_rows),
            ),
            max_width="60em",
            width="100%",
            variant="surface",
            transition="all 850ms ease",
        ),
        width="100%",
        max_width="60em",
        overflow="scroll",
    )


@base(
    "/interactive-table/dashboard", "Interactive Table", title="Dashboard - buridan/ui"
)
def dashboard():
    return [
        rx.hstack(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Dashboard",
                        size="5",
                        weight="bold",
                        color=rx.color("slate", 12),
                    ),
                    rx.text(
                        "Add UI changes live to your tables directly.",
                        color=rx.color("slate", 11),
                        weight="medium",
                        size="1",
                    ),
                    spacing="1",
                    align="start",
                    justify="start",
                    width="100%",
                    max_width="40em",
                ),
                rx.vstack(
                    wrapper(
                        "Data Set",
                        "Enter the source of your data (url).",
                        [
                            rx.hstack(
                                rx.input(value=State.source, width="300px"),
                                rx.button(
                                    "Run",
                                    color_scheme="gray",
                                    variant="surface",
                                    size="2",
                                    cursor="pointer",
                                    loading=State.is_loading,
                                    on_click=State.process_data_set,
                                ),
                                align="center",
                            ),
                        ],
                    ),
                    headers(),
                    position="relative",
                    spacing="6",
                    # max_width="40em",
                    width="100%",
                    margin="12px 0px",
                ),
                width="100%",
            ),
            rx.vstack(
                wrapper(
                    "Table",
                    "Changes are updated automatically.",
                    [table()],
                    display=State.is_table["display"],
                    opacity=State.is_table["opacity"],
                ),
                wrapper(
                    "Export Table",
                    "Export your table as reflex code!",
                    [
                        rx.button(
                            "Get Table Code",
                            rx.icon(tag="download", size=15, color_scheme="gray"),
                            size="2",
                            variant="surface",
                            color_scheme="gray",
                            cursor="pointer",
                        )
                    ],
                    display=State.is_export["display"],
                    opacity=State.is_export["opacity"],
                ),
                width="100%",
                position="relative",
                spacing="6",
            ),
            width="100%",
            align="start",
            justify="between",
            padding="35px",
            wrap="wrap",
        )
    ]
