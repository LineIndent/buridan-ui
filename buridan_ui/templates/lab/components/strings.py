chart_generators = {
    "line-v1": lambda: f"""rx.recharts.line_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.line(data_key="{chart_key_one}", type_="natural", dot=False),
    data={data_key},
    height={height}
)""",
    "line-v2": lambda: f"""rx.recharts.line_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.line(data_key="{chart_key_one}", type_="linear", dot=False),
    data={data_key},
    height={height}
)""",
    "line-v3": lambda: f"""rx.recharts.line_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.line(
        rx.recharts.label_list(**{ChartCodeGenerator._format_dict(GeneralChartStyle.labels)}),
        data_key="{chart_key_one}",
        type_="linear",
        dot=False
    ),
    data={data_key},
    height={height}
)""",
    "line-v4": lambda: f"""rx.recharts.line_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.line(data_key="{chart_key_one}", type_="natural", dot=False),
    rx.recharts.line(data_key="{chart_key_two}", type_="natural", dot=False),
    data={data_key},
    height={height}
)""",
    "area-v1": lambda: f"""rx.recharts.area_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.area(data_key="{chart_key_one}"),
    data={data_key},
    height={height}
)""",
    "area-v2": lambda: f"""rx.recharts.area_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.area(data_key="{chart_key_one}", type_="linear"),
    data={data_key},
    height={height}
)""",
    "area-v3": lambda: f"""rx.recharts.area_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.area(data_key="{chart_key_one}", type_="step"),
    data={data_key},
    height={height}
)""",
    "area-v4": lambda: f"""rx.recharts.area_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.area(data_key="{chart_key_one}"),
    rx.recharts.area(data_key="{chart_key_two}"),
    data={data_key},
    height={height}
)""",
    "area-v6": lambda: f"""rx.recharts.area_chart(
    rx.recharts.cartesian_grid(**{chart_config['cartesian_grid']}),
    rx.recharts.x_axis(data_key="{x_axis_key}", **{ChartCodeGenerator._format_dict(GeneralChartStyle.x_axis)}),
    rx.recharts.area(data_key="{chart_key_one}"),
    rx.recharts.area(data_key="{chart_key_two}"),
    rx.recharts.legend(),
    data={data_key},
    height={height}
)""",
}
