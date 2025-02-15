import asyncio
import inspect

import reflex as rx

from buridan_ui.pantry.logins.v1 import logins_v1
from buridan_ui.pantry.logins.v2 import logins_v2


class Editor(rx.State):
    code: str

    mapping: dict[str, rx.Component] = {"Login V1": logins_v1, "Login V2": logins_v2}

    @rx.event
    def handle_selection(self, value: str):
        # Get the source code of the function as a string
        function_code = inspect.getsource(self.mapping[value])

        # Use rx.call_script to set the editor's value to this function code
        yield rx.call_script(
            f"""
            var editor = ace.edit("editor");
            editor.setValue(`{function_code}`);
            console.log(editor.getValue());
            """,
        )

    @rx.event
    def handle_code_from_js(self, code: str) -> None:
        self.code = code

    @rx.event(background=True)
    async def automatic_reload(self):
        while True:
            async with self:
                yield rx.call_script(
                    "getEditorContentAutomatic();",
                    Editor.handle_code_from_js,
                )

            await asyncio.sleep(1)
