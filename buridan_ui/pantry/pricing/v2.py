import reflex as rx

check = """
<svg class="shrink-0 mt-0.5 size-4 text-blue-600 dark:text-blue-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
"""


freeSpecs = ["1 user", "Plan features", "Product & site support"]
startUpSpecs = [
    "Up to 5 users",
    "Access to premium features",
    "Email support",
    "Basic integrations",
]
teamSpecs = [
    "Up to 20 users",
    "Advanced features",
    "Priority email support",
    "Collaboration tools",
    "Team management features",
    "Advanced integrations",
]
enterpriseSpecs = [
    "Unlimited users",
    "All features included",
    "24/7 dedicated support",
    "Customizable integrations",
    "Advanced security features",
    "SLA support",
    "Onboarding assistance",
]


def pricingHeader(
    is_popular: bool,
    name: str,
    price: str,
    subtitle: str,
) -> rx.Component:
    return rx.vstack(
        rx.text(name, size="1", color=rx.color("slate", 11)),
        rx.heading(price, size="7", color=rx.color("slate", 12)),
        rx.text(subtitle, size="1", color=rx.color("slate", 11)),
        spacing="2",
        width="100%",
        align="center",
        text_align="center",
    )


def pricingSpecs(specs: list[str]) -> rx.Component:
    return rx.vstack(
        *[
            rx.hstack(
                rx.html(check),
                rx.text(
                    f"{spec}",
                    size="1",
                    weight="bold",
                    color=rx.color("slate", 11),
                ),
                align="center",
            )
            for spec in specs
        ],
        width="100%",
    )


def pricingButton(style: str) -> rx.Component:
    return rx.button("Sign Up", width="100%", padding="0.75em", variant=style)


def tierStack(
    is_popular: bool,
    name: str,
    price: str,
    subtitle: str,
    style: str,
    spec_list: list[str],
) -> rx.Component:
    return rx.vstack(
        pricingHeader(is_popular, name, price, subtitle),
        rx.divider(height="1em", opacity="0"),
        pricingSpecs(spec_list),
        rx.divider(height="1em", opacity="0"),
        rx.spacer(),
        pricingButton(style),
        padding="1em",
        border=(
            f"1px solid {rx.color('gray', 4)}"
            if not is_popular
            else f"1px solid {rx.color('blue', 6)}"
        ),
        border_radius="8px",
        flex="1 1 200px",
        align="stretch",
        height="50vh",
    )


def pricing_v2():
    return rx.hstack(
        tierStack(
            False,
            "FREE",
            "Free",
            "No pricing. Forever free.",
            "outline",
            freeSpecs,
        ),
        tierStack(
            True,
            "STARTUP",
            "39 USD",
            "All the basics for starting a new business.",
            "solid",
            startUpSpecs,
        ),
        tierStack(
            False,
            "TEAM",
            "59 USD",
            "Everything you need for a growing business.",
            "outline",
            startUpSpecs,
        ),
        tierStack(
            False,
            "ENTERPRISE",
            "199 USD",
            "Advanced features for scaling your business.",
            "outline",
            enterpriseSpecs,
        ),
        align="center",
        wrap="wrap",
        padding="1em",
        width="100%",
        min_height="60vh",
    )
