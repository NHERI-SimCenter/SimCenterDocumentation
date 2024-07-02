.. _lbl-release:
.. role:: blue

*************
Release Notes
*************

Version 3.1
===========

.. dropdown:: Version 3.1.0 (:blue:`Current`)
    :open:

    **Release date:** April 1st, 2024

    
    **Simulation Types**:

        a. Added ``Material Point Method`` via ``ClaymoreUW``.
        b. Updated ``Finite Volume Method`` + ``Finite Element Method`` via ``FOAMySees`` (``OpenFOAM`` + ``OpenSees``). 
        c. Partially deprecating ``Shallow Water Equations`` + ``Finite Volume Method`` via (``GeoClaw`` + ``OpenFOAM``). Pending an update in an upcoming minor release.

    **Physics**

        Broad capabilities of the underlying physics simulation now include:

        a. Large deformations
        b. Nonlinear materials
        c. Multi-material and multi-phase interaction
        d. Debris-fluid-structure interaction

    **Debris**

        a. Added debris modeling to ``MPM`` simulations.
        b. Added support for complex debris geometries (e.g. vehicles, shipping crates, composed primitives).
        c. Added support for advanced debris material models (e.g. ``Fixed-Corotated``, ``Neo-Hookean``, ``Drucker-Prager``, ``Non-Associative Cam-Clay``).


    **User Interface**

        Significant overhaul of the Event GUI to allow for a more intuitive and user-friendly experience. Includes backend updates to the schema and application logic to support the new features.

        #. **Settings**

            * Panel for setting simulation parameters (e.g. time step, characteristic length, domain size, CFL number).
            * Panel for setting computer parameters (e.g. number of cores, number of GPUs, etc.).
            * Panel for setting similitude parameters (e.g. Froude scale, Cauchy scale, etc.).

        #. **Bodies**

            Any entity in a simulation that is not a boundary condition or sensor is considered a ``Body``. ``Bodies``, the collection of ``Body`` objects, may be composed of particles, or meshes. Each ``Body`` is specified by its ``Material``, ``Geometry``, ``Algorithm``, and ``Partitions``.

            #. **Material**

                #. Supports ``elastic``, ``hyperelastic``, and ``elasto-plastic`` material models.
                
                #. New constitutive laws:

                    * ``J-Fluid``: Weakly-compressible isotropic fluid with viscous shear stress. Uses the Tait-Murnaghan equation of state. 
                    * ``Fixed-Corotated``: Hyperelastic material model for plastic and rubber-like materials.
                    * ``Neo-Hookean``: Hyperelastic material model for plastic and rubber-like materials.
                    * ``Drucker-Prager``: Applicable to granular materials, concrete, and other materials with a yield surface.
                    * ``Non-Associative Cam-Clay``: Applicable to clays, concrete, and other topology-changing material bodies


            #. **Geometry**

                * Added a composable geometry editor for creating and modifying geometry.
                * Implemented boolean operations for geometry (e.g. union, intersection, difference).
                * Implemented array operations for geometry (e.g. create an array of the same geometry at specified spacings in X, Y, and Z).
                * Implemented rotation operations for geometry (e.g. rotate a geometry about an axis by a specified angle).
                * Implemented translation operations for geometry (e.g. translate a geometry by a specified distance in X, Y, and Z).
                * Implemented geometry file import from ``.sdf`` files.
                * Added geometry primitives (e.g. ``sphere``, ``box``, ``cylinder``).

            #. **Algorithm**

                * Implemented Affine Particle-in-Cell (APIC) algorithm for ``MPM``
                * Implemented Fluid-Implicit Particles (FLIP) algorithm for ``MPM``
                * Implemented Affine-Separable Fluid-Implicit Particles (ASFIP) algorithm for ``MPM``
                * Implemented F-Bar volumetric antilocking algorithm for ``MPM``
                * Implemented quadratic B-Spline shape functions for ``MPM``

            #. **Partitions**

                * Bodies may be split across multiple hardware partitions.
                * Accelerates simulation times by running multiple bodies in parallel.
                * A valid hardware partition may be a core, a GPU, or a node in an HPC cluster.
                * Each partition may hold some maximum number of bodies at once (specific to the system on which the simulating tool was compiled).

        #. **Boundaries**

            Any object in a simulation that is not a sensor or body is considered a ``Boundary``. ``Boundaries``, the collection of ``Boundary`` objects, are enforced boundary conditions that may apply to parts of the simulation (e.g. on grid nodes or particles).

            * Added boundaries for geometry primitives (e.g. ``sphere``, ``box``, ``cylinder``).
            * Added selectable contact models (e.g. ``Sticky``, ``Slip``, ``Separable``).
            * Added boundaries for the ``OSU LWF`` and ``WU TWB`` digital twin bathymetries. 
            * Added boundary for the ``OSU LWF`` moving piston wave-maker. 
            * Implemented array operations for boundary conditions (e.g. instance a boundary at specified spacings in X, Y, and Z).

        #. **Sensors**

            Any object in a simulation that is not a boundary condition or body is considered a ``Sensor``. ``Sensors``, the collection of ``Sensor`` objects, are used to monitor the simulation, collect desired data, reduce said data, and report the aggregated output as a time-series. In effect, they replicate instruments/sensors used in experiments (e.g. load-cells, wave-gauges, piezometers, velocimeters).

            * Sensors may be placed on numerical bodies (e.g. on ``particles`` or ``grid-nodes`` for ``MPM``) to monitor the simulation.
            * Supports force, pressure, velocity, and elevation sensors by default.
            * Custom sensors may be added to the simulation through the GUI.
            * Supports automatic reduction operations (e.g. sum, average, max, min) to reduce sensor data to a single scalar or vector value per sampling step.
            * Allows specification of sensor output frequency.

        #. **Outputs**

            Collection of simulation settings that do not affect the simulation itself, but rather the output it gives to the user.

            * Supports output of simulation geometry data in the form of ``.bgeo`` files, ``.vtk`` files, and ``.csv`` files.
            * Supports output of simulation sensor data in the form of ``.csv`` and ``.txt`` files.
            * Supports output of simulation state data in the form of ``.bgeo`` files.
            * Enable/disable tracking of and output of simulation energy (kinetic, strain, etc.).
            * Enable/disable output of simulation checkpoints (allow for a simulation to be resumed if stopped).

    **Visualization**

        * Enabled visualization of the Event (``EVT``) using ``Qt3D``
        * Added support for mouse controls of the camera in 3D visualization.
        * Added support for visualizing simulation ``Bodies`` in 3D.
        * Added support for visualizing simulation ``Boundaries`` in 3D.
        * Added support for visualizing simulation ``Sensors`` in 3D.

    **Digital Twins**

        * Added Oregon State University's Large Wave Flume (``OSU LWF``) as a digital twin for ``MPM``.
        * Added Waseda University's Tsunami Wave Basin (``WU TWB``) as a digital twin for ``MPM``.
        * Digital twins now allow for debris and floating bodies.

    **DesignSafe Support and Hardware**

        * Multi-GPU accelerated simulations are now supported in certain simulation types (e.g. ``ClaymoreUW MPM``).

        * Updated support for the TACC Frontera supercomputer:

            * Access the ``rtx`` queue. Includes 4 NVIDIA RTX Quadro 5000 GPUs (16GB memory each).

        * Added support for the TACC Lonestar6 supercomputer:

            * Access the ``gpu-a100`` queue. Includes 3 NVIDIA A100 GPUs (40GB memory each).
            * Access the ``gpu-a100-small`` queue. Includes 1 NVIDIA A100 GPU (40GB memory).

        * Updated support for the Tapis API used to run jobs remotely.

    **Tools**

        * Events (``EVT``) may now run as standalone tools (i.e. does not require a SimCenter workflow for UQ, etc.)
        * Added ``Tapis`` API support for running Tools remotely, allowing for specialized ``Tapis`` applications and system/queue selection


    **Examples**

        * Added example simulations for ``OSU LWF`` digital twin in ``FOAMySees`` 
        * Added example simulations for ``OSU LWF`` digital twin in ``ClaymoreUW``.
        * Added example simulations for ``WU TWB`` digital twin in ``ClaymoreUW``.


Version 2.0
=================

.. dropdown:: Version 2.0.0
    :open:

    **Release date:**  November 30th, 2023

        #. **Simulation types**:
        
            b. ``Finite Volume Method`` + ``Finite Element Method`` via ``FOAMySees`` (``OpenFOAM`` + ``OpenSees``). Two-way FSI coupling between CFD and structural solvers. 

        #. **Digital Twin**
        
            a. ``OSU LWF`` digital twin now supports ``FOAMySees`` (``OpenFOAM`` + ``OpenSees``). 
            
            b. Added options for adjustable bathymetry and flexible two-way coupled structures.
        
        #. **New multi-model and multi-fidelity modeling options**


Version 1.0
=================

.. dropdown:: Version 1.0.0
    :open:

    **Release date:** Apr 30th, 2021

    #. Supports run on DesignSafe only. Local run on the user's desktop is not supported.

    #. |app| ``v1.0.0`` currently requires the users to ensure that the inputs provided are 

    #. Supports two-phase isothermal flows only. Water and air are considered as the two primary phases. However, this can be modified in the material properties to accommodate any other alternative two-phases instead.

    #. **Simulation types**:

        a. CFD to resolve SW (Using SW results), CFD using bathymetry data, CFD of wave flume is supported.
        b. For simulation type with SW-CFD coupling, ``v1.0.0`` considers one point on the interface. However, if you would like more flexibility, please let us know using the :ref:`lblBugs`.

    #. **Geometry**: 

        a. Geometry can be imported as Bathymetry files (GeoClaw format - type 1), STL files, or the Hydro flume digital twin. 
        b. Shallow-water to CFD interface can be imported as a ``.csv`` file only.
        c. Buildings of cuboid shapes are supported in ``v1.0.0``. For other shapes, the user can upload them as an STL file. The buildings need to be specified in the table or can be generated parametrically. Importing buildings as a ``.csv`` file is not currently supported in ``v1.0.0`` but can be requested using the :ref:`lblBugs`. 
        d. Floating bodies and debris modeling are not supported in ``v1.0.0``. Support will be added in upcoming versions. If you are interested in this feature, please write to us at :ref:`lblBugs`.

    #. **Meshing**: 
    
        a. Supports blockMesh and snappyHexMesh for internal meshing.
        b. Supports import for the following mesh formats: Ansys Fluent (.msh), Ansys I-DEAS (.ans), CFX mesh (.geo), GAMBIT mesh (.neu), Gmsh mesh (.msh).
        c. Supports import of OpenFOAM mesh dictionaries, namely the blockMeshDict and snappyHexMeshDict. Additionally, surfaceFeatureExtractDict is required if STL files are used to define the geometry.

    #. **Materials**: 
        a. Supports Newtonian materials only.

        b. Supports kinematic viscosity and density of the two phases in addition to the surface tension between the fluids.

    #. **Initial conditions**: 

        a. For CFD simulations that resolve the shallow-water solutions, the initial conditions are derived from the shallow-water solutions.
        b. For all other simulation types, the user-specified initial conditions include phase only. 

    #. **Boundary conditions**: 

        a. The boundary conditions can be selected based using standard patch names. Here standard patches include entry/exit / inlet/outlet / left/right. 
        b. Velocity boundary conditions for inlet conditions include shallow-water solutions, moving wall, and constant velocity; for outlet conditions include zeroGradient and inletOutlet
        c. Pressure boundary conditions include zeroGradient and fixedValue. Alternatively, the user can also leave the default option. An appropriate boundary condition relevant to the velocity boundary will be chosen.
        d. It is recommended to use the wall boundary conditions for walls

    #. **Domain decomposition and solver**: 

        a. Allows simple decomposition techniques from OpenFOAM.
        b. Can set start and end times for simulation
        c. Can set time intervals and write intervals
        d. Restarting facility is supported

    #. **Turbulence**:
    
        a. Presently, only RANS is supported for turbulence modeling.
        b. If you would like to use LES, please let us know about it using :ref:`lblBugs`.
