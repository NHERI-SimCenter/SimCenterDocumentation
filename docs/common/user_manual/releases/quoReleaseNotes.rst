.. _lbl-release_quoFEM:
.. role:: blue

*************
Release Notes
*************


Major Version 3
===============

   .. warning::

      The major version number was increased from 2 to 3 as changes were made to the input and output formats of |app|. This means old examples will not be loaded in this version of the tool.


   .. dropdown:: Version 3.5 (:blue:`Current`)
      :open:

      **Release date:** December. 2023

      **Highlights**
         #. Bayesian calibration of a **hierarchical model** 

   .. dropdown:: Version 3.4 
      :open:

      **Release date:** October. 2023

      **Highlights**
         #. **Multi-fidelity** Monte Carlo Simulation 

   .. dropdown:: Version 3.3 
      :open:

      **Release date:** March. 2023

      **Highlights**
         #. **Multimodel** uncertainty propagation
         #. Stochastic kriging **without replications**
         #. Display of correlation coefficients within the input/output dataset
         #. Switching the display order of the UQ method and UQ engine

   .. dropdown:: Version 3.2
      :open:

      **Release date:** September. 2022

      **Highlights**
         #. Support for **a gradient-free optimization** and **stochastic Kriging**
         #. Fast global sensitivity analysis for **very high dimensional** output (tested on 2 million QoIs)
         #. New option to **discard working directories** after each model simulation
         #. Support for **PLoM on DesignSafe**
         #. Significantly **enhanced speed** of surrogate validation and prediction 
         #. **None** option for FEM
         #. Improved user interface including error bounds of the surrogate prediction
         #. Major renaming: 

            * OpenseesPy → **python**
            * Parameters estimation → **deterministic calibration** 
            * Inverse problem → **Bayesian calibration** 


   .. dropdown:: Version 3.1
      :open:

      **Release date:** June. 2022

      Highlights

         #. New efficient global sensitivity analysis method for high-dimensional output (GSA-PCA)

         #. "Save RVs" and "Save QoIs" buttons were added to the results tab spreadsheet

         #. “NaN” handling option added to SimCenterUQ engine

         #. Improvements to reliability analysis and global sensitivity analysis user interface

         #. Minor bug fixes in the user interface, surrogate modeling, and sensitivity analysis scripts


   .. dropdown:: Version 3.0
      :open:

      **Release date:** March. 2022

      Highlights

         #. New option for surrogate modeling using Probabilistic Learning on Manifolds (PLoM)

         #. Restructured surrogate model scripts

         #. Improvements to the user interface for RV, QoI and RES tabs

         #. Improvements to the message area

         #. Major restructuring of the backend

         #. Minor bug fixes in the user interface, surrogate modeling and sensitivity analysis scripts

         #. Updated example files


Major Version 2
=================
   .. dropdown:: Version 2.4.1
      :open:

      **Release date:** Dec. 2021

      Highlights

         #. Added 'file_save' keyword in dakota.in to not delete paramsDakota.in files

         #. SimCenterUQ RV tab - preventing path strings from being deleted when "choose" is clicked (dataset inputs)

         #. SimCenterUQ checks if Python packages are missing in the environment and shows an error message if needed

         #. Minor fixes in surrogate UI (nugget values option should not show up by default, RVs should be uniform by default)

         #. A fix to prevent the mixed use of slash/backslash when printing a path

         #. Parameter values are passed to the log-likelihood script when using the UCSD_UQ engine


   .. dropdown:: Version 2.4.0
      :open:

      **Release date:** Oct. 2021

      Highlights

         #. New forward propagation method in SimCenterUQ to import existing sample sets (e.g. samples obtained by MCMC)

         #. New multi-fidelity surrogate modeling option in SimCenterUQ
         
         #. Local/remote parallel computing support for SimCenterUQ methods

         #. Visualization improved for surrogate results

         #. More adaptive design of experiment options added for surrogate modeling

         #. Nugget optimization options added for surrogate modeling

         #. Minor improvements and bug fixes

   .. dropdown:: Version 2.3
      :open:

      **Release date:** May 2021

      Highlights

         #. Data for calibration methods (DREAM, TMCMC, parameter estimation) required to be provided in a file

         #. Option to supply a covariance structure for error in Bayesian calibration methods

         #. Option to calibrate values of multipliers on error covariance structure in Bayesian calibration methods

         #. Log-likelihood function specification made optional for TMCMC


   .. dropdown:: Version 2.2
      :open:

      **Release date:** Oct. 2020

      Highlights

         #. Included new sensitivity method: probability model-based global sensitivity analysis (PM-GSA)

         #. Included new Bayesian calibration method: transitional Markov chain Monte Carlo (TMCMC)

         #. Option to allow users to include their own UQ engine

         #. Option to allow users to include their own FEM engine

         #. Changes to UI to reduce wasted space

   .. dropdown:: Version 2.0
      :open:

      **Release date:** Sept. 2019

      Highlights

         #. Forward uncertainty: Importance Sampling, Gaussian Process Regression

         #. Reliability: FORM and SORM

         #. Sensitivity with Monte Carlo or LHS

         #. Parameter Estimation
