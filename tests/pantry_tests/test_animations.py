import unittest

import reflex as rx
from reflex.components.radix.themes.layout.center import Center
from reflex.components.radix.themes.layout.stack import HStack, VStack

from buridan_ui.pantry.animations import v1, v2, v3, v4, v5


class TestAnimationComponent(unittest.TestCase):

    def _test_render_main_stack(self, animation_func) -> None:
        """Test if the component is an instance of VStack."""
        component = animation_func()
        assert isinstance(
            component,
            VStack | Center | HStack,
        ), "Component is not an instance of VStack!"  # fix error message ...

    def _test_stack_children(self, animation_func) -> None:
        """Test if all children are Reflex components."""
        component = animation_func()
        for child in component.children:
            assert isinstance(child, rx.Component), f"{child} is not a Reflex component"

    def test_all_animations(self) -> None:
        """Dynamically test all animation versions."""
        # You can dynamically load animation functions based on the versioned imports
        animation_versions = [
            v1.animation_v1,
            v2.animation_v2,
            v3.animation_v3,
            v4.animation_v4,
            v5.animation_v5,
        ]

        for animation_func in animation_versions:
            with self.subTest(animation=animation_func.__name__):
                self._test_render_main_stack(animation_func)
                self._test_stack_children(animation_func)


if __name__ == "__main__":
    unittest.main(verbosity=2)
