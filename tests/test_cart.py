import re

import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_remove_item_from_cart(inventory_page, cart_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    expect(cart_page.items).to_have_count(1)

    cart_page.remove_item("sauce-labs-backpack")
    expect(cart_page.items).to_have_count(0)


@pytest.mark.regression
def test_open_product_details(page, inventory_page):
    inventory_page.open_product("Sauce Labs Backpack")
    expect(page).to_have_url(re.compile(r"inventory-item\.html"))
    expect(page.locator("[data-test='inventory-item-name']")).to_have_text(
        "Sauce Labs Backpack"
    )