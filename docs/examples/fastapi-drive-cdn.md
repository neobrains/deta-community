---
title: FastAPI Drive CDN Example
description: A sample FastAPI Drive CDN
comments: true
---

# FastAPI Drive CDN Example
This tutorial will show you how to create a simple bare-bones CDN using a Deta Drive and a Micro.

## Setup
We'll start by installing the necessary packages.
```txt title="requirements.txt"
deta
fastapi
python-multipart
uvicorn[standard]
```

`deta` will be used to access the Deta Drive, `fastapi` to create the app, and `python-multipart` for receiving files. As always, we need `uvicorn` to run the app.

In order for your app to access Deta services such as Base and Drive, you need to set the `DETA_PROJECT_KEY` environment variable.
Check out the section on [project keys](/getting-started/general#project-keys) for instructions on how to do that.

## Code
Here is the Python code that will handle the API requests and responses.
```py title="main.py"
--8<-- "docs/code/example_fastapi_drive_cdn/main.py"
```

This might seem like a lot, so let's break it down.

First, we import some classes and modules. These will be used throughout the code.
```py
import random
import string

from deta import Deta
from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import Response, RedirectResponse
```

Next, we create a `FastAPI` app instance and an instance of the `Deta` class.
This instance allows us to interact with Deta services and automatically loads the project key from the environment.
The last line creates a Deta Drive named `storage` which we will use to store all the files uploaded to our CDN.
```py
app = FastAPI()
deta = Deta()
# Create a Drive named 'storage'.
storage = deta.Drive("storage")
```

Now let's start implementing the API endpoints.
The first one we'll add will allow us to upload files to our CDN.
```py
# Save a file to the storage Drive and return the URL of the file.
@app.post("/upload", status_code=201)
async def upload(request: Request, file: UploadFile):
    id = generate_id()
    storage.put(id, file.file)
    return {
        "url": f"{request.base_url}cdn/{id}",
    }
```

The `file` parameter here accepts a file upload.
Once we receive a file, we generate a random identifier string to be used as the file name, and save the file to the `storage` Drive.
Lastly, we return a URL which will allow us to download the file.

You might have noticed the `generate_id()` function is not defined yet, so let's do that now.
This will generate a random string of lowercase ASCII characters, with a length of 8 by default.
```py
# Generate a random string of ASCII characters.
def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))
```

Next, lets add an endpoint to download files from our CDN.
In this function we first try to get the file from the `storage` Drive.
If the file is not found (indicated by a `None` value), we respond with a `404` error.
Finally, we return the file in a [`Response`](https://fastapi.tiangolo.com/advanced/custom-response/#response)
and specify the MIME type as `application/octet-stream` to indicate that the file could be any binary data.

A CDN without caching would be inefficient, so we'll add a `Cache-Control` header to the response.
This header tells the browser to locally save the file for 24 hours before downloading it again,
which will greatly improve load times and reduce the number of requests our CDN needs to handle.
```py
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
```

As a final touch, let's redirect the root path to the API documentation page provided by FastAPI,
so that us humans have something to look at instead of `404 Not Found`.
```py
# Redirect to the docs page.
@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse("/docs")
```

## Deploy
Now we'll create a new Micro and deploy our code to it.
```console
$ deta new --name fastapi-drive-cdn --python
```

!!! success
    See it live at https://yacdn.deta.dev/

    (yacdn = yet another CDN)

!!! info "Fun Fact"
    This exact CDN is used to serve some files for this site, such as the images on the [404 page](/404).

## Use
Now that we have our CDN up and running, let's try it out.
You can either navigate to the CDN's root path in your browser and use the interactive API documentation to upload a file,
use a tool like `cURL` or `Postman`, or use the CDN from your own code.

Here's an example of how to use the CDN from Python using the `requests` package.
```py
import requests

# Upload a file to the CDN.
with open("image.jpg", "rb") as file:
    response = requests.post(
        "https://yacdn.deta.dev/upload",
        files={"file": file}
    )

url = response.json()["url"]

# Download the file from the CDN.
response = requests.get(url)

with open("downloaded_image.jpg", "wb") as file:
    file.write(response.content)
```

After we upload a file to the CDN, we get a URL that we can use to download the file.

!!! warning
    The returned URL is not saved anywhere, so make sure you save it somewhere.

For more information on each of the things we've used in this example, visit the
[FastAPI docs](https://fastapi.tiangolo.com/),
[Uvicorn docs](https://www.uvicorn.org/),
[Requests docs](https://requests.readthedocs.io/)
and [Deta docs](https://docs.deta.sh).
