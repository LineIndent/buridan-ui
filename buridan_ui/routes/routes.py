from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Routes:
    started: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Introduction", "path": "/getting-started/introduction"},
            {"name": "Installation", "path": "/getting-started/installation"},
            {"name": "Who is Buridan?", "path": "/getting-started/who-is-buridan"},
            {"name": "Changelog", "path": "/getting-started/changelog"},
        ]
    )

    interactive: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Dashboard", "path": "/interactive/dashboard", "is_beta": True},
            {
                "name": "RAG Application",
                "path": "/interactive/retrieval-augmented-generation",
                "is_new": True,
            },
        ]
    )

    pantries: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Logins", "path": "/pantry/logins"},
            {"name": "Standard Forms", "path": "/pantry/standard-forms"},
            {"name": "Standard Tables", "path": "/pantry/standard-tables"},
            {"name": "Pricing Sections", "path": "/pantry/pricing-sections"},
            {"name": "Popups", "path": "/pantry/popups"},
            {"name": "Payments & Billing", "path": "/pantry/payments-and-billing"},
            {"name": "Table Pagination", "path": "/pantry/table-pagination"},
            {
                "name": "Onboarding & Progress",
                "path": "/pantry/onboarding-and-progress",
            },
            {"name": "Menus", "path": "/pantry/menus"},
            {"name": "Backgrounds", "path": "/pantry/backgrounds"},
            {"name": "Featured", "path": "/pantry/featured"},
            {"name": "Descriptive Lists", "path": "/pantry/descriptive-lists"},
            {"name": "Timeline", "path": "/pantry/timeline"},
            {"name": "Animations", "path": "/pantry/animations"},
            {"name": "Prompt Boxes", "path": "/pantry/prompt-boxes"},
            {"name": "Cards", "path": "/pantry/cards"},
            {"name": "Subscribe", "path": "/pantry/subscribe"},
            {
                "name": "Frequently Asked Questions",
                "path": "/pantry/frequently-asked-questions",
            },
            {"name": "Footers", "path": "/pantry/footers"},
        ]
    )
    charts: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Bar Charts", "path": "/charts/bar-charts"},
            {"name": "Area Charts", "path": "/charts/area-charts"},
            {"name": "Line Charts", "path": "/charts/line-charts"},
        ]
    )

    resources: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Reflex Framework", "path": "https://reflex.dev/"},
            {"name": "Source Code", "path": "https://github.com/LineIndent/buridan-ui"},
            {"name": "GitHub", "path": "https://github.com/LineIndent"},
            {"name": "@LineIndent", "path": "https://www.youtube.com/@lineindent"},
        ]
    )


@dataclass
class NavigationRoutes:
    base: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Home", "path": "/"},
            {"name": "Getting Started", "path": GettingStartedRoutes[0]["path"]},
            {"name": "Interactive Table", "path": InteractiveRoutes[0]["path"]},
            {"name": "Pantry", "path": PantryRoutes[0]["path"]},
            {"name": "Charts", "path": ChartRoutes[0]["path"]},
        ]
    )


Routes: Routes = Routes()

GettingStartedRoutes: List[Dict[str, str]] = Routes.started
InteractiveRoutes: List[Dict[str, str]] = Routes.interactive
PantryRoutes: List[Dict[str, str]] = sorted(Routes.pantries, key=lambda x: x["name"])
ChartRoutes: List[Dict[str, str]] = sorted(Routes.charts, key=lambda x: x["name"])
ResourcesRoutes: List[Dict[str, str]] = Routes.resources

NavigationRoutes: List[Dict[str, str]] = NavigationRoutes().base
