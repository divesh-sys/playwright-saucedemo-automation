import pytest
from playwright.sync_api import expect

from tests.conftest import VALID_PASSWORD, VALID_USER


@pytest.mark.smoke
def test_valid_login(page, login_page):
    login_page.login(VALID_USER, VALID_PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='title']")).to_have_text("Productz")


@pytest.mark.regression
def test_locked_out_user(login_page):
    login_page.login("locked_out_user", VALID_PASSWORD)
    expect(login_page.error).to_contain_text("locked out")


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, message",
    [
        ("standard_user", "wrong_password", "do not match"),
        ("", VALID_PASSWORD, "Username is required"),
        (VALID_USER, "", "Password is required"),
    ],
)
def test_invalid_login(login_page, username, password, message):
    login_page.login(username, password)
    expect(login_page.error).to_contain_text(message)


@pytest.mark.regression
def test_logout(inventory_page, login_page):
    inventory_page.logout()
    expect(login_page.login_button).to_be_visible()
