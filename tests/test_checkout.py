import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_end_to_end_purchase(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    assert cart_page.item_names() == ["Sauce Labs Backpack"]

    cart_page.checkout()
    checkout_page.fill_details("Jane", "Doe", "12345")
    checkout_page.finish()

    expect(checkout_page.confirmation).to_have_text("Thank you for your order!")


@pytest.mark.regression
def test_checkout_requires_first_name(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_details("", "Doe", "12345")
    expect(checkout_page.error).to_contain_text("First Name is required")
