import reflex as rx
from dataclasses import dataclass, field
from typing import Dict, Literal

from reflex.components.recharts.recharts import RechartsCharts


@dataclass
class GeneralChartStyle:
    grid: Dict[str, str] = field(
        default_factory=lambda: {
            "horizontal": True,
            "vertical": False,
            "fill_opacity": 0.5,
            "stroke": rx.color("slate", 5),
        }
    )

    x_axis: Dict[str, str | int | bool | Dict[str, str]] = field(
        default_factory=lambda: {
            "axis_line": False,
            "tick_size": 10,
            "tick_line": False,
            "custom_attrs": {"fontSize": "12px"},
            "interval": "preserveStartEnd",
        }
    )

    y_axis: Dict[str, str | int | bool] = field(
        default_factory=lambda: {
            "axis_line": False,
            "min_tick_gap": 50,
            "tick_size": 10,
            "tick_line": False,
            "custom_attrs": {"fontSize": "12px"},
        }
    )

    labels: Dict[str, str | int | bool] = field(
        default_factory=lambda: {
            "position": "top",
            "offset": 10,
            "custom_attrs": {"fontSize": "12px", "fontWeight": "bold"},
        }
    )


GeneralChartStyle: GeneralChartStyle = GeneralChartStyle()

ChartTypes = Literal[
    "area-v1",
    "area-v2",
    "area-v3",
    "area-v4",
    "area-v6",
    "line-v1",
    "line-v2",
    "line-v3",
    "line-v4",
    "bar-v1",
    "bar-v3",
    "bar-v4",
]


class ChartRenderer:
    @staticmethod
    def render_chart(
        chart_type: ChartTypes,
        data_key=None,
        chart_key_one: str = "",
        chart_key_two: str = "",
        x_axis_key: str = "",
        height: int = 260,
        **kwargs,
    ) -> RechartsCharts:
        """
        Render a chart with flexible configuration.

        :param chart_type: Type of chart to render
        :param data_key: Data for the chart
        :param chart_key_one: Primary data key for the chart
        :param chart_key_two: Secondary data key for multi-series charts
        :param x_axis_key: Key for x-axis data
        :param height: Height of the chart
        :param kwargs: Additional configuration options
        :return: Recharts chart component
        """

        if data_key is None:
            data_key = []

        chart_config = {
            "cartesian_grid": GeneralChartStyle.grid,
            "x_axis": {"data_key": x_axis_key, **GeneralChartStyle.x_axis},
            "height": height,
        }

        # Merge any additional configuration
        chart_config.update(kwargs)

        # Chart type specific configurations
        chart_type_configs = {
            "line-v1": {
                "chart_func": rx.recharts.line_chart,
                "series_components": [
                    rx.recharts.line(data_key=chart_key_one, type_="natural", dot=False)
                ],
            },
            "line-v2": {
                "chart_func": rx.recharts.line_chart,
                "series_components": [
                    rx.recharts.line(data_key=chart_key_one, type_="linear", dot=False)
                ],
            },
            "line-v3": {
                "chart_func": rx.recharts.line_chart,
                "series_components": [
                    rx.recharts.line(
                        rx.recharts.label_list(**GeneralChartStyle.labels),
                        data_key=chart_key_one,
                        type_="linear",
                        dot=False,
                    )
                ],
            },
            "line-v4": {
                "chart_func": rx.recharts.line_chart,
                "series_components": [
                    rx.recharts.line(
                        data_key=chart_key_one, type_="natural", dot=False
                    ),
                    rx.recharts.line(
                        data_key=chart_key_two, type_="natural", dot=False
                    ),
                ],
            },
            "area-v1": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [rx.recharts.area(data_key=chart_key_one)],
            },
            "area-v2": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [
                    rx.recharts.area(data_key=chart_key_one, type_="linear")
                ],
            },
            "area-v3": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [
                    rx.recharts.area(data_key=chart_key_one, type_="step"),
                ],
            },
            "area-v4": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [
                    rx.recharts.area(data_key=chart_key_one),
                    rx.recharts.area(data_key=chart_key_two),
                ],
            },
            "area-v6": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [
                    rx.recharts.area(data_key=chart_key_one),
                    rx.recharts.area(data_key=chart_key_two),
                    rx.recharts.legend(),
                ],
            },
            "area-v7": {
                "chart_func": rx.recharts.area_chart,
                "series_components": [
                    rx.recharts.area(data_key=chart_key_one),
                    rx.recharts.area(data_key=chart_key_two),
                    rx.recharts.y_axis(**GeneralChartStyle.y_axis),
                ],
            },
            "bar-v1": {
                "chart_func": rx.recharts.bar_chart,
                "series_components": [
                    rx.recharts.bar(data_key=chart_key_one, radius=6),
                    rx.recharts.bar(
                        data_key=chart_key_two,
                        radius=6,
                        fill=rx.color("blue", 8),
                    ),
                ],
            },
            "bar-v3": {
                "chart_func": rx.recharts.bar_chart,
                "series_components": [
                    rx.recharts.bar(
                        data_key=chart_key_one, radius=[0, 0, 6, 6], stack_id="1"
                    ),
                    rx.recharts.bar(
                        data_key=chart_key_two,
                        radius=[6, 6, 0, 0],
                        stack_id="1",
                        fill=rx.color("blue", 8),
                    ),
                    rx.recharts.legend(),
                ],
                "kwargs": {"bar_size": 35},
            },
            "bar-v4": {
                "chart_func": rx.recharts.bar_chart,
                "series_components": [
                    rx.recharts.bar(
                        rx.recharts.label_list(**GeneralChartStyle.labels),
                        data_key=chart_key_one,
                        radius=6,
                    ),
                ],
                "kwargs": {"bar_size": 35, "margin": {"top": 25}},
            },
        }

        # Validate chart type (internal validation during dev-mode!)
        if chart_type not in chart_type_configs:
            raise ValueError(f"Unsupported chart type: {chart_type}")

        # Get chart configuration
        chart_type_config = chart_type_configs[chart_type]
        chart_type_kwargs = chart_type_configs[chart_type].get("kwargs", {})

        # Construct chart components
        chart_components = [
            rx.recharts.cartesian_grid(**chart_config["cartesian_grid"]),
            rx.recharts.x_axis(**chart_config["x_axis"]),
        ]
        chart_components.extend(chart_type_config["series_components"])

        # Render chart
        return chart_type_config["chart_func"](
            *chart_components,
            data=data_key,
            height=chart_config["height"],
            **chart_type_kwargs,
        )
