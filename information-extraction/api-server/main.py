# api server example
# author: Sizhong Du
# since: 2025-03-10


# pip install "fastapi[standard]"


# fastapi dev main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
