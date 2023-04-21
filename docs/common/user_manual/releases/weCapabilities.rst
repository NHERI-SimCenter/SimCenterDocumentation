.. _lbl-capabilities_weuq:
.. role:: blue

************
Cababilities
************

**Version 2.3.0** of |app| was released **March 2023**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)


Structural Information Model
============================

Applications used to specify/select the structural model to be used in analysis.

#. MDOF: creating idealized multi-degree-of-freedom models
#. OpenSees: user-defined OpenSees models
#. Steel Building Model: automating steel frame design and modeling
#. MDOF-LU: MDOF shear building model
#. CustomPy

    
Wind Loading Event
=======================

Applications used to specify/select wind loading for the structure.

#.  Stochastic Wind: simulating stochastic wind speed using spectral method
#.  CFD-Basic: generating CFD model for beginners with limited control options
#.  CFD-Expert: generating CFD model for advanced with several control options
#.  :blue:`CFD-Digital Wind Tunnel: generating CFD models to numerically simulate the Boundary Layer Wind Tunnel at University of Florida`
#.  DEDM_HRP: database-enabled design framework based on wind-tunnel data for high rise buildings 
#.  LowRiseTPU: extracting aerodynamics loads based on TPU database for low-rise buildings
#.  WInd Tuneel Experiment
#.  Existing: User supplied time varying floor loads


Engineering Demand Parameter Generator
======================================

Applications to identify the output parameters of interest given the ground motion and structural model.

#. Serviceability Design: inter story drift ratio, peak floor acceleration
#. Cladding Design: peak pressures
#. Structural Wind Design: equivalent static loads
#. User Defined: user-specified EDP
    
    
Finite Element Application
==========================

Applications used to determine the response output parameters given the ground motion and structural model.

#.  OpenSees: Open System for Earthquake Engineering Simulation


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
           a. Resample from existing correlated dataset of samples

#. Global Sensitivity Analysis

     A. Dakota Sensitivity Options

        #. MCS
        #. LHS

     B. SimCenterUQ Sensitivity Options

        #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

           a. Import input/output samples from data files


#. Surrogate Modeling

     A. SimCenterUQ Engine Surrogating Options:

        #. Surrogate modeling using Probabilistic Learning on Manifolds (PLoM)
	   
