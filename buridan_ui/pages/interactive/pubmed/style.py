from dataclasses import dataclass, field


@dataclass
class PubMedStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {"width": "100%", "min_height": "100vh"},
    )


PubMedStyle: PubMedStyle = PubMedStyle()
