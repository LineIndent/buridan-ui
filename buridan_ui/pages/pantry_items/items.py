from ...wrappers.base import base
from ...pantry.exports import *


@base("/pantry/logins", "Logins")
def logins():
    return [export_logins_v1(), export_logins_v2()]


@base("/pantry/table-pagination", "Table Pagination")
def tables_1():
    return [export_tables_v1()]


@base("/pantry/standard-tables", "Standard Tables")
def tables_2():
    return [export_tables_v2(), export_tables_v3()]


@base("/pantry/menus", "Menus & Lists")
def menus():
    return [export_menus_v1()]


@base("/pantry/backgrounds", "Backgrounds")
def backgrounds():
    return [
        export_backgrounds_v1(),
        export_backgrounds_v2(),
        export_backgrounds_v3(),
        export_backgrounds_v4(),
    ]


@base("/pantry/payments-and-billing", "Payments & Billing")
def payments_and_billing():
    return [export_payments_v1()]


@base("/pantry/standard-forms", "Standard Forms")
def standard_forms():
    return [export_forms_v1(), export_forms_v2(), export_forms_v3()]


@base("/pantry/featured", "Featured Forms")
def featured():
    return [export_featured_v1()]


@base("/pantry/descriptive-lists", "Descriptive Lists")
def descriptive():
    return [export_lists_v1()]


@base("/pantry/timeline", "Timeline")
def timeline():
    return [export_timeline_v1()]


@base("/pantry/onboarding-and-progress", "Onboarding & Progress")
def onboarding():
    return [export_onboardings_v1()]


@base("/pantry/pricing-sections", "Pricing")
def onboarding():
    return [export_pricing_v1()]


@base("/pantry/popups", "Popups")
def onboarding():
    return [export_popups_v1(), export_popups_v2()]
