.. _lblUQApp:

UQ Applications
===============

The **UQ application** is used to sample *random variables* (RV) specified in any of the worfklow steps (Event, Modeling, EDP, Simulation) for the purpose of uncertainty quantification, then to run commands written in the **driver file** which call on the backend applications to execute the RDT Workflow.
It first populates values for the RVs, sampled from specified probability distributions, in the corresponding files (EVENT.json, SAM.json, EDP.json, SIM.json) for each simulation before executing the workflow.
If no RVs are specified, then the UQ application directly runs commands in the driver file without random sampling.

.. _figContext:

.. figure:: figures/backendapps_UQ.png
   :align: center
   :figclass: align-center


The following options for UQ applications vary in the software package used to perform uncertainty quantification.

.. jsonschema:: App_Schema.json#/properties/UQApplications/Dakota-UQ

In the configuration file, **Dakota-UQ** is called under "Applications" as:

.. code-block::

      "UQ": {
         "Application": "Dakota-UQ",
            "ApplicationData": {
            "method": "LHS",
            "samples": 10,
            "type": "UQ",
            "concurrency": 1,
            "keepSamples": true
         }
      }
