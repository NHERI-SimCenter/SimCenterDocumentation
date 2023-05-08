OpenQuake Selection Widget
--------------------------
   
The **OpenQuake Selection Widget** allows for the selection of OpenQuake seismic sources in a GIS window and exporting only the selected sources into a new .xml file for use in OpenQuake. The **OpenQuake Selection Widget** input pane is given in :numref:`fig-R2DOpenQuakePane`. 

#. To load an OpenQuake file (only .xml files supported), click on the **Browse** button next to the input file box, and then select the input file in the dialog that will appear.

#. Next, select a subset of sources in the GIS window that you wish to keep. To be able to select the OpenQuake sources in the map, you first need to select a layer in the layer tree, shown on the left-hand side of :numref:`fig-R2DOpenQuakePane`. There are three layers that correspond to the different source geometries in OpenQuake; namely point, line, and area sources. 

There are several methods available to select the sources on the GIS map. Clicking on one of the **Selection Method** buttons, shown in :numref:`fig-R2DOpenQuakePane`, will change the selection tool to that corresponding method. 

.. note:: Only features that are in the current layer can be selected on the map. The current layer is the layer that is selected (highlighted) in the layer tree. 
	
Some tips for selecting features are:   

	- To select multiple features, hold down the shift key.
	- The selected features are highlighted in yellow.
	- A layer needs to be visible to enable asset selection on that layer.
	- To clear everything and start over again, click on the **Clear** button. 
	- To clear the selected features on the current layer, click anywhere on the map where there are no features. Alternatively, you can clear all the selected features from all layers by clicking on the **Clear Selection** button.

#. Once you are done with the selection process, you can export the selected sources (highlighted in yellow) by first providing a file path and name. Clicking on the **Browse** button next to the export file box will open a dialog where you can input a directory path and file name, i.e., the name and location where the .xml file containing the selected sources will be saved. Once you have entered a file name and path, clicking on the **Export** button will generate the new .xml file that can be used in OpenQuake. The name and path of the exported file will appear in the program output pane. 

.. _fig-R2DOpenQuakePane:

.. figure:: figures/R2DOpenQuakePane.png
  :align: center
  :figclass: align-center

  OpenQuake selection pane.


