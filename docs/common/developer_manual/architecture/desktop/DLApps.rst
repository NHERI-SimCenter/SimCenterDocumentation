.. _lblDLApp:

DL Applications
===============

The **DL application** performs the damage and loss assessment for the buildings subject to the regional event(s).
It takes as input the building properties used for determining damages and losses (e. g. building occupancy, structure type, replacement cost, number of stories),
specified in the :ref:`BIM file <lblBuildingApp>`, as well as the response simulation output recorded in the :ref:`EDP file <lblEDPApp>`.
It returns damage probabilities in a "DM.csv" file and decision variable estimates in a "DV.csv" for each simulation, saved in its corresponding
**simulation working directory**.

.. _figContext:

.. figure:: figures/backendapps_DL.png
   :align: center
   :figclass: align-center

The following options for DL applications vary in the software package used to perform the damage and loss assessment.


.. jsonschema:: App_Schema.json#/properties/DLApplications/pelicun

In the configuration file, **pelicun** is called under "Applications" as:

.. code-block::

    "DL": {
           "Application": "pelicun",
           "ApplicationData": {
               "DL_Method": "HAZUS MH EQ",
               "Realizations": 1000,
               "detailed_results": false,
               "log_file": true,
               "coupled_EDP": true,
               "event_time": "off",
               "ground_failure": false
           }
       }
