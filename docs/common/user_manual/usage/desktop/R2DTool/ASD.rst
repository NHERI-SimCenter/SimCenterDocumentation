ASD: Asset Definition
=====================

In this panel the user can import the databases of different asset classes. The user can select the type of asset from the **Asset Selection Ribbon**, e.g., Buildings and Gas Network, as shown on the left-hand side of :numref:`fig-buildingInputPanel`. The **Asset Selection Ribbon** appears when more than one type of asset is selected in the **GI: General Information** panel. Moreover, only the assets that are checked in the **GI: General Information** panel will appear in the **Asset Selection Ribbon**. As the user switches between assets, the main panel changes to reflect the applications available for the import of each type of asset. 

.. contents::
   :local:

.. _lbl-ASDBuildings:

Buildings
---------

The buildings input panel, as shown in :numref:`fig-buildingInputPanel`, allows a user to input a building inventory database. The **Building Import Selection** combo box is where the user selects the application for the import of buildings, and for the generation of a asset information model (AIM).

CSV to AIM
**********

The **CSV to AIM** application imports a building inventory database from a user provided .csv file. 

#. The **Path to Buildings Database** box is where the user supplies the file path to the .csv file that contains the building inventory. At a minimum, the .csv file must contain columns providing the building identification numbers (ID), in sequential order, and the latitudes and the longitudes of the locations of the buildings. Any number of columns can be added to the file to provide information required by other applications in the workflow.  

#. The **Building Selection Filtering** box is where the user can select a subset of buildings for analysis. There are two ways to select and filter buildings:

	#. Input a string of numbers that correspond to the building IDs that you want to analyze. A range of buildings is specified with a dash, and multiple buildings are separated with a comma, e.g., 2-8, 9, 13, 15, 21, 34-38.
	#. Employ the Advanced Filtering capabilities by clicking on the **Advanced Filter** button. The **Query Builder** dialog will appear, as seen in :numref:`fig-R2DQueryBuilderDialog`. You can create a custom filter expression (SQL format) using operators, e.g., ``<, =, OR``, and fields available in the imported building inventory, e.g., ``BuildingType``. Operators and fields can be combined to perform complex filtering expressions such as ``"YearBuilt" < 1970  AND  "BuildingType"  =  'Wood'``
	
	.. _fig-R2DQueryBuilderDialog:

	.. figure:: figures/R2DQueryBuilderDialog.png
	  :align: center
	  :figclass: align-center

	  Query Builder Dialog.

When the **Select** button is pressed, the buildings that are specified in the **Building Selection** box are added to the list of buildings that will be analyzed. Pressing the **Clear Selection** button will clear the list of buildings that will be analyzed.

The **Building Information** table, shown in :numref:`fig-buildingInputPanel`, provides a user-editable spreadsheet containing the information provided by the building inventory database file.

.. _fig-buildingInputPanel:

.. figure:: figures/R2DBuildingsInputPanel.png
  :align: center
  :figclass: align-center

  CSV to AIM input panel.

GIS to AIM
**********

The **GIS to AIM** application imports a building inventory database from a user-provided GIS file (e.g., shapefile, geodatabase). The input panel is shown in :numref:`fig-R2DGISBuildingsInputPanel`.

#. The **GIS Input File** box is where the user supplies the file path to the GIS file that contains the building inventory. Clicking on the **Browse** button will open a dialog where you can select the appropriate file. 

#. The **Building Selection Filtering** box is where the user can select a subset of buildings for analysis. There are two ways to select and filter buildings:

	#. Input a string of numbers that correspond to the building IDs that you want to analyze. A range of buildings is specified with a dash, and multiple buildings are separated with a comma, e.g., 2-8, 9, 13, 15, 21, 34-38.
	#. Employ the Advanced Filtering capabilities by clicking on the **Advanced Filter** button. The **Query Builder** dialog will appear, as seen in :numref:`fig-R2DQueryBuilderDialog`. You can create a custom filter expression (SQL format) using operators, e.g., ``<, =, OR``, and fields available in the imported building inventory, e.g., ``BuildingType``. Operators and fields can be combined to perform complex filtering expressions such as ``"YearBuilt" < 1970  AND  "BuildingType"  =  'Wood'``. When the **Select** button is pressed, the buildings that are specified in the **Building Selection** box are added to the list of buildings that will be analyzed. Pressing the **Clear Selection** button will clear the list of buildings that will be analyzed.

#. The **Building Information** table provides a user-editable spreadsheet containing the information provided by the building inventory database file. When a subset of buildings is selected for analysis, only the selected buildings will appear in the **Building Information** table. 

.. _fig-R2DGISBuildingsInputPanel:

.. figure:: figures/R2DGISBuildingsInputPanel.png
  :align: center
  :figclass: align-center

  GIS to AIM input panel.


Regional Water Distribution Networks
-------------------------------------

The water distribution network input panel, as shown in :numref:`fig-wdnInputPanel`, allows a user to input the nodes and pipelines of a water distribution network. The **Regional Water Network Selection** combo box is where the user selects the application for the import of buildings, and for the generation of a building information model (AIM).

CSV to Regional Water Network
*****************************

The **CSV to Water Network** application imports a water distribution network from a set of user provided .csv files that represent the nodes and pipelines of the network. 

#. The **Path to Nodes** box is where the user supplies the file path to the .csv file that contains the nodes of the water distribution network. At a minimum, the .csv file must contain columns providing the node identification numbers (ID), in sequential order, and the latitudes and the longitudes of the locations of each node. Any number of columns can be added to the file to provide information that may be required by other applications in the workflow.  

#. Similar to the nodes, the **Path to Pipelines** box is where the user supplies the file path to the .csv file that contains the pipelines of the water distribution network. At a minimum, the .csv file must contain columns providing the pipe identification numbers (ID), in sequential order, and two subsequent columns containing the node ids of the nodes where the pipe starts and where the pipe ends. Any number of columns can be added to the file to provide additional pipeline information that may be required by other applications in the workflow.  

The **Node and Pipeline Information** table, shown in :numref:`fig-WDNInputPanel`, provides a user-editable spreadsheet containing the information provided by the csv files, respectively. 

#. The **Selection Filtering** box for nodes and pipes is where the user can select a subset of assets for analysis. 

 There are two ways to select and filter assets:

	#. Input a string of numbers that correspond to the asset IDs that you want to analyze. A range of assets is specified with a dash, and multiple assetes are separated with a comma, e.g., 2-8, 9, 13, 15, 21, 34-38.
	#. Employ the Advanced Filtering capabilities by clicking on the **Advanced Filter** button. The **Query Builder** dialog will appear, as seen in :numref:`fig-R2DQueryBuilderDialog`. You can create a custom filter expression (SQL format) using operators, e.g., ``<, =, OR``, and the fields available in the imported asset inventory, e.g., ``BuildingType``. Operators and fields can be combined to perform complex filtering expressions such as ``"YearBuilt" < 1970  AND  "BuildingType"  =  'Wood'``. When the **Select** button is pressed, the assets that are specified in the **Asset Selection** box are added to the list of assets that will be analyzed. Pressing the **Clear Selection** button will clear the list of assets that will be analyzed.

.. _fig-WDNInputPanel:

.. figure:: figures/R2DWDNcsvInputPanel.png
  :align: center
  :figclass: align-center

  CSV to regional water network input panel.


GIS to Regional Water Network
*****************************

The **GIS to Regional Water Network** application imports a water distribution network from a set of user provided GIS files that represent the nodes and pipelines of the network.  The input panel is shown in :numref:`fig-R2DWDNgisInputPanel`. The GIS files can be in one of many common GIS file formats, e.g., shp, gdb, etc. 

#. The **Path to Nodes** box is where the user supplies the file path to the GIS file that contains the nodes of the water distribution network. At a minimum, the GIS file must contain a field providing the node identification numbers (id), in sequential order. Any number of attributes can be added to the node features to provide information that may be required by other applications in the workflow. R2D will load all feature attributes as columns in the **Node Information** table.

#. Similar to the nodes, the **Path to Pipelines** box is where the user supplies the file path to the GIS file that contains the pipelines of the water distribution network. Any number of attributes can be added to the pipeline features to provide information that may be required by other applications in the workflow. R2D will load all feature attributes as columns in the **Pipeline Information** table.

The **Node and Pipeline Information** table, shown in :numref:`fig-WDNInputPanel`, provides a spreadsheet containing the information provided by the GIS files, respectively. 

#. The **Coordinate Reference System (CRS)** dropdowns is where the coordinate reference system for a particular GIS file is specified. Each GIS file should have an accompanying CRS that will need to be specified so that R2D can place the features in the correct projected coordinate system. 

.. _fig-R2DWDNgisInputPanel:

.. figure:: figures/R2DWDNgisInputPanel.png
  :align: center
  :figclass: align-center

  GIS to regional water network input panel.
 
