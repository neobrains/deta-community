import random
import string

from deta import Deta
from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import Response, RedirectResponse

app = FastAPI()
deta = Deta()
# Create a Drive named 'storage'.
storage = deta.Drive("storage")


# Generate a random string of ASCII characters.
def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


# Redirect to the docs page.
@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse("/docs")


# Return a file from the storage Drive.
@app.get("/cdn/{id}")
async def cdn(id: str):
    file = storage.get(id)
    if file is None:
        raise HTTPException(status_code=404)
    headers = {"Cache-Control": "public, max-age=86400"}
    return Response(
        content=file.read(),
        media_type="application/octet-stream",
        headers=headers,
    )


# Save a file to the storage Drive and return the URL of the file.
@app.post("/upload", status_code=201)
async def upload(request: Request, file: UploadFile):
    id = generate_id()
    storage.put(id, file.file)
    return {
        "url": f"{request.base_url}cdn/{id}",
    }
