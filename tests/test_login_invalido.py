import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login

class TestCT03:
    def test_ct03_fazer_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()
        login_page.fazer_login("standard_user", "senha errada")
        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauc")
        #driver.find_element(By.ID, "login-button").click()
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)