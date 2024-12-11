import reflex as rx

from buridan_ui.pages.thumbnail_items.exports import export_thumbnail


def landing_page_pantry_items():
    return rx.vstack(
        *export_thumbnail,
        width="100%",
        display="grid",
        column_gap="2rem",
        row_gap="2.5rem",
        grid_template_columns=[
            f"repeat({i}, minmax(0, 1fr))" for i in [1, 2, 2, 3, 4, 4]
        ],
        height="100%",
        overflow="hidden",
        padding="18px 0px",
        position="relative",
        # ... use this is setting height to vh
        # mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 50%, hsl(0, 0%, 0%, 0) 100%)",
    )
