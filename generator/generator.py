import random

from data.data import Person, Color, Date
from faker import Faker
fake_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generate_data_person():
    yield Person(
        full_name=fake_ru.last_name() +
                  " " + fake_ru.first_name() +
                  " " + fake_ru.middle_name(),
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        email=fake_ru.email(),
        phone='8987155790',
        date_of_birth=fake_ru.date_of_birth(),
        age=str(random.randint(39, 40)),
        salary=str(random.randint(1, 9999999999)),
        department=fake_ru.job(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address()
    )

def generated_file():
    path = rf'E:\automation_qa_course\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00"
    )
