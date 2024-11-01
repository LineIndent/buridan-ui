import reflex as rx

from .state import InteractiveChartsState, ChartStruct, PlotStruct

from ....wrappers.base import base


def create_chart_entry(data: ChartStruct):
    return rx.hstack(
        rx.input(value=data.title),
        rx.vstack(
            rx.text(
                "xAxis",
                size="1",
                weight="bold",
            ),
            rx.select(
                InteractiveChartsState.columns,
                placeholder="Select an option",
                on_change=lambda name: InteractiveChartsState.update_chart_axis(
                    data, "x", name
                ),
                # on_change=lambda e: State.set_profile_stats(
                #     [title, e]),
            ),
            spacing="1",
            width="100%",
        ),
        rx.vstack(
            rx.text(
                "yAxis",
                size="1",
                weight="bold",
            ),
            rx.select(
                InteractiveChartsState.columns,
                placeholder="Select an option",
                on_change=lambda name: InteractiveChartsState.update_chart_axis(
                    data, "y", name
                ),
            ),
            spacing="1",
            width="100%",
        ),
    )


def create_chart(plot: PlotStruct):
    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Chart Visualization", size="5", weight="bold"),
                rx.text("Sales 2003 - 2005", size="1", color=rx.color("slate", 11)),
                spacing="1",
                margin_left="20px",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.line_chart(
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"}, item_style={"padding": "0px"}
                ),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    fill_opacity=0.5,
                    stroke=rx.color("slate", 5),
                ),
                rx.recharts.line(data_key=plot.yAxis, type_="linear", dot=False),
                rx.recharts.x_axis(data_key=plot.xAxis, axis_line=False),
                data=plot.data[:8],
                width="100%",
                height=200,
                margin={"left": 20},
            ),
            width="100%",
            max_width="50em",
            height="500px",
        ),
        width="100%",
        padding="32px 24px",
        flex="1",
    )


@base("/interactive-charts", "Interactive Charts", title="Charts - buridan/ui")
def interactive_charts():
    return [
        rx.input(
            value=InteractiveChartsState.url, on_change=InteractiveChartsState.set_url
        ),
        rx.button(
            "Test",
            on_click=InteractiveChartsState.get_data_from_url,
        ),
        rx.button(
            "add",
            on_click=InteractiveChartsState.add_new_chart,
        ),
        rx.vstack(rx.foreach(InteractiveChartsState.charts, create_chart_entry)),
        rx.button(
            "create chart",
            on_click=InteractiveChartsState.compile_chart_data_to_ui,
        ),
        rx.vstack(
            rx.foreach(InteractiveChartsState.plot, create_chart),
            width="100%",
            height="100%",
            align="center",
        ),
    ]
