from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REG_Form = (By.XPATH, '//form[@id="register_form"]')