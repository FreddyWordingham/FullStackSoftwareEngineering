from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import cv2
import numpy as np

from . import mandlebrot
from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return settings.TEMPLATES.TemplateResponse("index.html", {"request": request})


@app.get("/hello/{name}")
async def hello(name: str):
    return f"Hello, {name}!"


class SampleInput(BaseModel):
    real: float
    imag: float
    max_iters: int


@app.post("/sample")
async def sample(input: SampleInput):
    return mandlebrot.sample(input.real + input.imag * 1j, input.max_iters)


class ColInput(BaseModel):
    real: float
    imag: float
    max_iters: int
    hex_start: str
    hex_end: str


@app.post("/col")
async def col(input: ColInput):
    num_iters = mandlebrot.sample(input.real + input.imag * 1j, input.max_iters)
    rgb_start = hex_to_rgb(input.hex_start)
    rgb_end = hex_to_rgb(input.hex_end)
    rgb_sample = lerp_colour(rgb_start, rgb_end, num_iters / input.max_iters)
    hex_sample = rgb_to_hex(rgb_sample)
    return {"numIters": num_iters, "col": hex_sample}


@app.get("/area/{min_re}/{max_re}/{min_im}/{max_im}")
async def area(min_re: float, max_re: float, min_im: float, max_im: float):
    ans = mandlebrot.sample_area(min_re, max_re, min_im, max_im)
    return ans.tolist()


@app.get("/plot/{min_re}/{max_re}/{min_im}/{max_im}/{start_hex}/{end_hex}")
async def plot(
    min_re: float,
    max_re: float,
    min_im: float,
    max_im: float,
    start_hex: str,
    end_hex: str,
):
    hex = mandlebrot.plot(min_re, max_re, min_im, max_im, start_hex, end_hex)
    rgb = np.zeros((hex.shape[0], hex.shape[1], 3), dtype=np.uint8)
    for i in range(hex.shape[0]):
        for j in range(hex.shape[1]):
            rgb[i, j] = hex_to_rgb(hex[i, j])
    arr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    _success, im = cv2.imencode(".png", arr)
    headers = {"Content-Disposition": 'inline; filename="test.png"'}
    return Response(im.tobytes(), headers=headers, media_type="image/png")


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    return list(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def lerp_colour(col_a, col_b, t):
    r = int((1 - t) * col_a[0] + t * col_b[0])
    g = int((1 - t) * col_a[1] + t * col_b[1])
    b = int((1 - t) * col_a[2] + t * col_b[2])
    return (r, g, b)


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
