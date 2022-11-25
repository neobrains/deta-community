# CLI FAQs

### Issues with `deta login`
!!! help ""
    Most likely the issue is caused by your browser or an extension blocking scripts.
    Disable any extensions on the login page, or if you are using Brave, disable Brave Shields. Otherwise, try a different browser.
    If that doesn't work either, follow the instructions [here](https://docs.deta.sh/docs/cli/auth#deta-access-tokens) to log in with an access token.

### Stuck on deta new
!!! help ""
    If you are stuck on `deta new <more arguments>` for a long time, it is most likely that your requirements.txt file contains
    packages with more than 250mb size or your project size exceeds 240mb. You can use `.detaignore` to exclude files you don't
    need on the Micro (by default it excludes `.*` and `node_modules`).

### Connection refused on `deta new`
!!! help ""
    If you are getting a connection refused error on `deta new`, like this:
    ```shell
    Error: Get "https://v1.deta.sh/spaces/": dial tcp: lookup v1.deta.sh on [::1]:53: read udp [::1]:43928->[::1]:53: read: connection refused
    ```
    You can try to set your `DETA_ACCESS_TOKEN` environment variable with your access token. You can generate an access token from the [dashboard](https://web.deta.sh/).

    Read more about access tokens [here](https://docs.deta.sh/docs/cli/auth/#deta-access-tokens)