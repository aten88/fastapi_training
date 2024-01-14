from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AcceptedCategory(str, Enum):
    OUTPUT_DEVICES = 'Принтеры'
    VISUAL_DEVICES = 'Мониторы'
    OPTIONAL_DEVICES = 'Доп. оборудование'
    INPUT_DEVICES = 'Устройства ввода'


class Person(BaseModel):
    name: str
    surname: str
    age: Optional[int]
    is_staff: bool = False


class AuctionLot(BaseModel):
    category: AcceptedCategory
    name: str
    model: Optional[str]
    start_price: int = 1000
    seller: Person


@app.post('/new-lot')
def register_lot(lot: AuctionLot):
    # Здесь мог бы быть код для сохранения заявки,
    # но мы не станем его писать. И вам не надо.
    return {'result': 'Ваша заявка зарегистрирована!'}
