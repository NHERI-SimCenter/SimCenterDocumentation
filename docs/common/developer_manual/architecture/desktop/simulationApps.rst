.. _lblSimulationApp:

Simulation Applications
=======================

The **simulation application** specifies parameters and executes the script for the response simulation. These parameters may include the integrator scheme, convergence tolerance, step size, etc. of the numerical analysis.
It takes as input the :ref:`BIM file <lblBuildingApp>`, the :ref:`EVENT file <lblEventApp>`, the :ref:`SAM file <lblModelingApp>`, and the :ref:`EDP file <lblEDPApp>`.
After response simulation is completed, the "EDP.json" file is populated with the resulting EDPs and saved in the **simulation working directory**. Note that the "SIM.json" file is not saved in the directory.

The following options for simulation applications vary in the type of finite element program or procedure used for EDPs estimation.

.. jsonschema:: App_Schema.json#/properties/SimulationApplications/OpenSees-Simulation_R
.. jsonschema:: App_Schema.json#/properties/SimulationApplications/OpenSeesPy-Simulation
.. jsonschema:: App_Schema.json#/properties/SimulationApplications/IMasEDP
