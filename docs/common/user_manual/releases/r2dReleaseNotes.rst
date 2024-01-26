.. _lbl-release:

.. role:: blue

***************************
Release Notes
***************************

Version 4.0.1 (Current)
-----------------------

**Release date:** Jan. 2024

**Highlights**

#. Support the assessment of transportation infrastructure.
#. Revised interface for earthquake scenario simulation tool.
#. Added Brails-Transportation tool to generate transportation infrastructure inventory.
#. Allow using PreTrained Surrogate Models from EE-UQ as structural analysis models. 


Version 3.0.0
-----------------------

**Release date:** May. 2023

**Highlights**

#. Revised Interface, added new Tools section and moved some existing applications to that pulldown
#. Hazard Occurance Model added to earthquake selection
#. Revised input file format in anticipation of multiple asset types with multiple options for each

Version 2.2.0
-------------

**Release date:** Sept 2022

**Highlights**
   
#. Obtain information from Census and ARC
#. Updated ground motion input options for OpenQuake
   
Version 2.1.0
-------------

**Release date:** March 2022

**Highlights**
   
#. Ability to perform regional site response analysis taking motions at rock to surface
#. Ability to import hazards as a raster
#. Ability to employ custom fragility functions in Pelicun DL framework
#. Support of tsunami hazards
#. Ability to import population demographics from census and merge with building inventory
   
Version 2.0.0
-------------
**Release date:** Dec. 2021

#. QGIS integrated into R2D with the ability to:

   #. load several types of GIS files into R2D to visualize and extract information
post-process results based on advanced queries and expression filters
join external databases to GIS features to add additional information for pre- and post-processing
export GIS layers into many supported formats for viewing in other GIS applications

#. Filtering of assets to include in an analysis based on advanced queries and expressions

#. OpenQuake source selection tool

   #. OpenQuake Scenario-Based Seismic Hazard Analysis to calculate intensity measure from OpenQuake rupture sources
   #. OpenQuake Classical Probabilistic Seismic Hazard Analysis to calculate intensity measures from OpenQuake seismic source and ground motion logic trees

#. Widget to import building inventory in ShapeFile format

version updates to 2.0.0 as older versions run at design-safe will not load due to changes in backend.

Version 1.0.0
-------------

Initial Release allows assessment of impact of earthquake on a region

#. Ground motion Selection using EarthquakeScenario application to obtain scenario specific ground motions for user defined scenario utiling PEER NGA & user defined inputs
#. Building Inventory input by user
#. Building Modeling utilizing MDOF-LU
#. Building Loss Estimation using Pelicun and Hazus fragilities & consequence function.
#. Interface incorporated ArcGis


