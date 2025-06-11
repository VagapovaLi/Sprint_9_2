from selenium.webdriver.common.by import By


class RecipesPageLocators:

    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_menuLink') and text()='Выход']")
