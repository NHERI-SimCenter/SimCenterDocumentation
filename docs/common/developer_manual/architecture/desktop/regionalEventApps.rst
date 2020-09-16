.. _lblRegionalEventApp:

Regional Event Applications
===========================

The **regional event application** selects events for each building site.
It writes event information in its corresponding building file (#-BIM.json), which was created by the :ref:`Building Application <lblBuildingApp>`, in the **results** folder.

The following options for regional event applications vary in the algorithm or method used to make the event assignment.

.. jsonschema:: App_Schema.json#/properties/RegionalEventApplications/NNE


..
    .. jsonschema:: quoFEM_Schema.json
