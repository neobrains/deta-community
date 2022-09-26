---
title: Common FAQs
description: Frequently asked questions about Deta and it's services.
comments: true
---
# Common FAQs asked by people
This page consists of common questions asked by people.

Some FAQs regarding micros can be found [here](https://docs.deta.sh/docs/micros/faqs_micros)

## **Micro FAQs**

### Q.) How micros work?
!!! help ""
    Whenever a request is made to a micro, it is handled by a new instance of the micro.
    This instance is created on the fly and is destroyed after 10 seconds, or when the request is completed (within 10 seconds).
    If your request takes more than 10 seconds to complete, it will be terminated.
    
    Want to increase the timeout? Check out the [docs](https://docs.deta.sh/docs/micros/faqs_micros/#how-can-i-request-for-a-timeout-or-memory-increase)

### Q.) Websocket support?
!!! help ""
    No, Deta does not support websockets since it is a serverless platform.

### Q.) Can I run discord bots?
!!! help ""
    If you are running **Interaction** only discord bots , then yes, But if you are running **Websocket** based bots, then no.

### Q.) Unable to serve images/fonts?
!!! help ""
    Refer to [this](https://docs.deta.sh/docs/common_issues#nodejs-micros-cannot-serve-binary-files).

### Q.) Getting 413 (Entity Too Large) error on your webserver?
!!! help ""
    It can be due to the size of the request body. Deta Micros has a limitation of HTTP Payload limit of 5.5MB.

### Q.) Getting Micro Times Out / 502 (Bad Gateway) error?
!!! help ""
    It can appear due to a number of reasons. Some of the reasons are mentioned
    [here](https://docs.deta.sh/docs/micros/faqs_micros/#why-is-my-micro-returning-a-502-bad-gateway)

    Other reasons can be : 

    - The micro is serving a file larger than 5.5MB.


## **Base FAQs**

### Q.) How to delete a base?
!!! help ""
    You can delete a base by going to the [dashboard](https://web.deta.sh) and selecting the base you want to delete.
    Then click on the delete button by clicking on settings.

### Q.) Is there any limit to size / number of documents in a base?
!!! help ""
    No, there is no limit to deta base. You can store as many documents (or records) as you want. But the size of a 
    single document should be less than 400kb.

### Q.) What is the maximum number of digit i can store in a number field?
!!! help ""
    Base currently supports maximum 16 digit numbers (integers and floating points), 
    please store larger numbers as a string.

### Q.) How to fetch latest record/entry from a Base?
!!! help ""
    Refer to [https://github.com/orgs/deta/discussions/344](https://github.com/orgs/deta/discussions/344).

## **Drive FAQs**

### Q.) Can I increase the drive limit?
!!! help ""
    No, the drive limit is fixed at 10GB. It may soon be increased in later updates.

### Q.) Can I share drive contents?
!!! help ""
    Currently you can't share drive files via links. You have to download the file and then share it or 
    create a custom API to share the file.

## **CLI FAQs**

### Q.) Getting issue related to `deta login` command?
!!! help ""
    It can be due to your browser blocking the login page (lik brave browser ). Try using a different browser or 
    try the other login methods [here](https://docs.deta.sh/docs/cli/auth#deta-access-tokens).