.. _lbl-geoclaw:

Shallow Water Solvers
=======================

There are several shallow water equation (SWE) solvers available. Here we discuss two popular choices in the tsunami and storm-surge simulation fields: GeoClaw and AdCirc.

GeoClaw
-----------

GeoClaw is a part of Clawpack (Conservation Laws Package) that was originally developed in 1994 by Professor Randall LeVeque and co-workers. It is available as a part of the Clawpack package, using finite volume methods (FVM) to solve linear and nonlinear hyperbolic systems. It employs high-resolution, Godunov-type methods with limiters in a general framework applicable to wave-related problems. It is often used for tsunami modeling, having been validated extensively to demonstrate its viability for fast computations with good accuracy. More information on GeoClaw may be found at the dedicated website for `Clawpack <https://www.clawpack.org>`_.

Herein, we will only discuss aspects of GeoClaw with particular importance to the HydroUQ platform. This includes the possible input and output formats of the GeoClaw files. The Hydro-UQ tool allows the users to upload their own GeoClaw input files for continuiation in CFD tools (e.g. OpenFOAM) on the condition that they match a file format described herein exactly. 

.. toctree::
   :maxdepth: 1

   geoclaw-theory
   geoclaw-topo
   geoclaw-runtime
   geoclaw-output


AdCirc 
--------

Currently, AdCirc is not supported in HydroUQ but could become available granted there is enough user demand. AdCirc is a popular software for storm-surge simulations and broadly excellent solutions to water-borne events. Please contact us if you would like to use AdCirc in HydroUQ in the near-future.

SimCenter formats
--------------------

Development of shallow-water flow file standards can help in the sustainable growth of community projects. SimCenter proposes the below formats for storing information related to the shallow water solvers.

.. toctree::
   :maxdepth: 1

   simcenter-topo

