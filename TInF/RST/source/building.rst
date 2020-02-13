.. _sec_TInF-installation:

Building
========

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


The source code files are contained in a directory named \textcolor{blue}{inflowTurbulence}. Note that the code is provided for OpenFOAM version 6 and 7, and is slightly different in this two versions. Please choose the correct package to download according the version of OpenFOAM you have installed on your computer.

Create a project directory named *run* within the *$HOME/OpenFOAM* directory named <USER>-6 (e.g. Jack-6 for user Jack and OpenFOAM version 6) by typing the following script in a terminal prompt:

.. code-block:: none

   $ mkdir -p $FOAM_RUN

Copy or move the *inflowTurbulence* directory which has been downloaded earlier and all the
files in it to the *$HOME/OpenFOAM* directory. Go the relocated *inflowTurbulence* directory by typing:

.. code-block:: none

   $ cd $FOAM_RUN/inflowTurbulence

Compile the codes in the *inflowTurbulence* directory by typing the following in the terminal prompt:

.. code-block:: none

   $ wmake

After the compilation is successfully complete, a library file named
*libturbulentInflow.so* will be generated in the directory $FOAM_USER_LIBBIN.


