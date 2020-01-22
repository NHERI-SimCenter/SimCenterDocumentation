.. _lbl-downloadApp:

Download the Application
========================

To download the |app| application navigate to |appLink| 
the |short tool name| page}. As shown in \Cref{fig:app_choose_file}, this will bring you to another page which contains a list of downloadable files and directories. There are at least four files available for download from this page: 

    1. The PDF file is the User Manual that you are reading now.
    2. The MOV file is an video that provides an introduction to the usage of the application.
    3. The ZIP file is an archive that contains the application files for a Windows operating system.
    4. The DMG file is an archive that contains the application files for a Mac OS X operating system.


To download the |app| application click on the link for the appropriate file for your operating system and then 
click on the ``Download`` button at bottom right corner of the ensuing pop-up window. Unpackage the application 
from the downloaded file and place it in a location on your filesystem. On Windows, we
recommend that you create a **C:/SimCenter/** directory and extract the contents of the **ZIP** archive
there. It is also recommended to run the included installer for Visual C/C++ runtime library(vc\_redist.x64.exe).
If you use a Mac we recommend you copy the application to either your **Applications** or your **Desktop** folder. 

.. note: 

   You are free to place the applications anywhere you wish, you will need to make the
appropriate adjustments with the following instructions if you do so.

Now test that the application starts. To do this navigate to
the location where you placed the application and open it. You should
see the user interface (UI) shown in :numref:`fig:app_UI` after
starting the application. Now ``Quit`` the application. Additional installtion steps are required before 
computations can be performed.

.. _fig-generic-ui:

.. only:: PBE_app

   .. figure:: figures/PBE.png
	:align: center
	:figclass: align-center

	PBE Application on Startup

.. only:: EEUQ_app

   .. figure:: figures/EE-UQ.png
	:align: center
	:figclass: align-center

	EE-UQ Application on Startup

.. only:: WEUQ_app

   .. figure:: figures/WE-UQ.png
	:align: center
	:figclass: align-center

	WE-UQ Application on Startup


.. notes::
   The SimCenter is not recognized as either a Windows or an Apple vendor. Our applications are not recognized by the operating system as being signed. Consequently, you may receive a warning message when you start the |short tool name| application for the first time.

   On a Mac you will need to right click on the .dmg file to open it. The UI will not start correctly while in the DMG file, you need to open the .dmg file and then copy the |short tool name| application to your Documents or Desktop folder. You can then move the .dmg file to the trash or eject it after this has been done.

   The |short tool name| application requires additional software outlined in next subsections to work properly. Even if the application starts correctly, it will not run the simulations until these software, outlined in the next section, are installed.


