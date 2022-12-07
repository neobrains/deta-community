---
title: Home
description: Welcome to Basic Deta. Here you will find the basic documentation, FAQs and code examples.
---

# Basic Deta
Welcome to Basic Deta. Here you will find the basic documentation, FAQs and code examples.

!!! info
    This is **not** official documentation for Deta. This is a community project.
    Official documentation can be found [here](https://docs.deta.sh/).

## What is Deta?

Deta is a platform for building serverless applications. It provides a simple way to build, deploy, and scale your applications.
You don't have to worry about managing servers, databases, or scaling your application. Deta handles all of that for you.

### What is serverless?
Serverless is a cloud computing execution model in which the cloud provider runs the server, and dynamically manages the allocation of machine resources.
Pricing is based on the actual amount of resources consumed by an application, rather than on pre-purchased units of capacity.

But there's no need to worry about pricing, since Deta is free!

### "Serverless" vs "Serverful"
How exactly is "serverless" different from "serverful"?

A traditional server is a virtual machine (or bare metal machine) that runs continuously.
As such, you have to pay continuously for the server, even if it's not being used.
The main advantage of this kind of server is you have full control over it, including the filesystem, configuration, and everything else.
But sometimes an entire machine dedicated to hosting one (or a few) applications is overkill, and you only need a small amount of resources.

This is where serverless comes in. With serverless, a "temporary" or "ephemeral" server is created every time your application needs to run, and there's no server running when it's not needed.
This comes with the advantage that the server instances are managed for you by the cloud provider, and there is minimal setup, so there's less for the developer to worry about.
For most cloud providers, you would pay per-request, rather than per hour that a traditional server is running. This means that if your application is only used once a day, you only pay for that one request, rather than paying for a server to run 24/7.

Deta, however, is special. Everything is **completely free**, including the serverless instances, database, and storage.

One important thing to remember is that serverless apps are unable to keep a state between executions.
After an instance stops running, any changes made are lost, and the next instance will start with a clean slate.
You can work around this by using Deta Base to store persistent data.
Finally, since even Deta isn't infinitely rich, the serverless instances provided have a 10 second execution time limit.

## Services
Deta currently provides 3 services:

- Micros: serverless compute instances
- Base: cloud-based NoSQL database
- Drive: cloud-based file storage

## Read the Docs
It is recommended to read the official documentation for Deta [here](https://docs.deta.sh/) before asking for any help.
It contains much more in-depth information and references.

## Tutorials
Check out the [Tutorials](/tutorials) page for a guide on how to get started with Deta.

## Help
Make sure to read the [Help](/help) section for some guidelines on how to ask for help.

## Frequently Asked Questions
Read the [FAQs](/faq) page for solutions to common problems.

## Code Examples (Removed For Now)
Check out the [Examples](/examples) section for code examples and common snippets.

## Contributors
- @AyushSehrawat
- @LemonPi314
- @jnsougata
- @mikBighne98
