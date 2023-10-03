"""The main screen for the application."""

##############################################################################
# Textual imports.
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header


##############################################################################
class Main(Screen):
    """The main screen of the application."""

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield Header()
        yield Footer()


### main.py ends here
