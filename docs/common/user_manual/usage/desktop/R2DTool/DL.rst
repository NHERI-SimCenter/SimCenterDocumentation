DL: Damage and Loss
===================

The **Damage and Loss** panel is where the user selects a damage and loss methodology to estimate losses over a region. The following damage and loss applications are available:

.. contents::
   :local:

Pelicun Damage and Loss 
-----------------------

Shown in :numref:`fig-R2DPelicunDLPanel`, the **Pelicun Damage and Loss** application has the following inputs:

	#. **Damage and Loss Methodology:** The type of damage and loss methodology to use. The following damage and loss methodologies are available:
	
		- Hazus MH EQ
		- Hazus MH EQ IM
	
	#. **Event Time:** Select event time 'on' or 'off'. Selecting the event time to 'on' defines the time of the event in YYYY-MM-DD:HH format. ‘off’ turns all time-effects off.
	
	#. **Number of Realizations:** The number of loss realizations to generate in the analysis.
	
	#. **Output Detailed Results:** Checking this box will output detailed results.
	
	#. **Create Log File:** Checking this box will create a log file of the analysis.
	
	#. **Include Ground Failure:** Checking this box will include ground failure in the analysis. If ground failure is included, fragility groups associated with ground failure are added in the auto-population phase. Note that such analysis requires peak ground displacement (PGD) values as inputs.

.. _fig-R2DPelicunDLPanel:

.. figure:: figures/R2DPelicunDLPanel.png
	:align: center
	:figclass: align-center

	Pelicun Damage and Loss Input panel.
