from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# (venv) (base) PS C:\Users\Oleksii\PycharmProjects\Woodland ABC\Woodland_ABC\backend> uvicorn --reload app.main:app