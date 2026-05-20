.. _lblInstallMac:

===================
Install on MacOS
===================

Install Python
^^^^^^^^^^^^^^

SimCenter tools work with **Python 3.10, 3.11, or 3.12**. We recommend **Python 3.12**. To check whether your current Python is compatible, follow Steps **1** and **2** below. If it is incompatible (or you don't have Python installed), proceed with Steps **3** through **6** to install a compatible version.

#. Open a Terminal Window. To do this on your Mac:

   .. code::

     1) Press Command (⌘) + Spacebar to open Spotlight Search
     2) Type “Terminal” and press Enter in Spotlight Search.

#. To check whether your Python version is compatible, run the following command in your terminal window:

   .. code::

      python3 --version

   If the output reports Python 3.10, 3.11, or 3.12 (for example ``Python 3.12.7``), your installation is compatible -- skip to step **5**. Otherwise, proceed with steps **3** and **4** to install a compatible version.

#. Click on this link -> |appLink|. On the browser page that this brings up, you will find various files and directories available for download. Locate the file named **python-3.12.X-macos11.pkg** (where ``X`` is the latest patch number), which we copied from `Python.org <https://www.python.org/downloads/macos/>`_. Proceed to download this installer file.

#. Locate this installer file on your system and double click on it to start the installation process. Upon completion, a folder with several files will open, as shown in the figure below. Execute ``Update Shell Profile.command`` and ``Install Certificates.command`` by double-clicking each.

   .. figure:: figures/pythonInstallShell.png
      :align: center
      :figclass: align-center
      :width: 75%

      Python: Folder Displayed at Conclusion of Install

#. In the terminal window you opened in step **1**, run the following commands to install Apple's command line tools and the SimCenter Python packages needed by |app|.

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

   .. only:: quoFEM_app

      .. code-block:: bash

         xcode-select --install
         python3 -m pip install --upgrade "nheri_simcenter[quofem]"

   .. only:: HydroUQ_app

      .. code-block:: bash

         xcode-select --install
         python3 -m pip install --upgrade "nheri_simcenter[hydrouq]"

   The bracketed extra tells the installer to pull in only the packages |app| needs rather than every SimCenter dependency. The download is a few hundred megabytes and typically takes 1-3 minutes.

   If this step fails, see WARNING below.

#. Repeat steps **1** and **2** to ensure that Python was correctly installed. See note below if you still see the incorrect version in the ``NEW`` terminal window.

.. note::

   If step **5** was successful and you still have the incorrect version of Python after following the above steps, it probably means you forgot to invoke the **Update Shell Profile.command** script at the end of step **4**. You can still do it using **Finder**. Open Finder and navigate to the **/Applications/Python 3.12** folder. Here you will see a number of files, including the two you may have forgotten to run: **Install Certificates.command** and **Update Shell Profile.command**. Double-click each to run them. Finally repeat steps **1** and **2** again. If this still fails to produce the correct output for step **2**, please contact us for direct support.

.. warning::

   If step 5 above fails, it is because the system is finding a different version of Python on your system. This is going to require you do additional things.

   1. First you need to create a **Python environment** for your SimCenter applications. This is done by issuing the following set of commands.

      .. only:: R2D_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[r2d]"

      .. only:: PBE_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[pbe]"

      .. only:: EEUQ_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[eeuq]"

      .. only:: WEUQ_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[weuq]"

      .. only:: quoFEM_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[quofem]"

      .. only:: HydroUQ_app

         .. code-block:: bash

            cd ~
            mkdir python_env
            cd python_env
            /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv python_simcenter
            source ./python_simcenter/bin/activate
            python3 -m pip install --upgrade "nheri_simcenter[hydrouq]"

      The commands create a directory in your home folder called **python_env**, then create a new Python environment inside it (a folder called **python_simcenter**). To activate this environment you source the script **activate** in its **bin** folder. With the environment activated you can install the SimCenter Python package. If this too fails, please contact us.

   2. When the application is actually running, you need to change the location of the **Python** application that is run. To do this, in the top menu bar, under the tool icon select Preferences. Change the location of Python -- the first variable you can edit -- to the python3 in the new environment, i.e. **/Users/YOUR_LOGIN/python_env/python_simcenter/bin/python3**. Finally press the **Save** button. Please note that YOUR_LOGIN needs to be replaced with your actual login!
	
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

   **Install OpenMP**
   ^^^^^^^^^^^^^^^^^^

   .. note::
      OpenMP is required by ``pandarm``, the routing engine used by R2D's Residual Demand module for regional transportation network analysis. Install it via Homebrew:

      .. code-block:: bash

         brew install libomp

      If Homebrew is not yet installed, follow the instructions at `brew.sh <https://brew.sh>`_.


.. only:: WEUQ_app
   
   Install OpenFOAM for macOS
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
      The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on macOS, the user needs to use Docker for Mac. Docker will provide a virtual environment for running Linux applications on macOS.

   To download and install Docker for macOS from the following site `Docker for macOS <https://docs.docker.com/desktop/install/mac-install/>`_ .

   .. note::
      Make sure to download Docker distribution that maches your machine requirements (Apple or Intel chip). 
      
.. only:: HydroUQ_app
   
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

