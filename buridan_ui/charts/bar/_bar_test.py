import reflex as rx

data = [
    {"date": "Jan 23", "Successful": 12, "Refunded": 0},
    {"date": "Feb 23", "Successful": 24, "Refunded": 1},
    {"date": "Mar 23", "Successful": 48, "Refunded": 4},
    {"date": "Apr 23", "Successful": 24, "Refunded": 2},
    {"date": "May 23", "Successful": 34, "Refunded": 0},
    {"date": "Jun 23", "Successful": 26, "Refunded": 0},
    {"date": "Jul 23", "Successful": 12, "Refunded": 0},
    {"date": "Aug 23", "Successful": 38, "Refunded": 2},
    {"date": "Sep 23", "Successful": 23, "Refunded": 1},
    {"date": "Oct 23", "Successful": 20, "Refunded": 0},
    {"date": "Nov 23", "Successful": 24, "Refunded": 0},
    {"date": "Dec 23", "Successful": 21, "Refunded": 8},
]

data2 = [
    {"date": "Jan 23", "Successful": 31, "Refunded": 1},
    {"date": "Feb 23", "Successful": 32, "Refunded": 2},
    {"date": "Mar 23", "Successful": 44, "Refunded": 3},
    {"date": "Apr 23", "Successful": 23, "Refunded": 2},
    {"date": "May 23", "Successful": 35, "Refunded": 1},
    {"date": "Jun 23", "Successful": 48, "Refunded": 1},
    {"date": "Jul 23", "Successful": 33, "Refunded": 1},
    {"date": "Aug 23", "Successful": 38, "Refunded": 3},
    {"date": "Sep 23", "Successful": 41, "Refunded": 2},
    {"date": "Oct 23", "Successful": 39, "Refunded": 1},
    {"date": "Nov 23", "Successful": 32, "Refunded": 1},
    {"date": "Dec 23", "Successful": 19, "Refunded": 5},
]

data3 = [
    {"date": "Jan 23", "Successful": 65, "Refunded": 2},
    {"date": "Feb 23", "Successful": 78, "Refunded": 3},
    {"date": "Mar 23", "Successful": 55, "Refunded": 5},
    {"date": "Apr 23", "Successful": 79, "Refunded": 4},
    {"date": "May 23", "Successful": 41, "Refunded": 1},
    {"date": "Jun 23", "Successful": 32, "Refunded": 1},
    {"date": "Jul 23", "Successful": 54, "Refunded": 0},
    {"date": "Aug 23", "Successful": 45, "Refunded": 3},
    {"date": "Sep 23", "Successful": 75, "Refunded": 2},
    {"date": "Oct 23", "Successful": 62, "Refunded": 1},
    {"date": "Nov 23", "Successful": 55, "Refunded": 1},
    {"date": "Dec 23", "Successful": 58, "Refunded": 6},
]

sport = [
    {"date": "Jan 23", "Running": 167, "Cycling": 145},
    {"date": "Feb 23", "Running": 125, "Cycling": 110},
    {"date": "Mar 23", "Running": 156, "Cycling": 149},
    {"date": "Apr 23", "Running": 165, "Cycling": 112},
    {"date": "May 23", "Running": 153, "Cycling": 138},
    # {"date": "Jun 23", "Running": 124, "Cycling": 145},
    # {"date": "Jul 23", "Running": 164, "Cycling": 134},
    # {"date": "Aug 23", "Running": 123, "Cycling": 110},
    # {"date": "Sep 23", "Running": 132, "Cycling": 113},
    # {"date": "Oct 23", "Running": 124, "Cycling": 129},
    # {"date": "Nov 23", "Running": 149, "Cycling": 101},
    # {"date": "Dec 23", "Running": 129, "Cycling": 109},
]

color = ["accent", "ruby"]
categories = ["Successful", "Refunded"]
XAxis = "date"


def create_chart(data: list[dict[str, str | int]]):
    return rx.box(
        rx.el.style(
            """
.recharts-tooltip-item-unit {
    display: none;
}
.recharts-tooltip-item-value {
    font-family: "JetBrains Mono", monospace;
    color: var(--c-slate-12);
}

"""
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True,
                vertical=False,
                class_name="opacity-35",
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
                    is_animation_active=False,
                ),
            ),
            rx.recharts.x_axis(
                interval=10,
                data_key=XAxis,
                tick_size=10,
                class_name="text-xs font-semibold",
                axis_line=False,
                tick_line=False,
                # type_="category",
            ),
            rx.recharts.graphing_tooltip(
                content_style={
                    "background": rx.color("slate", 1),
                    "borderColor": rx.color("slate", 5),
                    "borderRadius": "5px",
                    "boxShadow": "0px 24px 12px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 8px 8px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 2px 6px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00))",
                    "fontFamily": "var(--font-instrument-sans)",
                    "fontSize": "0.875rem",
                    "lineHeight": "1.25rem",
                    "fontWeight": "500",
                    "letterSpacing": "-0.01rem",
                    "minWidth": "8rem",
                    "padding": "0.375rem 0.625rem ",
                    "position": "relative",
                },
                item_style={
                    "color": "currentColor",
                    "display": "flex",
                    "paddingBottom": "0px",
                    "justifyContent": "space-between",
                },
                label_style={"color": rx.color("slate", 9), "fontWeight": "500"},
                cursor={"opacity": "0"},
                separator="",
            ),
            data=data,
            width="100%",
            height=250,
            class_name="[&_.recharts-tooltip-item-unit]:text-slate-9 [&_.recharts-tooltip-item-unit]:font-mono [&_.recharts-tooltip-item-value]:!text-slate-12 [&_.recharts-tooltip-item-value]:!font-mono  [&_.recharts-tooltip-item-value]:mr-[0.2rem] [&_.recharts-tooltip-item]:flex [&_.recharts-tooltip-item]:items-center [&_.recharts-tooltip-item-name]:text-slate-9 [&_.recharts-tooltip-item-list]:flex [&_.recharts-tooltip-item-list]:flex-col [&_.recharts-tooltip-item-name]:pr-[3rem] [&_.recharts-tooltip-item-separator]:w-full",
            # class_name="[&_.recharts-tooltip-item-unit]:text-slate-9 [&_.recharts-tooltip-item-unit]:font-mono [&_.recharts-tooltip-item-value]:!text-slate-12 [&_.recharts-tooltip-item-value]:!font-mono  [&_.recharts-tooltip-item-value]:mr-[0.2rem] [&_.recharts-tooltip-item]:flex [&_.recharts-tooltip-item]:items-center [&_.recharts-tooltip-item]:before:content-[''] [&_.recharts-tooltip-item]:before:size-2.5 [&_.recharts-tooltip-item]:before:rounded-[2px] [&_.recharts-tooltip-item]:before:shrink-0 [&_.recharts-tooltip-item]:before:!bg-[currentColor] [&_.recharts-tooltip-item-name]:text-slate-9 [&_.recharts-tooltip-item-list]:flex [&_.recharts-tooltip-item-list]:flex-col [&_.recharts-tooltip-item-name]:pr-[3rem] [&_.recharts-tooltip-item-name]:pl-1.5 [&_.recharts-tooltip-item-separator]:w-full",
        ),
    )


def bar_chart():
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
            rx.tabs.content(create_chart(data), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(data2), value="2", margin_top="-5px"),
            default_value="1",
            width="100%",
            height="100%",
        ),
        rx.divider(class_name="w-full opacity-0 p-2"),
        rx.hstack(
            rx.hstack(
                rx.box(
                    class_name="w-2 h-2 p-1 rounded-sm shadow-sm",
                    bg=rx.color("accent", 6),
                ),
                rx.text("Successful", class_name="text-sm font-regular"),
                align="center",
            ),
            rx.text("784", class_name="text-sm font-semibold"),
            width="100%",
            align="center",
            justify="between",
        ),
        rx.divider(class_name="w-full opacity-50"),
        rx.hstack(
            rx.hstack(
                rx.box(
                    class_name="w-2 h-2 p-1 rounded-sm shadow-sm",
                    bg=rx.color("ruby", 6),
                ),
                rx.text("Refunded", class_name="text-sm font-regular"),
                align="center",
            ),
            rx.text("342", class_name="text-sm font-semibold"),
            width="100%",
            align="center",
            justify="between",
        ),
        width="100%",
        height="100%",
    )


def bar_chart_2():
    return rx.vstack(
        rx.text("Online Transactions", class_name="text-md font-semibold pb-3"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Europe", class_name="text-sm font-semibold"),
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Asia", class_name="text-sm font-semibold"),
                    value="2",
                ),
                rx.tabs.trigger(
                    rx.text("North America", class_name="text-sm font-semibold"),
                    value="3",
                ),
            ),
            rx.tabs.content(create_chart(data), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(data2), value="2", margin_top="-5px"),
            rx.tabs.content(create_chart(data3), value="3", margin_top="-5px"),
            default_value="1",
            width="100%",
            height="100%",
        ),
        # rx.divider(class_name="w-full opacity-0 p-2"),
        # rx.hstack(
        #     rx.hstack(
        #         rx.box(
        #             class_name="w-2 h-2 p-1 rounded-sm shadow-sm",
        #             bg=rx.color("accent", 6),
        #         ),
        #         rx.text("Successful", class_name="text-sm font-regular"),
        #         align="center",
        #     ),
        #     rx.text("784", class_name="text-sm font-semibold"),
        #     width="100%",
        #     align="center",
        #     justify="between",
        # ),
        # rx.divider(class_name="w-full opacity-50"),
        # rx.hstack(
        #     rx.hstack(
        #         rx.box(
        #             class_name="w-2 h-2 p-1 rounded-sm shadow-sm",
        #             bg=rx.color("ruby", 6),
        #         ),
        #         rx.text("Refunded", class_name="text-sm font-regular"),
        #         align="center",
        #     ),
        #     rx.text("342", class_name="text-sm font-semibold"),
        #     width="100%",
        #     align="center",
        #     justify="between",
        # ),
        width="100%",
        height="100%",
    )


def create_alternating_chart(data, colors, active):
    return rx.recharts.bar_chart(
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
        height=350,
        bar_size=18,
        bar_category_gap="30%",
    )


class State(rx.State):
    defi: str = "1"

    async def change_bar(self, value):
        self.defi = value


def bar_chart_3():
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
            height="100%",
        ),
        width="100%",
        height="100%",
    )


scat = [
    {"name": " ", "x": 10, "y": 30},
    {"name": "B", "x": 20, "y": 50},
    {"name": "C", "x": 30, "y": 70},
    {"name": "D", "x": 40, "y": 20},
    {"name": "E", "x": 50, "y": 90},
    {"name": "F", "x": 60, "y": 40},
    {"name": "G", "x": 70, "y": 60},
    {"name": "H", "x": 80, "y": 100},
    {"name": "I", "x": 90, "y": 10},
    {"name": " ", "x": 100, "y": 80},
]

scat_2 = [
    {"name": "K", "x": 5, "y": 15},
    {"name": "L", "x": 15, "y": 40},
    {"name": "M", "x": 25, "y": 60},
    {"name": "N", "x": 35, "y": 10},
    {"name": "O", "x": 45, "y": 80},
    {"name": "P", "x": 55, "y": 30},
    {"name": "Q", "x": 65, "y": 50},
    {"name": "R", "x": 75, "y": 90},
    {"name": "S", "x": 85, "y": 20},
    {"name": "T", "x": 95, "y": 70},
]


def scatter_example():
    return rx.fragment(
        rx.hstack(
            rx.foreach(
                [
                    ["Data 1", "blue"],
                    ["Data 2", "orange"],
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
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.scatter_chart(
            rx.recharts.scatter(data=scat, data_key="name"),
            rx.recharts.scatter(data=scat_2, data_key="name", fill=rx.color("orange")),
            rx.recharts.y_axis(
                data_key="y",
                hide=True,
            ),
            rx.recharts.x_axis(
                data_key="x",
                type_="number",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            width="100%",
            height=350,
            class_name="px-4",
        ),
    )
