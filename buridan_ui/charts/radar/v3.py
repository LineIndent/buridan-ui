import reflex as rx

from ...wrappers.component.wrapper import ComponentWrapperState
from ..style import info, tooltip_styles


def radar_v3():

    stats = [
        {"category": "Farming", "score": 6, "average": 8},
        {"category": "Fighting", "score": 8, "average": 9},
        {"category": "Aggressiveness", "score": 5, "average": 8},
        {"category": "Map Awareness", "score": 9, "average": 9},
        {"category": "Objective Control", "score": 7, "average": 8},
        {"category": "Positioning", "score": 6, "average": 9},
    ]

    return rx.vstack(
        info(
            "Radar Chart - Stacked",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.radar(
                data_key="average",
                fill_opacity=0.5,
                stroke="none",
                custom_attrs={"fill": "teal"},
            ),
            rx.recharts.radar(
                data_key="score",
                fill_opacity=1.0,
                stroke="none",
                custom_attrs={"fill": ComponentWrapperState.default_theme[1]},
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
