.. _lbl-capabilities_HydroUQ:
.. role:: blue

************
Capabilities
************

Version |tool version| of the |app| was released on **March 31, 2024**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)


UQ (Uncertainty Quantification and Optimization Options)
========================================================

#. Water Event Selection: Users are provided with multiple paths for water borne hazard generation:

   A. Generate/record integrated loads and point pressure measurements by creating and running a CFD
   model on DesignSafe.

   B. Run GeoClaw, a widely used shallow-water solver vetted for tsunamis / storm surges, via the graphical user interface.

   C. Define and adjust prebuilt, digital twin wave-makers (1D / 2D pistons, pumps, gravity head).

   D. For advanced users, full authority is provided to input hydrodynamic files from tools of their choice.

#. Structural Model: Defines the structural modeling approach and returns the scripts required to perform the response simulation. One or more models can be assigned to a workflow. Using more than one model allows for benchmarking and epistemic uncertainty analysis. The following options are available:

   A. Provide your own OpenSees model in Tcl or Python format.

   B. Provide a Python script that prepares a structural model and performs the response simulation.
   
   C. Automatically generate an idealized shear column model in OpenSees from basic building information.

#. Response Simulation: Defines the analysis options that will be used to perform the numerical simulation, e.g., time integration strategy, convergence criteria, and damping options. The user-specified modeling tool is used to perform the simulation and collect the requested response quantities.

#. Uncertainty Quantification: Samples the prescribed random input variables and obtains realizations of the outputs by executing the workflow with each input realization from the generated sample. The underlying UQ engines let you leverage the following techniques in your research:

   A. Forward propagation :ref:`Dakota<lblDakotaForward>` :ref:`SimCenterUQ<lblSimForward>`: Define a set of random input parameters and perform simulations to obtain a corresponding sample of output parameters and their statistics.

   B. Sensitivity analysis :ref:`Dakota<lblDakotaSensitivity>` :ref:`SimCenterUQ<lblSimSensitivity>`: Measure the influence of the uncertainty in each input on the uncertainty of outputs.

   C. Reliability analysis :ref:`Dakota<lblDakotaReliability>` :ref:`SimCenterUQ<lblSimSensitivity>`: Algorithms to estimate the probability of exceeding a failure surface.


.. note::
   
   Support for the running computation to be performed on a TACC high-performance computer, e.g. Frontera or Lonestar6, is provided through DesignSafe for all but the methods indicated with a star (*).  


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
     B. Save Columns Separately (Useful after Bayesian updating, the posterior samples can later be directly loaded in HydroUQ)
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



