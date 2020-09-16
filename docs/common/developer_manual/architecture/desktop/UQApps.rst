.. _lblUQApp:

UQ Applications
===============

The **UQ application** runs the commands written in the driver file which call on each of workflow steps (Event, Modeling, EDP, Simulation) to execute the RDT Workflow.
If set up to sample random variables (RV) for uncertainty quantification in any of the workflow steps, then the UQ application first populates values for the random variables, sampled from specified probability distributions, in the corresponding files (EVENT.json, SAM.json, EDP.json, SIM.json) for each simulation before executing the workflow.

The following options for UQ applications vary in the software package used to perform uncertainty quantification.
