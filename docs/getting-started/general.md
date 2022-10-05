# General Information

## Installing the SDK
In order to use Bases and Drives in your code, you'll need to install the Deta SDK for your chosen language.

=== "Python"
    ```console
    $ python -m pip install deta
    ```

=== "JavaScript"
    ```console
    $ npm install deta
    ```

=== "Go"
    ```console
    $ go get github.com/deta/deta-go
    ```

!!! note
    If you are using Windows, you may need to use `py` instead of `python`.

## Projects
Projects are groups of services that you can use to organize your applications, so that all the data and Micros for a particular application are in one place, using one project key.
By default your account has one project named `default`.
You can create as many new projects as you like to organize and group your Micros, Bases, and Drives.
To create a new project, go to the [Deta Dashboard](https://web.deta.sh/) and create a new project by clicking on the `+ New Project` button in dropdown menu.

![image](/images/create-project-1.png)

!!! warning
    Please note there is currently no way to delete a project.

## Project Keys
Each project has a project key (or multiple keys) that your code can use to create and access Bases and Drives within that project.
You can find your project keys in the [Deta Dashboard](https://web.deta.sh).

!!! warning
    Your project key is a secret, so please keep it safe.

It is good practice to store your project key in an environment variable called `DETA_PROJECT_KEY`, rather than hardcoding it into your code.
This particular environment variable name is automatically picked up by the Deta SDKs, so you don't need to do anything special in your code to use it.
To set this environment variable, you can use a terminal command like the ones below.
Replace `<your-project-key>` with your actual project key.

=== "Linux/macOS"
    ```console
    $ export DETA_PROJECT_KEY=<your-project-key>
    ```

=== "Windows PowerShell"
    ```powershell
    > $env:DETA_PROJECT_KEY=<your-project-key>
    ```

=== "Windows Command Prompt"
    ```shell
    > set DETA_PROJECT_KEY=<your-project-key>
    ```

You can also persist the environment variable by creating a `.env` file in the root of your project and adding your project key to it.
This file should be ignored by your version control system, so your secrets don't get committed to a repository.
```txt title=".env"
DETA_PROJECT_KEY=<your-project-key>
```

For more information on using `.env` files, see the [python-dotenv](https://pypi.org/project/python-dotenv/) documentation.
TODO