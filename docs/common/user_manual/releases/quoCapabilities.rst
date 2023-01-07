.. _lbl-capabilities_quoFEM:
.. role:: blue

************
Capabilities
************

   .. dropdown::    Version 3.2.0 (:blue:`Current`)
      :open:

      **Release date:** September. 2022


      **Current Availability** 
            New features and fixes in this release are marked :blue:`blue` in the following list of features.

         #. **UQ (Uncertainty Quantification and Optimization Options)**:

            * Dakota: :blue:`[← New option to discard working directories after each model evaluation]`

               a. Forward Uncertainty Propagation: 

                  #. Monte Carlo Sampling (MCS)
                  #. Latin Hypercube Sampling (LHS)
                  #. Gaussian Process Regression
                  #. Polynomial Chaos Expansion

               b. Deterministic Calibration :blue:`[← formerly Parameter Estimation]`: 

                  #. NL2SOL
                  #. OPT++GaussNewton

               c. Bayesian Calibration :blue:`[← formerly Inverse Problem]`:

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
                     b. Total-effect Sobol indices
                     c. Group-wise Sobol indices
                     d. Principal component analysis and probabilistic model-based GSA (PCA-PSA) for high-dimensional QoIs
                     e. Aggregated Sobol indices for field QoIs
                     f. :blue:`Import input/output samples from data files`


               b. Sampling

                  #. Monte Carlo Sampling (MCS)
                     a. Resample from existing correlated dataset of samples

               c. Train Gaussian Process (GP) Surrogate Model :blue:`[← Enhanced speed and stability]`

                  #. Multifidelity surrogate modeling
                  #. Adaptive design of experiments options for surrogate modeling
                  #. Nugget optimization options for surrogate modeling
                  #. :blue:`Stochastic Kriging`

               d. Surrogate modeling using Probabilistic Learning on Manifolds (PLoM)

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
            * Python :blue:`[← formerly OpenSeesPy]`:
            * Custom
            * SurrogateGP
            * :blue:`None`

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
                  #. Exponential
                  #. Discrete
                  #. Gamma
                  #. Chi-squared
                  #. Truncated exponential


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
               #. Inspect points on chart

            * Spreadsheet save options

               #. Save Table
               #. Save Columns Separately (Useful after Bayesian updating, the posterior samples can later be directly loaded in quoFEM)
               #. Save RVs (Useful for surrogate model training)
               #. Save QoIs (Useful for surrogate model training)
               #. Save Surrogate Predictions (Only for the surrogate model results)

            * Visualization of surrogate modeling results

               #. Goodness-of-fit measures            
               #. 90% confidence interval and :blue:`prediction interval`

            * Visualization of PLoM training results

               #. PCA representation error plot
               #. Diffusion maps eigenvalue plot


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
               b. Global Sensitivity Analysis (PM-GSA)
               c. Train GP Surrogate Model
               d. :blue:`PLoM`

            * UCSD_UQ

               a. TMCMC