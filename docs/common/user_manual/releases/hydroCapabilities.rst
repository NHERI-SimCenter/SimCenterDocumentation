.. _lbl-capabilities_HydroUQ:
.. role:: blue

************
Capabilities
************

Version |tool version| of the |app| was released on **August 20th, 2025**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)



#. Water Event Selection: Users are provided with multiple paths for water borne hazard generation:

   A. Generate/record integrated loads and point pressure measurements by creating and running a CFD model on DesignSafe.

   B. Run GeoClaw, a widely used shallow-water solver vetted for tsunamis / storm surges, via the graphical user interface.

   C. For advanced users, full authority is provided to input hydrodynamic files from tools of their choice.

   D. :blue:`Define and adjust prebuilt, digital twin wave-makers (piston based, vacuum-chamber release).`

   E. :blue:`Simulate coastal wave events using the Celeris wave-solver (Boussinesq, non-linear shallow water).`

   F. :blue:`Access BRAILS building inventories and NOAA bathymetry-topographies through the Celeris module coupling.`

   G. :blue:`Employ local high-performance computation (GPU & CPU) using Taichi Lang (examples provided).`

#. Structural Model: Defines the structural modeling approach and returns the scripts required to perform the response simulation. One or more models can be assigned to a workflow. Using more than one model allows for benchmarking and epistemic uncertainty analysis. The following options are available:

   A. Provide your own OpenSees model in Tcl or Python format.

   B. Provide a Python script that prepares a structural model and performs the response simulation.
   
   C. Automatically generate an idealized shear column model in OpenSees from basic building information.

#. Response Simulation: Defines the analysis options that will be used to perform the numerical simulation, e.g., time integration strategy, convergence criteria, and damping options. The user-specified modeling tool is used to perform the simulation and collect the requested response quantities.

UQ (Uncertainty Quantification and Optimization Options)
========================================================

#. Uncertainty Quantification: Samples the prescribed random input variables and obtains realizations of the outputs by executing the workflow with each input realization from the generated sample. The underlying UQ engines let you leverage the following techniques in your research:

   A. Forward propagation :ref:`Dakota<lblDakotaForward>` :ref:`SimCenterUQ<lblSimForward>`: Define a set of random input parameters and perform simulations to obtain a corresponding sample of output parameters and their statistics.

   B. Sensitivity analysis :ref:`Dakota<lblDakotaSensitivity>` :ref:`SimCenterUQ<lblSimSensitivity>`: Measure the influence of the uncertainty in each input on the uncertainty of outputs.

   C. Reliability analysis :ref:`Dakota<lblDakotaReliability>` :ref:`SimCenterUQ<lblSimSensitivity>`: Algorithms to estimate the probability of exceeding a failure surface.


SIM (Structural Model)
======================

#. Multi-degree-of-freedom (MDOF) model
#. MDOF-LU
#. OpenSees
#. :blue:`Steel Building Model`
#. :blue:`Concrete Building Model`
#. Custom Python Script (customPy)
#. Multiple Models


EVT (Event Selection)
======================

#. Style

     #. General Event

          #. Broad functionality for designing custom events with custom bathymetry, structures, initial conditions, etc.

     #. Digital Twins

          #. Prevalidated digital wave-flumes replicating experimental facilities

          #. Available digital wave-flumes

               #. Oregon State University Large Wave Flume (OSU LWF)

               #. :blue:`Oregon State University Directional Wave Basin (OSU DWB)`

               #. :blue:`University of Washington's Wind-and-Sea Interaction Facility (UW WASIRF)`

               #. :blue:`Waseda University's Tsunami Wave Basin (WU TWB)`

               #. :blue:`United States Geological Survey Debris-Flow Flume (USGS DFF)`

          #. Available wave-maker twins

               #. 1D Piston

               #. :blue:`Vacuum Chamber Reservoir`

               #. :blue:`Dam-break`

#. Numerical Methods

     #. :blue:`Material Point Method (ClaymoreUW MPM)`

          #. :blue:`Unified debris-fluid-structure-soil interaction simulations using Material Point Method (MPM)`

          #. :blue:`Accepts custom event probe types and locations`

          #. :blue:`Multi-GPU accelerated`

          #. :blue:`Available for running on TACC HPC`

     #. :blue:`Celeris`

          #. :blue:`Boussinesq wave solver`

          #. :blue:`Nonlinear shallow-water solver`

          #. :blue:`Accepts custom bathymetries and event probe locations`

          #. :blue:`Automatic BRAILS inventory with NOAA bathymetries`

          #. :blue:`Taichi Lang accelerated (GPU & CPU).`

          #. :blue:`Available for running on local machine`

     #. FOAMySees (**Returning Soon**) :sup:`1`

          #. Computational Fluid Dynamics using OpenFOAM

          #. Computational Structural Dynamics using OpenSees

          #. Two-way coupled using Precice library

          #. Available for running on TACC HPC

     #. OpenFOAM (**Returning Soon**) :sup:`2`
          
          #. Computational Fluid Dynamics

          #. Partially deprecated functionality for allowing inlets for GeoClaw / generic shallow-water equation solutions in OpenFOAM :sup:`2`

          #. Available for running on TACC HPC

     #. GeoClaw (**Returning Soon**) :sup:`2`

          #. Shallow-water solver for tsunamis and storm surges

          #. Available for running on DesignSafe

          #. Available for running on local machine

          #. Available for running on TACC HPC

.. note:: 
     
     :sup:`1` FOAMySees functionality from HydroUQ v2.0 is deprecated in the current version due to remote supercomputer migration from Frontera to Stampede3. It is to be fully reintroduced in the near future if funding returns to this project.
     :sup:`2` OpenFOAM-GeoClaw functionality from HydroUQ v1.0 is deprecated in the current version due to remote supercomputer migration from Frontera to Stampede3. It is to be fully reintroduced in the near future if funding returns to this project.



FEM (Computational Model Specification)
=======================================
            
#. OpenSees
#. Python
#. Custom
#. Multiple models

RV (Random Variable Options)
============================

#. Inspect probability distribution function (PDF) of RV

#. Distributions available: :sup:`1`
     
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

#. Available sets of EDPs:

     #. Standard Earthquake EDPs 

          #. Peak Inter-story Drift (PID)

          #. Peak Floor Acceleration (PFA)

          #. Peak Roof Displacement (PRD)

     #. :blue:`Standard Hydrodynamic EDPs`

          #. :blue:`Peak floor displacement (PFD)`

          #. :blue:`Peak floor acceleration (PFA)`

          #. :blue:`Peak floor force (PFF)`

          #. :blue:`Peak floor pressure (PFP)`

          #. :blue:`Peak wave height (PWH)`

          #. :blue:`Average wave velocity (AWV)`

          #. :blue:`Total wave momentum-flux (TWM)`

     #. User Defined EDPs

          #. Define EDPs in the additional input files

          #. Populate response parameter names in the GUI

          #. Define a post-processing script to create the ``results.out`` file of appropriate format (single line where each value corresponds to a response parameter) using only the FEM simulation output.

          #. Use the output of the FEM simulation to calculate the EDPs

#. Format of EDPs:

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



