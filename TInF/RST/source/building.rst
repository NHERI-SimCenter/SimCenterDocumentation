.. _sec_TInF-building:

Building TInF
=============

Install External Software
-------------------------

Please note that in order to build and run the Turbulent Inflow Tool, your system must have installations of the following components:

    #. Install a modern C++ compiler that is compliant with modern C++ standards (preferably C++17).
    
    #. Install the `Qt framework <https://www.qt.io/download/>`_. Qt is free for open source developers. Qt version 5.10 or later is required and version 5.12 or later is recommended.

    #. Install OpenFOAM (v10) from the |openfoam.org|

.. note::

   The first open source release of ``OpenFOAM`` was in 2004. It was based on the ``FOAM`` code, which was originally developed by Henry Weller in 1989. As sometimes happens with open source software when commercial interests get involved, the code forked over time and a number of open source distributions from different entities are available. The two main distributions of the code come from the |openfoam.org| and from |openfoam.com|. Currently |app| compiles and runs primarily with **10** of the code released by the |openfoam.org|.

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


The source code files are contained in a directory named *turbulentInflow*. Note that the code is provided for OpenFOAM version 6, 7, 10, 11 and is slightly different in each versions. Version 10 has been tested rigorously compared to the others. Please choose the correct package to download according the version of OpenFOAM you have installed on your computer. For all the inflow boundary condition used in WE-UQ, OpenFOAM-10 is used. 

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


