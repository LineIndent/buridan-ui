import os

import reflex as rx

from .wrapper.wrapper import landing_page_section_wrapper

from .style import LandingPageStyle
from .hero_landing.hero import hero
from .features.feature import feature

from .items.pantry import landing_page_pantry_items
from .items.charts import landing_page_chart_items

from ...templates.footer.footer import footer
from ...templates.drawer.drawer import drawer
from ...templates.navigation.navigation import landing_page_navigation


def count_python_files_in_folder(folder_name):
    total_files = 0

    for dirpath, dirnames, filenames in os.walk(folder_name):
        total_files += len([f for f in filenames if f.endswith(".py")])

    return total_files


def landing_page() -> rx.vstack:
    return rx.vstack(
        drawer(),
        rx.vstack(
            landing_page_navigation(),
            hero(),
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
                "Powerful charting components, designed to visualize your data effortlessly.",
                f"Explore {count_python_files_in_folder('buridan_ui/charts')}+ beautifully designed, fully responsive chart components ready to enhance your Reflex projects and visualize your data effectively.",
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
