import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# Define positive test data
positive_test_data = [
    {"username": "standard_user", "password": "secret_sauce", "product_name": "Sauce Labs Backpack"},
    {"username": "problem_user", "password": "secret_sauce", "product_name": "Sauce Labs Bolt T-Shirt"},
    {"username": "performance_glitch_user", "password": "secret_sauce", "product_name": "Sauce Labs Onesie"},
    # Add more positive test data for different scenarios
]

@pytest.mark.parametrize("data", positive_test_data)
def test_successful_login_and_checkout(browser, open_saucedemo_url, data):
    login_page = LoginPage(browser)
    
    login_page.login(data["username"], data["password"])
    
    # Assert that the login was successful by checking the URL
    assert "inventory.html" in browser.current_url

    # Select a product and add it to the cart
    product_page = ProductPage(browser)
    product_page.select_product(data["product_name"])
    product_page.add_to_cart()

    # Go to the cart and proceed to checkout
    product_page.open_cart()
    cart_page = CartPage(browser)
    cart_page.checkout()

    # Complete the checkout process
    cart_page.enter_user_information("John", "Doe", "12345")
    cart_page.finish_checkout()
    
    # Verify the order is successful by checking the URL
    assert "checkout-complete.html" in browser.current_url
