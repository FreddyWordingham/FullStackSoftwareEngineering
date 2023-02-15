from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

from . import colour
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


@app.get("/col/{re}/{im}/{start_hex}/{end_hex}", response_class=HTMLResponse)
async def col(re: float, im: float, start_hex: str, end_hex: str):
    ans = mandlebrot.sample(re + im * 1j)
    max_iter = 100
    print(f"#{start_hex}", f"#{end_hex}")
    col = colour.interpolate_linear(f"{start_hex}", f"{end_hex}", ans / max_iter)
    html = f"<body style='background-color: {col}'><h1>{col}</h1></body>"
    return html


@app.get("/area/{min_re}/{max_re}/{min_im}/{max_im}")
async def area(min_re: float, max_re: float, min_im: float, max_im: float):
    print(min_re, max_re, min_im, max_im)
    ans = mandlebrot.sample_area(min_re, max_re, min_im, max_im)
    return ans.tolist()


@app.get("/plot/{min_re}/{max_re}/{min_im}/{max_im}")
async def plot(min_re: float, max_re: float, min_im: float, max_im: float):
    print(min_re, max_re, min_im, max_im)
    rand = random.randint(0, 1000000)
    filename = "mandlebrot_{rand}.png"
    mandlebrot.plot(filename, min_re, max_re, min_im, max_im)

    return {"filename": filename}
