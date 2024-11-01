import os

import reflex as rx

from .navigation.navigation import landing_page_navigation
from .wrapper.wrapper import (
    landing_page_main_button,
    landing_page_section_wrapper,
    landing_page_features_wrapper,
    landing_page_section_wrapper_main,
)
from .style import LandingPageStyle

from .footer.footer import landing_page_footer

from .items.pantry import landing_page_pantry_items
from .items.charts import landing_page_chart_items

from ...templates.shared.drawbar import drawbar


def count_python_files_in_folder(folder_name):
    total_files = 0

    for dirpath, dirnames, filenames in os.walk(folder_name):
        total_files += len([f for f in filenames if f.endswith(".py")])

    return total_files


def create_landing_background(top: str, left: str):
    return rx.box(
        background_size="30px 30px",
        background_image=f"radial-gradient(circle, {rx.color('slate', 12)} 0.75px, transparent 1px)",
        mask=(
            "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
            "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
        ),
        width="100%",
        height="100vh",
        position="absolute",
        top=top,
        left=left,
        z_index="-2",
    )


@rx.page("/", title="Home - buridan-ui ")
def landing_page() -> rx.vstack:
    return rx.vstack(
        drawbar(),
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="4em", opacity="0"),
            landing_page_section_wrapper_main(
                "Powered by Reflex",
                "Build your next web app, faster than ever.",
                "Beautifully designed, expertly crafted components and templates built for the Reflex framework, empowering you to develop web apps in pure Python. The perfect foundation for your next project.",
            ),
            landing_page_section_wrapper(
                "Full Stack Features",
                "UI components designed with Reflex, all created using Python",
                "A full-stack framework complete with built-in features, including a comprehensive theming system, ready-to-use UI components, and customizable elements.",
                "Get started with buridan/ui →",
                [
                    rx.hstack(
                        landing_page_features_wrapper(
                            "Easily adjust colors, fonts, and styles to create a unique look that enhances your application's user experience.",
                            "Fully Customizable Components",
                            "component",
                        ),
                        landing_page_features_wrapper(
                            "Component Theming offers ready-to-use light and dark modes, allowing you to switch seamlessly between styles.",
                            "Light & Dark Mode",
                            "sun-moon",
                        ),
                        landing_page_features_wrapper(
                            "Our components are available under an open source license, empowering you to use, modify, and share them freely.",
                            "Open Source License",
                            "code",
                        ),
                        padding="2em 0em",
                        width="100%",
                        display="grid",
                        gap="2rem",
                        grid_template_columns=[
                            f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 3, 3, 3]
                        ],
                    )
                ],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "Pantry Components",
                "Beautifully crafted UI components, ready for your next project.",
                f"Over {count_python_files_in_folder('buridan_ui/pantry')}+ professionally designed, fully responsive, expertly crafted UI components you can seamlessly integrate into your Reflex projects and customize as needed.",
                "Browse all pantry pantry →",
                [landing_page_pantry_items()],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "Chart Components",
                "Powerful charting components, designed to visualize your data effortlessly.",
                f"Explore {count_python_files_in_folder('buridan_ui/charts')}+ beautifully designed, fully responsive chart components ready to enhance your Reflex projects and visualize your data effectively.",
                "Browse all charts →",
                [landing_page_chart_items()],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_section_wrapper(
                "buridan/ui",
                "Almost there, one click to launch your web application!",
                "Download and install Reflex to bring your ideas to life, or explore our 'Getting Started' pages for comprehensive guidance and resources.",
                "",
                [
                    rx.hstack(
                        landing_page_main_button(
                            "Installation",
                            "solid",
                            on_click=rx.redirect("/getting-started/installation"),
                        ),
                        landing_page_main_button(
                            "pip install reflex",
                            "surface",
                            on_click=rx.set_clipboard("pip install reflex"),
                        ),
                    ),
                ],
            ),
            rx.divider(height="5em", opacity="0"),
            landing_page_footer(),
            rx.divider(height="2em", opacity="0"),
            **LandingPageStyle.content,
        ),
        create_landing_background("0", "0"),
        **LandingPageStyle.base,
    )
