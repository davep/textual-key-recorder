from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class TextualKeyRecorder(App[None]):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
