.. _lbl-capabilities_eeuq:
.. role:: blue

************
Capabilities
************


**Version 3.0** of |app| was released **May 2023**. The following lists the functionality available in this current version. (Note: New features and fixes in this release are marked :blue:`blue` in the following list of features.) Note the version introduced major changes in how tool is used. Some of existing **Haz** options were moved to a new **Tool** main menu option.




**Release date:** May, 2023

#. **Hazard Types**:
    * User specified earthquakes
	* User specified hurricanes
	* ShakeMap Scenarios
		* Suports import of the following ShakeMap outputs:
			a. ShakeMap ground motion grid in .xml format
			b. PGA contours in .json format
			c. Fault rupture in .json format
	* Raster Defined Hazard for Earthquake, Hurricane, Inundation
	* GIS Defined Hazard for Earthquake, Hurricane, Inundation

#. **Asset Types**: 
    * Buildings:
	a. Building database in a ``.csv`` format.
	b. Building database in a ``.gis`` format.		   
	
#. **Asset Modeling**: 
    * Buildings:
		a. MDOF-LU (MDOF shear building model)
		b. OpenSeesPy script building generator
		c. IMasEDP, i.e., no analysis as the IM is considered the EDP
                d. CustomPy

#. **Asset Analysis**: 
    * Buildings:
		a. OpenSees
		b. OpenSeesPy 
		c. IMasEDP, i.e., no analysis as the IM is considered the EDP
		d. CustomPy for CustomPy in Asset Modeling
		d. None for IMasEDP option in Modeling.		   		   
		
#. **Damage and Loss**: 
    * Buildings:
		* Pelicun 
			a. HAZUS MH EQ
			b. HAZUS MH EQ IM
			c. HAZUS MH HU
			
#. **Uncertainty Quantification**: 
    * Dakota:
		a. Latin hypercube sampling (LHS)
		b. Monte Carlo Sampling (MCS)


#. ** Additional Tools To Perform Tasks Generating or Using Data in Workflow**:
    * Earthquake Scenario Simulation (ground motion selection)
		* Site definition:
			a. Grid
			b. Point
			c. Scattered sites (user defined sites in .csv format)
		* Rupture forecast models:
			a. OpenSHA UCERF rupture forecast models
			b. OpenSHA Point source user defined
			c. OpenQuake Scenario Based
			d. OpenQuake Classical PSHA
			e. :blue:`Hazard Occurrence Model`
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
			a. Spectral accelertion (SA)
			b. Peak ground acceleraation (PGA)
		* Vs30 Model:
			a. CGS/Wills Vs30 (Wills et al., 2015)
			b. Peak ground acceleraation (PGA)
			c. Thompson California Vs30 (Thompson et al., 2018)
			d. Global Vs30 (Heath et al., 2020)
			e. User Defined`

    * Hurricane Scenario Simulation (hurricane wind field generation)
		* Site definition:
			a. Grid
		* Hurricane track definition:
			a. User defined sites in .csv format
			b. Select from database of historical hurricanes
			c. Truncate hurricane track functionality
		* Landfall location and parameters:
			a. User select on GIS map
			b. Manual user entry in input box
		* Wind field generation model:
			a.  Snaiki and Wu (2017)

    * **OpenQuake Selection**
    * **Census Data & American Community Survey**

		
		   
