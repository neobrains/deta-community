---
title: Simple FastAPI Application
description: A sample FastAPI application
comments: true
---
# Simple FastAPI App
This tutorial will show you how to create a simple FastAPI application on Deta.

## Requirements
To start, we need to install `fastapi` to create the app, and `uvicorn` to run it.
```txt title="requirements.txt"
fastapi
uvicorn[standard]
```

## Code
This is the most basic FastAPI application you can make.
```py title="main.py"
--8<-- "docs/code/example_fastapi_app/main_simple.py"
```

Run it with `uvicorn main:app --reload`. Visit http://127.0.0.1:8000/ to see your app in action.

## Deploy to Deta
If you haven't already installed the Deta CLI, read the [Getting Started](/getting-started) section.

Now, lets create a new Micro under the default project called `fastapi-app`.
```bash
$ deta new --name fastapi-app --python
```

The current code will automatically be deployed, but once you make changes you will need to re-deploy with `deta deploy`.

!!! tip "Automatically deploy to Deta"
    If you have already deployed the application to deta, you can use `deta watch`
    to automatically deploy the application when you make changes to the code.

# A Slightly More Complex App
Most apps however will need to do more than just return a string.
Lets add HTML templates, CSS styles, and some JavaScript to our app to give it some actual frontend.

## Requirements
This will require installing one more package:
```txt title="requirements.txt"
fastapi
jinja2
uvicorn[standard]
```

## Code
Here's our new Python code,
```py title="main.py"
--8<-- "docs/code/example_fastapi_app/main.py"
```
A base HTML template,
```html title="templates/base.html"
--8<-- "docs/code/example_fastapi_app/templates/base.html"
```
And an index page template,
```html title="templates/index.html"
--8<-- "docs/code/example_fastapi_app/templates/index.html"
```
Some styles,
```css title="static/style.css"
--8<-- "docs/code/example_fastapi_app/static/style.css"
```
Some JavaScript,
```js title="static/script.js"
--8<-- "docs/code/example_fastapi_app/static/script.js"
```
And an image for good measure.

`static/ram.jpg`

<img src="../../code/example_fastapi_app/static/ram.jpg" alt="ram.jpg" width="200" />

Deploy as before with `deta deploy`.

!!! success
    See it live at https://2duy8q.deta.dev/
