.. _lblInstallMac:

Install on MacOS
===================

Install Python 3.9
^^^^^^^^^^^^^^^^^^

SimCenter tools require an x86-based Python 3.9. If your current Python version is incompatible, follow these steps to install the required version from `Python.org <https://www.python.org/downloads/macos/>`_.

To check your Python version compatibility, issue the following in a terminal window.

.. code::
   
   python3
   import platform
   platform.uname()
   exit()

Ensure the output indicates Python 3.9 and `machine='x86_64'`, as shown in the screenshot below. If not, proceed to install Python 3.9 x86.

.. figure:: figures/pythonKernel.png
      :align: center
      :figclass: align-center
      :width: 75%

      Python: Kernel Version
**1.** Visit `Python.org <https://www.python.org/downloads/macos/>`_ and download the **macOS 64-bit Intel-only installer** for Python 3.9.

.. figure:: figures/pythonDownload.png
      :align: center
      :figclass: align-center

      Python: python.org MacOS Download Page
**2.** Run the installer. Upon completion, a folder with several files will open, as shown in the figure below. Execute ``Update Shell Profile.command.sh`` and ``Install CertificateCommand.sh`` by double-clicking each.

   .. figure:: figures/pythonInstallShell.png
      :align: center
      :figclass: align-center
      :width: 75%

      Python: Folder Displayed at Conclusion of Install
**3.** Install additional packages via the **nheri_simcenter** package by starting a Terminal window and type the following command:

.. code-block:: bash

      pip3 install nheri_simcenter --upgrade


Make sure you see a message that confirms the successful installation of the nheri-simcenter package before proceeding to the next step.

.. note::

   1. If you forget to invoke the ``UpdateShellProfile.command.sh`` script at the end of the install, you can always execute the correct shell file later to update the ``PATH`` variable to point to the Python application.

   On Linux systems, the shell is the program that takes commands from the keyboard that you enter in the terminal window and passes them to the operating system to perform by invoking applications and passing data between applications. In the good old days, it was the only interface available to the user, i.e., there was no such thing as Finder! There are a number of shell programs that can be installed and made available to you. The most popular is the **bash** shell, and the up-and-coming one is the **Z** shell. Power MacOS users will write shell scripts to do many useful things. By default, the applications that the shell program will invoke are limited to applications in a few specific directories that are defined in the user's ``PATH``. Users can modify this path by editing files that the shell program will read from every time the program is started.

   When the frontend application is running the computations it is actually running a backend application using the shell program. As a consequence the shell program must be made aware of the locations of some of the external applications that you have installed as **OpenSees** and **Dakota** do not provide installers that automatically do this when they are installed. Other applications, like **Tcl** provide scripts that you invoke to do it. In short, you have to edit the file appropriate to the shell you are using.

   To find which shell program you are using when you issue commands inside the terminal window, type the following:

   .. code:: bash

      env | grep SHELL

   If the result is ``/bin/bash`` you will need to edit the ``.bashrc`` file or the ``bash_profile`` file. If the result is ``/bin/zsh`` you will need to edit the ``.zshrc`` or ``.zprofile``. Typically, the ``.bash_profile`` or the ``.zprofile`` file is the one to edit as by design these will invoke the ``.bashrc`` or ``.zshrc`` file. If in doubt, look for these files in your home directory and see which of these other installers have modified.

   2. Python 3.10 from python.org will also work, though there is no x86 installer. The reason we do not recommend its usage is that there are additional settings that need to be modified in the application under the Preferences tab as that python package has a different mechanism for invoking the x86 version, specifically **python3-intel64**.

.. only:: R2D_app

   **Install Java**
   ^^^^^^^^^^^^

   .. note::
      Java is required for utilizing OpenSHA for regional seismic hazard characterization (:ref:`ground_motion_tool`). Skip this step if you do not intend to use this feature.

   Download and install Java from the official Java website. Version `16.0.2 <https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html>`_ is confirmed compatible with the latest |app|. Follow the installation prompts. If a JVM error appears, suggesting the JAVA_HOME environment variable needs setting, refer to this `guide <https://docs.oracle.com/cd/E19182-01/821-0917/inst_jdk_javahome_t/index.html>`_.
 
   .. note::
      The Java website should automatically detect and suggest the appropriate installer for your operating system. Ensure "64-bit Java for Windows" is indicated before downloading the Java installer.


.. only:: WEUQ_app
   
   Install OpenFOAM for macOS
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
     The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on macOS, the user needs to use Docker for Mac. Docker will provide a virtual environment for running Linux applications on macOS.

   To install OpenFOAM-10 on macOS, follow the instructions in `OpenFOAM for macOS <https://openfoam.org/download/10-macos/>`_ .

**Download the Application**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To download the |app|, navigate to the |appLink| page which should resemble |figDownload|. The download page contains a list of downloadable files and directories.

.. only:: R2D_app

   .. _figDownload:

   .. figure:: figures/R2DDownload.png
      :align: center
      :figclass: align-center

      R2D Tool download page.


.. only:: PBE_app

   .. _figDownload:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center

      PBE download page.

.. only:: EEUQ_app

   .. _figDownload:

   .. figure:: figures/eeDownload.png
      :align: center
      :figclass: align-center

      EE-UQ download page.

.. only:: WEUQ_app

   .. _figDownload:

   .. figure:: figures/weDownload.png
      :align: center
      :figclass: align-center

      WE-UQ download page.


.. only:: quoFEM_app

   .. _figDownload:

   .. figure:: figures/quoFEMDownload.png
      :align: center
      :figclass: align-center
      :width: 75%

      quoFEM download page.


.. only:: Hydro

   .. _figDownload:

   .. figure:: figures/H20Download.png
      :align: center
      :figclass: align-center

      HydroUQ tool download page.



Click on the file with a name ending with **Mac_Download.dmg** to download the |app|. In the pop-up window, click on the **Download** button in the bottom right corner. After the download is completed, open the dmg file and **copy** the |short tool name| **to a location in your filesystem**.

.. note::

   We suggest copying the application to your Desktop. After copying the application, you can move the dmg file to the trash or eject it.

Test the Installation
^^^^^^^^^^^^^^^^^^^^^

Once the installation procedure has been completed, it is a good practice to run some basic checks. Navigate to the location where you placed the application and open it by running the |short tool id|.exe executable.

.. note::

   SimCenter apps are code-signed and notarized, but because they are not downloaded from the operating system's app store, they may not be recognized as safe applications. Depending on your security settings, when you start a SimCenter app for the first time, your operating system may show a dialog box indicating it is unsafe. If this dialog appears, choose the cancel button. Try to start the app again, this time by right-clicking on it and selecting open.

   If the app still fails to open. You need to go to System Settings->Privacy and Security. Under the Security section, you need to at least temporarily select the option to allow applications downloaded from the **App Store and Identified Developers**. With this checked try again. If it fails again, go back to System Settings->Privacy and Security. Just below the section you just checked, there should be some text about why the app was stopped and an option to **Open Anyway**, as shown in the figure below. Click on the button and the app should start.

   .. figure:: figures/AppleSecurity.png
           :align: center
           :figclass: align-center
           :width: 50%



Once the application starts, verify the setup by running an example problem |test example|, see |figUI|.

.. only:: R2D_app

   .. _figUI-R2D:

   .. figure:: figures/R2D-Startup.png
    :align: center
    :figclass: align-center

    R2D Tool on startup.

.. only:: PBE_app

   .. _figUI-PBE:

   .. figure:: figures/PBE_startup.png
	:align: center
        :figclass: align-center
        :width: 75%

    PBE application on startup.

.. only:: EEUQ_app

   .. _figUI-EE:

   .. figure:: figures/EE-UQ.png
        :align: center
        :figclass: align-center
        :width: 75%

    EE-UQ application on startup.

.. only:: WEUQ_app

   .. _figUI-WE:

   .. figure:: figures/WE-UQ.png
        :align: center
        :figclass: align-center
        :width: 75%

    WE-UQ application on startup.

.. only:: quoFEM_app

   .. _figUI-quoFEM:

   .. figure:: figures/quoFEM.png
           :align: center
           :figclass: align-center
           :width: 75%


    quoFEM application on startup.


.. only:: Hydro

   .. _figUI-HydroUQ:

   .. figure:: figures/HydroMac.png
        :align: center
        :figclass: align-center
        :width: 75%

    HydroUQ application on startup.

.. note::

   When the |app| is running, open the app/preferences or File/Preferences and make sure that python3 appears under **External Applications:Python**, as shown in the figure below. If you used older versions of SimCenter tools this was not the default. The exact location of Python3 that you installed can be found by opening the terminal application and executing the **which python3** command. Enter the path shown as a response in the Preferences panel under Python and then press the **Save** button.

      .. figure:: figures/pythonPreferences.png
           :align: center
           :figclass: align-center
           :width: 75%

    Set Python Preferences.

