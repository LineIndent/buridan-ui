import os
import reflex as rx

from random import randint
from buridan_ui.wrappers.component.wrapper import component_wrapper

from .infographic.v1 import infographic_v1
from .infographic.v2 import infographic_v2
from .infographic.v3 import infographic_v3
from .infographic.v4 import infographic_v4
from .infographic.v5 import infographic_v5
from .infographic.v6 import infographic_v6

from .price.v1 import price_v1
from .price.v2 import price_v2
from .price.v3 import price_v3
from .price.v4 import price_v4

from .expense.v1 import expense_v1
from .expense.v2 import expense_v2
from .expense.v3 import expense_v3
from .expense.v4 import expense_v4
from .expense.v5 import expense_v5

from .stats.v1 import stats_v1
from .stats.v2 import stats_v2
from .stats.v3 import stats_v3
from .stats.v4 import stats_v4
from .stats.v5 import stats_v5
from .stats.v6 import stats_v6
from .stats.v7 import stats_v7
from .stats.v8 import stats_v8

BASE_PATH: str = (
    "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/analytics/"
)


def get_source(directory: str, filename: str):
    with open(os.path.join("buridan_ui", "analytics", directory, filename)) as file:
        return file.read()


def create_export(func, directory, version):
    @component_wrapper(f"{BASE_PATH}{directory}/v{version}.py")
    def export():
        return [
            func(),
            get_source(directory, f"v{version}.py"),
            randint(0, 100000),
            rx.spacer(),
        ]

    return export


analytics_config_file = {
    "infographic": [
        create_export(infographic_v1, "infographic", 1),
        create_export(infographic_v2, "infographic", 2),
        create_export(infographic_v3, "infographic", 3),
        create_export(infographic_v4, "infographic", 4),
        create_export(infographic_v5, "infographic", 5),
        create_export(infographic_v6, "infographic", 6),
    ],
    "price": [
        create_export(price_v1, "price", 1),
        create_export(price_v2, "price", 2),
        create_export(price_v3, "price", 3),
        create_export(price_v4, "price", 4),
    ],
    "expense": [
        create_export(expense_v1, "expense", 1),
        create_export(expense_v2, "expense", 2),
        create_export(expense_v3, "expense", 3),
        create_export(expense_v4, "expense", 4),
        create_export(expense_v5, "expense", 5),
    ],
    "stats": [
        create_export(stats_v1, "stats", 1),
        create_export(stats_v2, "stats", 2),
        create_export(stats_v3, "stats", 3),
        create_export(stats_v4, "stats", 4),
        create_export(stats_v5, "stats", 5),
        create_export(stats_v6, "stats", 6),
        create_export(stats_v7, "stats", 7),
        create_export(stats_v8, "stats", 8),
    ],
}
