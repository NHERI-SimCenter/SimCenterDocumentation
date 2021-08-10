.. _lbl-geom-bathy:

Here the user needs to select the bathymetry files of the ocean floor. At present, HydroUQ can directly read the bathymetry provided in the GeoClaw format (Type 1) or the SimCenter format. For more information about the GeoClaw file format, check out :ref:`lbl-geoclawtopo`. Similarly, for the SimCenter formats, check out :ref:`lbl-simcentertopo`.

The other input is the direction of gravity. For this type of simulation, it is recommended to use ``-z`` for the gravity direction.

.. figure:: Geometry/figures/Bathy.png
   :align: center
   :width: 400
   :figclass: align-center

   UI for loading bathymetry of the ocean floor
    
.. note::

    #. The entire bathymetry provided is considered for the CFD simulation. Hence, please be mindful of the model size, especially if the bathymetry is very rough. A very irregular bathymetry can require refined meshes leading to longer computational times.