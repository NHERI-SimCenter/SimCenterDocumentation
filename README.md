# SimCenterDocumentation

This is the repository where documentation for SimCenter software is maintained. The current documentation is in reStructuredText format and is built using the Sphinx Python module.

Contributors should follow the [style reference](Help/docstyle.md) for guidelines on documentation formatting.

Build instructions are outlined below, with further details provided [here](Help/make.md).

## Directory Structure

+ `docs/`   - the folder containing the most up to date material (all other directories contain legacy material)
+ `docs/Makefile` - Legacy Linux and MacOS makefile for building current document
+ `docs/make.bat`   - Legacy Windows make.bat to do same thing
+ `docs/conf.py` - configuration file (in this file set app for which doc is requiretd)
+ `docs/index.rst` - main index file, which pulls in files in `docs/common`
+ otherFolder - ignore as these contain legacy text files


## Building the Documentation

Documentation files for a particular SimCenter application can be built by completing the following steps.

### 1. Download this repository from Github

For Git users, this can be done by running the following command in a terminal.

```shell
git clone https://github.com/NHERI-SimCenter/SimCenterDocumentation.git
```

Most of the remaining terminal commands should be run from the root of this repository, herein referred to as the *documentation root* (i.e., the top-level of the folder that was created after running the previous command).

### 2. Install dependencies

Install the project dependencies by running the following terminal command from the documentation root:

```shell
pip install -r requirements.txt
```

or

```shell
pip3 install -r requirements.txt
```

> Note: A Python 3 installation must be available in your terminal environment. The pip command is used on Windows and pip3 on a Mac. If you do not have admin rights, add a -U before the -r.

### 3a Build with Make

On systems with `make` installed, the following command can be run from the documentation root to build a particular documentation target. `make` is typically available by default for MacOS and Linux users and can readily be installed on Windows. However, Windows users who do not wish to install `make` may alternatively use the Powershell script outlined in step [3b](#Build-HTML-from-Powershell).

```shell
make <app> <target>...
```

where `<app>` is one of:

| `<app>` |  `<app-name>` |
| --------|---------------|
| `pelicun` |  Pelicun
| `qfem`    |  quoFEM
| `r2d`     |  R2D
| `pbe`     |  PBE
| `we`      |  WE-UQ
| `ee`      |  EE-UQ
| `hydro`   |  HydroUQ
| `rtm`     |  Requirements matrix

and `<target>` is one of:

| `<target>` | description |
|------------|-------------|
|  `web`    | Generate HTML output in the app publishing repository (i.e., `../<app-name>-Documentation/`).
|  `html`   | Generate HTML output in `build/<app-name>/html/`.
|  `latex`  | Generate LaTeX output in `build/<app-name>/pdf/`.
|  `pdf`    | Generate PDF output in `build/<app-name>/pdf/`.


Several targets may be chained at the end of a command for a particular application, as shown in the [examples](#examples) below.

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

- The following command will generate **latex** and **pdf** output for the **R2D** application in the directories `build/R2D/latex/`, and `build/R2D/pdf/`, respectively:

    ```shell
    make r2d latex pdf
    ```
    Note, however, that in order to achieve a proper build, one may need to run the `make <app> latex` target several times in succession before running `make <app> pdf`.

- It is often useful to clean and update the documentation when building, as some changes in other repositories can affect this one. The following command will clean the documentation and update the source files before building the **HydroUQ** application's example cases. Some example files may be in the individual app repositories, e.g. ../HydroUQ/Examples/, so it is recommended to download them locally. Within the SimCenterDocumentation root folder, run 

    ```shell
    cd ..
    git clone https://github.com/NHERI-SimCenter/HydroUQ.git
    cd ./SimCenterDocumentation/docs
    make clean
    cd ..
    make update
    make hydro examples
    make hydro html
    ```

> Note: Legacy build scripts in the `docs` directory do not sync example files from their source repositories.

