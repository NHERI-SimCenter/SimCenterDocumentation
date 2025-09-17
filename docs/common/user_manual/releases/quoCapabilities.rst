.. _lbl-capabilities_quoFEM:
.. role:: blue

************
Capabilities
************

Version |tool version| of the |app| was released on **August 14, 2024**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)


UQ (Uncertainty Quantification and Optimization Options)
========================================================

#. Forward Uncertainty Propagation

     A. :ref:`Dakota<lblDakotaForward>`

        #. Monte Carlo Sampling (MCS)
        #. Latin Hypercube Sampling (LHS)
        #. Gaussian Process Regression
        #. Polynomial Chaos Expansion

     B. :ref:`SimCenterUQ<lblSimForward>`

        #. Monte Carlo Sampling (MCS)

           a. Resample from the existing correlated dataset of samples

        #. Multi-fidelity Monte Carlo

#. Global Sensitivity Analysis

     A. :ref:`Dakota<lblDakotaSensitivity>`

        #. MCS
        #. LHS

     B. :ref:`SimCenterUQ<lblSimSensitivity>`

        #. Probability Model-based Global Sensitivity Analysis (PM-GSA)

           a. First-order Sobol indices
           b. Total-effect Sobol indices
           c. Group-wise Sobol indices
           d. Principal component analysis and probabilistic model-based GSA (PCA-PSA) for high-dimensional QoIs
           e. Aggregated Sobol indices for field QoIs
           f. Import input/output samples from data files

#. Reliability Analysis

     A. :ref:`Dakota<lblDakotaReliability>` 

        #. Local Reliability 
        #. Global Reliability
        #. Importance Sampling

#. Bayesian Calibration

     A. :ref:`Dakota<lblDakotaBayesianCalibration>`

        #. DREAM

     B. :ref:`TMCMC <lblUCSDTMCMC>`

        #. Transitional Markov Chain Monte Carlo (TMCMC) for Bayesian estimation
        
           a. Override default log-likelihood function
           b. Override default error covariance structure
           c. Calibrate multipliers on error covariance structure

        #. :blue:`Surrogate-aided Bayesian calibration using Gaussian Process (GP) surrogate model`

     C. :ref:`Hierarchical Models <lblUCSDHierarchical>`

        #. Bayesian updating of parameters of a hierarchical model

            a. Quantify aleatory uncertainty in the parameter values of a computational model

#. Deterministic Calibration

     A. :ref:`Dakota<lblDakotaDeterministicCalibration>`

        #. NL2SOL
        #. OPT++GaussNewton
        #. Gradient-free optimization
        
#. Surrogate Modeling 

     A. SimCenterUQ

        #. :ref:`Train Gaussian Process (GP) Surrogate Model<lblSimSurrogate>`

           a. Multifidelity surrogate modeling
           b. Adaptive design of experiment options for surrogate modeling
           c. Nugget optimization options for surrogate modeling
           d. Stochastic Kriging 

        #. :ref:`Surrogate modeling using Probabilistic Learning on Manifolds (PLoM)<lblSimCenterUQPLoM>` *

#.  :ref:`CustomUQ<lblCustomUQ>`

        #. Configure UQ analysis using JSON file


.. note::
   
   Support for the running computation to be performed on TACC's high-performance computer, Frontera, is provided through DesignSafe for all but the methods indicated with a star (*).  


FEM (Computational Model Specification)
=======================================
            
#. OpenSees
#. FEAPpv
#. Python
#. Custom
#. SurrogateGP  
#. None
#. Multiple models

RV (Random Variable Options)
============================

#. Inspect PDF of RV

#.  Distributions available: :sup:`1`
     
     #. Normal
     #. Lognormal
     #. Beta
     #. Uniform
     #. Weibull
     #. Gumbel
     #. Continuous :sup:`2`
     #. Exponential :sup:`3`
     #. Discrete :sup:`3`
     #. Gamma :sup:`3`
     #. Chi-squared :sup:`3`
     #. Truncated exponential :sup:`3`

.. note::
      
      :sup:`1`: For SimCenterUQ and UCSD algorithms only, the RVs can be defined through any of these options - parameters, moments, or a dataset.
      :sup:`2`: Available for Optimization routines in Dakota only.
      :sup:`3`: Available in SimCenterUQ and UCSD only.

EDP (Outputs from Computational Models)
=======================================
            
#. Scalar quantities of interest
#. Vector quantities of interest

RES (Summary and Visualization of UQ Analysis Results)
======================================================

#. Summary statistics of outputs displayed

     A. Mean
     B. Standard deviation
       
#. All output values presented in the spreadsheet

     A. Update the chart by clicking on spreadsheet columns
    
#. Output values visualized in the interactive chart

     A. Scatter plot 
     B. Histogram
     C. Cumulative distribution
     D. Inspect points on chart

#. Spreadsheet save options

     A. Save Table
     B. Save Columns Separately (Useful after Bayesian updating, the posterior samples can later be directly loaded in quoFEM)
     C. Save RVs (Useful for surrogate model training)
     D. Save QoIs (Useful for surrogate model training)
     E. Save Surrogate Predictions (Only for the surrogate model results)

#. Visualization of surrogate modeling (GP) results

     A. Goodness-of-fit measures
     B. 90% confidence interval and prediction interval
     C. Save GP model

#. Visualization of PLoM training results

     A. PCA representation error plot
     B. Diffusion maps eigenvalue plot



