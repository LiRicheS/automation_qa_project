from data.data import Person
from faker import Faker
import random
fake_ru = Faker('ru_RU')  # Генерация данных на русском
Faker.seed()  # Устанавливает фиксированное значение для генератора случайных чисел.


def generate_data_person():
    yield Person(
        full_name=fake_ru.last_name() + " " + fake_ru.first_name() + " " + fake_ru.middle_name(),
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        email=fake_ru.email(),
        age=str(random.randint(39, 40)),
        salary=str(random.randint(1, 9999999999)),
        department=fake_ru.job(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address()
    )

