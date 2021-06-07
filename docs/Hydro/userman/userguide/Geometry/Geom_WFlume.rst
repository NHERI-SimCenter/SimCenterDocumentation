.. _lbl-geom-wflume:

This constitutes the geometric definition of the wave flume. This is the first step in the description of the digital twin for the wave flume. One of the inputs is the direction of gravity. For this type of simulation, it is recommended to use ``-z`` for the gravity direction.

**Standard OSU flume**

The flume geometry can be defined using the standard flume definition. Here, a common flume geometry for the Large Wave Flume at the O.H. Hinsdale Wave Research Laboratory in Oregon State University. This is selected as shown in :numref:`Flume02`.

.. _Flume02:

.. figure:: Geometry/figures/Flume02.png
   :align: center
   :width: 400
   :figclass: align-center

   Using the standard wave flume geometry

The geometry of the wave flume is defined by providing the coordinates of the external profile of the wave flume, as shown below.
    
.. figure:: Geometry/figures/WaveFlumeGeo.png
   :align: center
   :width: 500
   :figclass: align-center

   The coordinates representing the external profile of the wave flume

The coordinates of the standard wave flume are provided below.

.. code-block:: Fortran

   -2.085,0
   14.2748,0
   14.2748,0.1524
   17.9324,0.1524
   28.9052,1.15
   43.5356,1.7526
   80.116,1.7526
   80.116,4.572
   -2.085,4.572

**Definition by coordinates**

Alternatively, the user can define their own custom wave-flume geometry, as shown below. Here, the user needs to specify the ``x`` (along the length) and ``z`` (along the height) coordinates in a tabular format. Additionally, breadth also needs to be provided to define the wave flume geometry uniquely. This is similar to the geometry defined above for the standard OSU flume. HydroUQ constructs the STL files necessary for the CFD simulation process using the provided coordinates and the breadth.

.. figure:: Geometry/figures/Flume01.png
   :align: center
   :width: 400
   :figclass: align-center

   Defining a custom wave-flume geometry

.. note::

    #. The breadth of the flume needs to be greater than 0. If the breadth is too small, this can lead to numerical issues.