from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.prices = page.locator("[data-test='inventory-item-price']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")

    def add_to_cart(self, product_slug: str) -> None:
        """product_slug example: 'sauce-labs-backpack'"""
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def sort_by(self, option: str) -> None:
        """option: az, za, lohi, hilo"""
        self.sort_dropdown.select_option(option)

    def get_prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def open_cart(self) -> None:
        self.cart_link.click()

    def logout(self) -> None:
        self.menu_button.click()
        self.logout_link.click()
