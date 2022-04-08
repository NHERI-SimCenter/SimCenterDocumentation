.. _lbl-release_quoFEM:
.. role:: blue

*************
Release Notes
*************

Major Version 3.0
=================

|app| Version 3.0.0 (Current)
-----------------------------

**Release date:** March. 2022

#. Major restructuring of the backend
#. Updated example files


.. warning::

   The version # was increased as changes were made to input and output formats. This means old examples will not load in this version of the tool.

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. Reliability:

         #. Local Reliability
         #. Global Reliability
         #. Importance Sampling

      e. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ:

      a. Sensitivity Analysis

         #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

            a. First-order Sobol indices
            b. Group-wise Sobol indices

      b. Sampling

         #. Monte Carlo Sampling (MCS)
            a. Resample from existing correlated dataset of samples

      c. Train Gaussian Process (GP) Surrogate Model

         #. Multifidelity surrogate modeling
         #. Adaptive design of experiments options for surrogate modeling
         #. Nugget optimization options for surrogate modeling

      d. :blue:`Surrogate modeling using Probabilistic Learning on Manifolds (PLoM)`

   * UCSD_UQ:

      a. Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation

         #. Override default log-likelihood function
         #. Override default error covariance structure
         #. Calibrate multipliers on error covariance structure

   * CustomUQ:

      a. Configure UQ analysis using JSON file


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv
   * OpenSeesPy
   * Custom
   * SurrogateGP

#. **RV (Inputs to Computational Models)**:

   * Inspect PDF of RV

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous

   * SimCenterUQ:

      a. Random variables (UQ): RVs can be defined by any of parameters, moments, or dataset.

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel
         #. Exponential
         #. Discrete
         #. Gamma
         #. Chi-squared
         #. Truncated exponential
   

   * UCSD_UQ:

      a. Random variables (Priors):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel
         #. :blue:`Exponential`
         #. :blue:`Discrete`
         #. :blue:`Gamma`
         #. :blue:`Chi-squared`
         #. :blue:`Truncated exponential`


#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest
   * Vector quantities of interest



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution
      #. :blue:`Inspect points on chart`

   * Visualization of surrogate modeling results

      #. Goodness-of-fit measures

   * :blue:`Visualization of PLoM training results`

      #. :blue:`PCA representation error plot`
      #. :blue:`Diffusion maps eigenvalue plot`


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Reliability:

         #. Local Reliability
         #. Global Reliability
         #. Importance Sampling

      c. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ

      a. Forward Uncertainty Propagation
      b. PM-GSA
      c. Train GP Surrogate Model

   * UCSD_UQ

      a. TMCMC


Major Version 2.0
=================

|app| Version 2.4.1
-------------------
**Release date:** Dec. 2021

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. Reliability:

         #. Local Reliability
         #. Global Reliability
         #. Importance Sampling

      e. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ:

      a. Sensitivity Analysis

         #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

      b. Sampling

         #. Monte Carlo Sampling (MCS)
            a. Resample from existing correlated dataset of samples

      c. Train Gaussian Process (GP) Surrogate Model

         #. Multifidelity surrogate modeling
         #. Adaptive design of experiments options for surrogate modeling
         #. Nugget optimization options for surrogate modeling

   * UCSD_UQ:

      a. Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation

         #. Override default log-likelihood function
         #. Override default error covariance structure
         #. Calibrate multipliers on error covariance structure

   * CustomUQ:

      a. Configure UQ analysis using JSON file


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv
   * OpenSeesPy
   * Custom
   * SurrogateGP

#. **RV (Inputs to Computational Models)**:

   * Inspect PDF of RV

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous

   * SimCenterUQ:

      a. Random variables (UQ): RVs can be defined by any of parameters, moments, or dataset.

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel
         #. Exponential
         #. Discrete
         #. Gamma
         #. Chi-squared
         #. Truncated exponential
   

   * UCSD_UQ:

      a. Random variables (Priors):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest
   * Vector quantities of interest



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution

   * Visualization of surrogate modeling results

      #. Goodness-of-fit measures


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Reliability:

         #. Local Reliability
         #. Global Reliability
         #. Importance Sampling

      c. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ

      a. Forward Uncertainty Propagation
      b. PM-GSA
      c. Train GP Surrogate Model

   * :blue:`UCSD_UQ`

      a. :blue:`TMCMC`



|app| Version 2.4.0
-------------------

**Release date:** Oct. 2021

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. Reliability:

         #. Local Reliability
         #. Global Reliability

      e. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ:

      a. Sensitivity Analysis

         #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

      b. Sampling

         #. Monte Carlo Sampling (MCS)
         
            a. :blue:`Resample from existing correlated dataset of samples`

      c. :blue:`Train Gaussian Process (GP) Surrogate Model`

         #. :blue:`Multifidelity surrogate modeling`
         #. :blue:`Adaptive design of experiments options for surrogate modeling`
         #. :blue:`Nugget optimization options for surrogate modeling`

   * UCSD_UQ:

      a. Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation

         #. Override default log-likelihood function
         #. Override default error covariance structure
         #. Calibrate multipliers on error covariance structure

   * CustomUQ:

      a. Configure UQ analysis using JSON file


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv
   * OpenSeesPy
   * Custom
   * :blue:`SurrogateGP`

#. **RV (Inputs to Computational Models)**:

   * Inspect PDF of RV

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous

   * SimCenterUQ:

      a. Random variables (UQ): RVs can be defined by any of parameters, moments, or dataset.

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel
         #. Exponential
         #. Discrete
         #. Gamma
         #. Chi-squared
         #. Truncated exponential
   

   * UCSD_UQ:

      a. Random variables (Priors):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest
   * Vector quantities of interest



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution

   * :blue:`Visualization of surrogate modeling results`


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Reliability:

         #. Local Reliability
         #. Global Reliability

      c. Sensitivity Analysis:

         #. MCS
         #. LHS

   * :blue:`SimCenterUQ`

      a. :blue:`Forward Uncertainty Propagation`
      b. :blue:`PM-GSA`
      c. :blue:`Train GP Surrogate Model`



|app| Version 2.3
-----------------

**Release date:** May 2021

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. Reliability:

         #. Local Reliability
         #. Global Reliability

      e. Sensitivity Analysis:

         #. MCS
         #. LHS

   * SimCenterUQ:

      a. Sensitivity Analysis

         #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

      b. Sampling

         #. Monte Carlo Sampling (MCS)

   * UCSD_UQ:

      a. Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation

         #. :blue:`Override default log-likelihood function`
         #. :blue:`Override default error covariance structure`
         #. :blue:`Calibrate multipliers on error covariance structure`

   * CustomUQ:

      a. Configure UQ analysis using JSON file


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv
   * OpenSeesPy
   * Custom

#. **RV (Inputs to Computational Models)**:

   * Inspect PDF of RV

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous

   * SimCenterUQ:

      a. Random variables (UQ): RVs can be defined by any of parameters, moments, or dataset.

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel
         #. Exponential
         #. Discrete
         #. Gamma
         #. Chi-squared
         #. Truncated exponential
   

   * UCSD_UQ:

      a. Random variables (Priors):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest
   * :blue:`Vector quantities of interest`



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Reliability:

         #. Local Reliability
         #. Global Reliability

      c. Sensitivity Analysis:

         #. MCS
         #. LHS


|app| Version 2.2
-----------------

**Release date:** Oct. 2020

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. Reliability:

         #. Local Reliability
         #. Global Reliability

      e. Sensitivity Analysis:

         #. MCS
         #. LHS

   * :blue:`SimCenterUQ`:

      a. :blue:`Sensitivity Analysis`

         #. :blue:`Probability Model-based Global Sensitivity Analysis (PM-GSA)`

      b. :blue:`Sampling`

         #. :blue:`Monte Carlo Sampling (MCS)`

   * :blue:`UCSD_UQ`:

      a. :blue:`Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation`

   * :blue:`CustomUQ`:

      a. :blue:`Configure UQ analysis using JSON file`


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv
   * :blue:`OpenSeesPy`
   * :blue:`Custom`

#. **RV (Inputs to Computational Models)**:

   * :blue:`Inspect PDF of RV`

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous

   * :blue:`SimCenterUQ`:

      a. :blue:`Random variables (UQ): RVs can be defined by any of parameters, moments, or dataset.`

         #. :blue:`Normal`
         #. :blue:`Lognormal`
         #. :blue:`Beta`
         #. :blue:`Uniform`
         #. :blue:`Weibull`
         #. :blue:`Gumbel`
         #. :blue:`Exponential`
         #. :blue:`Discrete`
         #. :blue:`Gamma`
         #. :blue:`Chi-squared`
         #. :blue:`Truncated exponential`
   

   * :blue:`UCSD_UQ`:

      a. :blue:`Random variables (Priors)`:

         #. :blue:`Normal`
         #. :blue:`Lognormal`
         #. :blue:`Beta`
         #. :blue:`Uniform`
         #. :blue:`Weibull`
         #. :blue:`Gumbel`



#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. Importance Sampling
         #. Gaussian Process Regression
         #. Polynomial Chaos Expansion

      b. Reliability:

         #. Local Reliability
         #. Global Reliability

      c. Sensitivity Analysis:

         #. MCS
         #. LHS


|app| Version 2.0
-----------------

**Release date:** Sept. 2019

This is a SimCenter research application whose purpose is to allow users to perform uncertainty quantification and optimization utilizing existing finite element applictions. 

It will run the computations locally utilizing laptop/desktop or remotely utilizing the computational resources at TACC made available through DesignSafe-CI.

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **UQ (Uncertainty Quantification and Optimization Options)**:

   * Dakota:

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. :blue:`Importance Sampling`
         #. :blue:`Gaussian Process Regression`
         #. :blue:`Polynomial Chaos Expansion`

      b. Parameter Estimation: 

         #. NL2SOL
         #. OPT++GaussNewton

      c. Inverse Problem:

         #. DREAM

      d. :blue:`Reliability`:

         #. :blue:`FORM`
         #. :blue:`SORM`

      e. :blue:`Sensitivity Analysis`:

         #. :blue:`MCS`
         #. :blue:`LHS`


#. **FEM (Computational Model Specification)**:
   
   * OpenSees
   * FEAPpv

#. **RV (Inputs to Computational Models)**:

   * Dakota:

      a. Random variables (UQ):

         #. Normal
         #. Lognormal
         #. Beta
         #. Uniform
         #. Weibull
         #. Gumbel


      b. Design variables (Optimization):

         #. Continuous
   


#. **EDP (Outputs from Computational Models)**:
   
   * Scalar quantities of interest



#. **RES (Summary and Visualization of UQ Analysis Results)**:

   * Summary statistics of outputs displayed

      #. Mean
      #. Standard deviation

   * All output values presented in spreadsheet

      #. Update chart by clicking on spreadsheet columns

   * Output values visualized in interactive chart

      #. Scatter plot
      #. Histogram
      #. Cumulative distribution


#. **Remote (Support for Analysis on DesignSafe's high performance super computer)**:

   * Dakota

      a. Forward Uncertainty Propagation: 

         #. Monte Carlo Sampling (MCS)
         #. Latin Hypercube Sampling (LHS)
         #. :blue:`Importance Sampling`
         #. :blue:`Gaussian Process Regression`
         #. :blue:`Polynomial Chaos Expansion`

      b. :blue:`Reliability`:

         #. :blue:`FORM`
         #. :blue:`SORM`

      c. :blue:`Sensitivity Analysis`:

         #. :blue:`MCS`
         #. :blue:`LHS`



We encourage new feature suggestions, please write to us at :ref:`lblBugs`.