.. _lblHowToBuild:

============
How to Build
============

SimCenter tools all comprise a frontend UI and some backend applications. They are kept in separate GitHub repositories and are also built separately. The following3 sections outline (1) the applications needed to build and run, (2) instructions for building the backend applications, (3) instructions for building the frontend UI, and (4) operations to perform in the running UI to link the UI and the backend.


.. note::

   As part of our continuous integration process, |app| is built evrey time we check code into the NHERI-SimCenter repositories. To do this we make use of a CI service. That current service is `appveyor <https://www.appveyor.com/>`_. As a consequence in the |app| repo that you will clone as part of this build process there is a file **appveyor.yml**. This file contains shell commands that are issued to set-up the operating system, download the software and build it. If the following commands fail for you, look at the appveyor.yml file to see what commands are currently beeing called as these may be more up to date than what is presented below.

********************
Install Dependencies
********************

First, ensure the following dependencies are installed:

* **C++17 compliant compiler**: many of the workflow applications included use C++17 features; consequently, they may need a newer C++17 compliant compiler. For Windows users, MSVC in `Visual Studio 2019 (Community Edition) <https://visualstudio.microsoft.com/vs/older-downloads/Install Dependencies>`_ can be used. Some extensions of Visual Studio are also needed: Open Visual Studio Installer, go to Installed / More / Modify, under the Workloads tab, check Desktop development with C++ and Visual Studio extension development; under the Individual components tab, check C++ CMake tools for windows. Then click Modify.

* **OpenSees**: The workflow applications require an installation of `OpenSees <http://opensees.berkeley.edu/>`_ to carry out a structural analysis using the finite element method.

* **DAKOTA**: The workflow applications require an installation of `DAKOTA <https://dakota.sandia.gov/>`_ to handle and propagate the uncertainties defined in the input files for the workflow applications.

* **Python**: The workflow requires at least Python 3.7.

* **Conan**: This repository uses `Conan <https://conan.io/>`_, a python library, for dependency management. **Install conan version 1.60.2**, for example, through

        .. code:: console

            pip install conan==1.60.2

        | See the `instructions <https://docs.conan.io/en/latest/installation.html>`_ if alternative installation methods are needed

* **CMake**: This repository uses `CMake <https://cmake.org/download/>`_ for managing the build process. Version 3.15 or later is recommended.

* **Qt**: `Qt <https://www.qt.io/download>`_ is free for open source developers. Version 5.15 or later is required. Make sure to include Qt Creator in the installer.

.. warning::

  Qt Version 6.0 is currently available. It is so new we do not use it.

******************************
Build the Backend Applications
******************************

Instructions to build the backend workflow applications on your local desktop depend on your operating system, but is a 2 step process involving some initial setup and finally the build.

Setup the development environment with Conan
============================================
1. Add Conan `SimCenter <https://bintray.com/nheri-simcenter/simcenter>`_ to the Conan remotes. You can add these remotes by typing the following commands in the terminal:

    .. code:: console

        conan remote add simcenter https://nherisimcenter.jfrog.io/artifactory/api/conan/simcenter

2. Create a default Conan profile if this is the first time you use Conan for building packages.

    .. code:: console

        conan profile new default --detect


3. Check the default profile of your build environment using:

    .. code:: console

       conan profile show default

4. If the compiler name and compiler version are *not* listed, you will need to select a specific compiler. For instance, on Windows using Visual Studio 2019, you can specify the compiler as follows:

    .. code:: console

       conan profile update settings.compiler="Visual Studio" default
       conan profile update settings.compiler.version="16" default


Build the applications
======================

#. Obtain the code in the SimCenterBackendApplications repository from `Github <https://github.com/NHERI-SimCenter/SimCenterBackendApplications>`_. You can do that by using your preferred Git client/GUI or by using the ``git clone`` command in the terminal:

    .. code::

        git clone https://github.com/NHERI-SimCenter/SimCenterBackendApplications	 

#. To build the applications you need to now navigate to the **SimCenterBackendApplications** folder that was created with the **git clone** command. Once there you will issue the following set of commands to create a **build** folder, change director to that folder, install needed software using conan, and finally use **cmake** to build and install thge applications. The following are the set of commands to type in the terminal (see notes below the code block if the commands fail).


    For those developers using the Windows operating system, in a terminal or powershell window you need to type the following:

            .. code:: console

              mkdir build
              cd build
              conan install .. --build missing
              cmake .. -G "Visual Studio 16 2019"
              cmake --build . --config Release
              cmake --install .
              cd ..

    On Windows, it is necessary to specify a compiler for CMake. To do this, you need to add additional arguments to line 4, i.e., if you have Visual Studio 2019, you would instead type:

            .. code:: console

              mkdir build
              cd build
              conan install .. --build missing
              cmake ..
              cmake --build . --config Release
              cmake --install .
              make install .
              cd ..	  

    .. note::

       #. For Mac users running **Big Sur** and version **12** of XCode there are some reported issues. Replace line 3 above with the following two lines:

          .. code::       

            conan install .. --build missing --build=libcurl
            mv ./missing/* ./

       #. For Mac users, add the following command after **cmake --install .** to ensure the binary applications are copied to the applications folder.

          .. code::       

            make install .

          
      
If building and installation were successful, you should find a folder called ``applications`` in the repository with all the applications inside of it.   The name of this folder should not be changed.
   

************************
Build the User Interface
************************

To build the interface, you first need to download the repo and a companion repo(SimCenterCommon) from Github using our `github repos <https://github.com/NHERI-SimCenter>`_. In a folder in which you wish to build the application, issue the following two commands.

.. only:: quoFEM_app

    .. code::
       
      git clone https://github.com/NHERI-SimCenter/SimCenterCommon.git
      git clone https://github.com/NHERI-SimCenter/quoFEM.git

.. only:: R2D_app

	  
   .. code::
      
      git clone https://github.com/NHERI-SimCenter/SimCenterCommon.git
      git clone https://github.com/NHERI-SimCenter/R2DTool.git      


.. only:: PBE_app

   .. code::	  

       git clone https://github.com/NHERI-SimCenter/SimCenterCommon.git
       git clone https://github.com/NHERI-SimCenter/QS3hark.git	  
       git clone https://github.com/NHERI-SimCenter/EE-UQ.git
       git clone https://github.com/NHERI-SimCenter/PBE.git       

.. only:: EEUQ_app

   .. code::
      
       git clone https://github.com/NHERI-SimCenter/SimCenterCommon.git
       git clone https://github.com/NHERI-SimCenter/QS3hark.git	  
       git clone https://github.com/NHERI-SimCenter/EE-UQ.git	  

.. only:: WEUQ_app	  

   .. code::

       git clone https://github.com/NHERI-SimCenter/SimCenterCommon.git
       git clone https://github.com/NHERI-SimCenter/WE-UQ.git	  


.. note::


   Use the above links if you just want to download and build the applications. If you intend to make changes to any of the code in the repo's, you should fork that repo and then clone your forked repo. Forking a repo at **github** is done through your browser as shown on the following `github guides page <https://guides.github.com/activities/forking/>`_

You now have two ways to build the application: (1) using the **Qt Creator** desktop application provided by **Qt** and (2) from terminal application.


Build using Qt Creator
========================

1. Start Qt Creator, then open the |short tool id|.pro file located in the |short tool id| directory that was downloaded in the previous step.
2. Setup the development kit in Qt Creator. This is usually done by selecting the Qt version, compiler, and configuration and following the onscreen dialog.
3. Build the application and run it in Qt Creator IDE using the **Run** button. This can be done using the keyboard shortcut ``F5`` to build and start the tool.


Build from the Terminal
========================

The operations are similar to what was done when building the backend applications. In the terminal application, starting inside the directory of the cloned application again, you will create a build directory, cd into that build directory, run **qmake**, and finally make (or on Windows nmake) to create the application.

Windows developers will type the following in a terminal or a powershell window:

    .. parsed-literal::

      mkdir build
      cd build
      conan install .. --build missing
      qmake ../|short tool id|.pro
      nmake

Linux or Mac users will type the following in a terminal window from inside the |app| directory:

    .. parsed-literal::

      mkdir build
      cd build
      conan install .. --build missing
      qmake ../|short tool id|.pro
      make

.. note::

   #. qmake is an application installed with Qt. To be able to run the command as known, the path to the Qt bin folder needs to be added to your **PATH** environment variable. Alternatively, you need to specify the full path to qmake, i.e., on my desktop (if I had not set my PATH variable). I would replace line 3 with the following:

      .. parsed-literal::

        /Users/fmckenna/Qt/5.15.2/clang_64/bin/qmake ../|short tool id|.pro


   #. On a Windows 10 with Visual Studio, the above commands need to be performed using a `Visual Studio x64 command prompt <https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-160>`_ . 

   #. If installed, jom can also be used to build in parallel.


Once built, you can now run the tool executable.


*************************************
Modify the User Interface Preferences
*************************************

Once built, the tool **Preferences** needs to be modified. To do this, open the |short tool id| tool, then click on File -> Preferences in the main menu if on Windows or |short tool id| -> Preferences if on a Mac. This will bring up a dialog window shown below. You need to modify specific values:

  #. Python: provide the full path to the python interpreter.
   
  #. OpenSees: provide the full path to the OpenSees executable

  #. Dakota: provide the full path to the Dakota executable.

  #. Custom Local Application: Here, select the checkbox to the left, and then provide the path to the SimCenterBackendApplications directory. The code assumes that the folder **applications**, which you created when building the backend applications, exists.

     
    .. _figPreferences:

.. only:: notQuoFEM

    .. figure:: figures/Preferences.png
       :align: center
       :figclass: align-center

       Preferences Dialog

.. only:: quoFEM_app

    .. figure:: figures/Preferences_qfem.png
       :align: center
       :figclass: align-center

       Preferences Dialog

