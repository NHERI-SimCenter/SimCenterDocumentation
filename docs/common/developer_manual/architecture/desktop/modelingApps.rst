.. _lblmodelingApp:

Modeling Applications
=====================

The **modeling application** consolidates information on the *structural analysis model* (SAM) used to represent the building on each site.
It takes as input the :ref:`BIM file <lblBuildingApp>`, the :ref:`EVENT file <lblEventApp>`, and information on the structural model used for response simulation, specified in the :ref:`configuration file <lblUserDefInputs>`.
The input structural model information is parsed into a "SAM.json" file, located in its corresponding **simulation working directory**.

.. _figContext:

.. figure:: figures/backendapps_Modeling.png
   :align: center
   :figclass: align-center


The following options for modeling applications vary in the type of model and finite element program used for response simulation.

.. jsonschema:: App_Schema.json#/properties/ModelingApplications/MDOF-LU


.. jsonschema:: App_Schema.json#/properties/ModelingApplications/OpenSeesInput


.. jsonschema:: App_Schema.json#/properties/ModelingApplications/OpenSeesPyInput

In the configuration file, **OpenSeesPyInput** is called under "Applications" as:

.. code-block::

      "Modeling": {
         "Application": "OpenSeesPyInput",
            "ApplicationData": {
             "mainScript": "cantilever.py",
             "modelPath": "model/",
             "ndm": 3,
             "dofMap": "1,2,3"
         }
      }
