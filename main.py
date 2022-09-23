from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# May separate this into a separate file ( routers ) if it gets big
app = FastAPI()
app.mount("/assets", StaticFiles(directory="site/assets"), name="assets")
templates = Jinja2Templates(directory="site")

# This is for index.md
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/faq")
async def faq(request: Request):
    return templates.TemplateResponse("faq/index.html", {"request": request})

@app.get("/getting-started")
async def getting_started(request: Request):
    return templates.TemplateResponse("getting-started/index.html", {"request": request})

@app.get("/search/search_index.json")
async def search_index():
    return FileResponse("site/search/search_index.json")

@app.get("/codes/{code}")
async def code_pages(request: Request, code: str):
    return templates.TemplateResponse(f"codes/{code}/index.html", {"request": request})

@app.get("/images/{image}")
async def images(request: Request, image: str):
    return FileResponse(f"site/images/{image}")

@app.get("/javascripts/{js}")
async def javascripts(request: Request, js: str):
    return FileResponse(f"site/javascripts/{js}")

@app.get("/sitemap.xml")
async def sitemap():
    return FileResponse("site/sitemap.xml")

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request})