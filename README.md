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


## Building the Documentation

Documentation files for a particular SimCenter application can be built by running the following steps.

### 1. Download the repository from Github

For Git users, this can be done by running the following command in a terminal.

```shell
git clone https://github.com/NHERI-SimCenter/SimCenterDocumentation.git
```

Most of the remaining terminal commands should be run from the root of this repository, herein referred to as the *documentation root* (i.e., the top-level of the folder that was created after running the previous command).

### 2. Install dependencies

Install the project dependencies by running the following terminal command from the documentation root:

```shell
pip3 install -U -r requirements.txt
```

> Note: A Python 3 installation must be available in your terminal environment.

### 3a Build with Make

On systems with `make` installed, the following command can be run from the documentation root to build a particular documentation target. Windows users who do not wish to install `make` can alternatively use the Powershell script outlined in step [3b](#3b).

```shell
make <app> <target>...
```

where `<app>` is one of:

| `<app>` |  `<app-name>` |
| --------|---------------|
| pelicun |  Pelicun
| qfem    |  quoFEM
| rdt     |  RDT
| pbe     |  PBE
| we      |  WE-UQ
| ee      |  EE-UQ

and `<target>` is one of:

    web    Run html target with the build directory
           set to the app publishing repository
           (i.e., `../<app-name>-Documentation/`).
    html   Generate HTML output in the dev build directory.
    latex  Generate LaTeX output in the dev build directory.
    pdf    

The "dev" build directory is given by the following path relative to the documentation root: `build/<app-name>/<target>` 

Several targets may be chained at the end of a command for a particular application, as shown in the [examples](#examples)

### 3b Build HTML from Powershell

The legacy Powershell script can be run from the `docs/` directory of this repository as follows:

```
./make html
```

The particular application must be selected by un-commenting the appropriate `app_name` variable at the top of the file `docs/conf.py`.

### 4. Examples

- The following command will generate **HTML** output for the **quoFEM** application in the directory `build/quoFEM/html/`:

    ```shell
    make qfem html
    ```

- The following command will generate **HTML** output for the **WE-UQ** application in the directory `../WE-UQ-Documentation/WE-UQ/html/`:

    ```shell
    make we web
    ```
    > Note: this will write / modify files that are located outside of the documentation repository!

- The following command will generate **latex** and **pdf** output for the **RDT** application in the directories `build/RDT/latex/`, and `build/RDT/pdf/`, respectively:

    ```shell
    make rdt latex pdf
    ```
Note, however, that in order to achieve a proper build, one may need to run the `make <app> latex` target several times in succession before running `make <app> pdf`.
