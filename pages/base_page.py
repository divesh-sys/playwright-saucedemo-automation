from playwright.sync_api import Page


class BasePage:
    """Common behaviour shared by all page objects."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/") -> None:
        self.page.goto(path)
