import reflex as rx

from ...thumbnail_items.exports import export_thumbnail


def landing_page_pantry_items():
    return rx.hstack(
        *export_thumbnail,
        width="100%",
        display="grid",
        gap="2rem",
        grid_template_columns=[
            f"repeat({i}, minmax(0, 1fr))" for i in [1, 2, 2, 2, 4, 4]
        ],
        min_height="100vh",
        padding="18px 0px",
    )
