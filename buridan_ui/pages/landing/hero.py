import os

import reflex as rx

from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import footer
from buridan_ui.templates.navigation.navigation import landing_page_navigation

from .features.feature import feature
from .hero_grid_layout import responsive_grid, create_grid_item
from .hero_landing.hero import hero
from .items.charts import landing_page_chart_items
from .items.pantry import landing_page_pantry_items
from .style import LandingPageStyle
from .wrapper.wrapper import (
    landing_page_section_wrapper,
    landing_page_section_wrapper_main,
)

from buridan_ui.charts.bar.v1 import barchart_v1
from buridan_ui.charts.bar._bar_test import *
from buridan_ui.pantry.menus.v1 import menus_v1
from buridan_ui.charts.line.v4 import linechart_v4
from buridan_ui.analytics.stats.v1 import stats_v1
from buridan_ui.pantry.tables.v2 import _tables_v2
from buridan_ui.pantry.inputs.v4 import _inputs_v4
from buridan_ui.pantry.subscribe.v1 import subscribe_v1
from ...wrappers.shared.scheme import component_wrapper_color_scheme_hero


def count_python_files_in_folder(folder_name):
    total_files = 0

    for _dirpath, _dirnames, filenames in os.walk(folder_name):
        total_files += len([f for f in filenames if f.endswith(".py")])

    return total_files


sum = count_python_files_in_folder("buridan_ui/charts") + count_python_files_in_folder(
    "buridan_ui/pantry"
)


def landing_page() -> rx.vstack:
    return rx.vstack(
        drawer(),
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="4em", opacity="0"),
            landing_page_section_wrapper_main(
                # "Build your next web app faster than ever",
                # "Beautifully designed, expertly crafted components and templates built for the Reflex framework, empowering you to develop web apps in pure Python.",
                "Reflex components to build your web apps faster than ever",
                f"Access {sum}+ high-quality, open-source components and templates for building production-ready web apps. Designed for the Reflex framework and Python.",
            ),
            responsive_grid(
                create_grid_item(barchart_v1(), 1, 1, 2),
                create_grid_item(bar_chart_2(), 1, 1, 1),
                lg=3,
            ),
            responsive_grid(
                rx.box(
                    create_grid_item(menus_v1(), 1, 1, 1),
                    create_grid_item(component_wrapper_color_scheme_hero(), 1, 1, 1),
                    create_grid_item(subscribe_v1(), 1, 1, 1),
                    create_grid_item(_inputs_v4(), 1, 1, 1),
                    class_name="col-span-1 lg:col-span-1 flex flex-col gap-4",
                ),
                rx.box(
                    create_grid_item(stats_v1(), 1, 1, 1),
                    create_grid_item(linechart_v4(), 1, 1, 1),
                    class_name="col-span-1 lg:col-span-1 flex flex-col gap-4",
                ),
                lg=2,
            ),
            responsive_grid(
                create_grid_item(_tables_v2(), 1, 1, 1),
                lg=1,
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
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "Chart Components",
                "Visualize your data with powerful charts.",
                f"Explore {count_python_files_in_folder('buridan_ui/charts')}+ beautifully designed, fully responsive chart components ready to enhance your Reflex projects. Control? You got it.",
                "Browse chart items →",
                "/charts/ui",
                [landing_page_chart_items()],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "buridan/ui",
                "Almost there, one click to launch your web application!",
                "Download and install Reflex to bring your ideas to life, or explore our Getting Started pages for comprehensive guidance and resources.",
                "Check out Reflex →",
                "https://reflex.dev/",
                [],
            ),
            rx.divider(height="6em", opacity="0"),
            footer(),
            rx.divider(height="2em", opacity="0"),
            **LandingPageStyle.content,
        ),
        **LandingPageStyle.base,
    )
