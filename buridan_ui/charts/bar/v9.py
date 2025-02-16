import reflex as rx
from ..style import tooltip_styles


def barchart_v9():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
    ]

    return rx.vstack(
        rx.hstack(
            rx.foreach(
                [["Desktop", "red"], ["Mobile", "sky"], ["Tablet", "orange"]],
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
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.bar_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.bar(data_key="desktop", fill=rx.color("red", 7), radius=4),
            rx.recharts.bar(data_key="mobile", fill=rx.color("sky", 7), radius=4),
            rx.recharts.bar(data_key="tablet", fill=rx.color("orange", 7), radius=4),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            width="100%",
            height=250,
            bar_size=18,
            bar_category_gap="30%",
        ),
        width="100%",
        class_name=f"{tooltip_styles.general_style} flex flex-col",
    )
