import unittest

from pydantic.v1.main import ModelMetaclass
from buridan_ui.pantry.animations.v1 import animation_v1, Animation
from reflex.components.radix.themes.layout.stack import VStack


class TestButtonRendering(unittest.TestCase):

    def test_render_button(self):
        component = animation_v1()

        self.assertIsInstance(
            component, VStack, msg="Component is not an instance of VStack!"
        )

    def test_animation_state(self):
        state = Animation
        self.assertIsInstance(state, ModelMetaclass)


if __name__ == "__main__":
    unittest.main()
