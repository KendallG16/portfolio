
import reflex as rx

class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return 


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()