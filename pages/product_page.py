from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        product_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, product_name)
        product_link.click()

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

    def open_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_icon.click()
