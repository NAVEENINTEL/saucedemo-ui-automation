import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
from config.config import BASE_URL

@pytest.fixture(scope="session")
def browser(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Create a logger instance for the test
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    request.node.logger = logger
    
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def open_saucedemo_url(browser):
    browser.get(BASE_URL)
