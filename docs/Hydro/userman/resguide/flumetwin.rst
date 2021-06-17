.. _lbl-flumetwin:

Wave Flume: Digital Twin
===============================

HydroUQ includes a digital twin of the wave flume. This includes a definition of the geometry and the boundary condition for the moving wall. This digital twin is of the Large Wave Flume facility at the O.H. Hinsdale Wave Research Laboratory at the Oregon State University. However, this can be adapted for any other wave flume facility as well.

Below is a template for the user to facilitate the use of the user-defined wave flume. Here, the user will define a child-class that would take precedence over the default class that uses the ``OSU wave flume``. If you would like to integrate your solver, please write to us through the |messageBoard| for more assistance.

.. literalinclude:: Template_flume.py
   :language: python