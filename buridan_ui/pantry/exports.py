import os
import reflex as rx

from random import randint
from buridan_ui.wrappers.component.wrapper import component_wrapper

from .animations.v1 import animation_v1
from .animations.v2 import animation_v2
from .animations.v3 import animation_v3
from .animations.v4 import animation_v4
from .animations.v5 import animation_v5
from .animations.v6 import animation_v6
from .backgrounds.v1 import background_v1
from .backgrounds.v2 import background_v2
from .backgrounds.v3 import background_v3
from .backgrounds.v4 import background_v4
from .cards.v1 import card_v1
from .cards.v2 import card_v2
from .cards.v3 import card_v3
from .faq.v1 import faq_v1
from .featured.v1 import featured_v1
from .featured.v2 import featured_v2
from .footers.v1 import footer_v1
from .footers.v2 import footer_v2
from .forms.v1 import forms_v1
from .forms.v2 import forms_v2
from .forms.v3 import forms_v3
from .inputs.v1 import inputs_v1
from .inputs.v2 import inputs_v2
from .inputs.v3 import inputs_v3
from .inputs.v4 import inputs_v4
from .lists.v1 import lists_v1
from .logins.v1 import logins_v1
from .logins.v2 import logins_v2
from .menus.v1 import menus_v1
from .onboardings.v1 import onboardings_v1
from .payments.v1 import payments_v1
from .popups.v1 import popups_v1
from .popups.v2 import popups_v2
from .pricing.v1 import pricing_v1
from .pricing.v2 import pricing_v2
from .prompts.v1 import prompt_v1
from .prompts.v2 import prompt_v2
from .subscribe.v1 import subscribe_v1
from .subscribe.v2 import subscribe_v2
from .tables.v1 import tables_v1
from .tables.v2 import tables_v2
from .tables.v3 import tables_v3
from .tables.v4 import tables_v4
from .timeline.v1 import timeline_v1

BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/pantry/"


def get_source(directory: str, filename: str):
    with open(os.path.join("buridan_ui", "pantry", directory, filename)) as file:
        return file.read()


def create_export(func, directory, version):
    @component_wrapper(f"{BASE_PATH}{directory}/v{version}.py")
    def export():
        return [
            func(),
            get_source(directory, f"v{version}.py"),
            # randint(0, 100000),
            # rx.spacer(),
        ]

    return export


pantry_exports_config = {
    "logins": [
        create_export(logins_v1, "logins", 1),
        create_export(logins_v2, "logins", 2),
    ],
    "tables": [
        create_export(tables_v1, "tables", 1),
        create_export(tables_v2, "tables", 2),
        create_export(tables_v3, "tables", 3),
        create_export(tables_v4, "tables", 4),
    ],
    "menus": [create_export(menus_v1, "menus", 1)],
    "backgrounds": [
        create_export(background_v1, "backgrounds", 1),
        create_export(background_v2, "backgrounds", 2),
        create_export(background_v3, "backgrounds", 3),
        create_export(background_v4, "backgrounds", 4),
    ],
    "payments": [create_export(payments_v1, "payments", 1)],
    "forms": [
        create_export(forms_v1, "forms", 1),
        create_export(forms_v2, "forms", 2),
        create_export(forms_v3, "forms", 3),
    ],
    "featured": [
        create_export(featured_v1, "featured", 1),
        create_export(featured_v2, "featured", 2),
    ],
    "lists": [create_export(lists_v1, "lists", 1)],
    "timeline": [create_export(timeline_v1, "timeline", 1)],
    "onboardings": [create_export(onboardings_v1, "onboardings", 1)],
    "pricing": [
        create_export(pricing_v1, "pricing", 1),
        create_export(pricing_v2, "pricing", 2),
    ],
    "popups": [
        create_export(popups_v1, "popups", 1),
        create_export(popups_v2, "popups", 2),
    ],
    "animations": [
        create_export(animation_v1, "animations", 1),
        create_export(animation_v2, "animations", 2),
        create_export(animation_v6, "animations", 6),
        create_export(animation_v3, "animations", 3),
        create_export(animation_v4, "animations", 4),
        create_export(animation_v5, "animations", 5),
    ],
    "prompts": [
        create_export(prompt_v1, "prompts", 1),
        create_export(prompt_v2, "prompts", 2),
    ],
    "cards": [
        create_export(card_v3, "cards", 3),
        create_export(card_v1, "cards", 1),
        create_export(card_v2, "cards", 2),
    ],
    "subscribe": [
        create_export(subscribe_v1, "subscribe", 1),
        create_export(subscribe_v2, "subscribe", 2),
    ],
    "faq": [
        create_export(faq_v1, "faq", 1),
    ],
    "footers": [
        create_export(footer_v1, "footers", 1),
        create_export(footer_v2, "footers", 2),
    ],
    "inputs": [
        create_export(inputs_v1, "inputs", 1),
        create_export(inputs_v2, "inputs", 2),
        create_export(inputs_v3, "inputs", 3),
        create_export(inputs_v4, "inputs", 4),
    ],
}
