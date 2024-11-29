from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.events import Mount
from textual.reactive import reactive
from textual.widgets import Header, Footer, Button, Static

class Audioplayer(App):
    """A Textual audioplayer app"""

    BINDINGS =  [
        ('d', 'toggle_dark', 'Dark mode!'),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Button("Exit")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    @on(Button.Pressed)
    def exit_the_app(self):
        self.exit()
    
if __name__ == '__main__':
    app = Audioplayer()
    app.run()