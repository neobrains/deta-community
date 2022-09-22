# Basic Deta
Welcome to Basic | Deta. Here you can find the basic docs, frequent FAQs, and code templates.

Website : https://basic.deta.dev

## Contributing

Download the required dependencies

```shell
pip install -r requirements.txt
```

If you want to edit the docs, run the following command

```shell
mkdocs serve
```
And then you can edit the files in the `docs` folder.

If you want to contribute to the code, you can edit `main.py`, and then run it using

```shell
uvicorn main:app --reload
```

But you should note that, you need to do 
```shell
mkdocs build
```
before you run the webserver. Also if you edit the docs, you need to run the above command again.
