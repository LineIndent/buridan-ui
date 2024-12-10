from typing import Optional

import reflex as rx

from .state import PubMedState
from .style import PubMedStyle
from .wrappers.item import wrapper

txt_overflow = {
    "white_space": "nowrap",
    "overflow": "hidden",
    "text_overflow": "ellipsis",
    "cursor": "pointer",
}


def user_query() -> rx.Component:
    return rx.input(
        value=PubMedState.user_query,
        width="100%",
        on_change=PubMedState.set_user_query,
    )


def button(name: str, color: str, kwargs: Optional = None) -> rx.Component:
    return rx.button(
        name,
        color_scheme=color,
        variant="surface",
        cursor="pointer",
        width="100%",
        **(kwargs if kwargs else {}),
    )


def loader_txt() -> rx.Component:
    return rx.text(
        PubMedState.loader_txt,
        size="2",
        color=rx.color("slate", 11),
        padding="1em 0em",
    )


def hover(txt: str) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(rx.text(txt, width="300px", **txt_overflow)),
        rx.hover_card.content(rx.text(txt)),
    )


def table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    ["", "ID", "Title", "Date", "URL", "Abstract"],
                    lambda title: rx.table.column_header_cell(
                        rx.text(title, font_size="12px", weight="bold"),
                    ),
                ),
            ),
        ),
        rx.table.body(
            rx.foreach(
                PubMedState.articles,
                lambda article: rx.table.row(
                    rx.table.cell(
                        rx.checkbox(
                            on_change=lambda _: PubMedState.compile_selected_article(
                                _,
                                article["id"],
                            ),
                        ),
                    ),
                    rx.table.cell(article["id"]),
                    rx.table.cell(hover(article["title"])),
                    rx.table.cell(article["date"]),
                    rx.table.cell(rx.link(article["url"], href=article["url"])),
                    rx.table.cell(hover(article["abstract"])),
                    align="center",
                    white_space="nowrap",
                ),
            ),
            transition="all 550ms ease",
        ),
        width="100%",
        variant="surface",
        size="2",
    )


def pubmed_ai():
    return rx.vstack(
        wrapper(
            "1. Enter a health topic you're interested in",
            [
                rx.vstack(
                    user_query(),
                    button(
                        "Send",
                        "blue",
                        {
                            "on_click": rx.event(PubMedState.process_request),
                            "loading": PubMedState.is_processing,
                        },
                    ),
                    width="100%",
                    max_width="25em",
                ),
            ],
        ),
        loader_txt(),
        rx.cond(
            PubMedState.articles,
            wrapper(
                f"2. Table Results for query",
                [rx.box(table(), width="100%")],
            ),
            rx.spacer(),
        ),
        rx.divider(height="1em", opacity="0"),
        rx.cond(
            PubMedState.selection,
            wrapper(
                f"3. Generate Summary for Selected Articles",
                [
                    button(
                        "Generate",
                        "blue",
                        {
                            "max_width": "25em",
                            "loading": PubMedState.is_generating,
                            "on_click": rx.event(PubMedState.generate_abstract_summary),
                        },
                    ),
                ],
            ),
            rx.spacer(),
        ),
        rx.divider(height="1em", opacity="0"),
        rx.cond(
            PubMedState.summary,
            wrapper(
                f"4. Summary of Abstracts",
                [rx.text(PubMedState.summary, size="3", color=rx.color("slate", 12))],
            ),
            rx.spacer(),
        ),
        **PubMedStyle.base,
    )
