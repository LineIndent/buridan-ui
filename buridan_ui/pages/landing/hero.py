import os

import reflex as rx

from .wrapper.wrapper import (
    button,
    button_with_key,
    landing_page_section_wrapper,
    landing_page_section_wrapper_main,
)
from .style import LandingPageStyle

from .features.feature import feature

from .bindings import key_bindings

from .items.pantry import landing_page_pantry_items
from .items.charts import landing_page_chart_items
from .items.credits import credit_banner

from ...templates.footer.footer import footer
from ...templates.drawer.drawer import drawer
from ...templates.navigation.navigation import landing_page_navigation
from ...templates.background.background import landing_page_grid_background

from ...states.routing import SiteRoutingState


def count_python_files_in_folder(folder_name):
    total_files = 0

    for dirpath, dirnames, filenames in os.walk(folder_name):
        total_files += len([f for f in filenames if f.endswith(".py")])

    return total_files


def landing_page() -> rx.vstack:
    return rx.vstack(
        rx.script(key_bindings()),
        drawer(),
        landing_page_grid_background(),
        credit_banner(),
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="10em", opacity="0"),
            landing_page_section_wrapper_main(
                "Powered by Reflex",
                "Build your next web app, faster than ever.",
                "Beautifully designed, expertly crafted components and templates built for the Reflex framework, empowering you to develop web apps in pure Python.",
            ),
            rx.divider(height="4em", opacity="0"),
            landing_page_section_wrapper(
                "Full Stack Features",
                "UI components designed with Reflex, all created using Python",
                "A full-stack framework complete with built-in features, including a comprehensive theming system, ready-to-use UI components, and customizable elements.",
                "Get started with buridan/ui →",
                "/getting-started/installation",
                [rx.box(feature(), padding="2em 0em", width="100%")],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "Pantry Components",
                "Beautifully crafted UI components, ready for your next project.",
                f"Over {count_python_files_in_folder('buridan_ui/pantry')}+ professionally designed, fully responsive, expertly crafted UI components you can seamlessly integrate into your Reflex projects and customize as needed.",
                "Browse pantry items →",
                "/pantry/animations",
                [landing_page_pantry_items()],
            ),
            rx.divider(height="2em", opacity="0"),
            rx.text(
                "There’s so much more to discover here. ",
                rx.link(
                    "View all pantry items now →",
                    on_click=SiteRoutingState.toggle_page_change(
                        {"name": "Animations", "path": "/pantry/animations"}
                    ),
                ),
                size="2",
                weight="medium",
                color=rx.color("slate", 11),
                width="100%",
                align="center",
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "Chart Components",
                "Powerful charting components, designed to visualize your data effortlessly.",
                f"Explore {count_python_files_in_folder('buridan_ui/charts')}+ beautifully designed, fully responsive chart components ready to enhance your Reflex projects and visualize your data effectively.",
                "Browse chart items →",
                "/charts/area-charts",
                [landing_page_chart_items()],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "buridan/ui",
                "Almost there, one click to launch your web application!",
                "Download and install Reflex to bring your ideas to life, or explore our Getting Started pages for comprehensive guidance and resources.",
                "",
                "",
                [
                    rx.hstack(
                        button(
                            "play",
                            "Getting Started",
                            "solid",
                            SiteRoutingState.toggle_page_change(
                                {
                                    "name": "Introduction",
                                    "path": "/getting-started/introduction",
                                }
                            ),
                        ),
                        button_with_key(
                            "github",
                            "X",
                            "Reflex GitHub Page",
                            "surface",
                            rx.redirect("https://github.com/reflex-dev/reflex"),
                        ),
                        width="100%",
                        max_width="30em",
                        display="grid",
                        grid_template_columns=[
                            f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 2, 2]
                        ],
                    ),
                ],
            ),
            rx.divider(height="5em", opacity="0"),
            footer(),
            rx.divider(height="2em", opacity="0"),
            **LandingPageStyle.content,
        ),
        **LandingPageStyle.base,
    )
