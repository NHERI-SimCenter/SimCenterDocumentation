.. _lbl-release_weuq:
.. role:: blue

*************
Release Notes
*************

Version 4.1 (Current)
-----------------------

**Release date:** Sept. 2024

**Highlights**

#. Implemented new functionality to visualize and export overall/pressure loads on building for performance based wind engineering analysis.
#. New capability to surrogate structural responses and use the surrogate model in the workflow.
#. Added numerical example for simulating wind loads on a building with surroundings assuming a idealized topology.
#. Minor bug fixes to pre-/post-processing of the CFD-based events.


Version 4.0
-----------------------

**Release date:** Aug. 2024

**Highlights**

#. Added CFD functionality to simulate wind loads on isolated buildings without running the entire workflow in WE-UQ
#. Major changes required for interfacing with DesignSafe the newly released Version 3 of Tapis. Updated major version to reflect preferences needed for users to submit jobs to TACC HPC resources.


Version 3.4
-----------------------

**Release date:** May. 2024

**Highlights**

#. Simulate wind loading on structures surrounded by an array of buildings. Surrounding buildings heights may be randomized or user-defined.
#. Minor bug fixes in the tool.
   

Version 3.3
-----------------------

**Release date:** Apr. 2024

**Highlights**

#. Simulate wind loading on structures surrounded by an array of buildings. Surrounding buildings heights may be randomized or user-defined.
#. A new wind load generator module: wind-tunnel informed stochastic wind pressure generator
#. Empty domain simulation tool.
   


Version 3.2
-----------

**Release date:** Mar. 2024

**Highlights**

#. Implemented a new capability to characterize Atmospheric Boundary Layer (ABL) flows using large-eddy simulation (LES).
#. Added advanced options for pre-processing, monitoring and postprocessing CFD simulation.
#. Integrated a new method to Turbulence Inflow Tool (TInF) tool for wind loading simulation.
#. Supports visualization of the simulation data using Paraview on local machine. 
#. Addressed bugs in the prior release 
#. Created a new example to demonstrate the recently added CFD features.
#. Option for multi-fidelity sampling, allowing for FEM models of different fidelity


Version 3.1
-----------

**Release date:** Oct. 2023

**Highlights**

#. Added capability to simulate wind load on building with arbitrary shape
#. Added options to import and transform the STL geometry of the building.
#. Fixed bugs in the prior release 
#. Created a new CFD example to demonstrate the recently added features. 


Version 3.0.0
---------------

**Release date:** July. 2023

**Highlights**

1. **New CFD-based event for wind load evaluation**: 
  a. Implemented CFD modeling option for generic isolated rectangular buildings.
  b. Added advanced feature for boundary condition specification including inflow and ground roughness representation.  
  c. Supports automated monitoring of integrated and cladding loads on the study building.   
  d. Supports different turbulence modeling options including Large-Eddy Simulation (LES), Reynolds-Averaged Navier-Stokes (RANS) and Detached-Eddy Simulation (DES).
  e. Updated solver selection (with PISO, SIMPLE and PIMPLE algorithms) and added new controls for numerical setup.  
  f. Included support for different OpenFOAM distributions starting from v7 up to v10.


2. **Improved GUI design** 
  a. Implemented user-friendly GUI support for creating the CFD model
  b. Added a new 3D model visualization window using Visualization Toolkit (VTK)
  c. Supports reading and writing of the case files to the user's local machine 

3. **Automated mesh generation** 
  a. Integrated automated mesh generation workflow with several refinement controls.  
  b. Added option to generate mesh on the user's local machine. 
  

4. **Examples** 
  a. Added a new CFD example to demonstrate the recently added features with uncertainty quantification. 



Version 2.3
-------------

**Release date:** March. 2022

**Highlights**

#. New Digital Wind Tunnel Event
#. New UQ options for sampling, sensitivity, reliability
#. Updated FEM analysis options
#. Updated TInF to avoid negative length scales during OpenFOAM run 
#. Minor bug fixes


Version 2.0
----------------

**Release date:** September. 2019

**Highlights**

#. Added new UQ features
#. Added the CWE interface to the tool to aid beginners in performing CFD simulations
#. Integrated with wind tunnel datasets
#. Updated example files



Version 1.0 (First Release)
-------------------

**Release date:** July. 2019

**Highlights**

#. High-Rise with Pressure Database (DEDM_HRP)
#. Stochastic Wind Load Generator 
#. Expert CFD Simulation Option
#. Selection from Existing Wind Event applications
