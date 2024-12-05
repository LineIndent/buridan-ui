
### Style Sheet

The following style sheet is used to customize and enhance the UI components found in this guide. Each class provides the necessary UI props used inside each component.

```python
from dataclasses import dataclass, field
from typing import Dict

import reflex as rx


@dataclass
class SandboxAuthStyle:
    base: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "60vh",
            "overflow": "hidden",
        }
    )

    content: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "22em",
            "align": "center",
            "justify": "center",
            "text_align": "center",
            "spacing": "2",
            "padding": "1.5em",
            "border_radius": "10px",
            "position": "relative",
            "margin": "10px",
            "background": rx.color("gray", 3),
        }
    )


@dataclass
class AuthDynamicStyle:
    passive: Dict[str, bool] = field(
        default_factory=lambda: {"loading": False, "disabled": False}
    )
    active: Dict[str, bool] = field(
        default_factory=lambda: {"loading": True, "disabled": True}
    )
    finished: Dict[str, bool] = field(
        default_factory=lambda: {"loading": False, "disabled": True}
    )

    alert_passive: Dict[str, str] = field(
        default_factory=lambda: {
            "height": "0vh",
            "filter": "blur(10px)",
            "transform": "scale(1.5)",
            "opacity": "0",
        }
    )

    alert_active: Dict[str, str] = field(
        default_factory=lambda: {
            "height": "100%",
            "filter": "blur(0px)",
            "transform": "scale(1)",
            "opacity": "1",
        }
    )


SandboxAuthStyle: SandboxAuthStyle = SandboxAuthStyle()
AuthDynamicStyle: AuthDynamicStyle = AuthDynamicStyle()
```
