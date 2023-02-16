from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings


class Environment(BaseSettings):
    SECRET_KEY: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()
TEMPLATES = Jinja2Templates(directory="templates")
