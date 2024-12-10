import reflex as rx

passive_component = {"filter": "blur(10px)", "transform": "scale(1.5)", "opacity": "0"}
active_component = {"filter": "blur(0px)", "transform": "scale(1)", "opacity": "1"}


class HeroLandingState(rx.State):

    component: dict[str, str] = passive_component

    def on_hero_page_load(self) -> None:
        self.reset()
        self.component = active_component
