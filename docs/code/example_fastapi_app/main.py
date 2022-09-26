from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
# Serve static files from the '/static' directory.
app.mount("/static", StaticFiles(directory="static"), name="static")
# Load HTML templates from the '/templates' directory.
templates = Jinja2Templates(directory="templates")


# Render the 'index.html' template.
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
