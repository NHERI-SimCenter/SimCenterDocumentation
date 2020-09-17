.. _lblmodelingApp:

Modeling Applications
=====================

The **modeling application** creates SAM files which consolidate information on the building model assigned to each simulation.
It takes as input the BIM file created by the :ref:`Building Application <lblBuildingApp>`, the EVENT file created by the :ref:`Event Application <lblEventApp>`, and information on the structural model used for response simulation, specified in the :ref:`building source file <lblUserDefInputs>`.
The input structural model information is parsed into a "SAM.json" file, located in its corresponding **simulation working directory**.

The following options for modeling applications vary in the type of model and finite element program used for response simulation.
