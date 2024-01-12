from fastapi import FastAPI

from enum import Enum

app = FastAPI()


class Tag(str, Enum):
    immutable = "immutable"
    mutable = "mutable"


@app.post('/a', tags=[Tag.immutable.name], summary='Функция "A"')
def a() -> str:
    """
    В данном методе возвращается неизменяемый тип данных.
    """
    return 'Вот это ответ!'


@app.get(
        '/b', tags=[Tag.mutable.name],
        summary='Функция "B"',
        description='Данный метод возвращает изменяемый тип данных'
    )
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post('/c', tags=[Tag.immutable.name], summary='Функция "C"')
def c() -> int:
    """
    В данном методе возвращается неизменяемый тип данных.
    """
    return 42


@app.get(
        '/d', tags=[Tag.mutable.name],
        summary='Функция "D"',
        description='Данный метод возвращает изменяемый тип данных'
    )
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
