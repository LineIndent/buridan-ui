import reflex as rx


def create_grid_item_chart_section(
    component: rx.Component,
    footer: rx.Component,
    sm_span: int = 1,
    md_span: int = 1,
    lg_span: int = 1,
    padding: int = 0,
) -> rx.Component:

    span_classes = (
        f"col-span-{sm_span} "
        f"sm:col-span-{sm_span} "
        f"md:col-span-{md_span} "
        f"lg:col-span-{lg_span} "
    )

    return rx.box(
        rx.box(
            component,
            border=f"1px solid {rx.color('gray', 4)}",
            class_name=f"{span_classes} p-{padding} rounded-2xl h-full shadow-md z-10",
        ),
        footer,
        # border=f"1px solid {rx.color('gray', 4)}",
        class_name=f"{span_classes} p-2 rounded-2xl h-full flex flex-col inset-shadow-sm",
    )


def create_grid_item(
    component: rx.Component,
    sm_span: int = 1,
    md_span: int = 1,
    lg_span: int = 1,
    padding: int = 4,
) -> rx.Component:

    span_classes = (
        f"col-span-{sm_span} "
        f"sm:col-span-{sm_span} "
        f"md:col-span-{md_span} "
        f"lg:col-span-{lg_span} "
    )

    return rx.box(
        rx.box(
            component,
            border=f"1px solid {rx.color('gray', 4)}",
            class_name=f"{span_classes} p-{padding} rounded-lg border-2 border-solid shadow-sm h-full",
        ),
        border=f"1px solid {rx.color('gray', 5)}",
        class_name=f"{span_classes} p-2 rounded-lg shadow-lg h-full",
    )


def responsive_grid(
    *children: rx.Component,
    lg: int = 1,
    md: int = 1,
    sm: int = 1,
    gap: int = 4,
    padding: int = 4,
) -> rx.Component:
    """
    Create a responsive grid layout.
    Args:
        *children: The grid items (created using `create_grid_item`).
        lg: Number of columns for large screens (default: 1).
        md: Number of columns for medium screens (default: 1).
        sm: Number of columns for small screens (default: 1).
        gap: The gap between grid items (default: 4).
        padding: The padding around the grid (default: 8).
    Returns:
        A responsive grid component.
    Example:
        from blocks import base_layout, line_chart, area_chart, bar_chart, pie_chart, dashboard_base_layout
        class State(rx.State):
            data: list[dict[str, str | int]] = [
                {"month": "Jan", "desktop": 186, "mobile": 80},
                {"month": "Feb", "desktop": 305, "mobile": 200},
                {"month": "Mar", "desktop": 237, "mobile": 120},
                {"month": "Apr", "desktop": 73, "mobile": 190},
                {"month": "May", "desktop": 209, "mobile": 130},
                {"month": "Jun", "desktop": 214, "mobile": 140},
            ]
        line = line_chart(data=State.data, x="month", y=["desktop", "mobile"])
        area = area_chart(data=State.data, x="month", y=["desktop", "mobile"])
        bar = bar_chart(data=State.data, x="month", y=["desktop", "mobile"])
        pie = pie_chart(data=State.data, data_key='desktop', name_key='month')
        def example_grid() -> rx.Component:
            return  dashboard_base_layout(
                main=responsive_grid(
                    create_grid_item(area),
                    create_grid_item(bar),
                    create_grid_item(area),
                    create_grid_item(bar, md_span=3, lg_span=3),
                    create_grid_item(line, md_span=2, lg_span=2),
                    create_grid_item(pie),
                    create_grid_item(line),
                    create_grid_item(area, md_span=2, lg_span=2),
                    lg=3,
                    md=2,
                    sm=1,
                    gap=4,
                    padding=8,
                )
            )
    """

    # Generate Tailwind classes for each breakpoint
    breakpoint_classes = (
        f"sm:grid-cols-{sm} "  # Small screens
        f"md:grid-cols-{md} "  # Medium screens
        f"lg:grid-cols-{lg} "  # Large screens
    )

    return rx.grid(
        *children,
        class_name=f"grid grid-cols-1 {breakpoint_classes} gap-{gap} p-{padding} size-full",
    )
