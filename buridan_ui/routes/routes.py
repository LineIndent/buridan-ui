from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Routes:
    landing: dict[str, str] = field(default_factory=lambda: {"path": "/"})

    started: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {
                "name": "Introduction",
                "path": "/getting-started/introduction",
                "dir": "introduction",
            },
            {
                "name": "Installation",
                "path": "/getting-started/installation",
                "dir": "installation",
            },
            {
                "name": "Who is Buridan?",
                "path": "/getting-started/who-is-buridan",
                "dir": "buridan",
            },
            {
                "name": "Changelog",
                "path": "/getting-started/changelog",
                "dir": "changelog",
            },
        ]
    )

    interactive: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {
                "name": "RAG Application",
                "path": "/interactive/retrieval-augmented-generation",
                "dir": "rag",
            },
            {
                "name": "PubMed Application",
                "path": "/interactive/pubmed-ai",
                "dir": "pubmed",
                "is_new": True,
            },
        ]
    )

    blueprints: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {
                "name": "Authentication",
                "path": "/blueprints/anonymous-authentication",
                "dir": "anon",
                "is_new": True,
            },
        ]
    )

    pantries: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Logins", "path": "/pantry/logins", "dir": "logins"},
            {
                "name": "Standard Forms",
                "path": "/pantry/standard-forms",
                "dir": "forms",
            },
            {
                "name": "Standard Tables",
                "path": "/pantry/standard-tables",
                "dir": "tables",
            },
            {
                "name": "Pricing Sections",
                "path": "/pantry/pricing-sections",
                "dir": "pricing",
            },
            {
                "name": "Popups",
                "path": "/pantry/popups",
                "dir": "popups",
            },
            {
                "name": "Payments & Billing",
                "path": "/pantry/payments-and-billing",
                "dir": "payments",
            },
            {
                "name": "Table Pagination",
                "path": "/pantry/table-pagination",
                "dir": "tables",
            },
            {
                "name": "Onboarding & Progress",
                "path": "/pantry/onboarding-and-progress",
                "dir": "onboardings",
            },
            {
                "name": "Menus",
                "path": "/pantry/menus",
                "dir": "menus",
            },
            {
                "name": "Backgrounds",
                "path": "/pantry/backgrounds",
                "dir": "backgrounds",
            },
            {
                "name": "Featured",
                "path": "/pantry/featured",
                "dir": "featured",
            },
            {
                "name": "Descriptive Lists",
                "path": "/pantry/descriptive-lists",
                "dir": "lists",
            },
            {
                "name": "Timeline",
                "path": "/pantry/timeline",
                "dir": "timeline",
            },
            {
                "name": "Animations",
                "path": "/pantry/animations",
                "dir": "animations",
            },
            {
                "name": "Prompt Boxes",
                "path": "/pantry/prompt-boxes",
                "dir": "prompts",
            },
            {
                "name": "Cards",
                "path": "/pantry/cards",
                "dir": "cards",
            },
            {
                "name": "Subscribe",
                "path": "/pantry/subscribe",
                "dir": "subscribe",
            },
            {
                "name": "Frequently Asked Questions",
                "path": "/pantry/frequently-asked-questions",
                "dir": "faq",
            },
            {
                "name": "Footers",
                "path": "/pantry/footers",
                "dir": "footers",
            },
            {"name": "Inputs", "path": "/pantry/inputs", "dir": "inputs"},
        ]
    )

    charts: List[Dict[str, str]] = field(
        default_factory=lambda: [
            {"name": "Bar Charts", "path": "/charts/bar-charts", "dir": "bar"},
            {"name": "Area Charts", "path": "/charts/area-charts", "dir": "area"},
            {"name": "Line Charts", "path": "/charts/line-charts", "dir": "line"},
            {"name": "Pie Charts", "path": "/charts/pie-charts", "dir": "pie"},
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
            {"name": "Interactive Apps", "path": InteractiveRoutes[0]["path"]},
            {"name": "Blueprints", "path": BlueprintRoutes[0]["path"]},
            {"name": "Pantry", "path": PantryRoutes[0]["path"]},
            {"name": "Charts", "path": ChartRoutes[0]["path"]},
        ]
    )


Routes: Routes = Routes()

GettingStartedRoutes: List[Dict[str, str]] = Routes.started
InteractiveRoutes: List[Dict[str, str]] = Routes.interactive
BlueprintRoutes: List[Dict[str, str]] = Routes.blueprints
PantryRoutes: List[Dict[str, str]] = sorted(Routes.pantries, key=lambda x: x["name"])
ChartRoutes: List[Dict[str, str]] = sorted(Routes.charts, key=lambda x: x["name"])

NavigationRoutes: List[Dict[str, str]] = NavigationRoutes().base
