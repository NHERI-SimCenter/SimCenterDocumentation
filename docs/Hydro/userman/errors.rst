.. _lbl-errors:

************************
Troubleshooting
************************

There can be two types of major issues, one during startup and other during the running of the program.

Startup Issues
--------------

On Windows operating systems, if you receive an error when starting the application with the message that MSVCP140.dll is missing. This is caused by a missing Visual C/C++ runtime library. You can fix this error by running the installer for the Visual C/C++ redistributable package **vc_redist.x64.exe**, which is included with the application.

Issues While Running
-----------------------

Common causes of failure include incorrect setup, non-functioning or poorly functioning websites, user error, and possible bugs in the software. To discover the errors, it is helpful to understand how the user interface and the backend work when the user submits to run a job. Several things occur when the Submit button is clicked:

#. The UI creates a folder in the working dir location specified called ``tmp.SimCenter`` and in that folder creates another folder called ``templatedir``.
#. The UI then iterates through all the widgets chosen. These widgets place all needed files for the computation into the ``templatedir`` directory.
#. A Python script is run in this ``templatedir`` directory that creates the UQ engine's input file. For example, using Dakota, the input file ``dakota.in`` is created and placed in the ``tmp.SimCenter`` folder.
#. The entire ``templatedir`` folder is sent to the TACC supercomputer. Here, the input dictionaries related to OpenFOAM are created, and the OpenFOAM event is run. 
#. Once the OpenFOAM event has been completed, the resulting forces on the buildings are calculated.
#. The UQ engine is then started and runs using the ``dakota.in`` input file.
#. As the UQ engine runs, it creates folders in ``tmp.SimCenter``, one folder for each deterministic run.
#. When completed, the UQ engine leaves the results files in the ``tmp.SimCenter`` folder.
#. The results files are then processed by the front-end and presented in the **RES** tab.

The following is a list of things that we have observed go wrong when the user interface informs the user of a failure and steps the user can take to fix the problem:

#.  **Could not create working dir**: The user does not have permission to create the ``tmp.SimCenter`` folder in the working dir location. Change the **Local Jobs Directory** and the **Remote Jobs Directory** in the application's **Preferences** menu option. 

#. **No Script File**: The user has changed the Local Applications directory location in Preferences, or the applications folder that accompanies the installation has been modified. Either set the correct directory location or re-install the tool.
#. **Dakota failed to finish**: This can occur for several reasons. Go to the ``tmp.SimCenter`` folder and look for the ``dakota.err`` file. If no file exists then, Dakota did not start. If the file exists, look at its contents to see if there are any errors.

   #. **No dakota.err file and no dakota.in file**: the Python script in ``templatedir`` failed to create the necessary files. Have a look at the workflow log file in the ``templatedir`` folder to see what the error is, as it could indicate an error in your input. If no workflow log file exists, it means Python failed to start. Check the installation of Python.

   #. **No dakota.err and dakota.in exists**: Dakota failed to run. Check installation of Dakota and Python. NOTE: Sometimes, if Python starts, it is not using the version of Python you specified in the environment variables when setting up Python. This is because many applications install their own version of Python. If Dakota is installed correctly, set the location of the Python executable in Preferences.

   #. **dakota.err file exists**: Open the file and see what the error is.  For example, if it says **Error: at least one variable must be specified.** This means no random variables have been set. You have only one deterministic event, or you have not set any random variables in the EDP.

   #. **dakota.err file exists but is empty**: This means that Dakota ran, but there was a problem with the simulation. Go to one of the ``workdir`` locations. There is a file workflow driver that can be run. Run it and see what the errors are.

   #. **You ran at DesignSafe and no dakota.out files come back**: Go to your data depot folder at DesignSafe using your browser. Go to archive/jobs and use the job number shown in table that pops up when you ask to get the job from DesignSafe. Study both the ``.err`` and ``.out`` files in that directory for a clues to as what went wrong.

If problems persists, please post them on the |messageBoard|

Other issues
----------------

Some of the other common tips and tricks for troubleshooting include:

**Know the objective**

Before starting the simulation, it is essential to understand the intended goal of the project. This will help set up appropriate inputs. ``Hydro-UQ`` workflows already helps with this to the best extent possible. Yet, the user's understanding of the physics is much necessary.

**Mesh quality**

Most often, the quality of the mesh can be the reason for the simulation failure. Check the mesh quality. ``Hydro-UQ`` has an in-built mesher, and we continue to optimize its performance. However, this is limited and might not serve the needs of advanced researchers. It is then recommended to use external meshing tools and directly import the mesh. If the tool you used for meshing is unavailable, please submit a feature request using :ref:`lblBugs`.

**Units**

Check that the units are consistent. The CFD event, ``EVT`` does not have specific units, but you need to ensure that the units provided need to be consistent.
