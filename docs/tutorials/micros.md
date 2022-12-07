# Getting Started with Micros
What is a "Micro"?
A Micro is basically a "serverless server" that runs your code. More about serverless [here](/#what-is-serverless).

## Creating a Micro
Create a new directory where your Micro's code will be located.
```console
$ mkdir my-micro
$ cd my-micro
```

Run the `deta new` command to create a new Micro.
```console
$ deta new --python
```

!!! info
    `--python` specifies that the Micro will be running Python code. If you want to make a Node.js Micro, use `--node` instead.
    For the rest of this guide, we will be using Python.

This will create a new Micro named `my-micro` under your default project. It will also create a `main.py` file with a basic "Hello World" example.
In the output of the command, you will see a URL that looks like this: `https://<micro-id>.deta.dev`. You can use this URL to access your Micro.

The `.deta` folder contains some metadata about the Micro, it can be safely ignored and excluded from version control.

The `deta new` command also lets you specify the Micro name, project name, and runtime.
```console
$ deta new --name <micro-name> --project <project-name> --runtime <runtime>
```

- `<micro-name>` is the name of the Micro you want to create.
- `<project-name>` is the name of the project you want to create the Micro under.
- `<runtime>` is the language and version of the runtime you want to use. For example, `python3.9` or `node14`.

Full command reference can be found [here](https://docs.deta.sh/docs/cli/commands#deta-new).

## Deploying your Micro
Deploying your Micro is as easy as:
```console
$ deta deploy
```

That's it! After the command completes, visit your Micro's URL and see your changes live!
If you make any changes to the Micro, you can redeploy it by running the `deta deploy` command again.

!!! tip
    You can also use `deta watch` to watch for changes in the directory and deploy the Micro automatically.

!!! tip
    You can also update the environment variables! Checkout the official docs.
