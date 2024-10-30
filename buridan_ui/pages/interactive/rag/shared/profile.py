import reflex as rx

from ..style import Style
from ..wrappers.item import app_profile_item_wrapper

from ..shared.profile_components import (
    profile_item_physical_stats,
    profile_item_unit,
    profile_item_activity_stats,
)

from ..state import State


physical_stats = rx.hstack(
    profile_item_physical_stats(State.height, "height", State.set_height),
    profile_item_physical_stats(State.weight, "weight", State.set_weight),
    profile_item_physical_stats(State.age, "age", State.set_age),
    spacing="6",
    padding="5px 0px",
    display="grid",
    width="100%",
    grid_template_columns=[f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 3, 3, 3]],
)

L1 = ["sedentary", "active", "moderately active", "very active", "super active"]
L2 = [f"{i + 1} day per week" + ("s" if i > 0 else "") for i in range(7)]
L3 = ["light", "moderate", "intense"]
L4 = [f"{i + 1} hour per night" + ("s" if i > 0 else "") for i in range(9)]

activity_stats = rx.vstack(
    rx.hstack(
        profile_item_activity_stats("Occupation Type", L1),
        profile_item_activity_stats("Exercise Frequency", L2),
        **Style.profile_activity_stat_hstack,
    ),
    rx.hstack(
        profile_item_activity_stats("Exercise Intensity", L3),
        profile_item_activity_stats("Sleep Pattern", L4),
        **Style.profile_activity_stat_hstack,
    ),
    width="100%",
    gap=["12px" if i <= 3 else "32px" for i in range(6)],
)


H1 = ["weight loss", "muscle gain", "maintenance"]
H2 = [f"{i} month" + ("s" if i > 1 else "") for i in [1, 3, 6, 12]]


health_goals = rx.vstack(
    rx.hstack(
        profile_item_activity_stats("Primary Goal", H1),
        profile_item_activity_stats("Timeframe", H2),
        **Style.profile_activity_stat_hstack,
    ),
    width="100%",
    gap=["12px" if i <= 3 else "32px" for i in range(6)],
)

D1 = [
    "vegetarian",
    "vegan",
    "gluten-free",
    "paleo",
    "ketogenic",
    "low-carb",
    "dairy-free",
    "none",
]

D2 = ["nuts", "shellfish", "dairy", "gluten", "soy", "eggs", "wheat", "none"]


diet_restrictions = rx.vstack(
    rx.hstack(
        profile_item_activity_stats("Dietary Restrictions", D1),
        profile_item_activity_stats("Food Allergies", D2),
        **Style.profile_activity_stat_hstack,
    ),
    width="100%",
    gap=["12px" if i <= 3 else "32px" for i in range(6)],
)


def app_profile_panel() -> rx.vstack:
    return rx.vstack(
        rx.divider(height="5em", opacity="0"),
        rx.box(
            rx.vstack(
                app_profile_item_wrapper(
                    "Select the unit of measurements for your data.",
                    "Unit Measurement",
                    [profile_item_unit()],
                ),
                app_profile_item_wrapper(
                    "Enter details about your physical characteristics.",
                    "Physical Stats",
                    [physical_stats],
                ),
                app_profile_item_wrapper(
                    "Help us understand your daily lifestyle and activity level.",
                    "Lifestyle & Activity Level",
                    [activity_stats],
                ),
                app_profile_item_wrapper(
                    "Tell us about your health and fitness goals.",
                    "Health Goals",
                    [health_goals],
                ),
                app_profile_item_wrapper(
                    "Let us know your dietary preferences and restrictions.",
                    "Dietary Preferences",
                    [diet_restrictions],
                ),
                **Style.profile_inner_content,
            ),
            padding=["0em 4em" if i >= 5 else "0em 2em" for i in range(6)],
            width="100%",
        ),
        **Style.profile_base,
    )
