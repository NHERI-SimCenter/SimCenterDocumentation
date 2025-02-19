.. _lbl-capabilities_eeuq:
.. role:: blue

************
Capabilities
************

**Version** |tool version| of |app| was released in **Nov 25, 2024**, introducing significant updates and enhancements. This document outlines the functionalities available in the current version, highlighting new features and improvements in :blue:`blue`.

Major updates from Version 4.0 are adding liquefaction-induced ground deformation estimation in the :blue:`regional earthquake event generation tool`, refactored :blue:`regional inventory generation tool BRAILS`, and upgraded :blue:`damage and loss engine Pelicun`. 

**Release date:** November, 2024

#. **Hazard Types**:

    * :ref:`User specified earthquakes <lbl-UserSpecifiedGroundMotions>`.
    * :ref:`User specified hurricanes <lbl-UserSpecifiedHurricane>`.
    * :ref:`ShakeMap Scenarios <lbl-shakeMapEQScenarios>` for earthquake events, allowing the import of ShakeMap `XML grid file <https://usgs.github.io/shakemap/manual4_0/ug_products.html#xml-grid>`_, PGA Contours (.json) file, and Fault Rupture (.json) file.
    * :ref:`Raster Defined Hazard <lbl-rasterDefinedHazard>` for Earthquake, Hurricane, Inundation.
    * **GIS Defined Hazard** for Earthquake, Hurricane, Inundation.

#. **Asset Types**:

    * :ref:`Buildings <lbl-ASDBuildings>`:
		a. Load building database in a ``.csv`` format.
		b. Load building database in a ``.gis`` format.
    * :ref:`Transportation infrastructure <lbl-ASDTransport>`:
		a. Load transportation infrastructure database in SimCenter's ``.geojson`` format.
		b. Load transportation infrastructure database in common ``.gis`` format.
    * :ref:`Water Distribution Network <lbl-ASDWaterDistributionNetwork>`:
		a. Load water distribution network database in EPANet's format (used for REWET).
		b. Load water distribution network from .csv files representing nodes and pipelines.
		c. Load water distribution network from GIS files representing nodes and pipelines.
		d. Load water distribution network database in EPANet's format.
		   
	
#. **Asset Modeling**: 
    * :ref:`Buildings <lbl-MODBuildings>`:
		a. MDOF-LU (MDOF shear building model).
		b. OpenSeesPy building generator.
		c. None (Used for the IMasEDP and Capacity Spectrum Method options in Asset Analysis).
		d. CustomPy.
    * :ref:`Transportation infrastructure <lbl-MODTransport>`:
	    a. None (Used for the IMasEDP option in Asset Analysis).

#. **Asset Analysis**: 
    * :ref:`Buildings <lbl-ANABuildings>`:
		a. OpenSees.
		b. OpenSeesPy. 
		c. IMasEDP (simplified analysis using Intensity Measures (IMs) as Engineering Demand Parameters (EDPs)).
		d. Capacity Spectrum Method.
		e. CustomPy for CustomPy Asset Modeling.
		f. Pre-trained surrogate models.
    * :ref:`Transportation infrastructure <lbl-ANATransport>`:
	    a. IMasEDP (simplified analysis using Intensity Measures (IMs) as Engineering Demand Parameters (EDPs)).
		
#. **Damage and Loss**: 
	* :ref:`Buildings <lbl-DLBuildingPelicun>`:
		* Pelicun Damage and Loss Methods:
			a. HAZUS MH EQ Story
			b. HAZUS MH EQ IM
			c. HAZUS MH HU
			d. User-provided Models
	* :ref:`Transportation infrastructure <lbl-DLTransportPelicun>`:
		* Pelicun Damage and Loss Methods:
			a. HAZUS MH EQ IM
			b. User-provided Models
	* :ref:`Water Network infrastructure <lbl-ASDWaterDistributionNetwork>`:
		* Pelicun Damage and Loss Methods:
			a. HAZUS MH EQ IM
			b. User-provided Models

#. **System Performance**:
	* :ref:`REWET <lbl-SPREWET>` System performance for water network with or without recovery 
	* :ref:`ResidualDemand <lbl-ResidualDemandTrafficSimulator>` Post-disaster traffic flow simulation
			
#. **Uncertainty Quantification**: 
    * :ref:`Dakota <lblUQ>`:
		a. Latin hypercube sampling (LHS)
		b. Monte Carlo Sampling (MCS)


#. **Additional Tools To Perform Tasks Generating or Using Data in Workflow**:
    * :ref:`Earthquake Scenario Simulation <ground_motion_tool>` (ground motion selection)
		* Site definition:
			a. Grid
			b. Point
			c. Scattered sites (user-defined sites in .csv format)
		* Rupture forecast models:
			a. OpenSHA UCERF rupture forecast models
			b. OpenSHA Point source user-defined
			c. OpenQuake rupture forecast
			d. Hazard Occurrence Model
		* Inter-event correlation:
			a. Baker and Jayaram (2008)
		* Intra-event correlation:
			a. Jayaram and Baker (2009)
			b. Markhvida et al. (2017)
			c. Loth and Baker (2013)
		* Record selection:
			a. PEER NGA West 2 ground motion database
			b. None, i.e., stop at the IM stage and no record selection
		* Ground motion models: 
			a. Abrahamson, Silva & Kamai (2014)
			b. Boore, Stewart, Seyhan & Atkinson (2014)
			c. Campbell & Bozorgnia (2014)
			d. Chiou & Youngs (2014)
		* Intensity measures: 
			a. Spectral acceleration (SA)
			b. Peak ground acceleraation (PGA)
			c. Peak ground velocity (PGV)
		* Ground failure models: 
			a. Liquefaction triggering
				1. Zhu et al. (2017) 
				2. Hazus (2020)
			b. Liquefaction lateral spreading permanent ground deformation (PGD_h)
				1. Hazus (2020)
			c. Liquefaction settlement permanent ground deformation (PGD_v)
				1. Hazus (2020)
		* Vs30 model:
			a. CGS/Wills Vs30 (Wills et al., 2015)
			b. Thompson California Vs30 (Thompson et al., 2018)
			c. Global Vs30 (Heath et al., 2020)
			d. User Defined

    * :ref:`Hurricane Scenario Simulation <hurricane_scenario_tool>` (hurricane wind field generation)
		* Site definition:
			a. Grid
		* Hurricane track definition:
			a. User-defined sites in .csv format
			b. Select from a database of historical hurricanes
			c. Truncate hurricane track functionality
		* Landfall location and parameters:
			a. User selects on GIS map
			b. Manual user entry in the input box
		* Wind field generation model:
			a.  Snaiki and Wu (2017)

    * :ref:`OpenQuake Selection <openquake_selection_tool>`
    * :ref:`Census Data & American Community Survey <lbl-censusDataAllocation>`
    * `Building and Infrastructure Recognition using AI at Large-Scale (BRAILS) <https://nheri-simcenter.github.io/BRAILS-Documentation/>`_
		* Building inventory generation
		* Transportation inventory generation
		
		   
