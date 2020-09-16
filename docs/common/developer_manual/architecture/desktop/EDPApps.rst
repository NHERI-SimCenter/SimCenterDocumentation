.. _lblEDPApp:

EDP Applications
================

The **EDP application** creates EDP files which specify the types of engineering demand parameters expected as output from the response simulation.
It takes as input the BIM file created by the :ref:`Building Application <lblBuildingApp>`, the EVENT file created by the :ref:`Event Application <lblEventApp>`, and the SAM file created by the :ref:`Modeling Application <lblModelingApp>`.
It writes the type, location, and direction (DOF) of each EDP for each simulation in an "EDP.json" file in its corresponding **simulation working directory**.

The following options for EDP applications vary in the type of EDPs identified for the simulation output.
