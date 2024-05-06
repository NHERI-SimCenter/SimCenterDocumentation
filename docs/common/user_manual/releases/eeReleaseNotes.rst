.. _lbl-release_eeuq:
.. role:: blue

*************
Release Notes
*************

Version 3.5.0 (Current)
-----------------------

**Release date:** March. 2024

**Highlights**

#. Physics-based ground motion simulations generate by the `M9 project <https://sites.uw.edu/pnet/m9-simulations/>`_.


Version 3.4.0
-----------------------

**Release date:** Oct. 2023

**Highlights**

#. Multi Fidelity Monte Carlo (MFMC) method

Version 3.3.0 
-----------------------

**Release date:** March. 2023

**Highlights**

#. Multi model uncertainty propagation options for Modeling (SIM) and Analysis (FEM) tabs
#. Gaussian process surrogate modeling


Version 3.2.0
-------------

**Release date:** Sept. 2022

**Highlights**

#. **New Structural Information Model Generators**
    a. Concrete Building Model: automatic concrete building design and model generation
    b. MDOF-LU: MDOF shear building model built using user supplied Hazus data
#. Moving damping ratio specification from FEM to SIM panels.
#. Improvements to the message area
#. Decoupling the output units defined in GI with the units used in the simulation.


Version 3.1.0
-----------------------

**Release date:** July 2022

** Highlights**

#. New Surrogate option in defining spectrum in PEER event
#. Fixing the radio button in Multiple Event (uncheck is now enabled)
#. Improvements to the message area, and minor bug fixes


Version 3.0.0
-------------

**Release date:** March. 2022

**Highlights**

#. New UQ engine: PLoM
  a. Training surrogate model for defined structural model
  b.  Training surrogate using user-supplied response data metric
  c. Generating new realizations of structural responses from trained surrogate
  d. Including user-defined ground motion intensity measures in the modeling training
#. Site-specific seismic disaggregation
  a. Seismic hazard disaggregation at given return period and user-defined IM
  b. Target conditional mean spectrum (ASCE7) calculation based on disaggregated mean magnitude and distance
  c. Ground motion selection and scaling to the disaggregation-based target spectrum     
#. Refactored results panel synced from new SimCenterCommon
  a. New data visualization panel
  b. Highlighting data points


Version 2.2.7
-------------

**Release date:** Jan. 2022

**Highlights**

#. New Options added for PEER NGA Event:
Specifying the fault type, pulse-like feature, and duration filter in ground motion selection
Adding the option of "Geometric" suite average for the PEER NGA West2 ground motion selection
#. In User Defined EDP fixed a bug of using user-specified EDP names


Version 2.2.6
--------------

**Release date:** Dec. 22nd, 2021

**Highlights**

#. Specifying the fault type, pulse-like feature, and duration filter in ground motion selection
#. Adding the option of "Geometric" suite average for the PEER NGA West2 ground motion selection
#. Bug fixes:
     a.  exporting ground motion names in the "Save Data
     b. using user-specified EDP name


Version 2.2.5
----------------

**Release date:** Oct. 4th, 2021

**Highlights**
#. new options for NGA selection
#. option to select motions from user flat file
#. changing look and feel for message box location

Version 2.2.0
-------------

**Release date:** Nov 6, 2020

**Highlights**

#. Site response now allows for random fields in soil layers for soil properties
#. Steel building model generator (designs and creates a model for steel buildiung)
#. PEER NGA scaling options added

Version 2.1.0
-------------

**Release date:** June, 2020

**Highlights**

#. Added Sensitivity and Reliability
#. Added new spectrum options for peerNGA
#. Modified FEM interface provides different damping options and more analysis options to user

Version 2.0.0
-------------

**Release date:** October, 2019

**Highlights**

#. More UQ Sampling capabilities,
#. another stocahstic loading module
#. calling PEER NGA to select and download files



   
