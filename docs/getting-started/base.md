# Getting started with Base
Deta Base is a easy-to use NoSQL database that lets you store persistent data.
A bonus of Base is that it is extremely fast when used from within Deta Micros.

## Creating a Base
Bases are created automatically when you put data into them using the SDK.
Getting started with Deta Base is super easy, so let's see how it's done.

## Setting up your environment
In order for your app to access Deta services such as Base and Drive, you need to set the `DETA_PROJECT_KEY` environment variable.
Check out the section on [project keys](/getting-started/general#project-keys) for instructions on how to do that.

Alternatively, you can also pass the project key as an argument to the `Deta` constructor class.
```py
from deta import Deta

deta = Deta("your-project-key")
```

!!! info
    For the rest of this guide, we'll be using Python, but the same concepts apply to all the other languages.

## Using Base
The basic methods of Base are `put`, `get`, and `delete`.

- `put` adds an item
- `get` retrieves an item
- `delete` deletes an item

Items can be any JSON serializable data type, including lists, dictionaries,
and primitive types like integers, strings, and booleans.

It's time to start writing some code!
```pycon
# Import the Deta class.
>>> from deta import Deta

# Intitialize the Deta class.
>>> deta = Deta()

# Create a Base named "mydb".
>>> db = deta.Base("mydb")

# Store an item with a random key.
>>> db.put({"title": "1984", "author": "George Orwell"})
{'author': 'George Orwell', 'key': 'e0bm8kq3yho7', 'title': '1984'}

# Store an item with a set key.
>>> db.put(
...     {"name": "Chika Fujiwara", "age": 16, "birthday": "March 3"},
...     key="user-123",
... )
{'age': 16, 'birthday': 'March 3', 'key': 'user-123', 'name': 'Chika Fujiwara'}

# Retrieve an item by key.
>>> db.get("user-123")
{'age': 16, 'birthday': 'March 3', 'key': 'user-123', 'name': 'Chika Fujiwara'}
```

!!! note
    Only numbers up to 16 digits long are currently supported.
    To store larger numbers, convert them to strings first.

Those aren't the only methods available, here are a few more.

- `update` updates an item
- `insert` is the same as `put`, but will throw an error if the key already exists
- `put_many` adds multiple items

```pycon
# Update an existing item.
>>> db.update({"age": 17}, key="user-123")
>>> db.get("user-123")
{'age': 17, 'birthday': 'March 3', 'key': 'user-123', 'name': 'Chika Fujiwara'}

# Insert an item.
>>> try:
...     # Will fail.
...     db.insert(
...         {"name": "Yu Ishigami", "age": 16, 'birthday': 'March 3'},
...         key="user-123",
...     )
... except:
...     # Will succeed.
...     db.insert(
...         {"name": "Yu Ishigami", "age": 16, 'birthday': 'March 3'},
...         key="user-456",
...     )
{'age': 16, 'birthday': 'March 3', 'key': 'user-456', 'name': 'Yu Ishigami'}

# Add multiple items.
>>> db.put_many(
...     [
...         {
...             "title": "Roadside Picnic",
...             "author": "Arkaday & Boris Strugatsky",
...         },
...         {
...             "title": "Tuf Voyaging",
...             "author": "George R. R. Martin",
...         },
...         {
...             "title": "The Door into Summer",
...             "author": "Robert A. Heinlein",
...         },
...     ],
... )
{
    'processed':
    {
        'items':
        [
            {
                'author': 'Arkaday & Boris Strugatsky',
                'key': 'lt4g72qhl3dw',
                'title': 'Roadside Picnic'
            },
            {
                'author': 'George R. R. Martin',
                'key': '4bnyytrozupq',
                'title': 'Tuf Voyaging',
            },
            {
                'author': 'Robert A. Heinlein',
                'key': '2xpuzt12jamq',
                'title': 'The Door into Summer'
            }
        ]
    }
}
```

There are more ways to update items, the details of which can be found in the
[official documentation](https://docs.deta.sh/docs/base/sdk/#update-operations-1).

## Querying Base
When you start storing more and more data, it can become difficult and inefficient to store the key of every single item.
If only there was a way to retrieve items based on their values...

Enter: the `fetch` method! `fetch` allows you to get items using **queries** based not only on their values,
but also by using conditonal statements like "greater than" and "contains".
The `fetch` method returns a `FetchResponse` object, which has the properties `count`, `items`, and `last`.

- `count` is the number of items in the response
- `items` is a list of items in the response
- `last` is the key of the last item in the response, which is useful for pagination

An example query looks like this:
```py
{
    "name?contains": "Smith",
    "age?gt": 30,
    "is_alive": True,
}
```

This translates into "items where the `name` field contains the string `"Smith"`, and the `age` field is greater than `30`, and the `is_alive` field is `true`".

```pycon
# Fetch all items.
>>> response = db.fetch()
>>> response
<deta.base.FetchResponse object at 0x000001B526949A20>
>>> response.count
6
>>> response.items
[
    {
        'author': 'Robert A. Heinlein',
        'key': '2xpuzt12jamq',
        'title': 'The Door into Summer'
    },
    ...
    {
        'author': 'George Orwell',
        'key': 'e0bm8kq3yho7',
        'title': '1984'
    }
]

# Fetch items where "birthday" is "March 3".
>>> db.fetch({"birthday": "March 3"}).items
[
    {
        'age': 17,
        'birthday': 'March 3',
        'key': 'user-123',
        'name': 'Chika Fujiwara'
    },
    {
        'age': 16,
        'birthday': 'March 3',
        'key': 'user-456',
        'name': 'Yu Ishigami'
    }
]

# Fetch items where "age" is greater than 16.
>>> db.fetch({"age?gt": 16}).items
[
    {
        'age': 17,
        'birthday': 'March 3',
        'key': 'user-123',
        'name': 'Chika Fujiwara'
    }
]

# Fetch items where the "author" field contains the string "George".
>>> db.fetch({"author?contains": "George"}).items
[
    {
        'author': 'George R. R. Martin',
        'key': '4bnyytrozupq',
        'title': 'Tuf Voyaging'
    },
    {
        'author': 'George Orwell',
        'key': 'e0bm8kq3yho7',
        'title': '1984'
    }
]
```

Needless to say, queries are a very powerful tool, and you can find out more about them in the [official documentation](https://docs.deta.sh/docs/base/queries).

As a final example, here's how you can fetch every single item in a Base with pagination.

```py
# Fetch the first page of items.
response = db.fetch()
all_items = response.items
# Run until there are no more items.
while response.last:
    # Fetch the next page of items.
    response = db.fetch(last=response.last)
    # Add the items to the list.
    all_items.extend(response.items)
```
