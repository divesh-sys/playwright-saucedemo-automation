import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open("/")
    return lp


@pytest.fixture
def inventory_page(page: Page, login_page: LoginPage) -> InventoryPage:
    """Returns an InventoryPage with a logged-in standard user."""
    login_page.login(VALID_USER, VALID_PASSWORD)
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)
