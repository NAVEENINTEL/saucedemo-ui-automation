from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        checkout_button = self.driver.find_element(By.NAME, "checkout")
        checkout_button.click()

    def enter_user_information(self, first_name, last_name, postal_code):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)

        continue_button = self.driver.find_element(By.NAME, "continue")
        continue_button.click()

    def finish_checkout(self):
        finish_button = self.driver.find_element(By.NAME, "finish")
        finish_button.click()
