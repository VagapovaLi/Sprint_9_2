import allure

from utilities.data_generator import DataGenerator
from data.data import AuthData as Ad
from pages.create_recipes_page import CreateRecipes
from pages.auth_page import AuthPage
from locators.recipe_card_locators import RecipeCardLocators as Rcdl
from locators.recipes_page_locators import RecipesPageLocators as Rl
from locators.recipe_creation_locators import RecipeCreationLocators as Rcl


@allure.feature("Рецепты")
@allure.story("Создание рецептов")
@allure.severity(allure.severity_level.CRITICAL)
class TestCreateRecipes:

    @allure.title('Создание нового рецепта')
    def test_create_recipes(self, driver):
        create_recipes = CreateRecipes(driver)
        auth_page = AuthPage(driver)

        comment = DataGenerator.create_random_comment()
        image_path = "data/zapekanka.png"
        uid = DataGenerator.generator_uid()
        name_recipes = f"Запеканка {uid}"

        auth_page.open(Ad.URL_AUTH)
        auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD)
        create_recipes.click_element(Rl.CREATE_RECIPE_LINK)

        create_recipes.set_input(Rcl.RECIPE_NAME_INPUT, name_recipes)
        create_recipes.click_element(Rcl.TAG_LUNCH)
        create_recipes.set_input(Rcl.COOKING_TIME_INPUT, 20)
        create_recipes.set_input(Rcl.DESCRIPTION_TEXTAREA, comment)

        ingredients = [
            ("яйца куриные", 50),
            ("творог 18%", 300),
            ("мука 1 сорт", 100)
        ]
        for name, amount in ingredients:
            create_recipes.add_ingredient(name, amount)

        create_recipes.upload_image(Rcl.IMAGE_UPLOAD_INPUT, image_path)
        create_recipes.click_element(Rcl.SUBMIT_BUTTON)
        title_recipes_text = create_recipes.get_element_text(Rcdl.RECIPE_TITLE)
        assert uid in title_recipes_text, (
            f"Ожидалось найти ID '{uid}' в названии рецепта, "
            f"но получено: '{title_recipes_text}'"
        )
