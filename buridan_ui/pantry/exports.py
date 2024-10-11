import os
from random import randint

from .logins.v1 import logins_v1
from .logins.v2 import logins_v2

from .tables.v1 import tables_v1
from .tables.v2 import tables_v2
from .tables.v3 import tables_v3

from .menus.v1 import menus_v1

from .backgrounds.v1 import background_v1
from .backgrounds.v2 import background_v2
from .backgrounds.v3 import background_v3
from .backgrounds.v4 import background_v4

from .payments.v1 import payments_v1

from .forms.v1 import forms_v1
from .forms.v2 import forms_v2
from .forms.v3 import forms_v3

from .featured.v1 import featured_v1

from .lists.v1 import lists_v1

from .timeline.v1 import timeline_v1

from .onboardings.v1 import onboardings_v1

from .pricing.v1 import pricing_v1

from .popups.v1 import popups_v1
from .popups.v2 import popups_v2

from .animations.v1 import animation_v1
from .animations.v2 import animation_v2
from .animations.v3 import animation_v3
from .animations.v4 import animation_v4

from ..wrappers.item import item

BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/pantry/"


def get_source(directory: str, filename: str):
    with open(os.path.join("buridan_ui", "pantry", directory, filename), "r") as file:
        return file.read()


def create_export(func, directory, version):
    @item(f"{BASE_PATH}{directory}/v{version}.py")
    def export():
        return [func(), get_source(directory, f"v{version}.py"), randint(0, 100000)]

    return export


# Create exports for logins
export_logins_v1 = create_export(logins_v1, "logins", 1)
export_logins_v2 = create_export(logins_v2, "logins", 2)

# Create exports for tables
export_tables_v1 = create_export(tables_v1, "tables", 1)
export_tables_v2 = create_export(tables_v2, "tables", 2)
export_tables_v3 = create_export(tables_v3, "tables", 3)

# Create exports for menus
export_menus_v1 = create_export(menus_v1, "menus", 1)

# Create exports for backgrounds
export_backgrounds_v1 = create_export(background_v1, "backgrounds", 1)
export_backgrounds_v2 = create_export(background_v2, "backgrounds", 2)
export_backgrounds_v3 = create_export(background_v3, "backgrounds", 3)
export_backgrounds_v4 = create_export(background_v4, "backgrounds", 4)

# Create exports for payments & billing
export_payments_v1 = create_export(payments_v1, "payments", 1)

# Create exports for standard forms
export_forms_v1 = create_export(forms_v1, "forms", 1)
export_forms_v2 = create_export(forms_v2, "forms", 2)
export_forms_v3 = create_export(forms_v3, "forms", 3)

# Create exports for featured
export_featured_v1 = create_export(featured_v1, "featured", 1)

# Create exports for descriptive lists
export_lists_v1 = create_export(lists_v1, "lists", 1)

# Create exports for timeline
export_timeline_v1 = create_export(timeline_v1, "lists", 1)

# Create exports for onboarding
export_onboardings_v1 = create_export(onboardings_v1, "onboardings", 1)

# Create exports or pricing
export_pricing_v1 = create_export(pricing_v1, "pricing", 1)

# Create exports or popups
export_popups_v1 = create_export(popups_v1, "popups", 1)
export_popups_v2 = create_export(popups_v2, "popups", 2)

# Create exports or animations
export_animation_v1 = create_export(animation_v1, "animations", 1)
export_animation_v2 = create_export(animation_v2, "animations", 2)
export_animation_v3 = create_export(animation_v3, "animations", 3)
export_animation_v4 = create_export(animation_v4, "animations", 4)
