import pytest
import time
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage 
from pages.carrinho_page import CarrinhoPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        #fazer login
        login_page.fazer_login("standard_user", "secret_sauce")
        #adicionar produto ao carrinho
        home_page.adicionar_ao_carrinho('Sauce Labs Backpack')
        #verificando que o produto foi adicionado
        home_page.acessar_carrinho()
        #assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']").is_displayed()
        carrinho_page.verificar_produto_carrinho_existe('Sauce Labs Backpack')

        #driver.find_element(By.ID, "continue-shopping").click()
        carrinho_page.clicar_continuar_comprando()
        home_page.adicionar_ao_carrinho('Sauce Labs Bike Light')

        #driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Bike Light']").click()
        #driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        #driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        home_page.acessar_carrinho()

        #assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Backpack']").is_displayed()
        #assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text() = 'Sauce Labs Bike Light']").is_displayed()
        carrinho_page.verificar_produto_carrinho_existe('Sauce Labs Backpack')
        carrinho_page.verificar_produto_carrinho_existe('Sauce Labs Bike Light')