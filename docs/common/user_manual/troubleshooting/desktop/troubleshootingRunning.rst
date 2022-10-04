.. _troubleshootingRunning:

Issues While Running
--------------------

Common causes of failure include incorrect setup, non-functioning or poorly functioning websites, user error, and possible bugs in the software. To discover the errors, it is useful to understand how the user interface (UI) and the backend work when the user submits to run a job. A number of things occur when the Submit button is clicked:

#. The UI creates a ``tmp.SimCenter`` folder in the working directory and later creates a ``templatedir`` within tmp.SimCenter.
#. The UI then iterates through all the input panels and the selected workflow applications place the files they need for the computation into the ``templatedir`` directory.
#. A Python script is run from this ``templatedir`` directory that manages the simulation workflow. Regional simulations use rWHALE.py, individual building assessments use sWHALE.py. rWHALE can be imagined as a wrapper that calls sWHALE for every asset in a regional simulation.
# If the workflow requires structural response simulation, the uncertainty propagation in the corresponding simulation is handled by the selected UQ Engine (e.g., Dakota). The workflow script creates an input file for the UQ Engine (e.g., ``dakota.in``) and places it in the ``tmp.SimCenter`` folder.
#. The response simulation is run in the workflow by the UQ engine using the input file created earlier.
#. The UQ engine creates one workdir folder in ``tmp.SimCenter`` for each realization of the structural response.
#. After all realizations have been generated, the UQ engine extracts the required outputs from the workdirs and prepares result files in the ``tmp.SimCenter`` folder.
#. These result files are then processed by the front-end and presented to the user in the **RES** tab of the desktop application.


The following is a list of issues we have observed when the user interface informs the user of a failure and steps you can take to fix them:

#.  **Could not create working dir**: The user does not have permission to create the ``tmp.SimCenter`` folder in the working directory. Change the **Local Jobs Directory** and the **Remote Jobs Directory** in the application's **Preferences** menu option.

#. **No Script File**: The application cannot find the main Python scripts (rWHALE.py, sWHALE.py, or qWHALE.py) that run the workflow using our backend engine. You might have changed the Local Applications directory location in Preferences, or modified the applications folder that accompanies the installation. Make sure the Local Applications points to the correct directory location. If that does not help, re-install the tool to fix a corrupted applications folder.

#. **Dakota failed to finish**: The simulation requested from the UQ Engine terminated before completion. This can occur for a number of reasons. Go to the ``tmp.SimCenter`` folder and look for the ``dakota.err`` file. If no file exists then the UQ Engine did not even start. If the file exists look at its contents to learn more about the errors.

   #. **No dakota.err file and no dakota.in file**: the Python script in ``templatedir`` failed to create the files required to start the UQ Engine. Take a look at the workflow log file in the ``tmp.SimCenter`` folder to see if it shows any errors. These errors typically point to an incorrect setting in your input file. If no workflow log file exists, the Python script managing the workflow failed to start. This is typically caused by an issue with your Python installation. Make sure you've followed the instructions in the Installation guide and set up your Python environment properly.

   #. **No dakota.err but dakota.in exists**: Even though the required files are available, the UQ Engine failed to start. If Dakota was selected as the UQ Engine, check the Dakota installation. Also make sure you've followed the instructions in the Installation guide and set up your Python environment properly.

   #. **dakota.err file exists but it is empty**: This means that the UQ Engine started successfully, but there was a problem during the simulation. Go to one of the ``workdir`` folders that contain individual realizations. You can run that simulation using the workflow driver file. Run the driver file from the command line to see what errors are generated during the simulation. These errors are typically related to the event or structural model description.

   #. **dakota.err file exists**: Open the file and see what the error is.  For example, if it says **Error: at least one variable must be specified.** This means no random variables have been specified. You have only one deterministic event or you have not specified any random variables for the analysis. Do not hesitate to reach out to the developers through the |messageBoard| if you do not understand the error messages in this file.

#. **You ran remotely at DesignSafe and no dakota.out files come back**: Go to your data depot folder at DesignSafe using your browser. Go to archive/jobs and use the job number from the table that pops up when you ask to get the job results from DesignSafe. Study both the ``.err`` and ``.out`` files in that directory for information on what went wrong.

#. **No results and you used the Site Response to create the event**. You must run a simulated event in the Site Response Widget before you can submit a job to run.


If the problems persist please post them on the |messageBoard|
