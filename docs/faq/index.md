# Frequently Asked Questions

In the following sections you can find answers to frequently asked questions,
as well as solutions to common problems.

- [Micros](/faq/micros) - Frequently asked questions about Deta Micros.
- [Base](/faq/base) - Frequently asked questions about Deta Base.
- [Drive](/faq/drive) - Frequently asked questions about Deta Drive.
- [CLI](/faq/cli) - Frequently asked questions about the Deta CLI.

## Quick Summary of Micros
- Timeout after 10 seconds
- Memory per execution is 512MB
- No state is maintained between executions
- You can't write to the file system except for the `/tmp` directory , which also gets cleared after some time
- You can send/receive a maximum of 5.5 MB of data in a request
- There's a limit on number of requests per second but if you don't exceed the limit you won't get any issues.


## Some common faqs regarding Deta

### What is this service for ?
!!! help ""
    This service is mostly used to deploy web apps and APIs. You can try to host a lot of stuff with some tweaks. A newever version of this service is in alpha (https://alpha.deta.space/) and it is more flexible and can be used to host any kind of application.

    For people who came from services similar to Heroku ( which support app running 24/7 and sleeping after x time ) this service is not for you if you
    are looking for something like that. This service is serverless and your app won't be active 24/7, though your app runs 24/7. Confused ? Deta uses
    micros to run your app, see how they work [here](/faq/micros)

### Why are they free ? How do they make money ? How are they planning to sustain ?
!!! help ""
    Deta is free and will be free forever. They are currently attracting developers to use their service and soon they will implement a system where
    developers can make their apps paid and they will get a cut from that.

    Deta has been sustaining since 3 years now and will in the future too. You can see their investors [here](https://angel.co/company/deta/funding)
