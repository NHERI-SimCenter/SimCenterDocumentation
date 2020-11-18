.. _lbltroubleshooting:

Troubleshooting Errors
===========================

If the workflow does not run successfully, the first and best method for troubleshooting is by reading error messages in the **log file**. For local runs, this log is displayed in the command terminal and is reproduced as "log.txt" in the **results** folder. For remote runs through Tapis, this log file is called "launcher.out" in the job archive folder on DesignSafe. This guide will explain how to understand the statements printed in the log file.

The following is an example log file for a successful workflow run.

    - **lines 12-13**: Identifies the path to the :ref:`configuration file <lblUserDefInputs>`, which specifies the job details, and the *application registry file*, which specifies all available applications.
    - **line 16**: Reads the application registry file and displays all available applications.
    - **line 64**: Reads the configuration file and displays the units, local application directory, remote application directory, reference directory, and the applications chosen for each workflow step. Any workflow steps which are skipped (excluded from the configuration file) are also listed here.
    - **line 93**: Python command for executing the :ref:`Building <lblBuildingApp>` application, creating the BIM files for each built asset.
    - **line 103**: Python command for executing the :ref:`RegionalMapping <lblRegionalMapApp>` application, assigning events to each of the built assets.
    - **line 111**: Starts with the first built asset ("1-BIM.json"). In this first pass, the supporting workflow output files are created, but the workflow is not executed yet.
    - **line 118**: Python command for executing the :ref:`Event <lblEventApp>` application, creating the EVENT file for the built asset.
    - **line 126**: Python command for executing the :ref:`Modeling <lblModelingApp>` application, creating the SAM file for the built asset.
    - **line 134**: Python command for executing the :ref:`EDP <lblEDPApp>` application, creating the EDP file for the built asset.
    - **line 142**: Python command for executing the :ref:`Simulation <lblSimulationApp>` application, creating the SIM file for the built asset.
    - **lines 153-157**: Commands which are written to the *workflow driver file*.
    - **line 165**: Python command for executing the :ref:`UQ <lblUQApp>` application, which executes the commands in the workflow driver file to sample random variables and perform the response simulation. This command outputs the EDP.csv for the built asset.
    - **line 189**: dakota command which calls on DAKOTA to execute the UQ application.
    - **line 198**: Python command for executing the :ref:`DL <lblDLApp>` application, which outputs the DM.csv and DV.csv for the built asset.
    - **line 213**: Continues to the second built asset ("2-BIM.json") and repeats the same workflow steps.
    - **line 315**: "Collects damage and loss results" by aggregating the content of EDP.csv, DM.csv, and DV.csv for every built asset into single output files (see :ref:`Outputs <lblOutputs>`).



.. literalinclude:: files/log.txt
    :linenos:
    :emphasize-lines: 12,13,16,64,93,103,111,118,126,134,142,153,154,155,156,157,165,189,198,213,315


For troubleshooting with the log file, the following steps are recommended:
    - **Identify which application failed in the workflow**. Read through the log file until an ERROR message appears after one of the Python commands.
    - **Verify that the paths to all workflow files are correct.** These paths are specified in the :ref:`initialization command <lblrunLocal>` when run locally, or in the :ref:`job script <lblrunRemote>` when run remotely.
    - **Check that the "ApplicationData" for each application in the configuration file are correct.** The workflow will fail if an application does not have all of its required application-specific inputs, or if inputs are provided with an incorrect data type. See the individual pages for the :ref:`Backend Applications <lblArchitecture>` for more details on application-specific inputs.
    - **Check that there are no JSON serialization errors in the configuration file.** Mistakes in unclosed brackets or incorrect indentation in the JSON file will cause errors.
    - **Check that the user-defined input files are in the correct format.** Mistakes in the header labels or formatting of CSV and JSON input files will cause errors.
    - **To view print messages in the model script during response simulation, rerun Dakota.** By default, any print messages in input files are suppressed in the log file. In order to view the messages and debug issues with the model script, navigate to the results folder for one of the built assets in the command window (i. e. "results/1"). You should find three files: dakota.in, dakota.err, and dakota.out. Running the following command will re-execute the UQ application for that particular built asset:

        ``dakota -input dakota.in -output dakota.out -error dakota.err``


If problems still persist, you are encouraged to read previously posted questions or post your own at `SimCenter Forum <https://simcenter-messageboard.designsafe-ci.org/smf/index.php>`_. A member of the SimCenter developer team will respond to your question on the platform. 
