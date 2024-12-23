import reflex as rx

from .style import DashboardNavBarStyle


def navbarAvatar() -> rx.avatar:
    return rx.avatar(
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-5.png",
        size="2",
        radius="full",
    )


utilityIconMap = {
    2: {"icon": "info", "msg": "Help & Support"},
    1: {"icon": "bell", "msg": "Notifications"},
    0: {"icon": "activity", "msg": "Activity"},
}


def navbarUtilityIcons(icon: str, msg: str) -> rx.hover_card:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.icon(tag=icon, size=14, color=rx.color("slate", 11)),
            cursor="pointer",
        ),
        rx.hover_card.content(rx.text(msg, size="1", weight="bold"), size="1"),
    )


theme = rx.el.button(
    rx.color_mode.icon(
        light_component=rx.icon(
            "moon",
            size=14,
            color=rx.color("slate", 12),
        ),
        dark_component=rx.icon(
            "sun",
            size=14,
            color=rx.color("slate", 12),
        ),
    ),
    on_click=rx.toggle_color_mode,
)


def dashboardNavbar() -> rx.hstack:
    return rx.hstack(
        rx.hstack(
            *[
                navbarUtilityIcons(item["icon"], item["msg"])
                for item in utilityIconMap.values()
            ],
            theme,
            align="center",
            spacing="5",
        ),
        rx.divider(width="0.75px", height="24px", orientation="vertical"),
        navbarAvatar(),
        **DashboardNavBarStyle.base,
    )
