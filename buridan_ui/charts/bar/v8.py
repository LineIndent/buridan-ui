import reflex as rx
from ..style import tooltip_styles


def barchart_v8():
    color = ["teal", "orange"]
    categories = ["Successful", "Refunded"]
    EUROPE = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [12, 24, 48, 24, 34, 26, 12, 38, 23, 20, 24, 21],
            [0, 1, 4, 2, 0, 0, 0, 2, 1, 0, 0, 8],
        )
    ]

    ASIA = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [31, 32, 44, 23, 35, 48, 33, 38, 41, 39, 32, 19],
            [1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 5],
        )
    ]

    def create_chart(data: list[dict[str, str | int]]):
        return rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-25"
            ),
            rx.foreach(
                categories,
                lambda key, index: rx.recharts.bar(
                    data_key=key,
                    fill=rx.color(
                        rx.Var.create(color)[index],
                        6 + (index * 2),
                    ),
                    stack_id="_",
                ),
            ),
            rx.recharts.x_axis(
                interval=10,
                data_key="date",
                tick_size=10,
                class_name="text-xs font-semibold",
                axis_line=False,
                tick_line=False,
            ),
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            data=data,
            width="100%",
            height=250,
            bar_size=25,
        )

    return rx.vstack(
        rx.text("Online Transactions", class_name="text-md font-semibold pb-3"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Europe", class_name="text-sm font-semibold"),
                    flex="1",
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Asia", class_name="text-sm font-semibold"),
                    flex="1",
                    value="2",
                ),
            ),
            rx.tabs.content(create_chart(EUROPE), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(ASIA), value="2", margin_top="-5px"),
            default_value="1",
            width="100%",
            class_name=tooltip_styles.general_style,
        ),
        width="100%",
        padding="0.5em",
    )
