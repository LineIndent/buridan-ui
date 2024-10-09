import os

from ...templates.thumbnail import thumbnail
from ...routes.pantry_routes import PANTRY_ROUTES

svg_files = [{"image": f} for f in os.listdir("assets") if f.endswith(".svg")]
svg_files.sort(key=lambda x: x["image"])

qty_components = []
pantry_folder = "buridan_ui/pantry"

for subdir, _, files in os.walk(pantry_folder):
    if os.path.basename(subdir) not in {"pantry", "__pycache__"}:
        qty_components.append(
            {"filename": os.path.basename(subdir), "quantity": len(files)}
        )

qty_components.sort(key=lambda x: x["filename"])

pantry_items = [item for item in PANTRY_ROUTES if item["name"] != "Table Pagination"]

quantity_map = {item["filename"]: item["quantity"] for item in qty_components}

# ... Create a normalization mapping based on the expected output
# ... The normalization_map directly associates each name from pantry_items to its corresponding    filename. This makes it easier to retrieve the correct filename for each pantry_item.
# ... filename is the name of the dir in /pantry/
normalization_map = {
    "Animations": "animations",
    "Backgrounds": "backgrounds",
    "Descriptive Lists": "lists",
    "Featured": "featured",
    "Logins": "logins",
    "Menus": "menus",
    "Onboarding & Progress": "onboardings",
    "Payments & Billing": "payments",
    "Popups": "popups",
    "Pricing Sections": "pricing",
    "Standard Forms": "forms",
    "Standard Tables": "tables",
    "Timeline": "timeline",
}

combined_items = []

for pantry_item in pantry_items:
    filename_key = normalization_map.get(pantry_item["name"])
    quantity = quantity_map.get(filename_key, 0)

    corresponding_image = next(
        (svg["image"] for svg in svg_files if svg["image"].startswith(filename_key)),
        None,
    )

    combined_item = {
        "image": corresponding_image,
        "quantity": quantity,
        "name": pantry_item["name"],
        "path": pantry_item["path"],
    }

    combined_items.append(combined_item)

export_thumbnail = []
for item in combined_items:
    export_thumbnail.append(
        thumbnail(
            item["path"],
            item["image"],
            item["name"],
            f"{item['quantity']}",
        )
    )
