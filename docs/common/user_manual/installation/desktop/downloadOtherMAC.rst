.. _lblDownloadOtherMAC:

MacOS Users
-----------

Python
^^^^^^

The Mac comes with Python pre-installed, which is currently the somewhat 
dated version 2.7. We recommend installing Python 3.7 from `Python.org <https://www.python.org/downloads/mac-osx>`_ . We recommend installing using the 
**macOS 64-bit installer**. The installer will place a python3 executable in your /usr/local/bin directory, 
whose location should be on your system PATH.

Once Python is installed, you need to extend it by installing the following packages: **numpy**, **scipy**, and **pandas**. To install these packages, start a terminal window and type the following instructions:

.. code-block:: none

      pip3 install numpy
      pip3 install scipy
      pip3 install pandas

.. note:: 
   #. To start a terminal window you can use the spotlight app (magnifying glass at the top right corner of the desktop). Start the spotlight app and type in terminal. The terminal application should appear as the top hit. Click on it to start it.

   #. When the |app| is running, open the File/Preferences and make sure that python3 appears under **External Applications:Python**. If you used older versions of SimCenter tools this was not the default.


Dakota
^^^^^^

|DakotaLink| is the default UQ engine used by the |app| that is publicily available from its |DakotaDownload|. The download page offers an extensive list of downloadable files. You can narrrow this down to the file to be selected by selecting **MacOS** in the `Platform`, **6.10** in the `Release`, and **Command Line Only** for the `interface type`. In the `Public`
area you should now only have a single option, click on the link to download |Dakota|. When you extract the files that you download, they will all be contained in a single folder, we suggest moving that folder to your **bin** folder.

OpenSees
^^^^^^^^

|OpenSeesLink| is an open-source finite element application publicly available for download from its |OpenSeesDownload|.  OpenSees requires |Tcl| be installed to run. If you have never downloaded |OpenSees| before, you will need to register your e-mail to gain access. After registration, you can proceed to the download page by entering your email address and clicking the Submit button. The Mac download link is at the bottom of the download page, with the appropriate Tcl installer beside the |OpenSees| link; 

Steps to Install:
      1. Download the OpenSees executable .zip file, uncompress it and put it in a folder. We suggest placing it in the **bin** folder in your local home directory. Note depending on the applications you use this may require you creating the **bin** folder.
      2. Download and run the Tcl installer.

Edit Your .bashrc file
^^^^^^^^^^^^^^^^^^^^^^

Finally you want to edit your .bashrc file so that the applications will find |OpenSees| and |Dakota|. You need to add the
following lines to that file:

.. code:: none
   
   export PATH=$HOME/bin:$PATH
   export PATH=$HOME/bin/dakota-6.10.0/bin:$PATH
   export PYTHONPATH=$HOME/bin/dakota-6.10.0/share/dakota/Python


.. warning:: 
   Apple, in the latest release of their operating system, MacOS 10.16 Catalina, has changed the default working of Gatekeeper. Gatekeeper, first introduced in OS X Mountain Lion, is a Mac security feature that helps protect your Mac from Malware and other malicious software. Gatekeeper checks to make sure the application is safe to run by checking it against the list of apps that Apple has vetted and approved for the Apple Mac Store and/or approved by Apple even if not offered through the app store. In previous versions of MacOS, Gatekeeper had three security level options: App Store, App Store and Identified Developers, and Anywhere. Anywhere has been removed and this will cause problems with Dakota. As a consequence, it is necessary to follow the following when you update the MacOS or install Dakota for the first time on machine with an updated MacOS. From the terminal app, with the above .bashrc settings set, you need to type the following in the terminal window:

   .. code:: none

      	     sudo spctl --master-disable
      	     dakota
      	     sudo spctl --master-enable

   This will temporarily disable gatekeeper (basically setting Gatekeeper options to Anywhere), allow the Dakota application and it's .dylib files to be registered as safe, and then turn Gatekeeper options back to default.

Test the Install of Python, OpenSees & Dakota
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps to Test:
   1. Open a terminal windows (type `terminal` in spotlight search)
   2. Type `python3` (this should bring up python interpreter)
   3. Enter the following to test the install of the modules and quit the application:
   
   .. code:: python

      import numpy
      import scipy
      import pandas
      quit()

   4. Type `OpenSees` (this should bring up the OpenSees interpreter)

   5. Enter the following to exit this program:
   
   .. code:: tcl

      exit

   6. Type `dakota` (this should start the dakota application which should give some error messages)
