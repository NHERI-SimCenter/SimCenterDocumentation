# SimCenterDocumentation

This is the repository where documentation for SimCenter software is maintained. The current documentation is in restructred text format and is built using the sphinx python module.

## Structure

+ docs   - the folder containing the most up to date material (all other directories contain legacy material)
+ docs/Makefile - linux and MAc makefile for building current document
+ docs/make.bat   - windows make.bat to do same thing
+ docs/conf.py - configuration file (in this file set app for which doc is requiretd)
+ docs/index.rst - main index file, which pulls in files in docs/common
+ otherFolder - ignore as these contain legacy text files
   

## Building the HTML files

### 1. Building requires sphinx and some packages for sphinx

```
pip install -U sphinx
pip install sphinx_rtd_theme
pip install sphinxcontrib.bibtex
```

### 2. Download the repo using git from a terminal window

```
git clone https://github.com/NHERI-SimCenter/SimCenterDocumentation.git
```

### 3. Once sphinx is installed and the repo downloaded, type make html to build it

```
cd SimCenterDocumentation
cd docs
make html
```

### 4. If it works the html files are in the web/html folder

on Linux type the following to open a browser with index page

```
xdg-open ./build/html/index.html
````

on a Mac

```
open ./_build/html/index.html
```
