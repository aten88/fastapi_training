from fastapi import FastAPI, Query

from enum import Enum

app = FastAPI()


@app.get('/math-sum')
def math_sum(
    add: list[float] = Query(
        None, gt=0, lt=9.99,
        title='Список чисел',
        description='Принимает список дробных чисел'
    )
):
    result = 0
    for param in add:
        result += param
    return result


class Tag(str, Enum):
    immutable = "immutable"
    mutable = "mutable"


@app.post('/a', tags=[Tag.immutable.name], summary='Функция "A"')
def a() -> str:
    """
    Данный метод возвращает неизменяемый тип данных.
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
    Данный метод возвращает неизменяемый тип данных.
    """
    return 42


@app.get(
        '/d', tags=[Tag.mutable.name],
        summary='Функция "D"',
        description='Данный метод возвращает изменяемый тип данных'
    )
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
