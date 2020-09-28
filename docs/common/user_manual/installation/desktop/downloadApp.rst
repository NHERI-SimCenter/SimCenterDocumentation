.. _lblDownloadApp:

Download the Application
========================


To download the |app|, first navigate to the |appLink| page. As shown in |figDownload|, from the application page you must click on the link ``Download app and User Manual`` which will bring you to another page. This page contains a list of downloadable files and directories. There are at least two files available for download from this page: 

1. The ZIP file is an archive that contains the application files for a Windows operating system.
2. The DMG file is an archive that contains the application files for a Mac OS X operating system.

.. only:: PBE_app

   .. _figDownloadPBE:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center

      PBE download page.

.. only:: EEUQ_app

   .. _figDownloadEE:

   .. figure:: figures/eeDownload.png
      :align: center
      :figclass: align-center

      EE-UQ download page.

.. only:: WEUQ_app

   .. _figDownloadWE:

   .. figure:: figures/weDownload.png
      :align: center
      :figclass: align-center

      WE-UQ download page.


.. only:: quoFEM_app

   .. _figDownloadQUO_FEM:

   .. figure:: figures/quoFEMDownload.png
      :align: center
      :figclass: align-center

      quoFEM download page.
To download the |app| click on the link for the appropriate file for your operating system: file ending with **Windows_Download.zip** for users on a Windows machine and file ending with **Mac_Download.dmg** for users on a Mac. This will bring up a pop-up window. Click on the **Download** button in bottom right hand corner of this pop-up. Unpackage the ensuing downloaded file and place it in a location on your filesystem. 

.. note::

   #. Windows: On computers running the Windows operating system we suggest placing the directory in the **C:\\SimCenter** folder. Once here, create a shorcut link to the application and move this shortcut link to your Desktop folder.
   #. MacOS: We sugget copying the app to your Desktop.

Now test that the application starts. To do this navigate to the location where you placed the application and open it. You should see the user interface (UI) shown in |figUI| after starting the application. Now quit the application. Additional installation steps, outlined in :numref:`lblDownloadOther`, are required before computations can be performed.

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

.. note::
   #. On a Mac you will need to right click on the .dmg file to open it. The UI will not start correctly while in the DMG file, you need to open the .dmg file and then copy the |short tool name| application to your Documents or Desktop folder. You can then move the .dmg file to the trash or eject it after this has been done.

   #. The SimCenter is not recognized as either a Windows or an Apple vendor. Our applications are not recognized by the operating system as being signed. Consequently, you may receive a warning message when you start the |short tool name| application for the first time. Follow the procedure you used in :numref:`lblDownloadOther` to remedy this issue.

The |short tool name| application requires an up to date version of Python, that outlined in :numref:`lblDownloadOther` to work properly. In :numref:`lblTestInstall`, instructions are given on testing the installation.



