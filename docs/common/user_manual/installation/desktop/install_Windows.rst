.. _lblInstallWindows:

Install on Windows 10
=====================

.. only:: R2D_app

   Install Java
   ^^^^^^^^^^^^

   .. note::
      Java is needed to use OpenSHA to characterize the regional seismic hazard (see :ref:`ground_motion_tool`). If you do not plan to use that feature, you can skip this step of the installation.

   If you have not yet installed Java, please download the installer from Java website. The version `16.0.2 <https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html>`_ has been tested to be working with the latest |app|. Follow the on-screen instructions to install Java. If you run into a JVM error that suggests setting JAVA_HOME environment variable, you can do so per this `link <https://docs.oracle.com/cd/E19182-01/821-0917/inst_jdk_javahome_t/index.html>`_
 
   .. note::
      The Java website should automatically detect your operating system and offer the corresponding installer for you to download. Make sure you see "64-bit Java for Windows" at the top of the page before downloading the installer.


.. only:: WEUQ_app

   This version of the |app| uses *OpenFOAM* for pre-processing the CFD model. At the backend, the mesh generation and visualization in the GUI utilize *OpenFOAM-10* built-in meshing tools.  

   .. note::
     The packaged distribution of OpenFOAM is only available for Linux systems. To install OpenFOAM on Microsoft Windows 10, the user needs to use Windows Subsystem for Linux (WSL). WSL will provide a virtual environment for running Linux applications on Windows.

   ..  The at mesh generation and pre-processing party applications s. 

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


Download the Application
^^^^^^^^^^^^^^^^^^^^^^^^

To download the |app|, navigate to the |appLink| page which should resemble |figDownload|. The download page contains a list of downloadable files and directories.


.. only:: R2D_app

   .. _figDownloadWin-R2D:

   .. figure:: figures/R2DDownload.png
      :align: center
      :figclass: align-center

      R2DTool download page.

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


.. only:: Hydro

   .. _figDownload-HydroUQ:

   .. figure:: figures/H20Download.png      
      :alt: HydroUQ tool download page
      :align: center
      :figclass: align-center		 

      HydroUQ tool download page.


Click on the file with a name ending with **Windows_Download.zip** to download the |app|. In the pop-up window, click on the **Download** button in the bottom right corner.

After the download is completed, extract the zip archive to a location in your filesystem. We suggest extracting it to the **C:/SimCenter/** folder. You can create a shortcut that points to the |short tool id|.exe executable of the application and move this shortcut to your Desktop for easy access.

.. tip:: Using an external compressor program, such as `7-Zip <https://www.7-zip.org/>`_, can significantly reduce the zip archive extraction time compared to the Windows default extraction function.

Test the Installation
^^^^^^^^^^^^^^^^^^^^^

Once the installation procedure has been completed, it is a good practice to run some basic checks. Navigate to the location where you placed the application and open it by running the |short tool id|.exe executable.

.. note::

   Since the SimCenter is not registered as a Windows vendor, our apps are not recognized by the operating system as signed applications. You may receive a warning message that lets you know about the risks involved in running unsigned applications from unknown sources when you start the |short tool name| application for the first time. It is safe to bypass that warning when running SimCenter applications.

Once the application starts, you should see the user interface shown in |figWinUI|. We recommend running the example problem |test example| to test the application.

.. only:: R2D_app

   .. _figWinUI-R2D:

   .. figure:: figures/R2D-Startup.png
    :align: center
    :figclass: align-center

    R2DTool on startup.

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

.. only:: Hydro

    .. _figWinUI-HydroUQ:

   .. figure:: figures/HydroWIN.png
    :align: center
    :figclass: align-center

    HydroUQ tool on startup in Windows 10    

    

Troubleshooting
^^^^^^^^^^^^^^^^^^^^^
If the analysis fails, please see the :ref:`troubleshooting<lblTroubleshooting>` page.

.. note::
   When analysis fails, a quick check is to inspect the **local working directory** path in the preference menu. The below could lead to the analysis failure 

   * The path is located under a cloud folder, e.g. OneDriver, Box (may give file-not-found error due to the real-time cloud-only sync)
   * The path contains non-alphabetic characters (may give an encoding error)
   * The path contains empty space (low likelihood, but it may give the file-not-found error)
   * The path is located under a different driver from the app executable (.exe) path, e.g. one is under C drive, and the other is under E drive (may give a permission error)
