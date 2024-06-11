.. _lblUQApp:

UQ Applications
===============

The **UQ application** is used to sample *random variables* (RVs) specified in any of the workflow steps (Event, Modeling, EDP, Simulation) for uncertainty quantification. It then runs commands written in the **driver file**, which call on the backend applications to execute the R2D Workflow.
First, it populates values for the RVs, sampled from specified probability distributions, in the corresponding files (EVENT.json, SAM.json, EDP.json, SIM.json) for each simulation before executing the workflow.
If no RVs are specified, the UQ application directly runs commands in the driver file without performing random sampling.

.. figure:: _static/images/backendapps_UQ.png
   :align: center
   :figclass: align-center

.. only:: HydroUQ_app

   .. raw:: html
      :file: _static/html/HydroUQ/preprocUQ.html

.. only:: EEUQ_app

   .. raw:: html
      :file: _static/html/EE-UQ/preprocUQ.html

.. only:: WEUQ_app

   .. raw:: html
      :file: _static/html/WE-UQ/preprocUQ.html
