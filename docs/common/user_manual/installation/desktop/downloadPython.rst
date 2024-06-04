.. _lblDownloadOther:

Install Python
==============

Install Python on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^

If you have not yet installed Python 3.7, we recommend installing Python 3.7 from 
`Python.org <https://www.python.org/downloads/windows>`_. We recommend installing using the 
**Windowsx86 64-bit executable installer**.  

.. note::

   Allow the installer to change your system environment variables so that the directory containing the executable is on your path. This requires checking the small box asking for this when the installer starts. The box is located at the bottom of the installer application window.

.. warning::
   The latest version of Python is 3.8.3 At the time of writing, Python 3.8.3 was not working with the current **numpy** package.

Once Python is installed, you need to extend it by installing the following packages: **numpy**, **scipy**, **tables**, **hdf5** and **pandas**. To install these packages, start a `terminal window as an Admin user <https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/>`_ and in that window type the following instructions:

.. code-block:: console

      pip install numpy
      pip install scipy
      pip install pandas
      pip install tables
      pip install hdf5

.. note::
   
   As an alternative, you can install the SimCenter's pelicun module, which will include all three of the above:

   .. code-block:: console

      pip install pelicun


Install Python on a Mac
^^^^^^^^^^^^^^^^^^^^^^^

The Mac comes with Python pre-installed, which is currently the outdated version 2.7. As of January 1st, 2020 no new bug reports, fixes, or changes will be made to Python 2, and Python 2 is officially no longer supported. SimCenter tools require Python 3. We recommend installing Python 3.7 from `Python.org <https://www.python.org/downloads/mac-osx>`_ using the 
**macOS 64-bit installer**. The installer will place a python3 executable in your /usr/local/bin directory, whose location should be on your system PATH. Version 3.8 does not appear to do so anymore, see the note below. 

.. note:: 
   
   #. We use the python.org installation over others, due to its simplicity of installation.
   #. In the current installation of Python it leaves two script files in a folder when the installation ends. You need to execute both script files to get Python set up correctly so that it can be invoked from the terminal. To execute the files, double-click on them. The two files, shown in the image below, are: ``Update Shell Profile.command.sh`` and ``Install CertificateCommand.sh``.

   .. figure:: figures/pythonInstallShell.png
      :align: center
      :figclass: align-center

      Python: Folder Displayed at Conclusion of Install

Once Python is installed, you need to extend it by installing the following packages: **numpy**, **scipy**, and **pandas**. To install these packages, start a terminal window and type the following instructions:

.. code-block:: python

      pip3 install numpy
      pip3 install scipy
      pip3 install pandas
      pip3 install tables
      pip3 install hdf5

.. note:: 

   #. To start a terminal window you can use the spotlight app (magnifying glass at the top right corner of the desktop). Start the spotlight app and type in the terminal. The terminal application should appear as the top hit. Click on it to start it.

   #. When the |app| is running, open the File/Preferences and make sure that python3 appears under **External Applications:Python**. If you used older versions of SimCenter tools this was not the default.

   #. As an alternative, you can install the SimCenter's pelicun module, which will include all three of the above

   .. code-block:: python

      pip3 install pelicun

.. note::

   If you forget to invoke the ``UpdateShellProfile.command.sh`` script at the end of the install, you can always edit the correct shell file later to update the ``PATH`` variable to point to the Python application.

   On Linux systems, the shell is the program that takes commands from the keyboard that you enter in the terminal window and passes them to the operating system to perform by invoking applications and passing data between applications. In the good old days, it was the only interface available to the user, i.e. there was no such thing as Finder! There are a number of shell programs that can be installed and made available to you. The most popular is the **bash** shell, and the up-and-coming one is the **Z** shell. Power MacOS users will write shell scripts to do many many useful things. By default, the applications that the shell program will invoke are limited to applications in a few specific directories that are defined in the user's ``PATH``. Users can modify this path by editing files that the shell program will read from every time the program is started.

  When the frontend application is running the computations it is actually running a backend application using the shell program. As a consequence the shell program must be made aware of the locations of some of the external applications that you have installed as **OpenSees** and **dakota** do not provide installers that automatically do this when they are installed. Other applications, like **Tcl** provide scripts that you invoke to do it. In short, you have to edit the file appropriate to the shell you are using.

  To find which shell program you are using when you issue commands inside the terminal window, type the following in a terminal window:

  .. code:: none
   
	env | grep SHELL

  If the result is **/bin/bash** you will need to edit the **.bashrc** file or the **bash_profile** file. If the result is **/bin/zsh** you will need to edit the **.zshrc** or **.zprofile**. Typically the **.bash_profile** or the **.zprofile** file is the one to edit as these typically by design will invoke the **.bashrc** or **.zshrc** file. If in doubt, look for these files in your home directory and see which of these other installlers have modified.



