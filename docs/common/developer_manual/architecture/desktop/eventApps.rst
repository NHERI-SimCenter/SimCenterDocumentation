.. _lblEventApp:

Event Applications
==================

The **event application** creates EVENT files which consolidate information on the events (earthquake, wind, hurricane, etc.) assigned to each simulation. It takes as input the BIM file created by the :ref:`Building Application <lblBuildingApp>` and JSON files corresponding to each event assigned to the building site.
The input information for each set of events is saved in an "EVENT.json" file, located in its corresponding **simulation working directory**.

The following options for event applications vary in the type of event, event properties, and format of the event file which it processes.
