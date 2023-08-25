import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage 

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login

class TestCT02:
    def test_ct02_fazer_login_valido(self):
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page = HomePage()
        home_page.verificar_login_com_sucesso()

        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #driver.find_element(By.ID, "login-button").click()
        #assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()