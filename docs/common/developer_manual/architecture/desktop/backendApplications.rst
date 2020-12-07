.. _lblbackendApps:

*********************
Backend Applications
*********************

.. note:: **Abbreviations**

   #. **BIM** = Building Information Model
   #. **DL** = Damage and Loss
   #. **EDP** = Engineering Demand Parameter
   #. **GM** = Ground Motion (of earthquake hazard)
   #. **IM** = Intensity Measure (of hazard event)
   #. **SAM** = Structural Analysis Model (i. e. finite element model)
   #. **SIM** = Simulation
   #. **UQ** = Uncertainty Quantification



This section broadly applies to all of the SimCenter's computational applications - quoFEM, EE-UQ, WE-UQ, Hydro-UQ, PBE, and RDT - which are run on a standardized workflow composed of the same set of backend applications. The backend applications are categorized by function into the following workflow **component applications** which create and populate *intermediate files* used to propagate information from one component application to the next. The component applications and their intermediate files are as follows:

   #. **Building Applications** - creates the BIM files for every building asset, containing building properties.
   #. **Regional Mapping Applications** - maps an IM or time series for the hazard event to each building asset site.
   #. **Event Applications** - creates the EVENT files for every building asset, containing loads corresponding to the hazard event(s).
   #. **Modeling Applications** - creates the SAM files for every building asset, containing structural model parameters.
   #. **EDP Applications** - creates the EDP files for every building asset, containing expected response outputs of the structural model.
   #. **Simulation Applications** - creates the SIM files for every building asset, containing analysis settings for response simulation.
   #. **UQ Applications** - executes all steps in the workflow, with the option to quantify uncertainty with experiments using random variables.
   #. **DL Applications** - estimates expected damages and losses from the EDP output.

These applications make up the "backbone" of SimCenter workflow systems, with each one calling on a different subset of the component applications. The component applications corresponding to each SimCenter workflow system is illustrated in :numref:`figFramework`.

.. figure:: figures/SimCenterFramework.png
   :name: figFramework
   :align: center
   :width: 1000
   :figclass: align-center

   SimCenter Software Framework


Reading the Log File
--------------------

The sequence of tasks carried out by the backend applications is outlined in the **log file** produced by the workflow. For :ref:`local runs <lblrunLocal>`, this log is displayed in the command terminal and is reproduced as "log.txt" in the **results** folder. For :ref:`remote runs <lblrunRemote>` through Tapis, this log file is called "launcher.out" in the job archive folder on DesignSafe. This guide will explain how to understand the statements printed in the log file.


The following is an example log file for a successful workflow run. The workflow can be broken down into the following sections:

I. **Reading the configuration file.** At the start of the workflow, the workflow settings specified in the configuration file are parsed. *Note that if a particular component application is excluded from the configuration file, then it is automatically skipped in the workflow.*

    - **lines 12-13**: Identifies the path to the :ref:`configuration file <lblUserDefInputs>`, which specifies the job details, and the *application registry file*, which specifies all available applications.

    - **line 16-62**: Reads the application registry file and displays all available applications.

    - **line 64-85**: Reads the configuration file and displays the units, local application directory, remote application directory, reference directory, and the applications chosen for each workflow step. Any workflow steps which are skipped (excluded from the configuration file) are also listed here.

II. **Pre-processing building and event data.** The workflow completes a one-time step of setting up BIM files for each building asset and assigning events to each building site.

    - **line 93**: Python command for executing the :ref:`Building <lblBuildingApp>` application, creating the BIM files for each building asset.

        ::

            python "C:/rWHALE/applications/createBIM/CSV_to_BIM/CSV_to_BIM.py" "--buildingFile" "C:/rWHALE/earthquake_example/results/buildings1-2.json" "--Min" "1" "--Max" "2" "--buildingSourceFile" "C:/rWHALE/earthquake_example/input_data/input_params.csv" "--getRV"


    - **line 103**: Python command for executing the :ref:`RegionalMapping <lblRegionalMapApp>` application, assigning events to each of the building assets.

        ::

            python "C:/rWHALE/applications/performRegionalMapping/NearestNeighborEvents/NNE.py" "--buildingFile" "C:/rWHALE/earthquake_example/results/buildings1-2.json" "--filenameEVENTgrid" "C:/rWHALE/earthquake_example/input_data/records/EventGrid.csv" "--samples" "2" "--neighbors" "1"


III. **Setting up and running simulations for each building asset.** From here, the workflow begins its iterative processes (usually parallelized) of running simulations for each building asset. The workflow runs two passes for each building asset: the supporting simulation files are set up in the first pass, and the workflow commands are executed in the second pass.

    - **line 111**: Starts with the first building asset. In this first pass, the EVENT, SAM, EDP, SIM files corresponding to "1-BIM.json" are created.

    - **line 118**: Python command for executing the :ref:`Event <lblEventApp>` application, creating the EVENT file for the building asset.

        ::

            python "C:/rWHALE/applications/createEVENT/SimCenterEvent/SimCenterEvent.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--pathEventData" "C:/rWHALE/earthquake_example/input_data/records/" "--getRV"


    - **line 126**: Python command for executing the :ref:`Modeling <lblModelingApp>` application, creating the SAM file for the built  asset.

        ::

            python "C:/rWHALE/applications/createSAM/openSeesPyInput/OpenSeesPyInput.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--filenameSAM" "SAM.json" "--mainScript" "cantilever.py" "--modelPath" "C:/rWHALE/earthquake_example/input_data/model/" "--ndm" "3" "--dofMap" "1,2,3" "--getRV"


    - **line 134**: Python command for executing the :ref:`EDP <lblEDPApp>` application, creating the EDP file for the building asset.

        ::

            python "C:/rWHALE/applications/createEDP/userEDP_R/UserDefinedEDP.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--filenameSAM" "SAM.json" "--filenameEDP" "EDP.json" "--EDPspecs" "C:/rWHALE/earthquake_example/input_data/EDP_specs.json" "--getRV"


    - **line 142**: Python command for executing the :ref:`Simulation <lblSimulationApp>` application, creating the SIM file for the building asset.

        ::

            python "C:/rWHALE/applications/performSIMULATION/openSeesPy/OpenSeesPySimulation.py" "--filenameBIM" "1-BIM.json" "--filenameSAM" "SAM.json" "--filenameEVENT" "EVENT.json" "--filenameEDP" "EDP.json" "--filenameSIM" "SIM.json" "--getRV"


    - **lines 153-157**: Commands which are written to the *workflow driver file*. In a "second pass" through the workflow, these commands are executed by running the workflow driver file.

        ::

            python "C:/rWHALE/applications/createBIM/CSV_to_BIM/CSV_to_BIM.py" "--buildingFile" "C:/rWHALE/earthquake_example/results/buildings1-2.json" "--Min" "1" "--Max" "2" "--buildingSourceFile" "C:/rWHALE/earthquake_example/input_data/input_params.csv"
            python "C:/rWHALE/applications/createEVENT/SimCenterEvent/SimCenterEvent.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--pathEventData" "C:/rWHALE/earthquake_example/input_data/records/"
            python "C:/rWHALE/applications/createSAM/openSeesPyInput/OpenSeesPyInput.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--filenameSAM" "SAM.json" "--mainScript" "cantilever.py" "--modelPath" "C:/rWHALE/earthquake_example/input_data/model/" "--ndm" "3" "--dofMap" "1,2,3"
            python "C:/rWHALE/applications/createEDP/userEDP_R/UserDefinedEDP.py" "--filenameBIM" "1-BIM.json" "--filenameEVENT" "EVENT.json" "--filenameSAM" "SAM.json" "--filenameEDP" "EDP.json" "--EDPspecs" "C:/rWHALE/earthquake_example/input_data/EDP_specs.json"
            python "C:/rWHALE/applications/performSIMULATION/openSeesPy/OpenSeesPySimulation.py" "--filenameBIM" "1-BIM.json" "--filenameSAM" "SAM.json" "--filenameEVENT" "EVENT.json" "--filenameEDP" "EDP.json" "--filenameSIM" "SIM.json"


    - **line 165**: Python command for executing the :ref:`UQ <lblUQApp>` application, which executes the commands in the workflow driver file to sample random variables and perform the response simulation. This command creates the EDP output file for the building asset.

        ::

            python "C:/rWHALE/applications/performUQ/dakota/DakotaFEM.py" "--filenameBIM" "1-BIM.json" "--filenameSAM" "SAM.json" "--filenameEVENT" "EVENT.json" "--filenameEDP" "EDP.json" "--filenameSIM" "SIM.json" "--driverFile" "driver" "--method" "LHS" "--samples" "2" "--type" "UQ" "--concurrency" "1" "--keepSamples" "True" "--runType" "run"


    - **line 189**: dakota command which calls on DAKOTA to execute the UQ application.

        ::

            running Dakota:  dakota -input dakota.in -output dakota.out -error dakota.err


    - **line 198**: Python command for executing the :ref:`DL <lblDLApp>` application, which outputs the DM.csv and DV.csv for the building asset.

        ::

            python "C:/rWHALE/applications/performDL/pelicun/DL_calculation.py" "--filenameDL" "1-BIM.json" "--filenameEDP" "response.csv" "--outputEDP" "EDP.csv" "--outputDM" "DM.csv" "--outputDV" "DV.csv" "--DL_Method" "HAZUS MH EQ" "--Realizations" "2" "--detailed_results" "False" "--log_file" "True" "--coupled_EDP" "True" "--event_time" "off" "--ground_failure" "False"


    - **line 213**: Continues to the second building asset ("2-BIM.json") and repeats the same workflow steps.


IV. **Aggregate outputs for all building assets.** After iterating through simulations, the workflow aggregates the content of individual EDP.csv, DM.csv, and DV.csv results for every building asset into single output summary files (see :ref:`Outputs <lblOutputs>`).

    - **line 315**: Aggregates results to create the EDP, DM, and DV output files.

        ::

            -----------------------------------------------------------
            Collecting damage and loss results
            Damage and loss results collected successfully.
            -----------------------------------------------------------


The full log file is shown below:

.. literalinclude:: files/log.txt
    :linenos:
    :emphasize-lines: 12,13,16,64,93,103,111,118,126,134,142,153,154,155,156,157,165,189,198,213,315



The procedure in the log file is visualized in :numref:`figBackendApps`:
    - User-provided input files are shown in orange.
    - Component applications are shown in blue. File dependencies for each component application are shown with arrows.
    - Intermediate files produced by the workflow to propagate data is shown in grey.
    - Output files provided to the user are shown in green.
    - Within the parallelized workflow for running each building asset simulation, two passes through the component applications are illustrated: the first pass in setting up the intermediate files (in red), then the second pass of executing the simulation and producing output results (in green).

.. figure:: figures/backendapps.png
   :name: figBackendApps
   :align: center
   :figclass: align-center

   Diagram of backend applications workflow.


The following pages provide more detail on the requirements for input files and types of backend applications available.


.. toctree::
   :maxdepth: 1

   buildingApps
   regionalMapApps
   eventApps
   modelingApps
   EDPApps
   simulationApps
   UQApps
   DLApps
