.. _lblDownloadApp:

Download the Application
========================


To download the |app| application navigate to |appLink| page. As shown in |figDownload|, from the application page you must click on the link ``Download app and User Manual`` which will bring you to another page. This page contains a list of downloadable files and directories. There are at least four files available for download from this page: 

1. The PDF file is the User Manual that you are reading now.
2. The MOV file is an video that provides an introduction to the usage of the application.
3. The ZIP file is an archive that contains the application files for a Windows operating system.
4. The DMG file is an archive that contains the application files for a Mac OS X operating system.

.. only:: PBE_app

   .. _figDownloadPBE:

   .. figure:: figures/pbeDownload.png
      :align: center
      :figclass: align-center

      PBE Download Page

.. only:: EEUQ_app

   .. _figDownloadEE:

   .. figure:: figures/eeDownload.png
      :align: center
      :figclass: align-center

      EE-UQ Download Page


.. only:: WEUQ_app

   .. _figDownloadWE:

   .. figure:: figures/weDownload.png
      :align: center
      :figclass: align-center

      WE-UQ Download Page


To download the |app| application click on the link for the appropriate file for your operating system. This will bring up a pop-up window. Click on the ``Download`` button in bottom right hand corner of this pop-up. Unpackage the ensuing downloaded file and place it in a location on your filesystem. 


.. note::

   1. On **Windows** we recommend that you create a **C:/SimCenter/** directory and extract the contents of the **ZIP** archive there. It is also recommended to run the included installer for Visual C/C++ runtime library(vc\_redist.x64.exe).

   2. If you use a **Mac** we recommend you copy the application to either your **~/Applications** folder or your **~/Desktop** folder. 

Now test that the application starts. To do this navigate to the location where you placed the application and open it. You should see the user interface (UI) shown in |figUI| after starting the application. Now ``Quit`` the application. Additional installtion steps, outlined in :numref:`lblDownloadOther`, are required before computations can be performed.

.. only:: PBE_app

   .. _figUI-PBE:

   .. figure:: figures/PBE.png
	:align: center
	:figclass: align-center

	PBE Application on Startup

.. only:: EEUQ_app

   .. _figUI-EE:

   .. figure:: figures/EE-UQ.png
	:align: center
	:figclass: align-center

	EE-UQ Application on Startup

.. only:: WEUQ_app

   .. _figUI-WE:

   .. figure:: figures/WE-UQ.png
	:align: center
	:figclass: align-center

	WE-UQ Application on Startup


.. note::
   The SimCenter is not recognized as either a Windows or an Apple vendor. Our applications are not recognized by the operating system as being signed. Consequently, you may receive a warning message when you start the |short tool name| application for the first time.

   On a Mac you will need to right click on the .dmg file to open it. The UI will not start correctly while in the DMG file, you need to open the .dmg file and then copy the |short tool name| application to your Documents or Desktop folder. You can then move the .dmg file to the trash or eject it after this has been done.

The |short tool name| application requires additional software outlined in next subsections to work properly. Even if the application starts correctly, it will not run the simulations until these other software packages, outlined in the next section, are installed.

