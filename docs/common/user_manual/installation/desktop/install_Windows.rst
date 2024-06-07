.. _lblInstallWindows:

Install on Windows 10
=====================

.. only:: R2D_app

   **Install Java**
   ^^^^^^^^^^^^^^^^

   .. note::
      Java is required for utilizing OpenSHA for regional seismic hazard characterization (:ref:`ground_motion_tool`). Skip this step if you do not intend to use this feature.

   Download and install Java from the official Java website. Version `16.0.2 <https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html>`_ is confirmed compatible with the latest |app|. Follow the installation prompts. If a JVM error appears, suggesting the JAVA_HOME environment variable needs setting, refer to this `guide <https://docs.oracle.com/cd/E19182-01/821-0917/inst_jdk_javahome_t/index.html>`_.
 
   .. note::
      The Java website should automatically detect and suggest the appropriate installer for your operating system. Ensure "64-bit Java for Windows" is indicated before downloading the Java installer.


.. only:: WEUQ_app

   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
     The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on Microsoft Windows 10, the user needs to use Windows Subsystem for Linux (WSL). WSL will provide a virtual environment for running Linux applications on Windows.

   Install OpenFOAM for Windows
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   To install OpenFOAM-10 on Windows 10, follow the instructions below: 

   #. First, open *PowerShell* from the start menu and run it as an administrator. Then, in the command window type ``wsl --install`` which will install all the necessary Linux features. For detailed instructions please follow `Install WSL <https://learn.microsoft.com/en-us/windows/wsl/install>`_.
   
   #. Open WSL from the start menu and run the following commands on the opened terminal window.  

   .. code:: bash

      sudo sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
      sudo add-apt-repository http://dl.openfoam.org/ubuntu
      sudo apt-get update
      sudo apt-get install openfoam10


   Further instructions can be found in `OpenFOAM.org <https://openfoam.org/download/windows/>`_.


.. only:: HydroUQ_app

   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. Backend mesh generation and visualization, which the GUI relies on, are powered by *OpenFOAM-10* and *OpenFOAM-7*'s built-in meshing tools.  

   .. note::
     The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on Microsoft Windows 10, the user needs to use Windows Subsystem for Linux (WSL). WSL will provide a virtual environment for running Linux applications on Windows.

   Install OpenFOAM for Windows
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   To install OpenFOAM-10 and OpenFOAM-7 on Windows 10, follow the instructions below: 

   #. First, open *PowerShell* from the start menu and run it as an administrator. Then, in the command window type ``wsl --install`` which will install all the necessary Linux features. For detailed instructions please follow `Install WSL <https://learn.microsoft.com/en-us/windows/wsl/install>`_.
   
   #. Open WSL from the start menu and run the following commands on the opened terminal window.  

   .. code:: bash

      sudo sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
      sudo add-apt-repository http://dl.openfoam.org/ubuntu
      sudo apt-get update
      sudo apt-get install openfoam10
      sudo apt-get install openfoam7


   Further instructions can be found in `OpenFOAM.org <https://openfoam.org/download/windows/>`_.



**Download the Application**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to the |appLink| page, which should resemble |figDownloadWin|, for a list of downloadable files and directories. Click the **Windows_Download.zip** file and select **Download** in the pop-up window's bottom right.


.. only:: R2D_app

   .. _figDownloadWin-R2D:

   .. figure:: figures/R2DDownload.png
      :align: center
      :figclass: align-center

      R2D Tool download page.

.. only:: PBE_app

   .. _figDownloadWin-PBE:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center

      PBE download page.

.. only:: EEUQ_app

   .. _figDownloadWin-EE:

   .. figure:: figures/eeDownload.png
      :align: center
      :figclass: align-center

      EE-UQ download page.

.. only:: WEUQ_app

   .. _figDownloadWin-WE:

   .. figure:: figures/weDownload.png
      :align: center
      :figclass: align-center

      WE-UQ download page.


.. only:: quoFEM_app

   .. _figDownloadWin-quoFEM:

   .. figure:: figures/quoFEMDownload.png
      :align: center
      :figclass: align-center

      quoFEM download page.


.. only:: HydroUQ_app

   .. _figDownloadWin-HydroUQ:

   .. figure:: figures/H20Download.png
      :alt: HydroUQ tool download page
      :align: center
      :figclass: align-center

      HydroUQ tool download page.

After downloading, extract the zip file to your preferred location, such as **C:/SimCenter/**. You can create and move a shortcut of the |short tool id|.exe to your Desktop for convenience.

.. tip:: Use an external compressor like `7-Zip <https://www.7-zip.org/>`_ for faster extraction than the default Windows function.



**Test the Installation**
^^^^^^^^^^^^^^^^^^^^^^^^^

After installation, perform basic checks by running the |short tool id|.exe from the installation directory.

.. note::

   Since the SimCenter is not registered as a Windows vendor, our applications may trigger a warning about unsigned applications from unknown sources when you start the |short tool name| application for the first time. It is safe to bypass this warning for SimCenter applications.


Launch the application to view the user interface as shown in |figWinUI|. It's recommended to run the |test example| to ensure proper operation.


.. only:: R2D_app

   .. _figWinUI-R2D:

   .. figure:: figures/R2D-Startup.png
    :align: center
    :figclass: align-center

    R2D Tool on startup.

.. only:: PBE_app

   .. _figWinUI-PBE:

   .. figure:: figures/PBE_startup.png
    :align: center
    :figclass: align-center

    PBE application on startup.

.. only:: EEUQ_app

   .. _figWinUI-EE:

   .. figure:: figures/EE-UQ.png
    :align: center
    :figclass: align-center

    EE-UQ application on startup.

.. only:: WEUQ_app

   .. _figWinUI-WE:

   .. figure:: figures/WE-UQ.png
    :align: center
    :figclass: align-center

    WE-UQ application on startup.

.. only:: quoFEM_app

   .. _figWinUI-quoFEM:

   .. figure:: figures/quoFEM.png
    :align: center
    :figclass: align-center

    quoFEM application on startup.


.. only:: HydroUQ_app

   .. _figWinUI-HydroUQ:

   .. figure:: figures/HydroWin.png
      :align: center
      :figclass: align-center

      HydroUQ tool on startup in Windows 10

    

**Troubleshooting**
^^^^^^^^^^^^^^^^^^^^^
If the test example fails, refer to :ref:`troubleshooting<lblTroubleshooting>`.

.. note::
   Analysis failure may be due to the **local working directory** path defined in the preference menu. Check for:

   - Avoid setting the local working directory under cloud-synced folders like OneDrive or Box, which may cause file-not-found errors.
   - Avoid including non-alphabetic characters or spaces in the path, which may potentially lead to encoding or file-not-found errors.
   - Avoid setting the local working directory on a different drive than the app executable (.exe), which may result in permission errors , e.g. the executable is under the C drive, and the working directory is under the E drive.
