import reflex as rx
from ..style import tooltip_styles


def barchart_v10():

    sport = [
        {"date": "Jan 23", "Running": 167, "Cycling": 145},
        {"date": "Feb 23", "Running": 125, "Cycling": 110},
        {"date": "Mar 23", "Running": 156, "Cycling": 149},
        {"date": "Apr 23", "Running": 165, "Cycling": 112},
        {"date": "May 23", "Running": 153, "Cycling": 138},
        {"date": "Jun 23", "Running": 124, "Cycling": 145},
        {"date": "Jul 23", "Running": 164, "Cycling": 134},
    ]

    def create_alternating_chart(data, colors, active):
        return rx.recharts.bar_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.foreach(
                ["Running", "Cycling"],
                lambda key, index: rx.recharts.bar(
                    is_animation_active=False,
                    radius=4,
                    data_key=key,
                    fill=rx.color(rx.Var.create(colors)[index]),
                    custom_attrs={
                        "opacity": rx.cond(
                            key == active,
                            "0.25",
                            "1",
                        )
                    },
                ),
            ),
            rx.recharts.x_axis(
                data_key="date",
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
        )

    return rx.vstack(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Running", class_name="text-sm font-semibold"),
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Cycling", class_name="text-sm font-semibold"),
                    value="2",
                ),
            ),
            rx.tabs.content(
                create_alternating_chart(sport, ["red", "blue"], "Running"),
                value="1",
                margin_top="-5px",
            ),
            rx.tabs.content(
                create_alternating_chart(sport, ["red", "blue"], "Cycling"),
                value="2",
                margin_top="-5px",
            ),
            default_value="1",
            width="100%",
        ),
        width="100%",
        class_name=tooltip_styles.general_style,
    )
