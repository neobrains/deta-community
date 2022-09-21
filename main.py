# Boilerplate for fastapi and jinja2

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets", StaticFiles(directory="site/assets"), name="assets")
templates = Jinja2Templates(directory="site")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})