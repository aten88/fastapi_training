from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str

    class Config:
        schema_extra = {
            'examples': {
                'first_prompt': {
                    'summary': 'Колобок',
                    'description': 'Актер и реплики Колобка',
                    'value': {
                        'actor': 'Медведь',
                        'replica': 'Колобок, колобок, я тебя съем!'
                    }
                },
                'second_prompt': {
                    'summary': 'Гамлет, принц датский',
                    'description': 'Актер и реплики Гамлета, принца датского',
                    'value': {
                        'actor': 'Гамлет',
                        'replica': 'Бедный Йорик! Я знал его, Горацио.'
                    }
                },
                'third_prompt': {
                    'summary': 'Палата номер 6',
                    'description': 'Актер и реплики Палата номер 6',
                    'value': {
                        'actor': 'Рагин',
                        'replica': 'Покой и довольство человека не вне его, а в нём самом.'
                    }
                },
            }
        }


@app.post('/give-a-hint')
def send_prompt(hint: PrompterHint = Body(
    ..., examples=PrompterHint.Config.schema_extra['examples']
    )
):
    return hint
