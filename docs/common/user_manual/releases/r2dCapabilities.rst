.. _lbl-capabilities_eeuq:
.. role:: blue

************
Capabilities
************


**Version** |tool version| of |app| was released **Jan 2024**. The following is the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.)
The major update from Version 3.0 is adding the analysis capability for :blue:`regional transportation infrastructure`. Note that since version 3.0, most **Haz** options were moved to the **Tool** main menu.




**Release date:** Dec, 2023

#. **Hazard Types**:

    * :ref:`User specified earthquakes <lbl-UserSpecifiedGroundMotions>`.
    * :ref:`User specified hurricanes <lbl-UserSpecifiedHurricane>`.
    * :ref:`ShakeMap Scenarios <lbl-shakeMapEQScenarios>`, which supports importing the following ShakeMap outputs:
            a. ShakeMap ground motion grid in .xml format.
            b. PGA contours in .json format.
            c. Fault rupture in .json format.	
    * :ref:`Raster Defined Hazard <lbl-rasterDefinedHazard>` for Earthquake, Hurricane, Inundation**.
    * **GIS Defined Hazard for Earthquake, Hurricane, Inundation**.



#. **Asset Types**:

    * :ref:`Buildings <lbl-ASDBuildings>`:
		a. Load building database in a ``.csv`` format.
		b. Load building database in a ``.gis`` format.
    * :ref:`Transportation infrastructure <lbl-ASDTransport>`:
		a. :blue:`Load transportation infrastructure database in SimCenter's` ``.geojson`` :blue:`format.`
		b. :blue:`Load transportation infrastructure database in common` ``.gis`` :blue:`format.`
		   
	
#. **Asset Modeling**: 
    * :ref:`Buildings <lbl-MODBuildings>`:
		a. MDOF-LU (MDOF shear building model)
		b. OpenSeesPy script building generator
		c. IMasEDP, i.e., no structural modeling, and the Intensity Measures (IMs) are considered the Engineering Demand Parameters (EDPs)
                d. CustomPy
    * :ref:`Transportation infrastructure <lbl-MODTransport>`:
	    a. IMasEDP, i.e., no structural modeling, and the Intensity Measures (IMs) are considered the Engineering Demand Parameters (EDPs)

#. **Asset Analysis**: 
    * :ref:`Buildings <lbl-ANABuildings>`:
		a. OpenSees
		b. OpenSeesPy 
		c. IMasEDP, i.e., no analysis as the IM is considered the EDP
		d. CustomPy for CustomPy in Asset Modeling
		e. None for IMasEDP option in Modeling.	
    * :ref:`Transportation infrastructure <lbl-ANATransport>`:
	    a. None for IMasEDP option in Modeling.	   		   
		
#. **Damage and Loss**: 
    * :ref:`Buildings <lbl-DLBuildingPelicun>`:
		* Pelicun
			a. HAZUS MH EQ
			b. HAZUS MH EQ IM
			c. HAZUS MH HU
    * :ref:`Transportation infrastructure <lbl-DLTransportPelicun>`
			a. HAZUS MH EQ
			b. HAZUS MH EQ IM
			
#. **Uncertainty Quantification**: 
    * :ref:`Dakota <lblUQ>`:
		a. Latin hypercube sampling (LHS)
		b. Monte Carlo Sampling (MCS)


#. ** Additional Tools To Perform Tasks Generating or Using Data in Workflow**:
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
		* Ground motion prediction equations: 
			a. Abrahamson, Silva & Kamai (2014)
			b. Boore, Stewart, Seyhan & Atkinson (2014)
			c. Campbell & Bozorgnia (2014)
			d. Chiou & Youngs (2014)
		* Intensity Measures: 
			a. Spectral acceleration (SA)
			b. Peak ground acceleraation (PGA)
		* Vs30 Model:
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

		
		   
