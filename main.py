from fastapi import FastAPI
from typing import Optional
# import uvicorn
from enum import Enum

app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None) - отключить SWAGGER и REDOCS
# app = FastAPI(docs_url='/swagger')


class EduactionLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me')
def hello_author():
    return {'Hello': 'author'}


@app.get('/{name}')
def greetings(
    name: str,
    surname: str,
    age: Optional[int] = None,
    is_staff: bool = False,
    education_level: Optional[EduactionLevel] = None,
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)
