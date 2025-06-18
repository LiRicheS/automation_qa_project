from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    date_of_birth: date = None
    age: str = None
    salary: str = None
    department: str = None
    current_address: str = None
    permanent_address: str = None

@dataclass
class Color:
    color_name: list = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

