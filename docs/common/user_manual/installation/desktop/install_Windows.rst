.. _lblInstallWindows:

Install on Windows 10
=====================

Install Python 3.8
^^^^^^^^^^^^^^^^^^

If you have not yet installed Python, we recommend installing Python 3.8 from
`python.org <https://www.python.org/downloads/windows>`_ , using the
**Windowsx86 64-bit executable installer**.

.. note::

   Allow the installer to change your system environment variables so that the directory containing the executable will be on your path. This requires checking the small box asking for this when the installer starts. The box is located at bottom of installer application window.

.. warning::
   The latest version of Python is 3.9.1. We require a previous version, 3.8.6 and above, to avoid issues with packages that have not have been adopted to the latest version and as a consequence fail to install.

Once Python is installed, you need to extend it by installing a few additional packages. To faciliate this phase of the installation, we created a **nheri_simcenter** python package that automatically installs all other dependencies. Start a `terminal window as an Admin user <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>`_ and type the following command:

.. code-block:: winbatch

      pip install nheri_simcenter --upgrade

Make sure you see a message that confirms the successful installation of the nheri-simcenter package before proceeding to the next step.

If you plan to use OpenSeesPy to run finite element analyses, you should also install that package at this point. (If you are not sure, we recommend you to install it.) You can install OpenSeesPy using a terminal window and the following command:

.. code-block:: winbatch

      pip install openseespy --upgrade


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

To download the |app|, first navigate to the |appLink| page. As shown in |figDownload|, to get to the download page, you need to click on the link ``Download app and User Manual`` in the application page. The download page contains a list of downloadable files and directories.

.. only:: R2D_app

   .. _figDownload:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center

      R2DTool download page.

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

      quoFEM download page.

Click on the file with a name ending with **Windows_Download.zip** to download the |app|. In the pop-up window, click on the **Download** button in the bottom right corner. After the download completed, extract the zip archive to a location in your filesystem.

.. note::

   We suggest placing the directory in the **C:\\SimCenter** folder. Once here, you can create a shorcut to the application and move this shortcut to your Desktop.

Test the Installation
^^^^^^^^^^^^^^^^^^^^^

Now test if the application starts properly. Navigate to the location where you placed the application and open it by running the |short tool id|.exe executable. You should see the user interface shown in |figUI|.

.. note::

   Since the SimCenter is not recognized as a Windows vendor, our applications are not recognized by the operating system as being signed. Consequently, you may receive a warning message when you start the |short tool name| application for the first time.

.. only:: R2D_app

   .. _figUI-R2D:

   .. figure:: figures/PBE.png
    :align: center
    :figclass: align-center

    R2DTool on startup.

.. only:: PBE_app

   .. _figUI-PBE:

   .. figure:: figures/PBE.png
    :align: center
    :figclass: align-center

    PBE application on startup.

.. only:: EEUQ_app

   .. _figUI-EE:

   .. figure:: figures/EE-UQ.png
    :align: center
    :figclass: align-center

    EE-UQ application on startup.

.. only:: WEUQ_app

   .. _figUI-WE:

   .. figure:: figures/WE-UQ.png
    :align: center
    :figclass: align-center

    WE-UQ application on startup.

.. only:: quoFEM_app

   .. _figQUO_FEM:

   .. figure:: figures/quoFEM.png
    :align: center
    :figclass: align-center

    quoFEM application on startup.

