.. _lbl-cfdsolvers:

CFD Solver
===============

HydroUQ uses an interchangeable workflow that relates two-dimensional shallow-water solvers as inputs. The workflow connects three-dimensional CFD (here OpenFOAM) and FEA (here OpenSees) solvers with the UQ engine (here Dakota). However, it is feasible that a user might intend to use a CFD solver other than OpenFOAM. In this case, you can provide a python script that reads the ``dakota.json`` file to write input files required for the user-defined solver.

Below is a template for the user to facilitate the use of the user-defined solver. Here, the user will define a child-class that would take precedence over the default class that uses the ``OpenFOAM`` solver. If you would like to integrate your solver, please write to us through the |messageBoard| for more assistance.

.. literalinclude:: Template_solver.py
   :language: python