import os
from collections import defaultdict
from typing import List, Dict

from ...templates.thumbnail import thumbnail
from ...routes.pantry_routes import PANTRY_ROUTES


def get_svg_files(
    base_url: str = "https://raw.githubusercontent.com/LineIndent/buridan-ui/main/assets",
) -> List[Dict[str, str]]:

    svg_files = [
        os.path.basename(directory)
        for directory, _, _ in os.walk("buridan_ui/pantry")
        if os.path.basename(directory) not in {"pantry", "__pycache__"}
    ]

    return sorted(
        [{"image": f"{base_url}/{f}.svg", "filename": f"{f}.svg"} for f in svg_files],
        key=lambda x: x["filename"],
    )


def get_component_quantities(
    pantry_folder: str = "buridan_ui/pantry",
) -> Dict[str, int]:
    quantities = defaultdict(int)
    for subdir, _, files in os.walk(pantry_folder):
        if os.path.basename(subdir) not in {"pantry", "__pycache__"}:
            quantities[os.path.basename(subdir)] = len(files)
    return dict(quantities)


def get_pantry_items() -> List[Dict[str, str]]:
    return [item for item in PANTRY_ROUTES if item["name"] != "Table Pagination"]


NORMALIZATION_MAP = {
    # ... key name == PANTRY_ROUTE[name]: value name == Pantry dir names
    "Animations": "animations",
    "Backgrounds": "backgrounds",
    "Cards": "cards",
    "Frequently Asked Questions": "faq",
    "Descriptive Lists": "lists",
    "Featured": "featured",
    "Logins": "logins",
    "Menus": "menus",
    "Onboarding & Progress": "onboardings",
    "Payments & Billing": "payments",
    "Popups": "popups",
    "Pricing Sections": "pricing",
    "Prompt Boxes": "prompts",
    "Subscribe": "subscribe",
    "Standard Forms": "forms",
    "Standard Tables": "tables",
    "Timeline": "timeline",
}


def combine_items(
    svg_files: List[Dict[str, str]],
    quantity_map: Dict[str, int],
    pantry_items: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    combined_items = []
    for pantry_item in pantry_items:
        filename_key = NORMALIZATION_MAP.get(pantry_item["name"])
        quantity = quantity_map.get(filename_key, 0)
        corresponding_image = next(
            (
                svg["image"]
                for svg in svg_files
                if svg["filename"].startswith(filename_key)
            ),
            None,
        )

        combined_items.append(
            {
                "image": corresponding_image,
                "quantity": quantity,
                "name": pantry_item["name"],
                "path": pantry_item["path"],
            }
        )
    return combined_items


def create_thumbnails(combined_items: List[Dict[str, str]]) -> List[str]:

    return [
        thumbnail(item["path"], item["image"], item["name"], str(item["quantity"]))
        for item in combined_items
    ]


def main():
    svg_files = get_svg_files()
    quantity_map = get_component_quantities()
    pantry_items = get_pantry_items()
    combined_items = combine_items(
        svg_files,
        quantity_map,
        pantry_items,
    )
    thumbnails = create_thumbnails(combined_items)
    return thumbnails


export_thumbnail = main()
