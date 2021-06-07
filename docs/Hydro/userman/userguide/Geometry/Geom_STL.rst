.. _lbl-geom-stl:

Here the user needs to provide the ``STL`` files related to the geometry here of the ocean floor. In addition, it is required to provide separate ``STL`` files for all the boundaries and buildings. The files need to be in the 'STL ASCII format. The files need to be named as

#. **Entry.stl** - This is the patch for the inlet of the fluid
#. **Exit.stl** - This is the patch for the outlet of the fluid
#. **Right.stl** - This is generally a wall patch on the right. Here, if one were to stand at the inlet and face the outlet, this is the wall on the right. 
#. **Left.stl** - This is generally a wall patch on the left. Here, if one were to stand at the inlet and face the outlet, this is the wall on the left. 
#. **Bottom.stl** - This is the ocean floor or the flume bathymetry
#. **Top.stl** - This is generally a surface high enough such that the air velocity does not affect the wind-water interface
#. **Buildings.stl** - This is the building of interest on which we aim to determine the structural response
#. **Otherbuildings.stl** - These are the other buildings around the structure of interest and could affect the flow around the structure of interest.

The other input is the direction of gravity. For this type of simulation, it is recommended to use ``-z`` for the gravity direction.

.. figure:: Geometry/figures/STLfile.png
   :align: center
   :width: 400
   :figclass: align-center

   UI for loading the geometry as ``STL`` files
    
.. note::

    #. It is necessary to provide each of these ``STL`` files separately. Hydro-UQ uses them to determine the boundary conditions accurately.