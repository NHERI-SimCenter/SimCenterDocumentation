.. _troubleshootingRunning:

Issues While Running
--------------------

When running simulations, failures can occur due to various reasons such as incorrect setup, malfunctioning websites, user errors, or software bugs. Understanding the sequence of actions initiated by the user interface (UI) and backend upon job submission can aid in diagnosing issues. Here's what happens when the Submit button is clicked:

#. A temporary directory, ``tmp.SimCenter``, is created in the working directory, followed by a ``templatedir`` within it.
#. The UI processes all input panels, and workflow applications transfer necessary files to the ``templatedir``.
#. A Python script, specific to the simulation type (rWHALE.py for regional simulations, sWHALE.py for individual assessments), is executed from the ``templatedir``. rWHALE serves as a wrapper, invoking sWHALE for each asset in regional assessments.
#. For structural response simulations, uncertainty quantification is managed by the chosen UQ Engine (e.g., Dakota), which generates an input file (e.g., ``dakota.in``) placed in ``tmp.SimCenter``.
#. The UQ engine runs the response simulation using the earlier created input file.
#. For each structural response realization, the UQ engine creates a separate workdir folder within ``tmp.SimCenter``.
#. Upon completing all realizations, the UQ engine compiles the outputs from these folders into result files in ``tmp.SimCenter``.
#. Finally, the front-end processes these results, displaying them under the **RES** tab in the desktop application.

Below are common issues encountered during failures, along with troubleshooting steps:

#. **Could not create working dir**: Lack of permission to create the ``tmp.SimCenter`` folder. Adjust the **Local Jobs Directory** and **Remote Jobs Directory** in the **Preferences**.

#. **No Script File**: Missing main Python scripts (rWHALE.py, sWHALE.py, or qWHALE.py). Verify the Local Applications directory in **Preferences** points to the correct location. Reinstallation may be necessary if the applications folder is corrupted.

#. **Dakota failed to finish**: The simulation requested from the UQ Engine terminated before completion. This can occur for a number of reasons. Go to the ``tmp.SimCenter`` folder and look for the ``dakota.err`` file. If no file exists then the UQ Engine did not even start. If the file exists look at its contents to learn more about the errors.

   #. **No dakota.err file and no dakota.in file**: the Python script in ``templatedir`` failed to create the files required to start the UQ Engine. Take a look at the workflow log file in the ``tmp.SimCenter`` folder to see if it shows any errors. These errors typically point to an incorrect setting in your input file. If no workflow log file exists, the Python script managing the workflow failed to start. This is typically caused by an issue with your Python installation. Make sure you've followed the instructions in the Installation guide and set up your Python environment properly.

   #. **No dakota.err but dakota.in exists**: Even though the required files are available, the UQ Engine failed to start. If Dakota was selected as the UQ Engine, check the Dakota installation. Also, make sure you've followed the instructions in the Installation guide and set up your Python environment properly.

   #. **dakota.err file exists but it is empty**: This means that the UQ Engine started successfully, but there was a problem during the simulation. Go to one of the ``workdir`` folders that contain individual realizations. You can run that simulation using the workflow driver file. Run the driver file from the command line to see what errors are generated during the simulation. These errors are typically related to the event or structural model description.

   #. **dakota.err file exists**: Open the file and see what the error is.  For example, if it says **Error: at least one variable must be specified.** This means no random variables have been specified. You have only one deterministic event, or you have not specified any random variables for the analysis. Do not hesitate to reach out to the developers through the |messageBoard| if you do not understand the error messages in this file.

#. **You ran remotely at DesignSafe and no dakota.out files came back**: Go to your data depot folder at DesignSafe using your browser. Go to archive/jobs and use the job number from the table that pops up when you ask to get the job results from DesignSafe. Study both the ``.err`` and ``.out`` files in that directory for information on what went wrong.

#. **No results and you used the Site Response to create the event**. You must run a simulated event in the Site Response Widget before you can submit a job to run.


#. **Don't Like Default Screen Layout**. There are configuarion you can do for startup. In the directory in which the executable exists you can place a **config.json** file. At present the options are limited: You can set screen size of the application to be full screen, and you can set and change the size of the **output** window. A sample config .json file:

.. code-block::

   {
      "screenSize":"fullScreen",
      "outputLocation":{"position":"right","numPixels":500}
   }

.. note::

   You can also start the application from the terminal and pass config options. These options overwrite any existing.
   
   .. code-block
   
       application -screenSize fullScreen -helpLocation '{"position":"right","numPixels":400}'
   
For unresolved issues, please seek assistance on the |messageBoard|.
