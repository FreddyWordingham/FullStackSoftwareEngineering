from fastapi import FastAPI

from . import mandlebrot


app = FastAPI()


@app.get("/")
async def index():
    return "Hello, world!"


@app.get("/hello/{name}")
async def hello(name: str):
    return f"Hello, {name}!"


@app.get("/sample/{re}/{im}")
async def sample(re: float, im: float):
    ans = mandlebrot.sample(re + im * 1j)
    return f"({re},{im}) == {ans}"
