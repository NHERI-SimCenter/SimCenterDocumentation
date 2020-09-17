.. _lblSimulationApp:

Simulation Applications
=======================

The **simulation application** creates SIM files which specify parameters for the numerical analysis in the response simulation. This script executes the ``build_model`` and ``run_analysis`` functions defined in the :ref:`model file <lblUserDefInputs>`.
It takes as input the BIM file created by the :ref:`Building Application <lblBuildingApp>`, the EVENT file created by the :ref:`Event Application <lblEventApp>`, the SAM file created by the :ref:`Modeling Application <lblModelingApp>`, and the EDP file created by the :ref:`EDP Application <lblEDPApp>`.
The "EDP.json" file is populated with the resulting EDPs from the response simulation and saved in the  in the **simulation working directory**. Note that the "SIM.json" file is not saved in the directory.

The following options for simulation applications vary in the type of finite element program or procedure used for EDPs estimation.
