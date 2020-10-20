.. _lblearthquakeAssessment:


*********************
Earthquake Assessment
*********************

This example is a small-scale regional earthquake risk assessment which performs response simulation and damage/loss estimation for a group of 20 buildings. The buildings are modeled as elastic-perfectly plastic single-degree-of-freedom (SDOF) systems defined by three input model parameters: the weight ``W``, yield strength ``f_yield``, and fundamental period ``T1``. The buildings are distributed in space in a 4x5 grid, within a 3x3 grid of event sites. At each event site, 5 ground motion records of similar intensity are assigned.

.. _figContext:

.. figure:: figures/regionalearthquakeexample.png
   :align: center
   :figclass: align-center


Inputs
==========

The configuration file specifies all simulation settings, including the application types, input file names, units, and type of outputs. The configuration file can be downloaded here: :download:`rWHALE_config.json <files/rWHALE_config.json>`

.. literalinclude:: files/rWHALE_config.json
   :language: python

:ref:`Building Application <lblBuildingApp>`: This example uses the **CSV_to_BIM** building application. In the configuration file, the Max and Min parameters are set to run the full set of 20 buildings, and the name of the building source file is provided as "input_params.csv". In the :ref:`building source file <lblUserDefInputs>`, input parameters for the response simulation and DL assessment are specified. The building source file can be downloaded here: :download:`input_params.csv <files/input_params.csv>`

.. csv-table:: input_params.csv
   :file: files/input_params.csv
   :header-rows: 1
   :align: center

:ref:`Regional Mapping Application <lblregionalMapApp>`: This example uses the **NearestNeighborEvents** regional mapping application. The algorithm is set to randomly select 5 samples of ground motion records from the 4 nearest neighbors for each building asset.

.. _figContext:

.. figure:: figures/regionalearthquakeexample_annot.png
   :align: center
   :figclass: align-center

:ref:`Event Application <lblEventApp>`: This example uses the **SimCenterEvents** event application. It takes as input the EventGrid.csv, event files with the ground motion intensity measures, and the site files which specify the five ground motions assigned to each event site. 

.. csv-table:: EventGrid.csv
   :file: files/EventGrid.csv
   :header-rows: 1
   :align: center


.. csv-table:: site0.csv
   :file: files/site0.csv
   :header-rows: 1
   :align: center

:ref:`Modeling Application <lblModelingApp>`: This example uses the **OpenSeesPyInput** modeling application. The buildings are modeled as elastic-perfectly plastic single-degree-of-freedom (SDOF) systems defined by three input model parameters: the weight ``W``, yield strength ``f_yield``, and fundamental period ``T1``. Functions are included which record the peak response as EDPs for each of the EDP types specified in the EDP_specs.json file. The model file can be downloaded here: :download:`cantilever.py <files/cantilever.py>`

.. literalinclude:: files/cantilever.py
   :language: python

:ref:`EDP Application <lblEDPApp>`: This example uses the **UserDefinedEDP** EDP application. Custom EDPs are specified in the EDP specifications file. The EDP types are peak interstory drift (PID) and peak floor acceleration (PFA), recorded at the base and top node of the structural model in two horizontal directions (1,2). The EDP specifications file can be downloaded here: :download:`EDP_specs.json <files/EDP_specs.json>`

.. literalinclude:: files/EDP_specs.json
   :language: python

:ref:`Simulation Application <lblSimulationApp>`: This example uses the **OpenSeesPySimulation** simulation application, which corresponds to the **OpenSeesPyInput** modeling application. It reads the ``build_model`` and ``run_analysis`` functions from the model file to perform the response simulation.

:ref:`UQ Application <lblUQApp>`: This example uses the **Dakota-UQ** UQ application.

:ref:`DL Application <lblDLApp>`: This example uses the **pelicun** DL application. From the :ref:`building source file <lblUserDefInputs>`, it uses input parameters, such as building occupancy class, number of stories, floor plan area, and construction year, to produce estimates of damage states and losses based on the HAZUS assessment method.

Outputs
==========

.. csv-table:: EDP_1-19.csv
   :file: files/EDP_1-19.csv
   :header-rows: 1
   :align: center


.. csv-table:: DM_1-19.csv
   :file: files/DM_1-19.csv
   :header-rows: 1
   :align: center


.. csv-table:: DV_1-19.csv
   :file: files/DV_1-19.csv
   :header-rows: 1
   :align: center
