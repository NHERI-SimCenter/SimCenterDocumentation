.. _lblInstallWindows:

Install on Windows 10
=====================

.. only:: R2D_app

   Install Java
   ^^^^^^^^^^^^

   .. note::
      Java is needed to use OpenSHA to characterize the regional seismic hazard (see :ref:`ground_motion_tool`). If you do not plan to use that feature, you can skip this step of the installation.

   If you have not yet installed Java, please download the latest installer from `java.com <https://java.com/en/download/>`_ , run it, and follow the on-screen instructions to install Java.

   .. note::
      The Java website should automatically detect your operating system and offer the corresponding installer for you to download. Make sure you see "64-bit Java for Windows" at the top of the page before downloading the installer.

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

After the download completed, extract the zip archive to a location in your filesystem. We suggest extracting to the **C:/SimCenter/** folder. You can create a shortcut that points to the |short tool id|.exe executable of the application and move this shortcut to your Desktop for easy access.

.. tip:: Using an external compressor program, such as `7-Zip <https://www.7-zip.org/>`_, can significantly reduce the zip archive extraction time compared to the Windows default extraction function.

Test the Installation
^^^^^^^^^^^^^^^^^^^^^

Once the installation procedure has been completed, it is a good practice to run some basic checks. Navigate to the location where you placed the application and open it by running the |short tool id|.exe executable.

.. note::

   Since the SimCenter is not registered as a Windows vendor, our apps are not recognized by the operating system as signed applications. You may receive a warning message that lets you know about risks involved in running unsigned applications from unkown sources when you start the |short tool name| application for the first time. It is safe to bypass that warning when running SimCenter applications.

Once the application started, you should see the user interface shown in |figWinUI|. We recommend running the example problem |test example| to test the application.

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

    
