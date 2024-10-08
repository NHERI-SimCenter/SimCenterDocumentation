.. _lblrunLocal:

Run Locally on Your Desktop
===========================

Running applications locally on a personal desktop is convenient for small-scale jobs and debugging. For larger jobs, the applications are available on DesignSafe to utilize high-performance computing resources.

1. Follow the directions in :ref:`How to Build <lblHowtoBuild>` to install the backend applications on your local desktop. The applications needed to run the backend are in the **applications** folder after you have built the backend. You can leave the folder where you have built it (which is useful if you plan to keep updating the backend applications as we make changes to the github repository, or you can move the applications folder to a seperate directory (such as ``C:/rWHALE/``) if you don't plan to update these applications.

2. To run a workflow you first need to create a folder on your filesystem in which you will place the necessary inputs. In this folder you will need an input file that describes the workflow to run, say **input.json**, and a directory **input_data**.

3. Create the input file, ``input.json`` that outlines the workflow to run. You may use the example configuration file (:download:`input.json <files/input.json>`) as a template. There are 3 lines in this file that need changing to run the default workflow (Example1 in the R2DTool):

   .. code::

      "remoteAppDir": "/Users/fmckenna/NHERI/SimCenterBackendApplications",
      "localAppDir": "/Users/fmckenna/NHERI/SimCenterBackendApplications",
      "runDir": "/Users/fmckenna/Documents/R2D/LocalWorkDir/tmp.SimCenter"

   - Set ``'runDir'`` to the path containing the ``input_data`` folder. 
   - Set ``'localAppDir'`` and ``''remoteAppDir'`` to the path containing the applications folder (such as ``C:/rWHALE/``).
   - If you wish to change thw workflow that is run, you need to specify applications for each workflow step and their inputs. For more details on the format of the configuration file, see :ref:`Inputs <lblUserDefInputs>`.

      
4. In the ``input_data`` folder, you need to place the files needed by the applications which will run in the workflow. You may use this example input file set (:download:`input_data.zip <files/input_data.zip>`) as a template. Again, the downloaded default is for Example1 in R2D.


5. Now you are ready to run the Workflow. The workflow is run through the command window by calling on Python and specifying paths to the application files, input files, and desired location for the results folder. The following is the command to issue on the command line:

.. code-block::

    python <path to rWhale.py> <path to wfInput.json> --registry <path to WorkflowApplications.json> --referenceDir <path to input_data folder> -w <path to output results folder>

where:
    - **<path to R2D_workflow.py>** is the full path to the file "rWhale.py" in the **/applications/Workflow** folder
    - **<path to rWHALE_config.json>** is the full path to the workflow input file, ``input.json``
    - **<path to WorkflowApplications.json>** is the full path to the file ``WorkflowApplications.json`` in the **applications/Workflow** folder
    - **<path to input_data folder>** is the full path to the folder with all input files
    - **<path to output results folder>** is the full path to where a "results" folder will be created to contain the output files


.. note::

   If you are on a Mac, python in the above needs to be replaced by **python3**. 
   
6. A results folder is produced, which contains both the aggregated output files (EDP_{min id}_{max id}.csv, DM_{min id}_{max id}.csv, DV_{min id}_{max id}.csv), as well as the individual output files (EDP.csv, DM.csv, DV.csv) for each built asset in their respective folders.

::

   results
   ├── 1                            # folder for building asset 1
      ├── templatedir               # folder of template files
      ├── workdir.1                 # working directory for each event simulation
      ├── workdir.2
      ├── workdir.3
      .
      .
      .
      ├── dakota.err                # dakota files
      ├── dakota.in
      ├── dakota.out
      ├── DL_summary.csv            # damage/loss summary
      ├── DM.csv                    # individual building asset output files
      ├── DV.csv
      ├── EDP.csv
      └── response.csv
   ├── 2
   .
   .
   .
   ├── 1-BIM                       # BIM files for each building asset
   ├── 2-BIM
   .
   .
   .
   ├── DM_{min id}_{max id}.csv    # aggregated results
   ├── DV_{min id}_{max id}.csv
   ├── EDP_{min id}_{max id}.csv
   └── log.txt                     # log file
