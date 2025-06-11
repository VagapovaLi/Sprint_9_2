import allure

from data.data import AuthData as Ad
from data.data import MainPage as Mp
from locators.recipes_page_locators import RecipesPageLocators as Rl
from pages.auth_page import AuthPage


@allure.feature("Авторизация")
@allure.story("Страница авторизации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestAuth:

    @allure.title('Авторизация')
    def test_auth_login(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open(Ad.URL_AUTH)
        auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD)
        assert auth_page.check_is_displayed(Rl.LOGOUT_BUTTON), "Кнопка 'Выход' не отображается после авторизации"

        current_url = driver.current_url
        assert current_url == Mp.URL_MAIN_PAGE, f"Текущий URL {current_url} не совпадает с ожидаемым {Mp.URL_MAIN_PAGE}"
