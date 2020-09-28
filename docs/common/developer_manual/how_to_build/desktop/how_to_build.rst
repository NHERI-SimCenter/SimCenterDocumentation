.. _lblHowToBuild:


============
How to Build
============

This page outlines steps to preparing the workflow applications, or "Backend Applications", on your local desktop.

************************
Install Dependencies
************************

First, ensure the following dependencies are installed:

* **C++11 compliant compiler**: many of the workflow applications included use C++11 features, consequently they may need a newer C++11 compliant compiler. In these instructions, MSVC in `Visual Studio (Community edition) <https://visualstudio.microsoft.com/vs/>`_ is used.

* **OpenSees**: The workflow applications require an installation of `OpenSees <http://opensees.berkeley.edu/>`_ to carry out structural analysis using the finite element method.

* **DAKOTA**: The workflow applications require an installation of `DAKOTA <https://dakota.sandia.gov/>`_ to handle and propagate the uncertainties defined in the input files for the workflow applications.

* **Python**: The workflow requires Python 3.6.

* **Conan**: This repository uses `Conan <https://conan.io/>`_ for dependency management. Conan is a python library and can be installed using the following `instructions <https://docs.conan.io/en/latest/installation.html>`_. Version 1.25 or later is recommended.

* **CMake**: This repository uses `CMake <https://cmake.org/download/>`_ for managing the build process. Version 3.15 or later is recommended.

* **Qt Creator**: The Qt framework is only necessary if you choose to build the user interface for the |short tool id| software. `Qt Creator <https://www.qt.io/download>`_ is free for open source developers. Version 5.10 or later is required, and version 5.12 or later is recommended.


************************
Build the Workflow Application Files
************************

Instructions to build the workflow applications on your local desktop depend on your operating system.

Build on Windows
----------------
For Windows systems, the steps to building the workflow application are as follows:

    #. **Obtain the source code:** Clone the SimCenterBackendApplications repository from `Github <https://github.com/NHERI-SimCenter/SimCenterBackendApplications>`_. You can do that by using your preferred Git client/GUI or by using the ``git clone`` command in the terminal:

        ``git clone https://github.com/NHERI-SimCenter/SimCenterBackendApplications``

    #. **Set up the development environment:** Add Conan `SimCenter <https://bintray.com/nheri-simcenter/simcenter>`_ and  `BinCrafters <https://bintray.com/bincrafters/public-conan>`_ repositories to the Conan remotes. You can add these remotes using the following commands in the terminal:

        ``conan remote add simcenter https://api.bintray.com/conan/nheri-simcenter/simcenter``

        ``conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan``

    #. **Configure your compiler:** Check the default profile of your build environment using ``conan profile show default``. If the compiler name and compiler version are *not* listed, then you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

        ``conan profile update settings.compiler="Visual Studio" default``

        ``conan profile update settings.compiler.version="16" default``

    #. **Create the build output directory:** In the terminal, navigate into the "SimCenterBackendApplications" repository on your desktop. Create a new folder called "build" using the command ``mkdir build``, then navigate into that folder using ``cd build``.

    #. **Install backend dependencies:** You can install backend dependencies using Conan by running the command in the build output directory:

        ``conan install .. --build missing``

    #. **Run CMake configuration:** Run the command ``cmake ..``. If it is necessary to specify a compiler for CMake, you may alternatively run ``cmake .. -G "Visual Studio 16 2019"``.

    #. **Build the release version of the backend:** When using an IDE like Visual Studio on Windows, the generated project can opened in the IDE and used to build the code. This function can also be done from the same terminal window using CMake by the command:

        ``cmake --build . --config release``

    #.  **Install the workflow applications folder:** Run the command ``cmake --install .``. If the installation and build are successful, then you should find a folder called "applications" in the "SimCenterBackendApplications" repository which contains all the workflow application files.


Build on MacOS
--------------
For Mac systems, the steps to building the workflow application are as follows:

    #. **Obtain the source code:** Clone the |short tool id| repository from |tool github link|. You can do that by using your preferred Git client/GUI or by using the ``git clone`` command in the terminal.

    #. **Set up the development environment:** Add Conan `SimCenter <https://bintray.com/nheri-simcenter/simcenter>`_ and  `BinCrafters <https://bintray.com/bincrafters/public-conan>`_ repositories to the Conan remotes. You can add these remotes using the following commands in the terminal:

        ``conan remote add simcenter https://api.bintray.com/conan/nheri-simcenter/simcenter``

        ``conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan``

    #. **Configure your compiler:** Check the default profile of your build environment using ``conan profile show default``. If the compiler name and compiler version are *not* listed, then you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

        ``conan profile update settings.compiler="Visual Studio" default``

        ``conan profile update settings.compiler.version="16" default``

    #. **Create the build output directory:** In the terminal, navigate into the "SimCenterBackendApplications" repository on your desktop. Create a new folder called "build" using the command ``mkdir build``, then navigate into that folder using ``cd build``.

    #. **Install backend dependencies:** You can install backend dependencies using Conan by running the command in the build output directory:

        ``conan install ..``

    #. **Run CMake configuration:** Run the command ``cmake ..``. If it is necessary to specify a compiler for CMake, you may alternatively run ``cmake .. -G "Visual Studio 16 2019"``.

    #. **Build the release version of the backend:** When using an IDE like XCode on Mac, the generated project can opened in the IDE and used to build the code. This function can also be done from the same terminal window using CMake by the command:

        ``cmake --build . --config release``

    #.  **Install the workflow applications folder:** Run the command ``cmake --install .``. If the installation and build are successful, then you should find a folder called "applications" in the "SimCenterBackendApplications" repository which contains all the workflow application files.


Build on Unix
-------------
For Unix systems, the steps to building the workflow application are as follows:

    #. **Obtain the source code:** Clone the |short tool id| repository from |tool github link|. You can do that by using your preferred Git client/GUI or by using the ``git clone`` command in the terminal.

    #. **Set up the development environment:** Add Conan `SimCenter <https://bintray.com/nheri-simcenter/simcenter>`_ and  `BinCrafters <https://bintray.com/bincrafters/public-conan>`_ repositories to the Conan remotes. You can add these remotes using the following commands in the terminal:

        ``conan remote add simcenter https://api.bintray.com/conan/nheri-simcenter/simcenter``

        ``conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan``

    #. **Configure your compiler:** Check the default profile of your build environment using ``conan profile show default``. If the compiler name and compiler version are *not* listed, then you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

        ``conan profile update settings.compiler="Visual Studio" default``

        ``conan profile update settings.compiler.version="16" default``

    #. **Create the build output directory:** In the terminal, navigate into the "SimCenterBackendApplications" repository on your desktop. Create a new folder called "build" using the command ``mkdir build``, then navigate into that folder using ``cd build``.

    #. **Install backend dependencies:** You can install backend dependencies using Conan by running the command in the build output directory:

        ``conan install ..``

    #. **Run CMake configuration:** Run the command ``cmake ..``. If it is necessary to specify a compiler for CMake, you may alternatively run ``cmake .. -G "Visual Studio 16 2019"``.

    #. **Build the release version of the backend:** On Unix-based systems, building the backend can be achieved using the command ``make`` or ``make release``.

    #.  **Install the workflow applications folder:** Run the command ``cmake --install .``. If the installation and build are successful, then you should find a folder called "applications" in the "SimCenterBackendApplications" repository which contains all the workflow application files.



************************
Build the User Interface
************************

Build using the Qt Creator (Recommended)
----------------------------------------
    1. Start Qt Creator, then open the |short tool id|.pro file located in the |short tool id| directory that was downloaded in the previous steps.
    2. Setup the development kit in Qt Creator. This is usually done by selecting the Qt version, compiler and configuration and following the onscreen dialog.
    3. Build the application and run it in Qt Creator IDE by using the **Run** button. This can be done using the keyboard shortcut ``F5`` to build and start the tool.

Build using the terminal
------------------------
    1. First, create a build output directory. This can be done in the terminal using the command ``mkdir build``.
    2. Go into the build output directory and run QMake to Configure the project and create make files. This can be done by using the command:

        .. parsed-literal::

            qmake ../|short tool id|.pro

    3. Build the project by using the command ``make`` on Unix like systems. On Windows, you can either use ``nmake`` or ``jom`` to build in parallel. Once built, you can now run the tool executable.


**********************************
Set the User Interface Preferences
**********************************
    Once built, Open the |short tool id| tool, then click on file -> preferences and set the applications directory entry to point to the applications folder that the build process created for BackendApplications.
