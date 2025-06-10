import allure

from data.data import AuthData as Ad
from pages.registration_page import RegistrationPage
from locators.auth_page_locators import AuthLocators as Al
from utilities.data_generator import DataGenerator
from data.data import MainPage as Mp

@allure.feature("Авторизация")
@allure.story("Страница регистрации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistration:

    @allure.title('Регистрация нового пользователя в Продуктовом помощнике')
    def test_registration_user(self, driver):

        registration_page = RegistrationPage(driver)
        fake_user = DataGenerator.create_fake_user()
        registration_page.open(Ad.URL_AUTH)
        registration_page.click_element(Al.SIGNUP_BUTTON)
        registration_page.register_new_user(fake_user)

        assert registration_page.check_is_displayed(
            Al.FORM_TITLE), "Форма авторизации не отображается после регистрации"

        current_url = driver.current_url
        assert current_url == Mp.URL_SIGNUP_PAGE, f"Текущий URL {current_url} не совпадает с ожидаемым {Mp.URL_SIGNUP_PAGE}"