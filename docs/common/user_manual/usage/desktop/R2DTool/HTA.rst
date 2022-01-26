HTA: Hazard to Asset
====================


Regional Mapping
----------------

In a regional analysis, hazard intensities need to be specified over a geographic area. In some cases, hazard intensities are defined along a grid of points instead of at the exact location of an asset. The **Regional Mapping** pane, shown here with the **Nearest Neighbor Event** application selected as the **Regional Mapping Application**, provides a method for an asset to locate the nearest grid point(s) from which it will obtain the hazard intensities. 

Nearest Neighbor Event
**********************

The **Nearest Neighbor Event** application draws samples of hazard intensities from nearby grid points. The **Nearest Neighbor Event** input pane, shown in :numref:`fig-R2DHTAPanel`, requires the following inputs:

	#. **Number of samples:** Controls the number of samples considered at each grid point.
	#. **Number of neighbors:** Number of neighboring grid points that samples will be drawn from.

.. _fig-R2DHTAPanel:

.. figure:: figures/R2DHTAPanel.png
	:align: center
	:figclass: align-center

	Nearest neighbor event input panel.
	
	
Site Specified Event
********************

The **Site Specified Event** application, shown in :numref:`fig-R2DSSEPanel`, should be selected when the hazard intensities are provided at the exact location of an asset. The hazard intensities can be provided by the user or calculated within the R2D workflow.

.. _fig-R2DSSEPanel:

.. figure:: figures/R2DSSEPanel.png
	:align: center
	:figclass: align-center

	Site specified event input panel.
	

Local Mapping
-------------

The **Local Event Type** application allows a user to select the type of event from the **Local Event Type** dropdown. Currently, only the SimCenterEvent option is available, as seen in :numref:`fig-R2DHTAPanel`, 
