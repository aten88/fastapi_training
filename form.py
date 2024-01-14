from fastapi import FastAPI, Form, File, UploadFile


app = FastAPI()


@app.post('/login')
def login(
    username: str = Form(...),
    password: str = Form(...),
    some_file: UploadFile = File(...)
):
    file_content = some_file.file.read().splitlines()
    return {
        'username': username,
        'file_content': file_content
    }
