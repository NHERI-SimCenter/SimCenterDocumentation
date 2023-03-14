.. _lbl-release:

.. role:: blue

***************************
Release Notes
***************************

Major Version 1.0
===================

|app| Version 1.1.0 (Current)
------------------------------

**Release date:** June 25, 2021

Notable new features include the hurricane simulation application and ShakeMap support. Moreover, this release includes HAZUS MH HU (Hurricane) loss implementation in Pelicun. This release also includes performance updates, stability improvements, and bug fixes. New features in this release are denoted with a blue font color in the following list of features:

#. **Hazard Types**:
    * User specified earthquakes
	* User specified hurricanes
	* :blue:`ShakeMap Scenarios`
		* :blue:`Suports import of the following ShakeMap outputs:`
			a. :blue:`ShakeMap ground motion grid in .xml format`
			b. :blue:`PGA contours in .json format`
			c. :blue:`Fault rupture in .json format`

#. **Hazard Simulation**:
    * Earthquake Scenario Simulation (ground motion selection)
		* Site definition:
			a. Grid
			b. Point
			c. :blue:`Scattered sites (user defined sites in .csv format)`
		* Rupture forecast models:
			a. UCERF rupture forecast models
			b. Point source user defined
		* Inter-event correlation:
			a. Baker and Jayaram (2008)
		* Intra-event correlation:
			a. Jayaram and Baker (2009)
			b. Markhvida et al. (2017)
			c. Loth and Baker (2013)
		* Record selection:
			a. PEER NGA West 2 ground motion database
			b. :blue:`None, i.e., stop at the IM stage and no record selection`
		* Ground motion prediction equations: 
			a. Abrahamson, Silva & Kamai (2014)
			b. Boore, Stewart, Seyhan & Atkinson (2014)
			c. Campbell & Bozorgnia (2014)
			d. Chiou & Youngs (2014)
		* Intensity Measures: 
			a. Spectral accelertion (SA)
			b. Peak ground acceleraation (PGA)
		* :blue:`Va30 Model:`
			a. :blue:`CGS/Wills Vs30 (Wills et al., 2015)`
			b. :blue:`Peak ground acceleraation (PGA)`
			c. :blue:`Thompson California Vs30 (Thompson et al., 2018)`
			d. :blue:`Global Vs30 (Heath et al., 2020)`
			e. :blue:`User Defined`

    * :blue:`Hurricane Scenario Simulation (hurricane wind field generation)`
		* :blue:`Site definition:`
			a. :blue:`Grid`
		* :blue:`Hurricane track definition:`
			a. :blue:`User defined sites in .csv format`
			b. :blue:`Select from database of historical hurricanes`
			c. :blue:`Truncate hurricane track functionality`
		* :blue:`Landfall location and parameters:`
			a. :blue:`User select on GIS map`
			b. :blue:`Manual user entry in input box`
		* :blue:`Wind field generation model:`
			a.  :blue:`Snaiki and Wu (2017)`
		
#. **Asset Types**: 
    * Buildings:
		a. Building database in a ``.csv`` format.
	
#. **Asset Modeling**: 
    * Buildings:
		a. MDOF-LU (MDOF shear building model)
		b. OpenSeesPy script building generator

#. **Asset Analysis**: 
    * Buildings:
		a. OpenSees
		b. OpenSeesPy 
		c. IMasEDP, i.e., no analysis as the IM is considered the EDP
		
#. **Damage and Loss**: 
    * Buildings:
		* Pelicun 
			a. HAZUS MH EQ
			b. HAZUS MH EQ IM
			c. :blue:`HAZUS MH HU`
			
#. **Uncertainty Quantification**: 
    * Dakota:
		a. Latin hypercube sampling (LHS)
		b. Monte Carlo Sampling (MCS)

	
|app| Version 1.0.0
--------------------

**Release date:** Jan 1, 2021

Initial release of the R2D Tool. Supports the analysis of buildings subjected to earthquake hazards. Additionally, supports remote analysis on DesignSafe's high performance super computer and local analysis on user's computer. Moreover, this release supports Geographic Information System (GIS) visualization capabilities. The initial list of features is as follows:

#. **Hazard Types**:
    * User specified earthquakes

#. **Hazard Simulation**:
    * Earthquake Scenario Simulation (ground motion selection)
		* Site definition:
			a. Grid
			b. Point
		* Rupture forecast models:
			a. UCERF rupture forecast models
			b. Point source user defined
		* Inter-event correlation:
			a. Baker and Jayaram (2008)
		* Intra-event correlation:
			a. Jayaram and Baker (2009)
			b. Markhvida et al. (2017)
			c. Loth and Baker (2013)
		* Record selection:
			a. PEER NGA West 2 ground motion database
		* Ground motion prediction equations: 
			a. Abrahamson, Silva & Kamai (2014)
			b. Boore, Stewart, Seyhan & Atkinson (2014)
			c. Campbell & Bozorgnia (2014)
			d. Chiou & Youngs (2014)
		* Intensity Measures: 
			a. Spectral accelertion (SA)
			b. Peak ground acceleraation (PGA)

#. **Asset Types**: 
    * Buildings:
		a. Building database in a ``.csv`` format
	
#. **Asset Modeling**: 
    * Buildings:
		a. MDOF-LU (MDOF shear building model)
		b. OpenSeesPy script building generator

#. **Asset Analysis**: 
    * Buildings:
		a. OpenSees
		b. OpenSeesPy 
		c. IMasEDP, i.e., no analysis as the IM is considered the EDP
		
#. **Damage and Loss**: 
    * Buildings:
		* Pelicun 
			a. HAZUS MH EQ
			b. HAZUS MH EQ IM
			
#. **Uncertainty Quantification**: 
    * Dakota:
		a. Latin hypercube sampling (LHS)
		b. Monte Carlo Sampling (MCS)


We encourage new feature suggestions, please write to us at :ref:`lblBugs`.