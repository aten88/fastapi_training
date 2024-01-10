from fastapi import FastAPI

from enum import Enum

app = FastAPI()


class Tag(Enum):

    MUTABLE = 1
    IMMUTABLE = 2


@app.post('/a', tags=[Tag.MUTABLE.name], summary='Функция "A"')
def a() -> str:
    """
    В данном методе возвращается изменяемый тип данных.
    """
    return 'Вот это ответ!'


@app.get(
        '/b', tags=[Tag.MUTABLE.name],
        summary='Функция "B"',
        description='Данный метод возвращает изменяемый тип данных'
    )
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post('/c', tags=[Tag.IMMUTABLE.name], summary='Функция "C"')
def c() -> int:
    """
    В данном методе возвращается неизменяемый тип данных.
    """
    return 42


@app.get(
        '/d', tags=[Tag.MUTABLE.name],
        summary='Функция "D"',
        description='Данный метод возвращает изменяемый тип данных'
    )
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
