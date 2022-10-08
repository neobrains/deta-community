import random
import string

from deta import Deta
from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import Response, RedirectResponse

app = FastAPI()
deta = Deta()
# Create a Drive named 'storage'.
storage = deta.Drive("storage")
metadata_db = deta.Base("metadata")


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
    metadata = metadata_db.get(id) or {}
    filename = metadata.get('filename', id)
    media_type = metadata.get("content_type", "application/octet-stream")
    headers = {
        "Cache-Control": "public, max-age=86400",
        "Content-Disposition": f"inline; filename=\"{filename}\"",
    }
    return Response(
        content=file.read(),
        media_type=media_type,
        headers=headers,
    )


# Save a file to the storage Drive and return the URL of the file.
@app.post("/upload", status_code=201)
async def upload(request: Request, file: UploadFile):
    id = generate_id()
    metadata_db.put(
        {
            "id": id,
            "filename": file.filename,
            "content_type": file.content_type,
        },
        key=id,
    )
    storage.put(id, file.file)
    return {
        "url": f"{request.base_url}cdn/{id}",
    }