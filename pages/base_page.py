import os
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from data.data import BaseData as Bd


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Bd.TIMEOUT)

    # Открыть браузер
    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Ждем когда элемент {locator} загрузится')
    def wait_for_load(self, locator):
        try:
            return self.wait.until(Ec.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за отведенное время.")
            raise


    @allure.step('Проверяем видимость элемента {locator}')
    def check_is_displayed(self, locator):
        try:
            self.wait_for_load(locator)
            is_displayed = self.driver.find_element(*locator).is_displayed()
            return is_displayed
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент с локатором {locator} не найден на странице.")

    @allure.step('Ищем элемент по {locator} и возвращением его')
    def find_element(self, locator):
        element = self.wait.until(Ec.presence_of_element_located(locator))
        return element

    @allure.step('Ждем когда элемент {locator} станет кликабельным')
    def wait_for_click(self, locator):
        try:
            return self.wait.until(Ec.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным за отведенное время.")
            raise

    @allure.step('Вводим текст {set_data} в поле ввода {locator}')
    def set_input(self, locator, set_data):
        self.wait_for_click(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(set_data)

    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, locator):
        try:
            self.wait_for_click(locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

    def upload_image(self, locator, file_path):

        if not os.path.isabs(file_path):
                # Если путь относительный, строим абсолютный от корня проекта
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            absolute_path = os.path.join(base_dir, file_path)
        else:
            absolute_path = file_path

        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"Файл не найден: {absolute_path}")
        file_input = self.find_element(locator)
        file_input.send_keys(absolute_path)
        return os.path.basename(file_path)

    @allure.step('Достаем текст элемента по локатору {locator}')
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Нажимаем JS на элемент {locator}')
    def click_element_js(self, locator):
        try:
            button = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

