import reflex as rx


def ace_editor():
    return rx.box(
        rx.html(
            f"""
            <div id="editor" style="width: 100%; height: 700px; position: relative;"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ace.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ext-language_tools.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/mode-python.js"></script>
            """,
            position="relative",
            width="100%",
        ),
        flex=["100%" if i <= 3 else "65%" for i in range(6)],
    )
