.. _lbl-release_HydroUQ:
.. role:: blue

***************************
Release Notes
***************************

Version 3.1
=================

    .. dropdown:: Version 3.1.0 (:blue:`Current`)
        :open:

        **Release date:** April 1st, 2024

        **Highlights**

            #. **Simulation types**:

                a. Material Point Method via ClaymoreUW.

                b. Finite Volume Method + Finite Elements via FOAMySees (OpenFOAM + OpenSees). Two-way FSI coupling between CFD and structural solvers. 

            #. **Physics**

                a. Large deformations
                b. Nonlinear materials
                c. Multi-material and multi-phase interaction
                d. Debris-fluid-structure interaction

            #. **Materials**: 

                a. Supports elastic, plastic, hyperelastic, and elasto-plastic materials in MPM.

                b. Supports kinematic viscosity and density of the two phases in addition to the surface tension between the fluids in OpenFOAM.

            #. **Tools**
            
                a. Certain Events (EVT) may now run as standalone tools (i.e. does not require a SimCenter workflow for UQ, etc.). Simplifies implementation of new modules.

                b. Added Tapis API support for running Tools remotely, allowing for specialized Tapis applications and system/queue selection

            #. **Digital Twins**

                a. Digital twins now allow for debris and floating bodies.

                b. Added Oregon State University's Large Wave Flume (OSU LWF) as a digital twin for MPM and FOAMySees.

                c. Added Waseda University's Tsunami Wave Basin (WU TWB) as a digital twin for MPM.

            #. **DesignSafe Support and Hardware**

                a. Multi-GPU accelerated simulations now supported in certain simulation types (e.g. ClaymoreUW MPM).

                b. Updated support for the TACC Frontera supercomputer.

                    * Access the 'rtx' queue. Includes 4 NVIDIA RTX Quadro 5000 GPUs (16GB memory each).

                b. Added support for the TACC Lonestar6 supercomputer.

                    * Access the 'gpu-a100' queue. Includes 3 NVIDIA A100 GPUs (40GB memory each).
                    * Access the 'gpu-h100' queue. Includes 2 NVIDIA H100 GPUs (80GB memory each).

                c. Updated support for the Tapis API (used to run jobs remotely).



Version 2.0
=================
    .. dropdown:: Version 2.0.0
        :open:

        **Release date:**  November 30th, 2023

            #. **Simulation types**:
            
                a. Two-way FSI coupling between CFD and structural solvers. Uses FOAMySees (OpenFOAM + OpenSees) with coupling library preCICE.

            #. **Digital Twin**
            
                a. OSU LWF digital twin now supports FOAMySees (OpenFOAM + OpenSees). Added options for adjustable bathymetry and flexible two-way coupled structures.
            
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

            a. The boundary conditions can be selected based using standard patch names. Here standard patches include entry / exit / inlet / outlet / left / right. 
            b. Velocity boundary conditions for inlet conditions include shallow-water solutions, moving wall, and constant velocity; for outlet conditions include zeroGradient and inletOutlet
            c. Pressure boundary conditions include zeroGradient and fixedValue. Alternatively, the user can also leave the default option. An appropriate boundary condition relevant to the velocity boundary will be chosen.
            d. It is recommended to use the wall boundary conditions for walls

        #. **Domain decomposition and solver**: 

            a. Allows simple decomposition techniques from OpenFOAM.
            b. Can set start and end times for simulation
            c. Can set time interval and the write intervals
            d. Restarting facility is supported

        #. **Turbulence**:

            a. Presently, only RANS is supported for turbulence modeling.
            b. If you would like to use LES, please let us know about it using :ref:`lblBugs`.
