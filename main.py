import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import TemplateNotFound

# May separate this into a separate file (routers) if it gets big.
app = FastAPI()
app.mount("/assets", StaticFiles(directory="site/assets"), name="assets")
templates = Jinja2Templates(directory="site")


# Try to handle all paths.
@app.get("/{path:path}")
async def path(request: Request, path: str):
    # If the path is a file.
    if os.path.splitext(path)[1]:
        return FileResponse(os.path.join("site", path))
    # Otherwise, try serving an HTML template with the name.
    try:
        return templates.TemplateResponse(os.path.join(path, "index.html"), {"request": request})
    except TemplateNotFound:
        raise HTTPException(status_code=404)


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request})
