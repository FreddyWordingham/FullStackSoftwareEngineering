from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import cv2
import numpy as np

from . import colour
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


@app.post("/sample")
async def sample(input: SampleInput):
    return mandlebrot.sample(input.real + input.imag * 1j)


@app.get("/col/{re}/{im}/{start_hex}/{end_hex}", response_class=HTMLResponse)
async def col(re: float, im: float, start_hex: str, end_hex: str):
    print(re, im, start_hex, end_hex)
    ans = mandlebrot.sample(re + im * 1j)
    print(ans)
    max_iter = 100
    col = colour.interpolate_linear(f"{start_hex}", f"{end_hex}", ans / max_iter)
    print(col)
    html = f"<body style='background-color: {col}'><h1>{col}</h1></body>"
    return html


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


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return list(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))
