.. _lbl-geom-wflume:

-------------------
Wave Flume Geometry
-------------------

This sections discusses the geometric definition for wave flume simulations. This is the first step in the description of a digital twin of an experimental set in said flume facilities. 

For instance, one of the inputs required to use a simulation to represent a real-world representation is the direction of gravity. For fluid simulations, it is often recommended to use ``-z``, but ``-y`` is a common choice as well. Other parameters may entail wave-maker specifications, concrete wall roughness, the basic wave flume geometry height / width / depth, among others. 

Bathymetry, i.e. sloped panels that are often present in wave flumes to influence wave development, are important for replicating experiments digitally and so an adjustable bathymetry creator is present in HydroUQ. The wave flume geometry in particular is a critical parameter, as it determines whether a full wave flume simulation is done or a truncated one (i.e. if reduced values were chosen). Bathymetry, i.e. sloped panels that are often present in wave flumes to influence wave development, are likewise important and supported in HydroUQ. 

The basic domain geometry of the wave flume is defined by providing the coordinates of the external profile of the wave flume. The coordinates of the standard wave flume are provided below. 

.. _FlumeOSU:

Definition via Wave Flume Digital Twins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The flume geometry can be defined using a standard flume definition, i.e. a digital twin. Here, a common flume geometry for the Large Wave Flume at the O.H. Hinsdale Wave Research Laboratory in Oregon State University. This is selected as shown in :fig:`Flume02`.


.. _Flume02:

.. figure:: Geometry/figures/Flume02.png
   :align: center
   :width: 400
   :figclass: align-center

   Using the standard wave flume geometry


The geometry of the wave flume is defined by providing the coordinates of the external profile of the wave flume, as shown in :fig:`WaveFlumeGeo` below.
   
.. _WaveFlumeGeo:

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



.. _FlumeCoord:

Definition by Coordinates
^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, you may define your own custom wave-flume geometry, as shown in :fig:`Flume01`. Specify the ``x`` (along the length) and ``z`` (along the height) coordinates in a tabular format. Additionally, breadth must be provided for 3D simulations.

HydroUQ constructs the digital geometry repesentation, i.e. ``STL`` files, necessary for common CFD simulations using the provided coordinates and the breadth automatically.

.. _Flume01:

.. figure:: Geometry/figures/Flume01.png
   :align: center
   :width: 400
   :figclass: align-center

   Defining a custom wave-flume geometry


.. important::
   The breadth of the flume needs to be greater than 0, and typically a multiple of 4+ times the characteristic simulation length (e.g. a typical grid-cell width). If the breadth is too small, this can lead to numerical issues that may crash the simulation or over-constrain fluid motion.

