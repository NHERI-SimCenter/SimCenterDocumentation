.. _lbl-release_weuq:
.. role:: blue

*************
Release Notes
*************

Version 3.3 (Current)
-----------------------

**Release date:** Sept. 2023

**Highlights**

#. Added capability to simulate wind load on building with arbitrary shape
#. Added options to import and transform STL geometry of the building.
#. Fixed bugs in prior release 
#. Created a new CFD example to demonstrate the recently added features. 


Version 3.0
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