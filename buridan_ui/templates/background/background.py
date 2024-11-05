import reflex as rx

from dataclasses import dataclass, field


@dataclass
class BackgroundStyle:
    grid: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "30px 30px",
            "background_image": f"radial-gradient(circle, {rx.color('slate', 12)} 0.75px, transparent 1px)",
            "mask": (
                "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
                "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
            ),
            "width": "100%",
            "height": "100vh",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "z_index": "-2",
        }
    )

    tile: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "220px 220px",
            "background_image": "linear-gradient(hsla(0, 0%, 39%, 0.35) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsla(0, 0%, 39%, 0.35) 100%)",
            "mask": (
                "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
                "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
            ),
            "width": "100%",
            "height": "100vh",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "z_index": "-2",
        }
    )


BackgroundStyle: BackgroundStyle = BackgroundStyle()


def grid_background():
    return rx.box(**BackgroundStyle.grid)


def tile_background():
    return rx.box(**BackgroundStyle.tile)
