import reflex as rx

from ...wrappers.base import base


def text_wrapper(title: str, description: str):
    return rx.vstack(
        rx.hstack(
            rx.text(
                title,
                size="4",
                weight="bold",
                color=rx.color("slate", 12),
            ),
            align="center",
        ),
        rx.markdown(description),
        spacing="2",
        line_height="2px",
    )


@base("/getting-started/license", "Library License", title="License - buridan/ui")
def license():
    return [
        rx.box(
            rx.vstack(
                rx.markdown(
                    """## MIT License
</br>
Copyright (c) 2024 LineIndent
</br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
</br>

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
                    """
                ),
                max_width="50em",
                width="100%",
                spacing="6",
            ),
            width="100%",
            display="flex",
            justify_content="center",
            padding="0px 14px",
        )
    ]
