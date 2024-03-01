.. _sec_TInF-installation:

Installation
==============

Installing the Turbulence Inflow Tool
--------------------------------------

Download the installation package for your operation system from (a single line)

    https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/TurbulantInflowTool

SimCenter is providing packages for Windows~8/10 (64 bit version only) and MacOS.  
The installer will place the executable on your system.
On Windows systems, a shortcut will be added to your start menu.
On MacOS, the application is placed in your Applications folder.


For Linux systems, you will need to clone the source from 

    https://github.com/NHERI-SimCenter/TurbulenceInflowTool

and compile it yourself performing the following steps:

    $ git clone https://github.com/NHERI-SimCenter/TurbulenceInflowTool
    $ git clone https://github.com/NHERI-SimCenter/SimCenterCommon
    $ cd TurbulenceInflowTool
    $ qmake TurbulenceInflowTool.pro
    $ make
    $ sudo make install


Compiling the Source Code in OpenFOAM
--------------------------------------

Download the source code of the turbulent velocity boundary conditions from

    https://github.com/NHERI-SimCenter/TurbulenceInflowTool/tree/master/openFOAM_code


The source code files are contained in a directory named \textcolor{blue}{inflowTurbulence}. Note that the code is provided for OpenFOAM version 6 and 7, and is slightly different in this two versions. Please choose the correct package to download according the version of OpenFOAM you have installed on your computer.

Create a project directory named *run* within the *$HOME/OpenFOAM* directory named <USER>-6 (e.g. Jack-6 for user Jack and OpenFOAM version 6) by typing the following script in a terminal prompt:

    $ mkdir -p $FOAM_RUN

Copy or move the *inflowTurbulence* directory which has been downloaded earlier and all the
files in it to the *$HOME/OpenFOAM* directory. Go the relocated *inflowTurbulence* directory by typing:

	$ cd $FOAM_RUN/inflowTurbulence

Compile the codes in the *inflowTurbulence* directory by typing the following in the terminal prompt:

	$ wmake

After the compilation is successfully complete, a library file named
*libturbulentInflow.so* will be generated in the directory $FOAM_USER_LIBBIN.


