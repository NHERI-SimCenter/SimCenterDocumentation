.. _lbl-EVTHydro:

*****************
EVT: Hydro Events
*****************

The event panel presents the user with a drop-down menu with a list of available event applications. 

Event applications are applications that, given the building and user-supplied data inputs, will generate a list of events (i.e., typically time-dependent loads that represent natural disasters) for the building. 

The ``Hydro EVT`` is used to setup the flow parameters related to the water-borne hazard event. This can either be a coupling between the shallow-water and CFD solver or using the CFD solver alone. 

The following options are available in the drop-down menu:

.. toctree-filt::
   :maxdepth: 4

   general
   coupled
   MPM


.. note::
   :sup:`*` The new ``MPM`` module is only available in the current release |tool version| as a standalone ``Tools`` app, though it is designed to be an EVT option. It will be fully implemented as a workflow EVT in the next release.



.. The steps of the setup process for the event have been kept nearly similar to that often used in Finite Element Method to make it easier for researchers from structural engineering background to easily use this application. This includes ``project settings`` >> ``geometry`` >> ``meshing`` >> ``materials`` >> ``initial conditions`` >> ``boundary conditions`` >> ``solver settings``. These steps are available through a tree-structure as shown in :numref:`EVTSettings`.

.. .. _EVTSettings:

.. .. figure:: figures/HydroSteps_MPM.png
..    :align: center
..    :figclass: align-center

..    The steps involved in setup of the ``Hydro`` event
