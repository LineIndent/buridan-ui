from ...wrappers.base import base
from ...pantry.exports import *


@base("/pantry/logins", "Logins", title="Logins - buridan/ui")
def logins():
    return [export_logins_v1(), export_logins_v2()]


@base(
    "/pantry/table-pagination",
    "Table Pagination",
    title="Table Pagination - buridan/ui",
)
def tables_1():
    return [export_tables_v1()]


@base("/pantry/standard-tables", "Standard Tables", title="Tables - buridan/ui")
def tables_2():
    return [export_tables_v2(), export_tables_v3()]


@base("/pantry/menus", "Menus & Lists", title="Menus - buridan/ui")
def menus():
    return [export_menus_v1()]


@base("/pantry/backgrounds", "Backgrounds", title="Backgrounds - buridan/ui")
def backgrounds():
    return [
        export_backgrounds_v1(),
        export_backgrounds_v2(),
        export_backgrounds_v3(),
        export_backgrounds_v4(),
    ]


@base(
    "/pantry/payments-and-billing", "Payments & Billing", title="Payments - buridan/ui"
)
def payments_and_billing():
    return [export_payments_v1()]


@base("/pantry/standard-forms", "Standard Forms", title="Standard Forms - buridan/ui")
def standard_forms():
    return [export_forms_v1(), export_forms_v2(), export_forms_v3()]


@base("/pantry/featured", "Featured Forms", title="Featured - buridan/ui")
def featured():
    return [export_featured_v1()]


@base(
    "/pantry/descriptive-lists",
    "Descriptive Lists",
    title="Descriptive Lists - buridan/ui",
)
def descriptive():
    return [export_lists_v1()]


@base("/pantry/timeline", "Timeline", title="Timeline - buridan/ui")
def timeline():
    return [export_timeline_v1()]


@base(
    "/pantry/onboarding-and-progress",
    "Onboarding & Progress",
    title="Onboarding - buridan/ui",
)
def onboarding():
    return [export_onboardings_v1()]


@base("/pantry/pricing-sections", "Pricing", title="Pricing - buridan/ui")
def pricing():
    return [export_pricing_v1()]


@base("/pantry/popups", "Popups", title="Popups - buridan/ui")
def popups():
    return [export_popups_v1(), export_popups_v2()]


@base("/pantry/animations", "Animations", title="Animations - buridan/ui")
def animations():
    return [
        export_animation_v1(),
        export_animation_v2(),
        export_animation_v3(),
        export_animation_v4(),
    ]
