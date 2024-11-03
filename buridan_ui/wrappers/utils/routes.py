import reflex as rx


def capitalize_words(segment: str) -> str:
    return " ".join(word.capitalize() for word in segment.replace("-", " ").split())


def base_content_path_ui(route: str) -> rx.hstack:
    segments = route.strip("/").split("/")
    path_names = [
        item for segment in segments[:-1] for item in [capitalize_words(segment), "/"]
    ] + [capitalize_words(segments[-1])]

    return rx.hstack(
        *[
            (
                rx.text(name, font_size="11px", color_scheme="gray", weight="medium")
                if index != len(path_names) - 1
                else rx.text(name, font_size="11px", weight="medium")
            )
            for index, name in enumerate(path_names)
        ],
        spacing="1",
    )
