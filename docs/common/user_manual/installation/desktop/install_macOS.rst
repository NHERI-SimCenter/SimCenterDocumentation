.. _lblInstallMac:

===================
Install on MacOS
===================

.. only:: R2D_app
	  
   **Install OpenMP**
   ^^^^^^^^^^^^^^^^^^

      OpenMP is required by the python module ``pandarm``, the routing engine used by R2D's Residual Demand module for regional transportation network analysis. You need to install OpenMP before installing python. OpenMP is installed via Homebrew by entering the following in a terminal window:

      .. code-block:: bash

         brew install libomp

      .. note:: 

	 1. If Homebrew is not yet installed, follow the instructions at `brew.sh <https://brew.sh>`_.

	 2. To open a terminal window use Spotlight (⌘+Space), type "Terminal" and press your keyboards Enter key.


.. only:: R2D_app

   **Install Java (JDK 17)**
   ^^^^^^^^^^^^^^^^^^^^^^^^^

   .. note::
      Java is required only if you plan to use the OpenSHA-based regional seismic hazard feature in |app| (:ref:`ground_motion_tool`). If you do not need this feature, you can skip this section.

   |app| is tested with **Eclipse Temurin JDK 17**, the long-term-support (LTS) build of Java. We recommend this exact version.

   **Which installer should I download?**

   The right installer depends on your Mac's processor, because Java must match the architecture of the Python you installed earlier:

   * **Apple Silicon Mac** (chips named **M1**, **M2**, **M3**, or **M4** -- any Mac sold since late 2020): download the **macOS aarch64** installer from `Temurin JDK 17 — macOS Apple Silicon (aarch64) <https://adoptium.net/temurin/releases/?version=17&package=jdk&os=mac&arch=aarch64>`_.
   * **Intel Mac** (any Mac sold before late 2020): download the **macOS x64** installer from `Temurin JDK 17 — macOS x64 <https://adoptium.net/temurin/releases/?version=17&package=jdk&os=mac&arch=x64>`_.

   To check which kind of Mac you have, click the **Apple menu** in the top-left corner of your screen and choose **About This Mac**. Look at the **Chip** (or **Processor**) line: if it starts with "Apple" you want the aarch64 installer; if it says "Intel" you want the x64 installer.

   **To install:**

   1. Click the matching link above. On the Adoptium page, click the download icon next to the PKG option to download the ``.pkg`` file. You'll get a file named something like ``OpenJDK17U-jdk_aarch64_mac_hotspot_17.0.X_Y.pkg`` (or ``...x64...`` for Intel).
   2. Once the download finishes, double-click the ``.pkg`` file in your **Downloads** folder. The macOS installer will open. Accept the defaults on each screen and click **Install** at the end. You may be asked for your password.

   .. tip::
      If you already have a different Java version installed on your Mac, you do not need to remove it. Multiple Java versions coexist without conflict -- each lives in its own folder under ``/Library/Java/JavaVirtualMachines/``.

   .. note::
      The Java website should automatically detect and suggest the appropriate installer for your operating system.

	    
Install Python
^^^^^^^^^^^^^^

The |app| requires Python be installed on your machine and that the version of it be in the **3.10 -- 3.12** range. 

To check what you have, open Terminal (Spotlight: ⌘+Space, type
"Terminal", press Enter) and run::

   python3 --version

If it reports a 3.10, 3.11, or 3.12 number, you're set and can go to the next step. If not, you need to install an appropriate version. We recommend 3.12.

**To Install Python 3.12**

#.  Go to the tool download page (link: |appLink|). On the browser page that this brings up, you will find various files and directories available for download. Locate the file named **python-3.12.6-macosx11.pkg**, which we copied from `Python.org <https://www.python.org/downloads/macos/>`_. Proceed to download this installer file.

#. Locate this installer file in your Downloads folder, and double click on it to start the installation process. Upon completion, a folder with several files will open, as shown in the figure below. Execute ``Update Shell Profile.command.sh`` and ``Install CertificateCommand.sh`` by double-clicking each.

#. Click on this link -> |appLink|. On the browser page that this brings up, you will find various files and directories available for download. Locate the file named **python-3.12.X-macos11.pkg** (where ``X`` is the latest patch number), which we copied from `Python.org <https://www.python.org/downloads/macos/>`_. Proceed to download this installer file.

#. Locate this installer file on your system and double click on it to start the installation process. Upon completion, a folder with several files will open, as shown in the figure below. Execute ``Update Shell Profile.command`` and ``Install Certificates.command`` by double-clicking each.


   .. figure:: figures/pythonInstallShell.png
      :align: center
      :figclass: align-center
      :width: 75%

      Python: Folder Displayed at Conclusion of Install


#. Repeat the first python version check above in a ``NEW`` terminal window.

.. note::

   If you still have the incorrect version of python installed after following the above steps, it probably means you forgot to invoke the **Update Shell Profile Command.command** script. You can still do it using **Finder**. Open Finder and navigate to the **/Applications/Python 3.12** folder. Here you will see a number of files, including the two you forgot to run: **Install Certificates Command.command** and **Update Shell Profile Command.command**. Double click on these files to run them. Finally open a **NEW** terminal again and check your version of python.


Optional: Create a Python Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have a current version of Python that meets the requirements (3.10, 3.11 or 3.12) and want to re-use it, or if you will be using additional SimCenter applications, we strongly recommend creating a **python virtual environment**. This is in case the python modules wou will install in next step don't mix with your current ones or ones you will need in the future. To create a python environment for |app| and then switch to that environment, issue the following in the terminal window:

.. parsed-literal::		     
      
        cd ~
        mkdir python_env
        cd python_env
        python3 -m venv python-|short tool id|
        source ./python-|short tool id|/bin/activate

.. note::

  These commands create a folder in your home directory named **python_env**, instruct the current default python interpreter to create a directory for a virtual environment named python-{short tool id| in this folder, and from the many files in this new folder that are present, you invoke a script ``activate`` that sets up the terminal environment such that it uses the python interpreter you created the environment with and, most importantly, will install python packages into this folder.

Install Python Modules
^^^^^^^^^^^^^^^^^^^^^^

In the terminal window you have opened, you need to issue the following **2** commands to ensure the command line tools for x-code exist on your machine and that some python modules are installed for the current python you are using:

.. only:: quoFEM_app

   .. code-block:: bash
      
      xcode-select --install
      python3 -m pip install --upgrade "nheri_simcenter[quofem]"

.. only:: R2D_app

   .. code-block:: bash

      xcode-select --install
      python3 -m pip install --upgrade "nheri_simcenter[r2d]"

.. only:: PBE_app

   .. code-block:: bash

      xcode-select --install
      python3 -m pip install --upgrade "nheri_simcenter[pbe]"

.. only:: EEUQ_app

   .. code-block:: bash

      xcode-select --install
      python3 -m pip install --upgrade "nheri_simcenter[eeuq]"

.. only:: WEUQ_app

   .. code-block:: bash

      xcode-select --install
      python3 -m pip install --upgrade "nheri_simcenter[weuq]"

.. only:: HydroUQ_app

   .. code-block:: bash

     xcode-select --install
     python3 -m pip install --upgrade "nheri_simcenter[hydrouq]"

   The bracketed extra tells the installer to pull in only the packages |app| needs rather than every SimCenter dependency. The download is a few hundred megabytes and typically takes 1-3 minutes.


Note Your Python Path
^^^^^^^^^^^^^^^^^^^^^

|app| needs the full path to the Python interpreter. Find it with the ``which`` command in Terminal.

   .. code-block:: bash

      which python3

If you are using the newly installed python without a virtual environment you should see: ``/Library/Frameworks/Python.framework/Versions/3.12/bin/python3``. If using a python environment you willl instead see: /Users/YOUR_LOGIN/python_env/python-|short tool id|/bin/python3. Copy this path to your clipboard.

.. note::

   When the application is actually running, you will need to change the location of the **python** application that will run **if** you are using a virtual environment or if the existing python interpreter you are using is in a different location. To do this, in the top menu bar, under the tool icon select Preferences (on some macOS versions it is Settings). Change the location of python, the first variable you can edit, to the python3 path noted, e.g. /Users/YOUR_LOGIN/python_env/python-|short tool id|/bin/python3. Finally press the **Save** button. Please note that YOUR_LOGIN needs to be replaced with your actual login!

.. only:: WEUQ_app
   
   Install OpenFOAM for macOS
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
      The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on macOS, the user needs to use Docker for Mac. Docker will provide a virtual environment for running Linux applications on macOS.

   To download and install Docker for macOS from the following site `Docker for macOS <https://docs.docker.com/desktop/install/mac-install/>`_ .

   .. note::
      Make sure to download Docker distribution that matches your machine requirements (Apple or Intel chip). 
      
.. only:: HydroUQ_app
   
   Install OpenFOAM for macOS
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
      The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on macOS, the user needs to use Docker for Mac. Docker will provide a virtual environment for running Linux applications on macOS.

   To install OpenFOAM-10 on macOS, follow the instructions in `OpenFOAM for macOS <https://openfoam.org/download/10-macos/>`_ .

**Download the Application**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To download the |app|, navigate to the |appLink| page which should resemble |figDownload|. The download page contains a list of downloadable files and directories. Two macOS build are listed |tool app id|_MacOS_Download_arm64.dmg, for Apple Silicon Macs (chips named **M1**, **M2**, **M3**, **M4*, and *M5*)  and |tool app id|_Mac_Download_x86_64.dmg for older INtel-based Macs. 

.. note::

   To check which you have: click the **Apple menu** in the top-left corner of your screen and choose **About This Mac**. Look at the **Chip**
   (o**Processor**) line. If it starts with "Apple", you want the **arm64** download. If it says "Intel", you want the **x86_64** download.
   If you pick the arm64 build on an Apple Silicon Mac, |short tool id|  runs natively and is significantly faster than under emulation. The
   arm64 build will not run on an Intel based Mac.


.. only:: R2D_app

   .. _figDownload-R2D:

   .. figure:: figures/R2DDownload.png
      :align: center
      :figclass: align-center
      
      R2D Tool download page.


.. only:: PBE_app

   .. _figDownload-PBE:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center
      
      PBE download page.


.. only:: EEUQ_app

   .. _figDownload-EE:

   .. figure:: figures/eeDownload.png
      :align: center
      :figclass: align-center
      
      EE-UQ download page.


.. only:: WEUQ_app

   .. _figDownload-WE:

   .. figure:: figures/weDownload.png
      :align: center
      :figclass: align-center
      
      WE-UQ download page.


.. only:: quoFEM_app

   .. _figDownload-quoFEM:

   .. figure:: figures/quoFEMDownload.png
      :align: center
      :figclass: align-center
      :width: 75%
      
      quoFEM download page.


.. only:: HydroUQ_app

   .. _figDownload-HydroUQ:

   .. figure:: figures/H20Download.png
      :align: center
      :figclass: align-center
      
      HydroUQ tool download page.



Click on the appropriate file link in the pop-up window, then click on the **Download** button in the bottom right corner. After the download is completed, open the dmg file and **copy** the |short tool id| **to a location in your filesystem**.

.. note::
   
   We suggest copying the application either the Applications folder or your Desktop. After copying the application, you can move the dmg file to the trash or eject it.


Test the Installation
^^^^^^^^^^^^^^^^^^^^^

Once the installation procedure has been completed, it is a good practice to run some basic checks. Navigate to the location where you placed the application and open it by double-clicking the |short tool id| application.

.. note::

   SimCenter apps are code-signed and notarized, but because they are not downloaded from the **Apple** app store, they will not be recognized as safe applications. Depending on your security settings, when you start a SimCenter app for the first time, your operating system may show a dialog box indicating it is unsafe. If this dialog appears, choose the cancel button. Try to start the app again, this time by right-clicking on it and selecting open.

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


.. only:: HydroUQ_app

   .. _figUI-HydroUQ:

   .. figure:: figures/HydroMac.png
      :align: center
      :figclass: align-center
      :width: 75%
      
      HydroUQ application on startup.

.. note::

   When the |app| is running, open the app/preferences or File/Preferences and make sure that ``python3`` appears under **External Applications:Python**, as shown in the figure below. If you used older versions of SimCenter tools this was not the default. The exact location of Python3 that you installed can be found by opening the terminal application and executing the **which python3** command. Enter the path shown as a response in the Preferences panel under Python and then press the **Save** button.

   .. _figUI-preferences:
   
   .. figure:: figures/pythonPreferences.png
      :align: center
      :figclass: align-center
      :width: 75%
      
      Set Python Preferences.

