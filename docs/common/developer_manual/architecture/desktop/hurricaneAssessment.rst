.. _lblhurricaneAssessment:


*********************
Hurricane Assessment
*********************

This example is a small-scale regional hurricane risk assessment which performs damage/loss estimation for a group of 65 residential wood buildings. The buildings are subject to two types of hazards: wind, measured by peak wind speed (PWS), and flooding, measured by flood water depth (FWD). This example does not use response simulation; rather, an **IMasEDP** application translates the IMs directly to the DL application and uses IM-based component fragility functions to estimate damage.
The distribution of the buildings' structural types and stories are illustrated below.

.. _figContext:

.. figure:: figures/hurricaneeexample.png
   :align: center
   :figclass: align-center


Inputs
==========

The example input files can be downloaded here: :download:`input_data_hu.zip <files/input_data_hu.zip>`. For more information about required input files, refer to :ref:`Inputs <lblUserDefInputs>`.


1. **Configuration file**: The configuration file specifies all simulation settings, including the application types, input file names, units, and type of outputs.

.. literalinclude:: files/rWHALE_config_hu.json
   :language: python
   :linenos:

2. **Building Application**: This example uses the :ref:`CSV_to_BIM <lblBuildingApp>` building application. In the configuration file, the Max and Min parameters are set to run the full set of 65 buildings, and the name of the building source file is provided as "input_params.csv". In the :ref:`building source file <lblUserDefInputs>`, input parameters for the DL assessment (``stories``, ``yearbuilt``, ``occupancy``, ``structure``, ``areafootprint``, ``replacementCost``) are specified.

**Building source file:**

.. csv-table:: input_params_hu.csv
   :file: files/input_params_hu.csv
   :header-rows: 1
   :align: center

3. **Regional Mapping Application**: This example uses the :ref:`NearestNeighborEvents <lblregionalMapApp>` regional mapping application. From the parameters set in the configuration file, the algorithm is set to randomly select 10 samples of wind/flooding IMs from the 4 nearest neighbors for each building asset.



4. **Event Application**: This example uses the :ref:`SimCenterEvents <lblEventApp>` event application. It takes as input the EventGrid.csv, event files with the ground motion intensity measures, and the site files which specify the five ground motions assigned to each event site.

**Event grid file:**

.. csv-table:: EventGrid.csv
   :file: files/EventGrid.csv
   :header-rows: 1
   :align: center

**Site file:**

.. csv-table:: site0.csv
   :file: files/site0.csv
   :header-rows: 1
   :align: center


5. **Modeling Application**: This example uses the :ref:`OpenSeesPyInput <lblModelingApp>` modeling application. The buildings are modeled as elastic-perfectly plastic single-degree-of-freedom (SDOF) systems defined by three input model parameters: the weight ``W``, yield strength ``f_yield``, and fundamental period ``T1``. Functions are included which record the peak response as EDPs for each of the EDP types specified in the EDP_specs.json file.

**Model file:**

.. literalinclude:: files/cantilever.py
   :language: python
   :linenos:

6. **EDP Application**: This example uses the :ref:`UserDefinedEDP <lblEDPApp>` EDP application. Custom EDPs are specified in the EDP specifications file. The EDP types are peak interstory drift (PID) and peak floor acceleration (PFA), recorded at the base and top node of the structural model in two horizontal directions (1,2).

**EDP specifications file:**

.. literalinclude:: files/EDP_specs.json
   :language: python
   :linenos:

7. **Simulation Application**: This example uses the :ref:`OpenSeesPySimulation <lblSimulationApp>` simulation application, which corresponds to the **OpenSeesPyInput** modeling application. It reads the ``build_model`` and ``run_analysis`` functions from the model file to perform the response simulation.



8. **UQ Application**: This example uses the :ref:`Dakota-UQ <lblUQApp>` UQ application to execute the workflow.



9. **DL Application**: This example uses the :ref:`pelicun <lblDLApp>` DL application. From the :ref:`building source file <lblUserDefInputs>`, it uses input parameters, such as building occupancy class, number of stories, floor plan area, and construction year, to produce estimates of damage states and losses based on the HAZUS assessment method.



Outputs
==========

The example output files can be downloaded here: :download:`output_data_eq.zip <files/output_data_eq.zip>`. For more information about the output files produced, refer to :ref:`Outputs <lblOutputs>`.

1. **EDP_1-19.csv**: reports statistics on the EDP results from simulating 5 ground motions for each building asset. The statistics reported are the median and lognormal standard deviation of peak interstory drift (PID) and peak floor acceleration (PFA) in two directions.

.. csv-table:: EDP_1-19.csv
   :file: files/EDP_1-19.csv
   :header-rows: 1
   :align: center


2. **DM_1-19.csv**: reports collapse probability and damage state probability for each building asset.

.. csv-table:: DM_1-19.csv
   :file: files/DM_1-19.csv
   :header-rows: 1
   :align: center


2. **DV_1-19.csv**: reports decision variable estimates (repair cost, repair time, injuries) for each building asset.

.. csv-table:: DV_1-19.csv
   :file: files/DV_1-19.csv
   :header-rows: 1
   :align: center
