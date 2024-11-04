import reflex as rx


class DrawerState(rx.State):
    is_open: bool = False

    def toggle_drawer(self):
        self.is_open = not self.is_open
