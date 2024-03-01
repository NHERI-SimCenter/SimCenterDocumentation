RES: Results
============

The **Results** panel is where the user can review the results of an analysis. Currently, the results post-processor supports output from the following applications:

.. contents::
   :local:

Pelicun Damage and Loss 
-----------------------

:numref:`fig-R2DRESPanel` shows the results panel for the **Pelicun Damage and Loss** application. The results panel is comprised of several docking windows that can be moved, rearranged, resized, and opened and closed by the user. The results panel contains these main docks:

	#. **Regional Map Dock:** Geographic map of the region. The assets are colored according to their most likely critical damage state. Clicking on an asset will produce a popup showing the detailed information of that asset.
	
	.. note:: The critical damage state of an asset is defined as the largest damage
		state experienced by its components. For asset-level damage assessment (e.g., Hazus-MH EQ IM)
		each asset is represented by several components that are prone to different hazard 
		intensity measure inputs. For example, a building may be represeted by one
		ground shaking vulnerable component and one ground failure vulnerable component.
		The damage state of the first component is determined by `PGA` while the
		damage state of the second component is determined by `PGD`. The large damage state of
		the two components is defined as the critical damage state. The `Most likely` critical
		damage state is the mode of the critical damage state realizations. Pelicun will 
		generate a number of damage state realizations as defined in :numref:`fig-R2DPelicunDLPanel`.
		Additional information on Pelicun and descriptions of its output are available at `Pelicun Documentation <https://nheri-simcenter.github.io/pelicun/common/user_manual/usage/pelicun/outputs.html>`_. 
		A critical damage state can be determined in each realization and the 
		most likely damage state is the mode of the critical damage state realizations.

	
	#. **Detailed Building Results Dock:** Table showing the detailed results. For each asset, the table provides the:
		 
		 - Asset ID
		 - Mean and standard deviation of repair Cost
		 - Mean and standard deviation of repair Time
		 - Mean and standard deviation of most likely damage state
	
		The **Table Sort** combo box, shown in :numref:`fig-R2DRESPanel`, sorts the table in descending order according to the selected filter, e.g., repair cost. 

.. _fig-R2DRESPanel:

.. figure:: figures/R2DRESPanelNew.png
	:align: center
	:figclass: align-center

	Pelicun results visualization panel.

