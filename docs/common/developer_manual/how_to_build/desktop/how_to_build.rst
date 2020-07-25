.. _lblHowToBuild:


============
How to Build
============

To build the tool, follow the following instructions:


*********************************
Setup the Development Environment
*********************************

    #. Install a modern C++ compiler that is compliant with modern C++ standards (preferably C++17).
    
    #. Install the `Qt framework <https://www.qt.io/download/>`_. Qt is free for open source developers. Qt version 5.10 or later is required and version 5.12 or later is recommended.

    #. Install `CMake <https://cmake.org/download/>`_ build tools. CMake version 3.15 or later is preferred.

    #. Install `Conan <https://docs.conan.io/en/latest/installation.html>`_ package manager, version 1.25 or later is preferred.
    
    #. Add Conan `SimCenter <https://bintray.com/nheri-simcenter/simcenter>`_ and  `BinCrafters <https://bintray.com/bincrafters/public-conan>`_ repositories to the Conan remotes. You can add these remotes using the following commands in the terminal:
        
        ``conan remote add simcenter https://api.bintray.com/conan/nheri-simcenter/simcenter``

        ``conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan``


**********************
Obtain the Source Code
**********************

    #. Clone the |short tool id| repository from |tool github link|. You can do that by using your preferred Git client/GUI or by using the ``git clone`` command in the terminal.

    #. Clone the following repositories for the dependencies:

        * `SimCenterCommon repository <https://github.com/NHERI-SimCenter/SimCenterCommon>`_.

        .. only:: earthquake

            * `GroundMotionUtilities repository <https://github.com/NHERI-SimCenter/GroundMotionUtilities>`_
            * `s3hark repository <https://github.com/NHERI-SimCenter/s3hark>`_

        .. only:: PBE_app

            * `EE-UQ repository <https://github.com/NHERI-SimCenter/EE-UQ>`_

    You will need to clone each dependency from its GitHub repository and place it in the same parent directory where the |short tool id| repository was cloned (note: not inside the |short tool id| directory itself, but directory above it, i.e. SimCenterCommon and |short tool id| directories both exist in the same parent directory).

.. only:: quoFEM_app

   .. include:: quoFEMBackend.rst

.. only:: earthquake

   .. include:: SimCenterBackend.rst

.. only:: WEUQ_app

   .. include:: SimCenterBackend.rst

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
