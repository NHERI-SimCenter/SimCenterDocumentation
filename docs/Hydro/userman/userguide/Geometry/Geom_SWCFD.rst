.. _lbl-geom-swcfd:

Here the user needs to select the bathymetry files and solution files related to the shallow-water solutions. At present, HydroUQ can directly read the shallow water solutions from the ``GeoClaw`` solver. The bathymetry can be provided in the GeoClaw format (Type 1) or the SimCenter format. Similarly, the shallow-water solutions can be provided in the GeoClaw format or the SimCenter format.

For more information about the GeoClaw file format, check out :ref:`lbl-geoclawtopo`. Similarly, for the SimCenter formats, check out :ref:`lbl-simcentertopo`.

The other input is the direction of gravity. For this type of simulation, it is recommended to use ``-z`` for the gravity direction.

.. figure:: Geometry/figures/SWCFD.png
   :align: center
   :width: 400
   :figclass: align-center

   UI for loading bathymetry and shallow-water solution files
    
.. note::

    #. Please provide as much of the bathymetry as possible. HydroUQ will crop the required areas for the CFD simulation. 

    #. The solution files can be large in size. Hence, it is recommended to restrict the times required for the CFD simulation only. Here, it is essential to note that the boundaries can lead to unphysical accumulation if there are excessive reflections.