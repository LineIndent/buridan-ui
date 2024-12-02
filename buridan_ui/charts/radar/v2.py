import reflex as rx
from ..style import tooltip_styles, info
from ...wrappers.component.wrapper import ComponentWrapperState


def radar_v2():

    stats = [
        {"category": "Farming", "score": 8},
        {"category": "Fighting", "score": 7},
        {"category": "Aggressiveness", "score": 6},
        {"category": "Map Awareness", "score": 5},
        {"category": "Objective Control", "score": 9},
        {"category": "Positioning", "score": 7},
    ]

    return rx.vstack(
        info(
            "Radar Chart - Dots",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300", "text-sm stroke-gray-700"
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300", "text-sm stroke-gray-700"
                ),
            ),
            rx.recharts.radar(
                data_key="score",
                dot=True,
                stroke=ComponentWrapperState.default_theme[0],
                custom_attrs={
                    "fill": ComponentWrapperState.default_theme[1],
                    "strokeWidth": 2,
                },
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        width="100%",
        align="center",
        padding="0.5em",
    )
