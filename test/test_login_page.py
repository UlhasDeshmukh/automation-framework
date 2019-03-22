import pytest
from pages.login_page import Loginpage

def test_login(driver):
    driver.get("https://ulhasdeshmukh.github.io/test-website/login.html")
    page = Loginpage(driver)
    page.login("Tom Smith", "123456")
    assert "Welcome" in driver.page_source