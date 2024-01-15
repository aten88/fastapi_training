import re

from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str

    @root_validator(skip_on_failure=True)
    def cant_use_forbidden_names(cls, value):
        checked_value = ' '.join([value['name'], value['surname']])
        if re.search('|'.join(FORBIDDEN_NAMES), checked_value, re.IGNORECASE):
            raise ValueError('Не используйте имена из киновселенной STAR WARS')
        return value


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}
