from selenium.webdriver.common.by import By

class AuthLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button') and contains(text(), 'Войти')]")

    FORM_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_title')]")
    SIGNUP_BUTTON = (By.XPATH, "//a[@href='/signup']")