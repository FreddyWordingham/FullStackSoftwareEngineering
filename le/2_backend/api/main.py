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


@app.get("/area/{min_re}/{max_re}/{min_im}/{max_im}")
async def sample(min_re: float, max_re: float, min_im: float, max_im: float):
    print(min_re, max_re, min_im, max_im)
    ans = mandlebrot.sample_area(min_re, max_re, min_im, max_im)
    return ans.tolist()


@app.get("/plot/{min_re}/{max_re}/{min_im}/{max_im}")
async def plot(min_re: float, max_re: float, min_im: float, max_im: float):
    print(min_re, max_re, min_im, max_im)
    mandlebrot.plot(min_re, max_re, min_im, max_im)
