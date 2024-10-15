from ...wrappers.base import base
from ...pantry.exports import exports_config


def get_exports(directory):
    return [export() for export in exports_config[directory]]


@base("/pantry/cards", "Cards", title="Cards - buridan/ui")
def cards():
    return get_exports("cards")


@base("/pantry/logins", "Logins", title="Logins - buridan/ui")
def logins():
    return get_exports("logins")


@base(
    "/pantry/table-pagination",
    "Table Pagination",
    title="Table Pagination - buridan/ui",
)
def tables_1():
    return get_exports("tables")[:1]


@base("/pantry/standard-tables", "Standard Tables", title="Tables - buridan/ui")
def tables_2():
    return get_exports("tables")[1:]


@base("/pantry/menus", "Menus & Lists", title="Menus - buridan/ui")
def menus():
    return get_exports("menus")


@base("/pantry/backgrounds", "Backgrounds", title="Backgrounds - buridan/ui")
def backgrounds():
    return get_exports("backgrounds")


@base(
    "/pantry/payments-and-billing", "Payments & Billing", title="Payments - buridan/ui"
)
def payments_and_billing():
    return get_exports("payments")


@base("/pantry/standard-forms", "Standard Forms", title="Standard Forms - buridan/ui")
def standard_forms():
    return get_exports("forms")


@base("/pantry/featured", "Featured Forms", title="Featured - buridan/ui")
def featured():
    return get_exports("featured")


@base(
    "/pantry/descriptive-lists",
    "Descriptive Lists",
    title="Descriptive Lists - buridan/ui",
)
def descriptive():
    return get_exports("lists")


@base("/pantry/timeline", "Timeline", title="Timeline - buridan/ui")
def timeline():
    return get_exports("timeline")


@base(
    "/pantry/onboarding-and-progress",
    "Onboarding & Progress",
    title="Onboarding - buridan/ui",
)
def onboarding():
    return get_exports("onboardings")


@base("/pantry/pricing-sections", "Pricing", title="Pricing - buridan/ui")
def pricing():
    return get_exports("pricing")


@base("/pantry/popups", "Popups", title="Popups - buridan/ui")
def popups():
    return get_exports("popups")


@base("/pantry/animations", "Animations", title="Animations - buridan/ui")
def animations():
    return get_exports("animations")


@base("/pantry/prompt-boxes", "Prompt Boxes", title="Prompts - buridan/ui")
def prompts():
    return get_exports("prompts")
