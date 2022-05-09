.. _r2d-viz:

VIZ: Visualization
==================

In this panel, shown in :numref:`fig-regionalGISPanel`, the user can visualize the assets and hazards over a geographical region.

.. _fig-regionalGISPanel:

.. figure:: figures/R2DVIZPanel.png
  :align: center
  :figclass: align-center

  Geographic visualization panel.

#. The **Geographic Visualization (GIS)** pane displays the map of a region and the various objects that can be visualized, e.g., assets and hazards. R2D employs the `QGIS <https://www.qgis.org/en/site/index.html>`_ geospatial information system as the GIS engine. Much of the core QGIS functionality is built into R2D. For additional information about QGIS functionality, please see the QGIS `documentation <https://www.qgis.org/en/docs/index.html>`_. You can review the GIS functionality available in R2D by clicking on the **GIS Map** menu item. 

#. The **Base map Selection** dropdown is where you can select a base map that will be the map shown in the background of the GIS pane.

#. The **Map Layer Tree** shows the layers that are in the map. Checking the box to the left of a layer name will show or hide the corresponding layer in the map. Moreover, right-clicking on a layer will display a pop-up with any available layer functionality, e.g., **Zoom to Layer**. You can drag and drop layers to rearrange their visibility in the GIS window. Layers that are lower down in the layer tree will be rendered under the layers that are on top. You can right-click on a layer to see the available options, e.g., **Zoom to Layer(s)** and **Show Feature Count**. 

#. The **Asset Subset Selection** allows a user to select a subset of assets for analysis or to "identify" assets,i.e., to view the asset attributes. 

	- To select a subset of assets, click on the **Select** button, shown in :numref:`fig-R2DAssetSelection`, to start the selection process. 
	- You can click on a single asset to select it, or click-hold and drag to create a rectangle that will select all assets that it intersects. By holding the shift key, you can continue selecting assets until you are satisfied. 
	- Clicking on the **Add Assets** button will add the selected assets to the **Selected Assets** layer for that type of asset, e.g., **Selected Buildings**. Only assets added to the **Selected Assets** layer will be analysed. 
	
	.. note:: Only features that are in the current layer can be selected on the map. The current layer is the layer that is selected (highlighted) in the layer tree. 
	
   Some tips for selecting features are:
   
	- To select multiple features, hold down the shift key.
	- The selected features are highlighted in yellow.
	- A layer needs to be visible to enable asset selection on that layer.
	- To clear everything and start over again, click on the **Clear** button. 
	- To clear the selected features on the current layer, click anywhere on the map where there are no features. Or, you can clear all selected features from all layers by clicking on the **Clear Selection** button.
	
	.. _fig-R2DAssetSelection: 

	.. figure:: figures/R2DAssetSelection.png
	  :align: center
	  :figclass: align-center

	  Asset selection.
	  
	
#. The **Identify** button allows you to select an asset, or assets, in the GIS pane to query the asset attributes. When you click on a asset, a table will appear in the righthand side of the GIS window, as illustrated in :numref:`fig-R2DVizAssetIdentify`. This table contains the feature attributes that consist of the field name (left column) and corresponding value (right column).

	.. _fig-R2DVizAssetIdentify:

	.. figure:: figures/R2DVizAssetIdentify.png
	  :align: center
	  :figclass: align-center

	  Asset identify.








