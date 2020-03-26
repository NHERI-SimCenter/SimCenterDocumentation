.. _lblDownloadOtherWindows:

Windows Users
-------------

Python
^^^^^^

If you have not yet installed Python 3.7, we recommend installing Python 3.7 from 
`Python.org <https://www.python.org/downloads/windows>`_. We recommend installing using the 
**Windowsx86 64-bit executable installer**.  

.. note:

   allow the installer to change yur system envuronment variables so that the directory containing the executable is on your path.

.. warning:
   The latest version of Python is 3.8. At time of writing Python 3.8 was no working with the current pandas package.

Once Python is installed, you need to extend it by installing the following packages: **numpy**, **scipy**, and **pandas**. To install these packages, start a `terminal window as an Admin user <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>`_ and in that window type the following instructions:

.. :code-block:: python

      pip install numpy
      pip install scipy
      pip install pandas


Dakota
^^^^^^

|DakotaLink| is the default UQ engine used by the |app| that is publicily available from its |DakotaDownload|. The download page offers an extensive list of downloadable files. You can narrrow this down to the file to be selected by selecting **Windows** in the `Platform`, **6.10** in the `Release`, and **Command Line Only** for the `interface type`. In the `Public` area you should now only have a single option, click on the link to download |Dakota|. When you extract the files that you download, they will all be contained in a single folder, we suggest moving that folder to a `C:\SimCenter\dakota\` folder.




OpenSees
^^^^^^^^

|OpenSeesLink| is an open-source finite element application publicly available for download from its |OpenSeesDownload|.  OpenSees requires |Tcl| be installed to run. If you have never downloaded |OpenSees| before, you will need to register your e-mail to gain access. After registration, you can proceed to the download page by entering your email address and clicking the Submit button. The file to download is in the section `Windows Version`. Click on the link to download the file, extract it and place in a C:\SimCenter\OpenSees directory.

Modify the Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You now need to make some changes to your environment variables as neither OpenSees or Dakota includes an installer which typically performs this task.

1. Open the Start Search, type in “env”, and choose “Edit the system environment variables”
2. Click the ``Environment Variables…`` button at the bottom right of the application that pop up.
3. Now we are going to edit the  **PATH** variable. Select the Path variable row to highlight it and then press the ``Edit`` button.
4. to the variables value you want to **APPEND** the following:

.. :code-block:: none
   
   C:\SimCenter\OpenSees\bin;C:\SimCenter\dakota\bin

5. Press the ``OK`` button.
6. Now we are going to create a new variable, **PYTHONPATH** variable. Press the ``NEW`` button.
7. For the variable name enter: **PYTHONPATH**.
8. For the variable path enter

.. :code-block:: none
   C:\SimCenter\dakota\share\dakota\Python

9. Press the ``OK`` button.
10. Press now the `Apply`` button and exit the SystemProperties application


Test the Install of Python, OpenSees & Dakota
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps to Test:
   1. Open a command window window(type `cmd` in search)
   2. Type `python3` in the application that starts (this should bring up python interpreter)
   3. Enter the following to test the install of the modules and quit the application:
   
   .. :code-block:: python

      import numpy
      import scipy
      import pandas
      quit()

   4. Type `OpenSees` in the command window (this should bring up the OpenSees interpreter)

   5. Enter the following to exit this program:
   
   .. :code-block:: tcl

      exit

   6. Type `dakota` in the command window (this should start the dakota application which should give some error messages)
