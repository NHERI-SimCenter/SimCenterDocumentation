.. _lbl-swcfdinter:

SW / CFD Interface
===============================

HydroUQ allows an interface between two-dimensional shallow-water solver (presently, GeoClaw) and three-dimensional CFD solver (presently, OpenFOAM). Here, depth-averaged velocities obtained as a solution from the shallow-water solver is provided as initial and boundary condition to the CFD solver. HydroUQ uses an interchangeable workflow.

This workflow facilitates the users to use the solutions from other user-defined shallow-water solvers instead of those from GeoClaw. Below is a template for the user to facilitate use of the solutions from other user-defined shallow-water solvers. Here, user will define a child-class that would take precedence over the default class that uses the ``sw-cfd-interface``. If you would like to integrate your shallow-water solver as input, please write to us through the |messageBoard| for more assistance.

.. literalinclude:: Template_SWCFDInter.py
   :language: python