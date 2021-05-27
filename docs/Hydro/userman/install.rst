.. _lbl-install:

***************************
Installation
***************************

All SimCenter applications can be downloaded from the `SimCenter Research Tools <https://simcenter.designsafe-ci.org/research-tools/overview/>`_ page. This section walks you through the install process from downloading the application to testing that it has been installed correctly.

Download HydroUQ
===================
To download the |app|, navigate to the |appLink| page which should resemble |figDownload|. The download page contains a list of downloadable files and directories.

.. _figDownload-Hydro:

   .. figure:: figures/H20Download.png
      :align: center
      :figclass: align-center

      HydroUQ tool download page.

Windows
============
Click on the file with a name ending with **Windows_Download.zip** to download the |app|. In the pop-up window, click on the **Download** button in the bottom right corner. After the download completed, extract the zip archive to a location in your filesystem.

We suggest placing the directory in the **C:\\SimCenter** folder. Once here, you can create a shortcut to the application (|app|.exe) and move this shortcut to your Desktop. 

Once the installation procedure has been completed, it is a good practice to run some basic checks. Navigate to the location where you placed the application and open it by running the |short tool id|.exe executable. You should see the user interface shown in |figUI|. The installation can be tested by running the example problem |test example| which is provided with the installation.

.. note::

   SimCenter apps are code-signed and notarized, but because they are not downloaded from the operating system's app store, they may not be recognized as such. As a consequence, depending on your security settings, when you start a SimCenter app for the first time, your operating system may bring up a dialog box indicating it is unsafe. If this dialog should appear, hit the cancel button. Restart the app by right clicking on it and selecting open.

.. _figUI-Hydro:

   .. figure:: figures/H20Download.png
      :align: center
      :figclass: align-center

      HydroUQ tool on startup.


MacOS
========



Preferences
===============

.. note::

   When the |app| is running, open the File/Preferences and make sure that python3 appears under **External Applications:Python**. If you used older versions of SimCenter tools this was not the default.