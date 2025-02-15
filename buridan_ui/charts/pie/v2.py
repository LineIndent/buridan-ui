import reflex as rx

from ...wrappers.state import ComponentWrapperState
from ..style import info, tooltip_styles


def piechart_v2():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    data = [
        {**item, "fill": rx.color(ComponentWrapperState.selected_theme, index + 5)}
        for index, item in enumerate(data)
    ]

    return rx.vstack(
        info("Pie Chart - Hovering Labels", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.pie(
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                label=True,
                is_animation_active=False,
                label_line=False,
                custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        width="100%",
        align="center",
        padding="0.5em",
    )


def _pie_chart():

    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.fragment(
        rx.recharts.pie_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.pie(
                rx.foreach(
                    ["red", "blue", "green", "yellow", "purple"],
                    lambda color, index: rx.recharts.cell(
                        fill=rx.color(color),
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                inner_radius=90,
                custom_attrs={"paddingAngle": 3, "cornerRadius": 5},
            ),
            width="100%",
            height=350,
        ),
        rx.hstack(
            rx.foreach(
                [
                    ["Chrome", "red"],
                    ["Safari", "blue"],
                    ["Firefox", "green"],
                    ["Edge", "yellow"],
                    # ["Other", "purple"],
                ],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=rx.color(key[1])),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full justify-center flex-wrap",
        ),
    )
