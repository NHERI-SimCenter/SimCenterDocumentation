.. _lbl-geom-swcfd:

-----------------------------------------------
Coupling Shallow Water and CFD Model Geometries 
-----------------------------------------------

To couple high-fidelity CFD and with simplified shallow-water equations (**SWE**), you must input the bathymetry defining files you previously used in a SWE simulation.  

.. tip::
   Please provide as much of the bathymetry as possible. HydroUQ will crop the required areas for the CFD simulation.


You must also provide the corresponding solution files from said simulation. 

.. note::
   The solution files can be large in size. Hence, it is recommended to restrict the times required for the CFD simulation only. 
   Here, it is essential to note that the boundaries can lead to unphysical accumulation if there are excessive reflections.


Once these files are provided, HydroUQ will produce a convenient graphical interface for a one-way SWE-CFD coupling in a larger UQ workflow. Namely, for GeoClaw and OpenFOAM.

.. _fig-geom-swcfd:

.. figure:: Geometry/figures/SWCFD.png
   :align: center
   :width: 400
   :figclass: align-center

   UI for loading bathymetry and shallow-water solution files into a HydroUQ workflow.
    
HydroUQ can directly read the shallow water solutions from the ``GeoClaw`` solver, so little to no effort is required regarding pre-processing for any user. See :ref:`lbl-geom-geoclaw` for more information on the GeoClaw solver. 

The bathymetry can be provided in the GeoClaw format (Type 1) or the SimCenter format. Similarly, the shallow-water solutions can be provided in the GeoClaw format or the SimCenter format.
    
For details regarding the GeoClaw file format(s), see :ref:`lbl-geoclawtopo`. For the SimCenter shallow-water format, refer to :ref:`lbl-simcentertopo`. 
