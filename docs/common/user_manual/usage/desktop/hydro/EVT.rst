.. _lbl-EVTHydro:

******************************************
EVT: Hydro Events
******************************************

The ``Hydro EVT`` is used to setup the flow parameters related to the water-borne hazard event. This can either be a coupling between the shallow-water and CFD solver or using the CFD solver alone. The steps of the setup process for the event have been kept nearly similar to that often used in Finite Element Method to make it easier for researchers from structural engineering background to easily use this application. This includes ``project settings`` >> ``geometry`` >> ``meshing`` >> ``materials`` >> ``initial conditions`` >> ``boundary conditions`` >> ``solver settings``. These steps are available through a tree-structure as shown in :numref:`EVTSettings`.

.. _EVTSettings:

.. figure:: figures/HydroSteps.png
   :align: center
   :figclass: align-center

   The steps involved in setup of the ``Hydro`` event

Each of the above steps in the setup process differs depending on the type of simulation considered. They will be outlined in detail below:

.. toctree::
    :maxdepth: 1

    Project
    Geometry
    Meshing
    Materials
    Initial
    Solver
