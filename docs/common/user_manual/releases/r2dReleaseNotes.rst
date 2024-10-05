.. _lbl-release:

.. role:: blue

***************************
Release Notes
***************************

Version 5.1.0 (Current)
-----------------------

**Release date:** September 2024

**Highlights**

#. **Inclusion of REWET for recovery of water networks after event** (WBS 1.1.4.2.4, 1.1.3.4.1, 1.1.3.4.3, and 1.1.3.4.7)
#. **Add Datasets to Simulate High-Resolution Damages and Losses in Buried Pipeline Networks** (WBS 1.3.5.4): Expansion of the `SimCenter Damage and Loss Model Library <https://github.com/NHERI-SimCenter/pelicun/tree/master/pelicun/resources/SimCenterDBDL>`_ to include detailed water pipeline damage and loss models.
#. **Revise interface to review uncertainty in recovery response** (WBS 1.1.3.6.4)
#. **Add the capacity spectrum method to for building seismic performance estimation** (`R2D.3.2 <https://nheri-simcenter.github.io/R2D-Documentation/common/reqments/R2D.html>`_)
#. **Develop Multi-Fidelity Models in Regional Simulations** (WBS 1.3.3.1): Allowing multiple fidelities of models in a single regional analysis by allowing user-defined OpenSees models for a subset of buildings in the region to run in workflows.


Version 5.0.0
-------------

**Release date:** August 2024

**Highlights**

#. A needed release for changes required to interact with DesignSafe and new TapisV3 interface.
#. Due to AI generated spam on message board, users now directed to post questions using github discussions.
#. A procedure for estimating shear-induced seismic slope displacement for shallow crustal earthquakes is added to the earthquake event generation tool.

Version 4.1.0
-------------

**Release date:** April 2024

**Highlights**

#. Enhanced earthquake event generation toolbox to include simulation of Peak Ground Velocity (PGV) and liquefaction-induced Permanent Ground Deformation (PGD).
#. Improved BRAILS-Buildings widget for more flexible interaction with BRAILS building inventory generation capabilities, allowing:
   
   #. Import of footprint and building data from OpenStreetMaps, Microsoft Global Building Footprints dataset, FEMA USA Structures, and user-specified data sources.
   #. Use of National Structures Inventory data or other user-specified data to create a baseline building inventory.
   #. Requesting specific attributes for inventory generation.

#. Updated the damage and loss engine Pelicun to version 3.3. 

Version 4.0.1
-------------

**Release date:** January 2024

**Highlights**

#. Added support for transportation infrastructure assessment.
#. Revised earthquake scenario simulation tool interface.
#. Introduced Brails-Transportation tool for transportation infrastructure inventory generation.
#. Integration of PreTrained Surrogate Models from EE-UQ for structural analysis.

Version 3.0.0
-------------

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