from fastapi import FastAPI, HTTPException
import uvicorn
import json
from pydantic import BaseModel
from caeser import *


class Data(BaseModel):
    encrypt: str


app = FastAPI()


def load_data():
    with open("data.json") as f:
        return json.load(f)


def save_data(data):
    with open("data.json", "w") as f:
        f.write(json.dumps(data))


@app.get("/")
def hello():
    return "welcome to the website"


@app.get("/test")
def return1():
    return {'msg': 'hi from test'}


@app.post("/test/{name}")
def write_file(name):
    with open("names.txt", "w") as f:
        f.write("names.txt" + name)
    return {"msg": "saved user"}


@app.post("/caesar")
def encrypt(text):
    a = caesar(text)
    return {"encrypted_text": a}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
