.. _lbl-release:

.. role:: blue

***************************
Release Notes
***************************

Version 4.1.0 (Current)
-----------------------

**Release date:** April 2024

**Highlights**

#. Enhanced earthquake event generation toolbox to include simulation of Peak Ground Velocity (PGV) and liquefaction-induced Permanent Ground Deformation (PGD).
#. Improved BRAILS-Buildings widget for more flexible interaction with BRAILS building inventory generation capabilities, allowing:
   
   #. Import of footprint and building data from OpenStreetMaps, Microsoft Global Building Footprints dataset, FEMA USA Structures, and user-specified data sources.
   #. Use of National Structures Inventory data or other user-specified data to create a baseline building inventory.
   #. Requesting specific attributes for inventory generation.

#. Updated the damage and loss engine Pelicun to version 3.3. 

Version 4.0.1
-----------------------

**Release date:** January 2024

**Highlights**

#. Added support for transportation infrastructure assessment.
#. Revised earthquake scenario simulation tool interface.
#. Introduced Brails-Transportation tool for transportation infrastructure inventory generation.
#. Integration of PreTrained Surrogate Models from EE-UQ for structural analysis.

Version 3.0.0
-----------------------

**Release date:** May 2023

**Highlights**

#. Interface revision with a new Tools section and reorganization of existing applications.
#. Addition of Hazard Occurrence Model for earthquake selection.
#. Updated input file format to support multiple asset types with multiple asset subtypes.

Version 2.2.0
-------------

**Release date:** September 2022

**Highlights**
   
#. Enhanced data acquisition from Census and ARC.
#. Updated ground motion input options for OpenQuake.
   
Version 2.1.0
-------------

**Release date:** March 2022

**Highlights**
   
#. Regional site response analysis capability for motion translation from rock to surface.
#. Hazard import as raster.
#. Custom fragility function support in Pelicun DL framework.
#. Tsunami hazard support.
#. Import population demographics from census and integration with building inventory.
   
Version 2.0.0
-------------
**Release date:** December 2021

**Highlights**

#. Integration of QGIS into R2D, enabling:

   #. Loading of various GIS files for visualization and information extraction.
   #. Post-process results based on advanced queries and expression filters.
   #. External database joining to GIS features for enhanced pre- and post-processing.
   #. Export of GIS layers in multiple formats for external GIS application viewing.

#. Advanced query and expression-based asset filtering for analysis inclusion.

#. OpenQuake source selection tool enhancements:

   #. Scenario-Based and Classical Probabilistic Seismic Hazard Analysis using OpenQuake for intensity measure calculation.

#. Building inventory import widget supporting ShapeFile format.

Note: Version updates to 2.0.0 are critical as older versions will not run on design-safe due to backend changes.

Version 1.0.0
-------------

Initial Release for earthquake impact assessment on regions:

#. Earthquake Scenario application for ground motion selection based on PEER NGA & user-defined inputs.
#. User-defined building inventory input.
#. Building modeling with MDOF-LU.
#. Building loss estimation utilizing Pelicun and Hazus fragilities and consequence functions.
#. ArcGIS integrated interface.
```