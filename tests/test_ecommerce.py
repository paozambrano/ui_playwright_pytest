import pytest
from playwright.sync_api import Page, expect

def test_search_and_add_to_cart(page: Page):
    page.goto("https://ecommerce-playground.lambdatest.io/")

    page.fill("input[name='search']", "iPhone")

    page.click("button[type='submit']")

    header = page.locator("h1")
    expect(header).to_contain_text("Search - iPhone")

    print("Test completado: ¡Producto encontrado!")

    



    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("textbox", name="Search For Products").click()
    page.get_by_role("textbox", name="Search For Products").fill("Iphone")
    page.get_by_text("iPhone").nth(3).click()
    page.get_by_role("button", name="Add to Cart").click()

    toast = page.get_by_text("Success: You have added")
    expect(toast).to_be_visible()