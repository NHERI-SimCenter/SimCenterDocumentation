.. _lblEDPApp:

EDP Applications
================

The **EDP application** specifies the types of *engineering demand parameters* (EDP) expected as output from the response simulation.
It determines the EDP type from building properties in the :ref:`BIM file <lblBuildingApp>`, the type of event in the :ref:`EVENT file <lblEventApp>`, and the model information from the :ref:`SAM file <lblModelingApp>`.
It writes the type, location, and direction (DOF) of each EDP for a simulation in an "EDP.json" file in, located in its corresponding **simulation working directory**.
Note that in the EDP file, DOF=1,2 are assumed to correspond to perpendicular horizontal directions, and DOF=3 corresponds to the vertical direction.

.. _figContext:

.. figure:: figures/backendapps_EDP.png
   :align: center
   :figclass: align-center



The following options for EDP applications vary in the type of EDPs identified for the simulation output.


.. jsonschema:: App_Schema.json#/properties/EDPApplications/StandardEarthquakeEDP_R

In the configuration file, **StandardEarthquakeEDP_R** is called under "Applications" as:

.. code-block::

      "EDP": {
         "Application": "StandardEarthquakeEDP_R",
         "ApplicationData": {
         }
      }


.. jsonschema:: App_Schema.json#/properties/EDPApplications/UserDefinedEDP_R

In the configuration file, **UserDefinedEDP_R** is called under "Applications" as:

.. code-block::

      "EDP": {
         "Application": "UserDefinedEDP_R",
            "ApplicationData": {
             "EDPspecs": "EDP_specs.json"
         }
      }
