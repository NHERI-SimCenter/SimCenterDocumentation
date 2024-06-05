DL: Damage and Loss
===================

The **Damage and Loss** panel enables users to select a damage and loss methodology for estimating losses across a region. It supports various applications:

.. contents::
   :local:

.. _lbl-DLBuildingPelicun:

Pelicun Damage and Loss for Buildings
-------------------------------------

As depicted in :numref:`fig-R2DPelicunDLPanel`, the **Pelicun Damage and Loss** application offers these inputs:

	#. **Damage and Loss Methodology:** Choose a methodology from the following options:
	
		- **Hazus MH EQ:** For earthquake scenarios, requiring engineering demand parameters (EDPs) like peak inter-story drift ratio (PID), peak floor acceleration (PFA), peak roof drift (PRD), and peak floor displacement (PFD). Suitable for building response analysis.
		- **Hazus MH EQ IM:** A simpler option requiring only an intensity measure (IM), such as peak ground acceleration (PGA), for scenarios not involving building response analysis. Use this option when the Building Modeling type is set to **None** in the **MOD** tab and the Building Analysis Engine type to **IMasEDP** in the **ANA** tab.
		- **Hazus MH HU:** For the prediction of damage and loss to buildings subjected to hurricanes. This option requires a wind intensity measure (IM) as an input, e.g., peak wind speed (PWS).
		- **User-provided Fragilities:** Allows for custom fragility functions. Users must provide a script for auto-population and the path to a folder with the fragility functions, as shown in :numref:`fig-R2DPelicunDLPanel`. Refer to Example 9 in :ref:`R2D examples <lbl-examples>` for implementation.
		
		The HAZUS options utilize data from the Hazards U.S. Multi-Hazard project (HAZUS-MH), with **Hazus MH EQ** and **Hazus MH EQ IM** tailored for earthquakes, and **Hazus MH HU** for hurricanes.
	
	#. **Event Time:** Toggle 'on' to set the event time in YYYY-MM-DD:HH format, or 'off' to disable time-effects.
	
	#. **Number of Realizations:** Set the number of loss realizations for the analysis.
	
	#. **Output Detailed Results:** Enable to output detailed results.
	
	#. **Create Log File:** Enable to generate a log file of the analysis.
		
	#. **Include Ground Failure:** Checking this box will include ground failure in the analysis. If ground failure is included, fragility groups associated with ground failure are added in the auto-population phase. Note that such analysis requires peak ground displacement (PGD) values as inputs.
	
	#. **Auto-populate Script:** Path to a user-provided Python script for mapping assets to their respective fragility functions.
	
	#. **User-defined Fragility Function Folder:** Path to a folder containing user-defined fragility functions. 


.. _fig-R2DPelicunDLPanel:

.. figure:: figures/R2DPelicunDLPanel.png
	:align: center
	:figclass: align-center

	Pelicun Damage and Loss Input panel.

For more on Pelicun, including output descriptions, visit the `Pelicun Documentation <https://nheri-simcenter.github.io/pelicun/common/user_manual/usage/pelicun/outputs.html>`_.

.. _lbl-DLTransportPelicun:

Pelicun Damage and Loss for Transportation Infrastructure
---------------------------------------------------------
The interface for Transportation Infrastructure damage and loss in Pelicun mirrors that of buildings, as shown in :numref:`fig-R2DPelicunDLPanel`. Supported **damage and loss methodology** options include **Hazus MH EQ IM** and **User-provided Fragilities**. 

**Hazus MH EQ IM** follows the damage and loss model from the `Hazus Earthquake Model Technical Manual <https://www.fema.gov/sites/default/files/documents/fema_hazus-earthquake-model-technical-manual-5-1.pdf>`_. For bridges, it requires `SA_0.3` and `SA_1.0` for ground shaking-induced damage assessment. Ground failure considerations require permanent ground deformation (`PGD_h` and `PGD_v`) inputs for bridges and roadways, while tunnels need peak ground acceleration (`PGA`) and permanent ground deformation (`PGD_h` and `PGD_v`).

The **User-provided Fragilities** option allows for custom fragility functions, necessitating an auto-populate script and a folder path for the fragility functions, as detailed in :numref:`fig-R2DPelicunDLPanel`. See Example 9 in :ref:`R2D examples <lbl-examples>` for an example.