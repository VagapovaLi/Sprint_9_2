from selenium.webdriver.common.by import By


class RecipeCreationLocators:
    # Заголовок формы
    FORM_TITLE = (By.XPATH, "//h1[text()='Создание рецепта']")

    RECIPE_NAME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField') and preceding-sibling::div[text()='Название рецепта']]")
    COOKING_TIME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField') and preceding-sibling::div[contains(text(), 'Время приготовления')]]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField')]")

    # Теги рецепта
    TAG_BREAKFAST = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Завтрак']]")
    TAG_LUNCH = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Обед']]")
    TAG_DINNER = (By.XPATH, "//button[contains(@class, 'styles_checkbox') and following-sibling::span[text()='Ужин']]")

    # Ингредиенты
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd') and text()='Добавить ингредиент']")

    # Загрузка изображения
    IMAGE_UPLOAD_INPUT = (By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput')]")

    # Кнопка создания рецепта
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_button') and contains(text(), 'Создать рецепт')]")

