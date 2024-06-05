.. _lbl-BodiesMPM:

======
Bodies
======

Bodies are any physical object that is not represented as a boundary condition. They can be water, debris, structures, etc., but not, for instance, a boundary condition like a moving velocity boundary condition.

This section discusses the setup of bodies in the model.

.. contents:: Table of Contents
   :local:
   :backlinks: none



.. include:: MaterialMPM.rst


.. _lbl-GeometriesMPM:

----------
Geometries
----------

There are four aspects related to the definition of geometry, namely geometry of the ocean floor or wave flume, buildings or specimens, floating bodies, and shallow water to CFD interface. This section discusses the setup of all aspects of geometry.


.. _lbl-AlgorithmMPM:

---------
Algorithm
---------

The algorithm tab is used to define the algorithmic parameters for the body. 


.. _lbl-PartitionsMPM:

----------
Partitions
----------

The partitions tab is used to distribute a body across the available hardware partitions, e.g. a Graphics Processing Unit or supercomputer node, for parallel computation.


.. _lbl-DebrisMPM:

------
Debris
------

Currently, HydroUQ only supports floating bodies in the Material Point Method Event. This may expand to include OpenFOAM in an upcoming versions of |app|.
