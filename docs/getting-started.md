---
title: How-To Guide For Deta
description: Get started with Deta by following this guide.
---
# How-To
This page consists of a guide on how to get started with Deta.

## Getting Started
Install the Deta CLI by following the instructions [here](https://docs.deta.sh/docs/cli/install).

Can't login to the CLI via the browser? Try the other login methods [here](https://docs.deta.sh/docs/cli/auth#deta-access-tokens).

Also, if you are using browser based login, for browsers like Brave, you need to `allow all trackers and ads` in brave shield
for it to work

## Creating a Project
Go to the [Deta Dashboard](https://web.deta.sh/) and create a new project by clicking on the `New Project` button in dropdown menu.

![image](images/create-project-1.png)

Default project is 'default'.

## Creating a Micro
Go to the directory where the code you want to deploy is located.

!!! note "This is an example of FastAPI"
    Add `requirements.txt` file to the directory if you are using a framework like FastAPI or Flask.

    ```txt
    fastapi
    uvicorn[standard]
    ```

The root of the directory should contain a `main.py` file.

If you are logged in to the CLI, you can run the following command to deploy the micro.

```bash
deta new --name <micro-name> --python --project <project-name>
```

* `micro-name` is the name of the micro you want to create.
* `project-name` is the name of the project you want to deploy the micro to.
* `--python` is the language of the micro.

!!! help "Sample Command"
    ```bash
    deta new --name hello --python --project default
    ```

After running the command, a new micro will be created and a `.deta` folder will be created in the directory.

## Deploying a Micro
To deploy the micro, run the following command.

```bash
deta deploy
```

It will return a URL which you can use to access the micro.

You can also add subdomains and custom domains to the micro via the dashboard.

!!! tip "There are more deploy commands"
    You can also use `deta watch` to watch for changes in the directory and deploy the micro automatically.

!!! note "Using a .env file?"
    If you are using a `.env` file, you can use `deta update -e .env` after deploying the micro to update
    the environment variables (`.env` in same directory as of in which command ran).

## More About Deta CLI
You can find more about the Deta CLI [here](https://docs.deta.sh/docs/cli/commands/).
