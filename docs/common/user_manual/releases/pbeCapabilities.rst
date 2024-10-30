.. _lbl-capabilities_pbe:
.. role:: blue

************
Capabilities
************

The following functionality is available in **version 4.1** of the |app| that was released on **September 30, 2024**.

Structural Response
===================
Obtain a set of response quantities that can characterize the demands acting on the structure under the natural hazard event.

The following options are available:

#. Use the integrated EE-UQ modules to set up a seismic response simulation workflow. Standard earthquake EDPs are automatically recorded and passed on to the damage and loss calculation.
#. Import external demand data in tabulated format. This option supports any arbitrary hazard and corresponding EDPs as well as any calculation method performed outside of the PBE Application.


Damage and Loss
===============
Define a set of interconnected models in the Pelicun framework that describe the number and locations of vulnerable components in a structure; the demands acting on each component; and the resulting damage and its repair consequences

The following options are available:

#. Use built-in libraries and methods for a standard FEMA P-58 or Hazus Earthquake assessment.
#. Extend FEMA P-58 or Hazus analyses with additional components in your own component library
#. Develop new methods by creating your own damage process and loss map


Post-Disaster Performance and Recovery
======================================
Use functional recovery simulation engines to estimate the recovery process and the time it takes to reach important milestones during recovery.

The following options are available:

#. ARUP REDi Seismic Downtime Model


Uncertainty Quantification
==========================
Sample the prescribed random input variables and obtain realizations of the outputs by executing the workflow with each input realization from the generated sample. 

The underlying UQ engines let you leverage the following techniques:

#. Forward propagation: Define a set of random input parameters and perform Monte Carlo simulations to obtain a corresponding sample of output parameters.
#. Surrogate models: Generate training data, develop, and utilize surrogate models that employ Gaussian Process and Probabilistic Learning on Manifolds techniques.