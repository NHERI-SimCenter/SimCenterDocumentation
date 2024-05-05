SP: System Performance
===================

The **System Performance** panel is where the user selects a system performance methodology to perform a system (i.e., network) performance functionality assessment. The following system performance applications are available:

.. contents::
   :local:

.. _lbl-SPREWET:

REWET
-----

Shown in :numref:`fig-R2DREWETSYMPanel`, the **REWET System Performance** assessment application has three  tabs:

	#. **Simulation:** This tab refer to the input required for simulating the Water Distortion Network (WDN) service restoration after an event. The following inputs are require for in REWET's simulation tab
	
		- Event Time
		This refers to the time of the event after the simulation starts. For instance, if the time in the example INP file is 12 AM, an event time equal to 7200 corresponds to 2 AM.

		- Simulation End Time
		This specifies the time at which the simulation ends.

		- Terminate Simulation after the Last Job Sequence Is Done
		This option, if selected, allows the simulation to be ended before the simulation end time is reached if all the jobs defined for recovery are completed.

		- Terminate Simulation after the Demand Is Met
		This option, if selected, allows the simulation to be ended before the simulation end time is reached if the ratio of demand after the event to the demand before the event meets or exceeds a given threshold for all demand nodes.

		- Demand Checking Time Window
		This parameter defines the time window for checking demand after selecting “Terminate Simulation after the Demand.”

		- Demand Checking Criteria
		This shows the ratio of demand after to demand before, which determines when the simulation ends when “Terminate Simulation after the Demand” is selected.
		
		.. _fig-R2DREWETSYMPanel:

		.. figure:: figures/R2DSPREWETSim.png
			:align: center
			:figclass: align-center
		
	#. **Hydraulic:** This tab refers to the input required for hydraulics of the Water Distortion Network (WDN) and damage simulation. The following inputs are require for in REWET's hydraulics tab.
	
		- Hydraulic Solver Selection
		Users can specify their preferred hydraulic solver for their hydraulic simulation based on the available versions of REWET in R2D. The Modified EPANET V2.2 is a customized version of EPANET V2.2 that handles flow from negative pressure scenarios.
		
		- Minimum Pressure Override and Required Pressure Override
		These options allow users to override the minimum and required pressure values specified in the INP file. Since the minimum and required pressure values in the example are correct, we leave them unchanged (set as -1 so that they will be ignored).
		
		- Pipe Damage Modeling
		In pipe damage modeling, the relationship between the pipe’s diameter and the equivalent orifice diameter - similar to the approach proposed by Shi and O’Rourke (2008) - for each pipe material (or damage type) is defined. The default value is set to Cast Iron, with average values derived from Shi and O’Rourke (2008). If the user does not provide a material (or damage subtype) name list in the asset, R2D assumes the default value to be Cast Iron.
		
		.. _fig-R2DREWETHYDPanel:

		.. figure:: figures/R2DSPREWETHyd.png
			:align: center
			:figclass: align-center
	
	REWET System-Performance Hydraulic Input panel.

	#. **Restoration:**	This tab refers to the input required for Restoration of the Water Distortion Network (WDN) that pursuits after the damages after an event. The following inputs are require for in REWET's restoration tab.
		- Hydraulic Solver Selection
		The user can specify their preferred hydraulic solver for their hydraulic simulation based on the available versions of REWET in R2D. The Modified EPANET V2.2 is a customized version of EPANET V2.2 that handles flow from negative pressure scenarios.
		
		- Minimum Pressure Override and Required Pressure Override
		These options allow users to override the minimum and required pressure values specified in the INP file. set as **-1** so that they will be ignored.
			
			..Note: This is a an overwrite option for the ease of user's uage. The user can modify the inp file using EPANET's interface or just use a text editor to edit the pressure just like other inputs.
		
		- Pipe Damage Modeling
		In pipe damage modeling, the relationship between the pipe’s diameter and the equivalent orifice diameter - similar to the approach proposed by Shi and O’Rourke (2008) - for each pipe material (or damage type) is defined. The default value is set to Cast Iron, with average values derived from Shi and O’Rourke (2008). If the user does not provide a material (or damage subtype) name list in the asset, R2D assumes the default value to be Cast Iron.
	
	
	.. _fig-R2DREWETHYDPanel:

	.. figure:: figures/R2DSPREWETRes.png
		:align: center
		:figclass: align-center
	
Additional information on REWET and descriptions of its output are available at Naeimi Dafchahi, S., & Davidson, R. A. (2023), titled "Post-event restoration simulation of water distribution systems: a generally applicable approach."
	
