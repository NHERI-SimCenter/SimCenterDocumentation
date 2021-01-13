# SimCenterDocumentation

This is the repository where documentation for SimCenter software is maintained. The current documentation is in restructred text format and is built using the sphinx python module.

Contributors should follow the [style reference](docstyle.md) for guidelines on documentation formatting.

## Directory Structure

+ docs   - the folder containing the most up to date material (all other directories contain legacy material)
+ docs/Makefile - Linux and MacOS makefile for building current document
+ docs/make.bat   - Windows make.bat to do same thing
+ docs/conf.py - configuration file (in this file set app for which doc is requiretd)
+ docs/index.rst - main index file, which pulls in files in docs/common
+ otherFolder - ignore as these contain legacy text files


## Building the HTML files


### 1. Download the repository from Github

For Git users, this can be done by running the following command in a terminal.

```shell
git clone https://github.com/NHERI-SimCenter/SimCenterDocumentation.git
```

### 2. Install dependencies

Install the project dependencies by running the following terminal command from the root of the project:

```shell
pip3 install -U -r requirements.txt
```

> Note: A Python 3 installation must be available in your terminal environment.

### 3. Run the build script

```shell
make <app_name> html
```

where <app> is one of:
    {pelicun, qfem, rdt, pbe, we, ee}

### 4. If it works the html files are in the build/<app_name>/html folder

on Linux type the following to open a browser with index page

```
xdg-open ./build/html/index.html
````

on a Mac

```
open ./_build/html/index.html
```
