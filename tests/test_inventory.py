import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_inventory_shows_six_products(inventory_page):
    expect(inventory_page.items).to_have_count(6)


@pytest.mark.regression
def test_sort_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_price_high_to_low(inventory_page):
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.regression
def test_cart_badge_updates(inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    expect(inventory_page.cart_badge).to_have_text("2")
