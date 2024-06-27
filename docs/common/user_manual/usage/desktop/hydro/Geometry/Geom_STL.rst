.. _lbl-geom-stl:

-------------------------------
Custom Geometry Using STL Files
-------------------------------

The ``STL`` file format is pervasive in fluid simulation software, hence HydroUQ provides support for the format.

To define a complex ocean bathymetry, you may use multiple ``STL`` files to replicate the ocean floor if they form a manifold when combined. 

Custom structures, boundaries, and other features may also be defined using  ``STL`` files. An example is shown in the HydroUQ UI below:

.. _fig-geom-stl:

.. figure:: Geometry/figures/STLfile.png
   :align: center
   :width: 400
   :figclass: align-center

   UI for loading the geometry as ``STL`` files


.. important::
   For the most robust experience, HydroUQ requires that these custom input files obey the ``STL ASCII`` format. 


For OpenFOAM simulations, the following ``STL`` files are **required** to be either produced by the user or selected from existing files: 

#. **Entry.stl** - This is the patch for the inlet of the fluid
#. **Exit.stl** - This is the patch for the outlet of the fluid
#. **Right.stl** - This is generally a wall patch on the right. Here, if one were to stand at the inlet and face the outlet, this is the wall on the right. 
#. **Left.stl** - This is generally a wall patch on the left. Here, if one were to stand at the inlet and face the outlet, this is the wall on the left. 
#. **Bottom.stl** - This is the ocean floor or the flume bathymetry
#. **Top.stl** - This is generally a surface high enough such that the air velocity does not affect the wind-water interface
#. **Buildings.stl** - This is the building of interest on which we aim to determine the structural response
#. **Otherbuildings.stl** - These are the other buildings around the structure of interest and could affect the flow around the structure of interest.


.. warning::
   Failure to provide any of the above files will result in an error for HydroUQ OpenFOAM simulations.


.. note::
   It is necessary to provide each of these ``STL`` files separately, not preemptively combined into a single file.

