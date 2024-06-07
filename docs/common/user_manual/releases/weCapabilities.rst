.. _lbl-capabilities_weuq:
.. role:: blue

************
Capabilities
************

**Version 3.2.0** of |app| was released **March 2024**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)


Structural Information Model
============================

Applications are used to specify/select the structural model to be used in the analysis.

#. MDOF: creating idealized multi-degree-of-freedom models
#. MDOF-LU: auto-generated multi-degree-of-freedom model     
#. OpenSees: user-defined OpenSees models
#. CustomPy: user-defined OpenSees models

    
Wind Loading Event
=======================

Applications used to specify/select wind loading for the structure.

#.  Stochastic Wind: simulating stochastic wind speed using spectral method
#.  CFD - Digital Wind Tunnel: CFD simulation of boundary layer wind tunnel
#.  CFD - Wind Load on Isolated Buildings: CFD-based wind load simulation for isolated buildings with complex geometry
#.  DEDM_HRP: database-enabled design framework based on wind-tunnel data for high-rise buildings 
#.  LowRiseTPU: extracting aerodynamics loads based on the TPU database for low-rise buildings
#.  Wind Tunnel Experiment: uses pressure tap measurements from building in wind tunnel experiment
#.  Existing: User-supplied time-varying floor loads


Engineering Demand Parameter Generator
======================================

Applications to identify the output parameters of interest given the wind loading and the structural model.

#. Standard Wind: (serviceability) inter-story drift ratio, peak floor acceleration
#. User Defined: user-specified EDP
    
    
Finite Element Application
==========================

Applications used to determine the response output parameters given the wind load generation and structural models.

#.  OpenSees: Open System for Earthquake Engineering Simulation
#.  CustomPy: Any user-supplied Python application can be incorporated

Uncertainty Quantification
==========================

Applications to perform the uncertainty quantification for the response parameters given the inputs and the random variables present.

#. Forward Uncertainty Propagation

     A. Dakota Options 

        #. Monte Carlo Sampling (MCS)
        #. Latin Hypercube Sampling (LHS)
        #. Gaussian Process Regression
        #. Polynomial Chaos Expansion

     B. SimCenterUQ Options

        #. Monte Carlo Sampling (MCS)
           a. Resample from an existing correlated dataset of samples

#. Global Sensitivity Analysis

     A. Dakota Sensitivity Options

        #. MCS
        #. LHS

     B. SimCenterUQ Options

        #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

           a. Import input/output samples from data files

#. Surrogate Modeling

     A. SimCenterUQ Engine Surrogate Options:

        #. Surrogate modeling using Probabilistic Learning on Manifolds (PLoM)
	   
Additional Tools 
===============

#. :blue:`Empty Domain CFD Simulation`:
   Capability to perform empty domain simulation to characterize Atmospheric Boundary Layer (ABL) flows using large-eddy simulation (LES). This feature uses the Turbulence Inflow Tool (TInF) tool for calibrating ABL flows for a subsequent wind load evaluation study. 