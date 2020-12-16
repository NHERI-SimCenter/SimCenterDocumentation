<h1>Documentation Design Philosophy</h1>

This document proposes a general approach for the design and layout of SimCenter documentation websites.

Every website is assumed to be associated with one clearly identifiable **primary application**. Websites are divided into structured **documents** which identify a target **audience**.

- [User Manual](#user-manual)
  - [Audience: `Base User`](#audience-base-user)
  - [Document Components](#document-components)
    - [Installation](#installation)
    - [User Guide](#user-guide)
    - [Troubleshooting](#troubleshooting)
    - [Examples](#examples)
    - [Bugs \& Feature Requests](#bugs--feature-requests)
- [Technical Manual](#technical-manual)
  - [Audience: `Engaging User`](#audience-engaging-user)
- [Developer Manual:](#developer-manual)
  - [Audience: `Developing User`](#audience-developing-user)
  - [Components](#components)
    - [How to Build](#how-to-build)
    - [Software Architecture](#software-architecture)
      - [File Types and Schemas](#file-types-and-schemas)
      - [Workflow (Backend) Applications](#workflow-backend-applications)
      - [Creating Workflows](#creating-workflows)
      - [Running Manually # (Manually Building Workflows)](#running-manually--manually-building-workflows)
      - [C4 Model of Framework](#c4-model-of-framework)
    - [Coding Style](#coding-style)
- [Front Matter (About)](#front-matter-about)
  - [Audience: `General`](#audience-general)
  - [Components](#components-1)
    - [Acknowledgments](#acknowledgments)
    - [Copyright](#copyright)
    - [Abbreviations](#abbreviations)
    - [Glossary](#glossary)


## User Manual

### Audience: `Base User`

This document is targeted at *base users* of the **primary application**. Documentation catering to this user must make the following accommodations:

- [ ] Coding experience?
    - [ ] control flow (`if`/`then`, `for`) ?
    - [ ] tcl?
    - [ ] C/C++ tools chains?
- [ ] Command line?
    - [ ] option parsing?
    - [ ] streams/pipes?
    - [ ] ssh?

### Document Components

####  Installation

####  User Guide

####  Troubleshooting

####  Examples

####  Bugs \& Feature Requests

## Technical Manual

### Audience: `Engaging User`

This document is targeted at *engaging users* of the **primary application**.

## Developer Manual:

Throughout this manual, care should be taken to identify how the concepts presented are abstracted away by the primary application.

### Audience: `Developing User`

A **developing user** is one that may be expected to engage in software development. The following assumptions are made:


### Components

####  How to Build

####  Software Architecture

##### File Types and Schemas

This section should NOT include any files which a **base user** may be required to prepare.

##### Workflow (Backend) Applications

This section should begin by clearly defining what is meant by a "backend application"

##### Creating Workflows

This section should begin by clearly defining what is meant by a "workflow". 

##### Running Manually # (Manually Building Workflows)

##### C4 Model of Framework

#### Coding Style

## Front Matter (About)

This section contains meta and reference material that is relevant to the project or primary application as a whole, but disruptive to a particular document structure.

### Audience: `General`

For the most part the material of this section should be generally understandable by anybody. Absolutely no technical background should be assumed.

### Components

#### Acknowledgments

#### Copyright

#### Abbreviations

#### Glossary
