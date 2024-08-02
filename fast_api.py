from fastapi import FastAPI
from pydantic import BaseModel

class User_Input(BaseModel):
    number: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/predict')
def test(input):
    return f'{input}'