.. _lbl-release:

***************************
Release Notes
***************************

Version 1.0
=================

Version 1.0.0
----------------

**Release date:** Apr 30th, 2021

#. Supports run on DesignSafe only. Local run on the user's desktop is not supported.

#. |app| ``v1.0.0`` currently requires the users to ensure that the inputs provided are 

#. Supports two-phase isothermal flows only. Water and air are considered as the two primary phases. However, this can be modified in the material properties to accommodate any other alternative two-phases instead.

#. **Simulation types**:
    a. CFD to resolve SW (Using SW results), CFD using bathymetry data, CFD of wave flume is supported.
    c. For simulation type with SW-CFD coupling, ``v1.0.0`` considers one point on the interface. However, if you would like more flexibility, please let us know using the :ref:`lblBugs`.

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