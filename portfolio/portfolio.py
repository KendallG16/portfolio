import reflex as rx


def index() -> rx.Component:
    return rx.text("Hello, world!")

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
