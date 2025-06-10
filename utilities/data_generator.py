from faker import Faker

class DataGenerator:

    @staticmethod
    def create_fake_user():
        """Метод для создания фейковых данных заказчика."""
        fake = Faker("ru_RU")
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        user_name = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)

        user = {"first_name": first_name,
                "last_name": last_name,
                "user_name": user_name,
                "email": email,
                "password": password
                }
        return user



    @staticmethod
    def create_random_comment():
        """Метод для создания случайного комментария длиной 100 символов"""
        fake = Faker("ru_RU")
        comment = fake.text(max_nb_chars=100)
        return comment[:100]

    @staticmethod
    def generator_uid():
        """Метод для генерации uid"""
        fake = Faker()
        uid = fake.uuid4()
        return uid



