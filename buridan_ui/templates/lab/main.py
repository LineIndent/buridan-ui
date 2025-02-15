import reflex as rx
import ast
import json

from reflex.components.radix.themes.layout.stack import VStack
from typing import List, Dict, Any, Callable

from .components.wrappers import data_wrapper
from .components.charts import ChartRenderer, ChartTypes, GeneralChartStyle


class ChartLabState(rx.ComponentState):
    """State management for chart lab functionality."""

    # Core data attributes
    data: str = ""
    processed_data: List[Dict[str, Any]] = []
    keys: List[str] = []

    # Axis and chart configuration
    x_axis_key: str = ""
    chart_key: str = ""
    chart_key_second: str = ""

    # Validation flags
    x_axis_key_valid: bool = False
    chart_key_valid: bool = False

    # Available keys for selection
    chart_keys_list: List[str] = []
    x_axis_keys_list: List[str] = []

    @staticmethod
    def validate_key(key: str, available_keys: List[str]) -> bool:
        """
        Validate if a given key exists in the available keys.

        Args:
            key (str): The key to validate
            available_keys (List[str]): List of available keys

        Returns:
            bool: True if key is valid, False otherwise
        """
        return key in available_keys

    @rx.event
    def process_chart_keys(self, value: str):
        """Process and validate chart key selection."""
        self.chart_key = value
        self.chart_key_valid = self.validate_key(self.chart_key, self.keys)

    @rx.event
    def process_chart_keys_second(self, value: str):
        """Process and validate chart key selection."""
        self.chart_key_second = value
        self.chart_key_valid = self.validate_key(self.chart_key, self.keys)

    @rx.event
    def process_axis_keys(self, value: str):
        """Process and validate x-axis key selection."""
        self.x_axis_key = value
        self.x_axis_key_valid = self.validate_key(self.x_axis_key, self.keys)

    @rx.event
    def process_user_data(self, value: str):
        """
        Process and parse user-provided data.

        Validates the input, extracts keys, and prepares data for charting.
        """
        self.data = value
        if not self.data:
            return

        try:
            # Safely parse the data
            parsed_data = ast.literal_eval(self.data)

            # Extract keys from the first data entry
            keys = list(parsed_data[0].keys())

            # Update state
            self.keys = keys
            self.chart_keys_list = keys
            self.x_axis_keys_list = keys

            # Convert to JSON for display and store processed data
            self.data = json.dumps(parsed_data, indent=4)
            self.processed_data = parsed_data

        except (SyntaxError, ValueError) as e:
            # Handle potential parsing errors
            print(f"Error processing data: {e}")
            # Optionally, you could set an error state here

    @classmethod
    def _create_input(cls, value_attr: str, on_change_method: Callable[[str], None]):
        return rx.hstack(
            rx.text(
                "Key",  # Use last word of label as display text
                size="1",
                weight="bold",
                color=rx.color("slate", 10),
                width="70px",
            ),
            rx.input(
                value=value_attr,
                width="100%",
                variant="soft",
                bg="transparent",
                outline="none",
                on_change=on_change_method,
            ),
            align="center",
            width="100%",
            border_bottom=f"0.75px solid {rx.color('gray', 4)}",
        )

    @classmethod
    def _create_input_section(
        cls, label: str, value_attr: str, on_change_method: Callable[[str], None]
    ) -> rx.Component:
        """
        Create a reusable input section for dialog.

        Args:
            label (str): Label for the input section
            value_attr (str): State attribute for the input value
            on_change_method (method): Method to call on input change

        Returns:
            rx.Component: Structured input section
        """
        return data_wrapper(
            label,
            [cls._create_input(value_attr, on_change_method)],
        )

    @classmethod
    def _create_input_section_double(
        cls,
        label: str,
        value_attr: str,
        on_change_method: Callable[[str], None],
        value_attr_second: str,
        on_change_method_second: Callable[[str], None],
    ) -> rx.Component:
        """
        Create a reusable input section for dialog.

        Args:
            label (str): Label for the input section
            value_attr (str): State attribute for the input value
            on_change_method (method): Method to call on input change

        Returns:
            rx.Component: Structured input section
        """
        return data_wrapper(
            label,
            [
                rx.vstack(
                    cls._create_input(value_attr, on_change_method),
                    cls._create_input(value_attr_second, on_change_method_second),
                    width="100%",
                )
            ],
        )

    @rx.event
    def generate_code(self, chart_type: str):
        grid_ = {**GeneralChartStyle.grid}
        x_axis = {**GeneralChartStyle.x_axis}

        mapping = {
            "line-v1": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.line_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.line(data_key="{self.chart_key}", type_="natural", dot=False),
            data=data,
            height=300,
        )""",
            "line-v2": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.line_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.line(data_key="{self.chart_key}", type_="linear", dot=False),
            data=data,
            height=300,
        )""",
            "line-v3": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.line_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.line(
                rx.recharts.label_list(**GeneralChartStyle.labels),
                data_key="{self.chart_key}",
                type_="linear",
                dot=False
            ),
            data=data,
            height=300,
        )""",
            "line-v4": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.line_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.line(data_key="{self.chart_key}", type_="natural", dot=False),
            rx.recharts.line(data_key="{self.chart_key_second}", type_="natural", dot=False),
            data=data,
            height=300,
        )""",
            "area-v1": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.area(data_key="{self.chart_key}"),
            data=data,
            height=300,
        )""",
            "area-v2": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.area(data_key="{self.chart_key}", type_="linear"),
            data=data,
            height=300,
        )""",
            "area-v3": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.area(data_key="{self.chart_key}", type_="step"),
            data=data,
            height=300,
        )""",
            "area-v4": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.area(data_key="{self.chart_key}"),
            rx.recharts.area(data_key="{self.chart_key_second}"),
            data=data,
            height=300,
        )""",
            "area-v6": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.area(data_key="{self.chart_key}"),
            rx.recharts.area(data_key="{self.chart_key_second}"),
            rx.recharts.legend(),
            data=data,
            height=300,
        )""",
            "area-v7": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.area_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.y_axis(**GeneralChartStyle.y_axis),
            rx.recharts.area(data_key="{self.chart_key}"),
            rx.recharts.area(data_key="{self.chart_key_second}"),
            data=data,
            height=300,
        )""",
            "bar-v1": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.bar(data_key="{self.chart_key}", radius=6),
            rx.recharts.bar(data_key="{self.chart_key_second}", radius=6, fill=rx.color("blue", 8)),
            data=data,
            height=300,
        )""",
            "bar-v3": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.bar(data_key="{self.chart_key}", radius=[0, 0, 6, 6], stack_id="1"),
            rx.recharts.bar(data_key="{self.chart_key_second}", radius=[6, 6, 0, 0], stack_id="1", fill=rx.color("blue", 8)),
            rx.recharts.legend(),
            data=data,
            height=300,
            bar_size=35,
        )""",
            "bar-v4": f"""
            grid = {grid_}
            data = {self.data}

            rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(**grid),
            rx.recharts.x_axis(data_key="{self.x_axis_key}", **{x_axis}),
            rx.recharts.bar(
                rx.recharts.label_list(**GeneralChartStyle.labels),
                data_key="{self.chart_key}", 
                radius=6
            ),
            data=data,
            height=300,
            bar_size=35,
            margin={{"top": 25}},
        )""",
        }

        yield rx.set_clipboard(mapping[chart_type])
        yield rx.toast.success("Code copied to clipboard!")

    @classmethod
    def get_component(
        cls,
        *children,
        chart_type: ChartTypes,
        **props,
    ) -> VStack:
        """
        Create the main dialog component for chart lab.

        Returns:
            VStack: Fully configured dialog component
        """
        return rx.dialog.root(
            *children,
            rx.dialog.trigger(
                rx.button(
                    rx.text("Dev Lab", size="1", color=rx.color("slate", 11)),
                    height="25px",
                    variant="surface",
                    color_scheme="gray",
                    cursor="pointer",
                ),
            ),
            rx.dialog.content(
                rx.vstack(
                    # Data input section
                    data_wrapper(
                        "Enter your raw data below",
                        [
                            rx.text_area(
                                value=cls.data,
                                on_change=cls.process_user_data,
                                height="35vh",
                                width="100%",
                            )
                        ],
                    ),
                    # X-Axis input section (using new helper method)
                    cls._create_input_section(
                        "Set the x-axis value", cls.x_axis_key, cls.process_axis_keys
                    ),
                    # Chart Key input section (using new helper method)
                    (
                        cls._create_input_section(
                            "Set the chart key value",
                            cls.chart_key,
                            cls.process_chart_keys,
                        )
                        if chart_type
                        in [
                            "area-v1",
                            "area-v2",
                            "area-v3",
                            "line-v1",
                            "line-v2",
                            "line-v3",
                            "bar-v4",
                        ]
                        else cls._create_input_section_double(
                            "Set the chart key value",
                            cls.chart_key,
                            cls.process_chart_keys,
                            cls.chart_key_second,
                            cls.process_chart_keys_second,
                        )
                    ),
                    # Chart output section
                    rx.cond(
                        cls.data & cls.x_axis_key & cls.chart_key,
                        data_wrapper(
                            "Chart Output",
                            [
                                ChartRenderer.render_chart(
                                    chart_type,
                                    cls.processed_data,
                                    cls.chart_key,
                                    cls.chart_key_second,
                                    cls.x_axis_key,
                                ),
                            ],
                        ),
                        rx.spacer(),
                    ),
                    rx.cond(
                        cls.data & cls.x_axis_key & cls.chart_key,
                        rx.button(
                            "Generate Code",
                            on_click=cls.generate_code(chart_type),
                            width="100%",
                            variant="surface",
                        ),
                        rx.spacer(),
                    ),
                    height="100%",
                    spacing="6",
                ),
                width="100%",
            ),
            **props,
            size="1",
        )


# Create the component
ChartLab = ChartLabState.create
