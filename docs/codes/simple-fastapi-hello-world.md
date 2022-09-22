---
title: Simple FastAPI Application
description: A sample FastAPI application
comments: true
---
# This is a sample , soon update

## Requirements
```txt
uvicorn[standard]
fastapi
```

## Code (`main.py`)
```py
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)

# Here main is the file name and app is the name of the FastAPI app
```

Run it with `uvicorn main:app --reload` or `uvicorn main:app --reload --port 8000`. Or you can just `python main.py`

## Deploy to Deta
Install the Deta CLI and run the following command in the same directory as the `main.py` file.
```sh
deta new --name name_of_app --python --project project_name
deta deploy
```
`--project` is optional ( `default` is used if not specified )
So,
```sh
det new --name name_of_app --python
```
Also Works! Now go to the url given by the command and you will see the app running!