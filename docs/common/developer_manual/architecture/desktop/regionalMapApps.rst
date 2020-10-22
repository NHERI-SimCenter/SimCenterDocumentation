.. _lblRegionalMapApp:

Regional Mapping Applications
=============================

The **regional mapping application** selects events for each building site.
The number of events is specified by the user in the :ref:`configuration file <lblUserDefInputs>` under "samples".
For the set of candidate events, :ref:`event files <lblUserDefInputs>` must be provided by the user in the **input_data/records** folder.
Once events are chosen, the application writes the name of the event file in its corresponding building file (:ref:`#-BIM.json <lblBuildingApp>`) in the **results** folder.

The following options for regional mapping applications vary in the algorithm or method used to make the event assignment.

.. jsonschema:: App_Schema.json#/properties/RegionalMapApplications/NNE
