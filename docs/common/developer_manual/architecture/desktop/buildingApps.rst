.. _lblBuildingApp:

Building Applications
=====================


The **building application** creates *building information model* (BIM) files for each building. It takes as input the range of asset IDs selected for simulation (expressed as "min" and "max" ID, specified in the :ref:`configuration file <lblUserDefInputs>`) and the building-specific parameters for each simulation (specified in the :ref:`building source file <lblUserDefInputs>`).
The inputs are parsed into "#-BIM.json" files in the **results** folder.

.. _figContext:

.. figure:: figures/backendapps_Building.png
   :align: center
   :figclass: align-center


The following options for building applications vary in the file type of the input building source file it processes.



.. jsonschema:: App_Schema.json#/properties/BuildingApplications/CSV_to_BIM

In the configuration file, **CSV_to_BIM** is called under "Applications" as:

.. code-block::

    "Building": {
      "Application": "CSV_to_BIM",
      "ApplicationData": {
        "Min": "1",
        "Max": "3",
        "buildingSourceFile":"input_params.csv"
      }
    }
