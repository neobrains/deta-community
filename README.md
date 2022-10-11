# Basic Deta 🚀
Basic docs, FAQs, , featured projects and code templates for [Deta](https://www.deta.sh/).

Website: https://basic.deta.dev

## Feature your project on Basic Deta 🥰
Send us a pr with your project details in the [feature.json](feature.json)

### Step #1
Add another element in the json with contents like
```json
{
    ...above content},
    "project-name" : {
        "about" : "A paragraph about your project",
        "details" : "URL: abc\\nRepository: abc\\nAuthor: abc",
        "preview" : 1,
        "image_uri" : "abc"
    }
}
```

Make sure to add `\\n` between each line of details as to separate them in the markdown. Also note that about should be a single line which can be big enough to contain the whole paragraph.

Moreover note that if your project contains no image remove `image_uri` and set `preview` to 0.

See the json file for better understanding.

### Step #2
Edit the [feature-boiler.md](docs/feature-boiler.md) and add your project name like this -

```
### Project Name
<!--start project-name-->

<!--end-->
````

`project-name` is the tag to be used in the `feature.json` file.

### Step #3
There's no need to edit the `docs/feature.md` file! Just send us the pr and after successfull merge it will automatically add in there!.

## Contributing ✔️
### Setting up the environment
Install the required dependencies.
```console
$ pip install -r requirements.txt
```

To preview the site while editing, use the following command.
```console
$ mkdocs serve
```

You can also do `python feature.py` to update `feature.md` file (optional in case of any changes to boiler and json file by you).

Before committing, stop the MkDocs server and preview the site using `uvicorn` to make sure everything works.
```console
$ mkdocs build
$ uvicorn main:app --reload
```
