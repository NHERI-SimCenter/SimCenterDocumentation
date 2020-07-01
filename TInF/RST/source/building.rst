.. _sec_TInF-installation:

Building
========

Installing Qt and OpenFOAM
--------------------------

Please note that in order to install and run the Turbulent Inflow Tool, your system must have installations of the following components:

* Qt

* OpenFOAM (v6 or v7 released by the OpenFOAM Foundation)

The installations of these two components can be found through the links https://www.qt.io/download and https://openfoam.org/download/, respectively.

Building the UI from Source
---------------------------

You must first obtain the source-code from |githubLink| and then compile and build it using Qt's qmake. This can be done in a command window on Windows or a terminal window on a Mac machine using the following commands:

.. code-block:: none

    git clone https://github.com/NHERI-SimCenter/TurbulenceInflowTool
    git clone https://github.com/NHERI-SimCenter/SimCenterCommon
    cd TurbulenceInflowTool
    qmake TurbulenceInflowTool.pro
    make


Compiling the Source Code in OpenFOAM
-------------------------------------

Download the source code of the turbulent velocity boundary conditions from

.. code-block:: none

    https://github.com/NHERI-SimCenter/TurbulenceInflowTool/tree/master/openFOAM_code


The source code files are contained in a directory named *turbulentInflow*. Note that the code is provided for OpenFOAM version 6 and 7, and is slightly different in this two versions. Please choose the correct package to download according the version of OpenFOAM you have installed on your computer.

Create a project directory by typing the following script in a terminal prompt:

.. code-block:: none

   $ mkdir -p $FOAM_RUN

Copy or move the *turbulentInflow* directory which has been downloaded earlier and all the files in it to the above created directory. Go to the relocated *turbulentInflow* directory by typing:

.. code-block:: none

   $ cd $FOAM_RUN/turbulentInflow

Compile the codes in the *turbulentInflow* directory by typing the following in the terminal prompt:

.. code-block:: none

   $ wmake

After the compilation is successfully complete, a library file named *libturbulentInflow.so* will be generated in the directory $FOAM_USER_LIBBIN.


