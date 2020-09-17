.. _lblBuildingApp:

Building Applications
=====================


The **building application** creates BIM (building information model) files for each simulation. It takes as input the range of building IDs selected for simulation (expressed as "min" and "max" ID, specified in the :ref:`configuration file <lblUserDefInputs>`) and the building-specific parameters for each simulation (specified in the :ref:`building source file <lblUserDefInputs>`).
The inputs are parsed into a dictionary in separate JSON files, labeled as "#-BIM.json", in the **results** folder.

The following options for building applications vary in the file type of the input building source file it processes.



.. jsonschema:: App_Schema.json#/properties/BuildingApplications/CSV_to_BIM


..
    .. jsonschema:: quoFEM_Schema.json
