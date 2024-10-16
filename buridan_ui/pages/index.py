import asyncio

import reflex as rx

from .thumbnail_items.exports import export_thumbnail
from ..routes.chart_routes import CHART_ROUTES
from ..styles.base import ACTIVE
from ..templates.shared.drawbar import drawbar

from ..templates.shared.navbar import right_items, left_items, NAVBAR
from ..routes.pantry_routes import PANTRY_ROUTES
from ..templates.shared.sidebar import Sidebar


def wrapper(title: str, instructions: str, tag: str):

    return rx.hstack(
        rx.vstack(
            rx.text(title, size="2", weight="bold", color=rx.color("slate", 12)),
            rx.text(instructions, size="2", weight="bold", color=rx.color("slate", 11)),
            width="100%",
            spacing="1",
            align="start",
            justify="start",
            text_align="start",
        ),
        rx.box(
            background_size="16px 16px",
            background_image=f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            mask=f"radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="100%",
            position="absolute",
        ),
        rx.icon(
            tag=tag,
            size=26,
            position="absolute",
            bottom="16px",
            right="16px",
        ),
        align="start",
        justify="start",
        position="relative",
        flex="1 1 300px",
        height="220px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 3),
        border_radius="12px",
        padding="16px",
        overflow="hidden",
        z_index="30",
        box_shadow="0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
    )


def create_background():
    return rx.box(
        background_size="90px 90px",
        background_image=(
            "linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)"
        ),
        mask=(
            "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
            "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
        ),
        width="100%",
        height="100%",
        position="absolute",
        z_index="1",
    )


def create_navigation():
    return rx.hstack(
        left_items(),
        right_items(),
        top="0",
        width="100%",
        max_width="70em",
        z_index="100",
        align="center",
        position="fixed",
        justify="between",
        padding="13px 0px 12px 18px",
        backdrop_filter="blur(2.5px)",
        border_bottom=f"1px solid {rx.color('gray', 5)}",
    )


ROOT = dict(
    width="100%",
    align="center",
    justify="start",
    overflow="scroll",
    padding="0px 12px",
    min_height="100vh",
    background=rx.color("gray", 3),
)

CONTENT = dict(
    spacing="1",
    z_index="50",
    width="100%",
    padding="12px",
    align="center",
    justify="start",
    max_width="70em",
    text_align="center",
)


def create_section_header(title: str, description: str):
    return rx.vstack(
        rx.heading(
            title,
            weight="bold",
            font_size=[f"{i}rem" for i in [2, 3, 3, 3, 3.5, 3.5]],
            line_height="1.25",
            font_family="var(--chakra-fonts-serif)",
            color=rx.color("slate", 12),
        ),
        rx.text(
            description,
            font_size=[f"{i}px" for i in [14, 14, 16, 16, 18, 18]],
            weight="medium",
            max_width="45em",
            color=rx.color("slate", 11),
        ),
        width="100%",
        text_align="center",
        padding="14px 0px",
        transition="all 350ms linear",
        align="center",
    )


def create_footer_item(title: str, item_list: list[dict[str, str]]):
    return rx.vstack(
        rx.text(title, weight="bold", size="2", color=rx.color("slate", 12)),
        rx.hstack(
            *[
                rx.hstack(
                    rx.link(
                        rx.text(
                            item["name"],
                            weight="bold",
                            size="1",
                            text_align="start",
                            color=rx.color("slate", 11),
                            on_click=Sidebar.delta_page(item),
                        ),
                        href=item["path"],
                        is_external=True,
                    ),
                    rx.cond(
                        item.get("is_beta", ""),
                        rx.badge("Beta", color_scheme="orange"),
                        rx.spacer(),
                    ),
                    align="center",
                )
                for item in item_list
            ],
            display="grid",
            grid_template_columns=[
                f"repeat({i}, minmax(0, 1fr))" for i in [2, 2, 3, 3, 3, 4]
            ],
            justify="start",
            width="100%",
            gap="1rem 3rem",
        ),
        width="100%",
    )


class Index(rx.State):
    default_icon: bool = True

    async def toggle_icon(self):
        self.default_icon = False
        yield
        await asyncio.sleep(1)
        self.default_icon = True


@rx.page("/", "buridan-ui")
def index():
    return rx.vstack(
        drawbar(),
        create_navigation(),
        rx.vstack(
            rx.divider(height="10em", opacity="0"),
            rx.vstack(
                rx.hstack(
                    *[
                        rx.badge(
                            rx.heading(
                                name,
                                size="2",
                                letter_spacing="-1px",
                                font_family="var(--chakra-fonts-serif)",
                                color=rx.color("slate", 11),
                            ),
                            variant="surface",
                            color_scheme="gray",
                        )
                        for name in ["Accessible", "Modern", "Open Source"]
                    ],
                    align="center",
                    z_index="20",
                ),
                rx.heading(
                    "A Component Library Built With ",
                    rx.text.em("Reflex"),
                    weight="bold",
                    font_family="var(--chakra-fonts-serif)",
                    font_size=[f"{i}rem" for i in [2.5, 3, 3, 4, 4.5, 4.5]],
                    line_height="1.25",
                    color=rx.color("slate", 12),
                ),
                rx.text(
                    "Speed up your development with ready-made components designed for seamless integration. Create stunning applications effortlessly!",
                    font_size=[f"{i}px" for i in [14, 14, 16, 16, 18, 18]],
                    weight="medium",
                    color=rx.color("slate", 11),
                    max_width="45em",
                    align="center",
                ),
                rx.hstack(
                    rx.button(
                        rx.link(
                            "Getting Started",
                            href="/getting-started/introduction",
                            text_decoration="none",
                            _hover={"color": rx.color("slate", 12)},
                        ),
                        variant="surface",
                        cursor="pointer",
                        flex="4",
                        size="3",
                        color_scheme="gray",
                        z_index="20",
                    ),
                    rx.button(
                        rx.link(
                            "Pantry",
                            href="/pantry/animations",
                            text_decoration="none",
                            _hover={"color": rx.color("slate", 12)},
                        ),
                        cursor="pointer",
                        variant="soft",
                        color_scheme="gray",
                        flex="2",
                        size="3",
                        z_index="20",
                    ),
                    width="100%",
                    max_width="20em",
                    justify="center",
                    padding="24px 0px",
                ),
                width="100%",
                align="center",
                spacing="5",
            ),
            rx.divider(height="12em", opacity="0"),
            create_section_header(
                "Components Entirely Built With Reflex",
                "A full-stack framework complete with built-in features, including a comprehensive theming system, ready-to-use UI components, and customizable elements.",
            ),
            rx.hstack(
                wrapper(
                    "Fully Customizable Components",
                    "Easily adjust colors, fonts, and styles to create a unique look that enhances your application's user experience.",
                    "component",
                ),
                wrapper(
                    "Light & Dark Mode",
                    "Component Theming offers ready-to-use light and dark modes, allowing you to switch seamlessly between styles.",
                    "sun-moon",
                ),
                wrapper(
                    "Open Source License",
                    "Our components are available under an open source license, empowering you to use, modify, and share them freely.",
                    "code",
                ),
                gap="2rem",
                width="100%",
                display="grid",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 3, 3]
                ],
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            create_section_header(
                "Reflex Components",
                "Built on the Reflex framework, our components provide a set of prebuilt UI elements that streamline the development of responsive, web-based applications.",
            ),
            rx.hstack(
                *export_thumbnail,
                width="100%",
                display="grid",
                gap="1rem",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 2, 3, 4, 4]
                ],
                min_height="100vh",
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            create_section_header(
                "One Step Away From Shipping Your Web Application",
                "Download and install Reflex to start building out your idea, or check our the get started pages for more information.",
            ),
            rx.box(
                rx.hstack(
                    rx.button(
                        rx.link(
                            "Get Started",
                            href="/getting-started/introduction",
                            text_decoration="none",
                            _hover={"color": rx.color("slate", 12)},
                        ),
                        variant="surface",
                        color_scheme="gray",
                        cursor="pointer",
                        flex="2",
                        size="3",
                        z_index="20",
                    ),
                    rx.button(
                        "pip install reflex",
                        rx.cond(
                            Index.default_icon,
                            rx.icon(tag="clipboard-list", size=14),
                            rx.icon(
                                tag="check",
                                size=14,
                                color=rx.color("grass", 12),
                            ),
                        ),
                        variant="soft",
                        color_scheme="gray",
                        flex="3",
                        size="3",
                        z_index="20",
                        display="flex",
                        justify_content="space-between",
                        cursor="pointer",
                        on_click=[
                            Index.toggle_icon,
                            rx.set_clipboard("pip install reflex"),
                        ],
                    ),
                    width="100%",
                    justify="center",
                    padding="24px 0px",
                ),
                width="100%",
                max_width="25em",
            ),
            rx.divider(height="5em", opacity="0"),
            rx.vstack(
                rx.spacer(),
                rx.divider(height="15em", opacity="0"),
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "buridan/ui", size="5", font_weight="900", color=ACTIVE
                        ),
                        rx.hstack(
                            rx.link(
                                rx.icon(
                                    tag="github",
                                    size=18,
                                    color=rx.color("slate", 11),
                                ),
                                href="https://github.com/LineIndent/buridan-ui",
                                color_scheme="gray",
                                bg=rx.color("gray", 4),
                                border_radius="20%",
                                padding="3.5px",
                            ),
                            rx.link(
                                rx.icon(
                                    tag="youtube",
                                    size=18,
                                    color=rx.color("slate", 11),
                                ),
                                href="https://www.youtube.com/@lineindent",
                                color_scheme="gray",
                                bg=rx.color("gray", 4),
                                border_radius="20%",
                                padding="3.5px",
                            ),
                            align="center",
                        ),
                        rx.text(
                            "Copyright © 2024 Ahmad Hakim.",
                            size="1",
                            color=rx.color("slate", 11),
                            weight="bold",
                            height="100%",
                        ),
                        justify="center",
                        flex=["100%", "100%", "100%", "20%", "20%"],
                        align="start",
                    ),
                    rx.vstack(
                        create_footer_item(
                            "Home",
                            [
                                {
                                    "name": "Introduction",
                                    "path": "/getting-started/introduction",
                                },
                                {
                                    "name": "Installation",
                                    "path": "/getting-started/installation",
                                },
                                {
                                    "name": "Who is Buridan?",
                                    "path": "/getting-started/who-is-buridan",
                                },
                                {
                                    "name": "Interactive Tables",
                                    "path": "/interactive-table/dashboard",
                                    "is_beta": True,
                                },
                            ],
                        ),
                        rx.divider(height="1em", opacity="0"),
                        create_footer_item("Charts", CHART_ROUTES),
                        rx.divider(height="1em", opacity="0"),
                        create_footer_item("Pantry", PANTRY_ROUTES),
                        rx.divider(height="1em", opacity="0"),
                        create_footer_item(
                            "Resources",
                            [
                                {
                                    "name": "Reflex Framework",
                                    "path": "https://reflex.dev/",
                                },
                                {
                                    "name": "Source Code",
                                    "path": "https://github.com/LineIndent/buridan-ui",
                                },
                                {
                                    "name": "GitHub",
                                    "path": "https://github.com/LineIndent",
                                },
                                {
                                    "name": "@LineIndent",
                                    "path": "https://www.youtube.com/@lineindent",
                                },
                            ],
                        ),
                        rx.divider(height="1em", opacity="0"),
                        width="100%",
                        flex=["100%", "100%", "100%", "50%", "65%"],
                    ),
                    width="100%",
                    align="start",
                    flex_wrap=[
                        "wrap-reverse",
                        "wrap-reverse",
                        "wrap-reverse",
                        "wrap",
                        "wrap",
                    ],
                ),
                width="100%",
                border_top=f"1px solid {rx.color('gray', 12)}",
                padding="64px 0px 32px 0px",
                bg=rx.color("gray", 3),
                mask="linear-gradient(to top, hsl(0, 0%, 0%, 1) 50%, hsl(0, 0%, 0%, 0))",
                align="end",
                justify="between",
                z_index="50",
            ),
            **CONTENT,
        ),
        create_background(),
        **ROOT,
    )
