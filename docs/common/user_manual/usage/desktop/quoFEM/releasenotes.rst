.. _lbl-release_quoFEM:
.. role:: blue

*************
Release Notes
*************

Version 3.0
===========

Version 3.0.0 (Current)
-----------------------

**Release date:** March. 2022

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. New option for surrogate modeling using Probabilistic Learning on Manifolds (PLoM)
#. Restructured surrogate model scripts
#. Improvements to the user interface for RV, QoI and RES tabs
#. Improvements to the message are
#. Major restructuring of the backend
#. Minor bug fixes in the user interface, surrogate modeling and sensitivity analysis scripts
#. Updated example files

.. warning::

   The version # was increased as changes were made to input and output formats. This means old examples will not load in this version of the tool.
   
Version 2.4
===========

**Release date:** Oct. 2021

#. new forward propagation method in SimCenterUQ to import existing sample sets (eg. samples obtained by MCMC)
#. new multi-fidelity surrogate modeling option in SimCenterUQ
#. local/remote parallel computing support for SimCenterUQ methods
#. visualization improved for surrogate results
#. more adaptive design of experiments options added for surrogate modeling
#. nugget optimization options added for surrogate modeling
#. minor improvements and bug fixes



Version 2.3
-----------

**Release date:** May 2021


#. Data for calibration methods (DREAM, TMCMC, parameter estimation) required #. to be provided in a file
#. Option to supply a covariance structure for error in Bayesian calibration methods
#. Option to calibrate values of multipliers on error covariance structure in Bayesian calibration methods
#. Log-likelihood function specification made optional for TMCMC


Version 2.2
-----------

**Release date:** Oct. 2020

#. Included new sensitivity method: probability model-based global sensitivity analysis (PM-GSA)
#. Included new reliability method: transitional Markov chain Monte Carlo (TMCMC)
#. Option to allow user to include their own UQ engine
#. Option to allow user to include their own FEM engine

Version 2.0
-----------

**Release date:** Sept. 2019

#. forward uncertainty: Importance Sampling, Gaussian Process Regression
#. reliability: FORM and SORM
#. sensitivity with Monte Carlo or LHS
#. Parameter Estimation

