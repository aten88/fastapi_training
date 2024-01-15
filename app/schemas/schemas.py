from enum import Enum
from typing import Optional, Union
import re

from pydantic import BaseModel, Field, validator, root_validator


class EduactionLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str = Field(
        ..., max_length=20,
        title='Полное имя', description='Можно вводить в любом регистре'
    )
    surname: Union[str, list[str]] = Field(
        ..., max_length=50
    )
    age: Optional[int] = Field(None, gt=4, le=99)
    is_staff: bool = Field(False, alias='is-staff')
    education_level: Optional[EduactionLevel]

    class Config:
        title = 'Класс приветствия'
        min_anystr_length = 2
        schema_extra = {
            'examples': {
                'single_surname': {
                    'summary': 'Одна фамилия',
                    'description': 'Одиночная фамилия передается строкой',
                    'value': {
                       'name': 'Taras',
                       'surname': 'Belov',
                       'age': 20,
                       'is_staff': False,
                       'education_level': 'Среднее образование'
                    }
                },
                'multiple_surnames': {
                    'summary': 'Несколько фамилий',
                    'description': 'Несколько фамилий передаются списком',
                    'value': {
                       'name': 'Eduardo',
                       'surname': ['Santos', 'Tavares'],
                       'age': 20,
                       'is_staff': False,
                       'education_level': 'Высшее образование'
                    }
                },
                'invalid': {
                    'summary': 'Некорректный запрос',
                    'description': 'Возраст передается только целым числом',
                    'value': {
                        'name': 'Eduardo',
                        'surname': ['Santos', 'Tavares'],
                        'age': 'forever young',
                        'is_staff': False,
                        'education_level': 'Среднее специальное образование'
                    }
                }
            }
        }

    @validator('name')  # В качестве аргумента валидатору передается имя поля,
    # которое нужно проверить.
    # Первый параметр функции-валидатора должен называться строго cls.
    # Вторым параметром идет проверяемое значение,
    # его можно назвать как угодно.
    # Декоратор @classmethod ставить нельзя, иначе валидатор не сработает.
    def name_cant_be_numeric(cls, value: str):  # Проверяем, не состоит ли
        # строка исключительно из цифр:
        if value.isnumeric():
            raise ValueError('Имя не может быть числом')  # При ошибке
        # валидации можно выбросить # ValueError, TypeError или AssertionError.
        return value  # Если проверка пройдена, возвращаем значение поля.

    @root_validator(skip_on_failure=True)
    def using_different_values(cls, values):
        surname = ''.join(values['surname'])
        checked_value = values['name'] + surname
        if (
            re.search('[а-я]', checked_value, re.IGNORECASE) and
            re.search('[a-z]', checked_value, re.IGNORECASE)
        ):
            raise ValueError(
                'Пожалуйста, не смешивайте русские и латинские буквы'
            )
        return values
