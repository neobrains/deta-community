---
title: Getting Started with Deta
description: Get started with Deta with this guide.
---

Install the Deta CLI by following the instructions [here](https://docs.deta.sh/docs/cli/install).
Log in using the `deta login` command.
```bash
$ deta login
```

Can't login to the CLI through the browser? Check out the [FAQs](/faq/cli#issues-with-deta-login).

## Creating a Micro
A Micro is basically a "serverless server" that runs your code. More about Micros [here](/TODO).

Create a new directory where your Micro's code will be located.
```bash
$ mkdir my-micro
$ cd my-micro
```

Run the `deta new` command to create a new Micro.
```bash
$ deta new --python
```

!!! note
    `--python` specifies that the Micro will be running Python code. If you want to make a Node.js Micro, use `--node` instead.
    For the rest of this guide, we will be using Python.

This will create a new Micro named `my-micro` under your default project. It will also create a `main.py` file with a basic "Hello World" example.
In the output of the command, you will see a URL that looks like this: `https://<micro-id>.deta.dev`. You can use this URL to access your Micro.

The `.deta` folder contains some metadata about the Micro, it can be safely ignored and excluded from version control.

The `deta new` command also lets you specify the Micro name, project name, and runtime.
```bash
deta new --name <micro-name> --project <project-name> --runtime <runtime>
```

- `<micro-name>` is the name of the Micro you want to create.
- `<project-name>` is the name of the project you want to create the Micro under.
- `<runtime>` is the language and version of the runtime you want to use. For example, `--runtime python3.9` or `--runtime node14`.

Full command reference can be found [here](https://docs.deta.sh/docs/cli/commands#deta-new).

## Deploying your Micro
Deploying your Micro is as easy as:
```bash
$ deta deploy
```

After the command completes, visit your Micro's URL and see your changes live!

!!! tip
    You can also use `deta watch` to watch for changes in the directory and deploy the Micro automatically.

## Creating a Project
By default your account has one project named `default`. You can create as many new projects as you like to organize and group your Micros, Bases, and Drives.
To create a new project, go to the [Deta Dashboard](https://web.deta.sh/) and create a new project by clicking on the `+ New Project` button in dropdown menu.

![image](images/create-project-1.png)

!!! warning
    Please note there is currently no way to delete a project.
