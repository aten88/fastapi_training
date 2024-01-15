from fastapi import APIRouter, Body

from app.schemas.schemas import Person

router = APIRouter()


@router.post('/hello')
def greetings(person: Person = Body(
    ..., examples=Person.Config.schema_extra['examples']
    )
) -> dict[str, str]:
    # ПЛОХОЙ ПРИМЕР ИСПОЛЬЗОВАНИЯ В КОДЕ ФУНКЦИИ
    #     ...,
    #     examples={
    #         # Первый пример.
    #         'single_surname': {
    #             'summary': 'Одна фамилия',
    #             'description': 'Одиночная фамилия передается строкой',
    #             'value': {
    #                 'name': 'Taras',
    #                 'surname': 'Belov',
    #                 'age': 20,
    #                 'is_staff': False,
    #                 'education_level': 'Среднее образование'
    #                 }
    #         },
    #         # Второй пример.
    #         'multiple_surnames': {
    #             'summary': 'Несколько фамилий',
    #             'description': 'Несколько фамилий передаются списком',
    #             'value': {
    #                 'name': 'Eduardo',
    #                 'surname': ['Santos', 'Tavares'],
    #                 'age': 20,
    #                 'is_staff': False,
    #                 'education_level': 'Высшее образование'
    #             }
    #         },
    #         # Третий пример.
    #         'invalid': {
    #             'summary': 'Некорректный запрос',
    #             'description': 'Возраст передается только целым числом',
    #             'value': {
    #                 'name': 'Eduardo',
    #                 'surname': ['Santos', 'Tavares'],
    #                 'age': 'forever young',
    #                 'is_staff': False,
    #                 'education_level': 'Среднее специальное образование'
    #             }
    #         }
    #     }
    # )
    # ЛУЧШЕ ХРАНИТЬ ЭТОТ СЛОВАРЬ В schemas.py и потом на него сослаться

    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
