import reflex as rx

from .style import LandingPageNavigationStyle
from ....templates.shared.navbar import right_items, left_items


def landing_page_navigation():
    return rx.hstack(left_items(), right_items(), **LandingPageNavigationStyle.style)
