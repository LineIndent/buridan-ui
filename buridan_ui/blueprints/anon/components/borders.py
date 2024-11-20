import reflex as rx
from typing import Callable

BORDER_SIDES = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}

createAuthBorders: Callable[[str, str], rx.box] = (
    lambda direction, gradient_direction: rx.box(
        position="absolute",
        width="140%" if direction in ["top", "bottom"] else "4px",
        height="4px" if direction in ["top", "bottom"] else "140%",
        **{
            "top": (
                "0"
                if direction == "top"
                else ("-20%" if direction in ["left", "right"] else None)
            ),
            "bottom": "0" if direction == "bottom" else None,
            "left": (
                "-20%"
                if direction in ["top", "bottom"]
                else ("0" if direction == "left" else None)
            ),
            "right": "0" if direction == "right" else None,
        },
        **{f"border_{BORDER_SIDES[direction]}": "solid"},
        border_image=f"linear-gradient(to {gradient_direction}, transparent, {rx.color('gray', 6)}, transparent) 2 / 4px",
        border_image_width=(
            "0px 0px 1px 0px" if direction in ["top", "bottom"] else "0px 0px 0px 1px"
        ),
        z_index=1,
    )
)
