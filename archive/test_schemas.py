from enum import Enum

from pydantic import BaseModel


class PythonFramework(str, Enum):
    DJANGO = 'Django'
    FASTAPI = 'FastAPI'
    FLASK = 'Flask'
    PYRAMID = 'Pyramid'
    QUART = 'Quart'
    SANIC = 'Sanic'
    TORNADO = 'Tornado'


class Bulletin(BaseModel):
    framework: PythonFramework
    your_name: str
