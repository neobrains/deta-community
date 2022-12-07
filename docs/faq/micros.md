# Micro FAQs

### How do Micros work?
!!! help ""
    Whenever a request is made to a Micro, it is handled by a new instance of the Micro.
    This instance is created on the fly and is destroyed after 10 seconds, or when the request is completed (within 10 seconds).
    If your request takes more than 10 seconds to complete, it will be terminated. More about serverless [here](/#what-is-serverless).

    Want to increase the timeout? Check out the [docs](https://docs.deta.sh/docs/micros/faqs_micros/#how-can-i-request-for-a-timeout-or-memory-increase).

### Do Micros support websockets?
!!! help ""
    No, Micros do not support websockets because they are serverless compute instances that have a maximum lifespan of 10 seconds per request.

### Can I run Discord bots?
!!! help ""
    If your bot uses **interactions only**, yes. If your bot uses **websockets**, then no.

    Examples of interactions are:

    - Slash commands
    - Modals
    - Buttons
    - Dropdowns

### I'm getting an "Unsupported framework" error
!!! help ""
    Make sure to include the following line of code at the end of your `index.js` file.
    ```js
    module.exports = app;
    ```

### I'm unable to serve images or fonts
!!! help ""
    Add `BINARY_CONTENT_TYPES=image/*,font/*` to a `.env` file in your project root, and run `deta update -e .env`.
    More info [here](https://docs.deta.sh/docs/common_issues#nodejs-micros-cannot-serve-binary-files).

### I'm getting HTTP error 413 (Entity Too Large)
!!! help ""
    It can be due to the size of the request body. The maxiumum payload size is 5.5 MB.

### I'm getting HTTP error 502 (Bad Gateway)
!!! help ""
    Most likely there is a syntax error or other problem in your code that is preventing the Micro from starting.
    Some more reasons are mentioned [here](https://docs.deta.sh/docs/micros/faqs_micros/#why-is-my-micro-returning-a-502-bad-gateway).
    Other reasons can be:

    - The Micro is serving a file larger than 5.5MB.

### My Micro timed out
!!! help ""
    This means that your Micro took more than 10 seconds to respond to the request. Check for any code that might take a long time to execute.
    If you really need more than 10 seconds, you can increase the timeout by following the instructions [here](https://docs.deta.sh/docs/micros/faqs_micros/#how-can-i-request-for-a-timeout-or-memory-increase).

### How do I link my code to an existing Micro?
!!! help ""
    If you don't have a `.deta` folder for a Micro anymore, but would like to use that Micro again,
    follow the steps below to regenerate the `.deta` folder.
    ```shell
    # Make a temporary directory.
    mkdir temp
    cd temp
    # Clone your Micro.
    deta clone --project <project-name> --name <micro-name>
    # Move the new .deta folder to your project root.
    mv .deta ..
    # Delete the temporary directory.
    cd ..
    rm -rf temp
    ```

### orjson related issue
!!! help ""
    In case you face this issue you have to remove orjson from your code/requirements.txt and then run `deta deploy` again.


### How to redeploy/delete a Micro?
!!! help ""
    You can redeploy a micro by running `deta deploy` again.

    You can delete a micro by deleting the `.deta` folder and deleting from the dashboard. To create a new Micro now, run `deta new <arguments here> again`.

### Support for Python3.11
!!! help ""
    Current Deta micros are running on AWS Lambda under the hood and they have python runtime support upto 3.9. So that's something Deta micros will support once AWS Lambda start supporting those runtimes.

----

More FAQs regarding Micros can be found [here](https://docs.deta.sh/docs/micros/faqs_micros).
