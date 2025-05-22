from pages.login_page import LoginPage

def test_login_success(driver):
    page = LoginPage(driver)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "secure" in driver.current_url
