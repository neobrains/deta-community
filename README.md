# Basic Deta
Basic docs, FAQs, and code templates for [Deta](https://www.deta.sh/).

Website: https://basic.deta.dev

## Contributing
### Setting up the environment
Install the required dependencies.
```console
$ pip install -r requirements.txt
```

To preview the site while editing, use the following command.
```console
$ mkdocs serve
```

Before committing, stop the MkDocs server and preview the site using `uvicorn` to make sure everything works.
```console
$ mkdocs build
$ uvicorn main:app --reload
```
