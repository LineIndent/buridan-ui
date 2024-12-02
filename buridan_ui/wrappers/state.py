import asyncio
import reflex as rx
from reflex.constants.colors import Color

start: int = 8
color_map = {
    "blue": {i: rx.color("blue", i + start) for i in range(4)},
    "ruby": {i: rx.color("ruby", i + start) for i in range(4)},
    "jade": {i: rx.color("jade", i + start) for i in range(4)},
    "gray": {i: rx.color("gray", i + start) for i in range(4)},
    "purple": {i: rx.color("purple", i + start) for i in range(4)},
}


class ComponentWrapperState(rx.State):
    uuid: dict[int, str]

    default_icon: bool = True

    default_theme: dict[int, Color] = color_map["blue"]
    selected_theme: rx.Field[str] = rx.field("blue")

    async def toggle_theme(self, color: str):
        self.selected_theme = color
        self.default_theme = color_map[color]

    async def toggle_icon(self):
        self.default_icon = False
        yield
        await asyncio.sleep(1)
        self.default_icon = True

    def resize(self, uuid: int, size: str):
        self.uuid[uuid] = size
