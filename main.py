import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse

app = FastAPI()


# Try to handle all paths.
@app.get("/{path:path}")
async def path(request: Request, path: str):
    # If the path is a file, the path will be relative to "/site".
    if os.path.splitext(path)[1]:
        path = os.path.join("site", path)
    # Otherwise, try serving an HTML file with the name.
    else:
        path = os.path.join("site", path, "index.html")
    if not os.path.exists(path):
        raise HTTPException(status_code=404)
    return FileResponse(path)


@app.exception_handler(404)
async def not_found_handler(request: Request, exception):
    # Redirects for moved pages.
    path = request.url.path.split("/")
    if path and path[1] == "getting-started":
        if len(path) > 2 and path[2] == "general":
            return RedirectResponse("/tutorials")
        return RedirectResponse(f"/tutorials/{'/'.join(request.url.path.split('/')[2:])}")

    return FileResponse("site/404.html")
