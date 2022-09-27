# Getting started with Base

Deta Base is a fully-managed, fast, scalable and secure NoSQL database with a focus on end-user simplicity.
It offers a [UI](https://docs.deta.sh/docs/base/base_ui) through which you can easily see, query, update and delete records in the database.

If you are using a deta micro, then base can be useful to you as it gives a latency of 5-9ms only.

## Creating a Base
Base can't be created via UI or CLI. It is created automatically when you put something in it. So, let's create a base.

### Installing the SDK
We'll start by installing the necessary packages.

```txt title="requirements.txt"
deta
```

`deta` will be used to connect to the database.

In order for your app to access Deta services such as Base and Drive, you need to set the `DETA_PROJECT_KEY` environment variable.
You can find your project key in the [Deta Dashboard](https://web.deta.sh).

Alternatively, you can also pass the project key to the `Deta` class.

```py 
deta = deta.Deta("project_key")
```

```py title="base.py"
#### TODO!!!
import deta
deta = deta.Deta()
my_db = deta.Base("my_db")

from deta import Deta
deta = Deta("project key")  
db = deta.Base("simple_db")

# store objects

# a key will be automatically generated
db.put({"name": "alex", "age": 77})  

# we will use "one" as a key
db.put({"name": "alex", "age": 77}, "one")  

# the key could also be included in the object itself  
db.put({"name": "alex", "age": 77, "key": "one"})

# retrieve objects
item = db.get("one") # retrieving item with key "one"

```