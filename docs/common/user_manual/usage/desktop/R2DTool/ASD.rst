ASD: Asset Definition
=====================

In this panel the user can import the databases of different asset classes. The user can select the type of asset from the **Asset Selection Ribbon**, e.g., Buildings and Gas Network, as shown on the left-hand side of :numref:`fig-buildingInputPanel`. The **Asset Selection Ribbon** appears when more than one type of asset is selected in the **GI: General Information** panel. Moreover, only the assets that are checked in the **GI: General Information** panel will appear in the **Asset Selection Ribbon**. As the user switches between assets, the main panel changes to reflect the applications available for the import of each type of asset. 

.. contents::
   :local:

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
  

Housing Unit Allocation
-----------------------

The **Housing Unit Allocation** application can be employed to augment an existing asset inventory with US Census demographic information and socio-economic information from the American Community Survey (ACS). The input panel is shown in :numref:`fig-R2DHUAPanel`. As seen in the figure, the asset information is supplied via selection of an already imported layer in R2D. Alternatively, a user can supply an asset layer in a GIS format, e.g., shapefile, geodatabase, and the supplied layer will be employed.

.. note:: R2D will always make a copy of the asset layer it is working with. Going forward, the copied asset layer is employed to preserve the original data.

The procedure is as follows:
	#. Given an asset inventory, R2D cross-references the assets with a US counties map (2021), generating a set of US county codes that overlap with the provided asset inventory.
	#. The US Census API is queried and the population demographic information within each county is downloaded at the block level and saved locally . Similarly, the ACS API is called to download socio-economic information and the data is saved as a second GIS file. The ACS data is saved at the block group level. The GIS files are found in the output folder specified by the user (shown below).
	#. The Census and ACS information from the downloaded GIS files is extracted and appended to the copied layer by performing a spatial join. This means that each asset within the copied layer will be augmented to contain the informtaion extracted from the Census block level layer and the ACS block group layer of which it is located in.

.. note:: The download of census data employs a modified version of the ``censusutil.py`` script from the `pyincore-data <https://github.com/IN-CORE/pyincore-data>`_ module, a component of IN-CORE. 

#. The **Asset Layer Selection Dropdown** is where the user selects the GIS layer that contains the asset inventory. When the user selects a layer, it will be copied automatically.

#. If the user provides their own GIS file with the asset inventory, they will also have to provide the **Coordinate Reference System (CRS)**. The CRS dropdown is where the coordinate reference system for a particular GIS file is specified so that it can be located in the correct projected coordinate system.

#. The **Census Date** dropdown is where the Census vintage is provided. Currently, the 2010 and 2020 Census dates are supported. 

#. The **Census Variables** input box is where the user can provide custom variables to download from the Census API. For the 2010 vintage the default variables are ``P005001,P005003,P005004,P005010``, and for the 2020 vintage, the default variables are ``P2_001N,P2_002N,P2_005N,P2_006N``. You can go to the Census website for a particular vintage to see what the variables mean.

	The default variables for 2010 are:
		- P005001 = Total
		- P005003 = Total!!Not Hispanic or Latino!!White alone
		- P005004 = Total!!Not Hispanic or Latino!!Black or African American alone
		- P005010 = Total!!Hispanic or Latino
	
	The default variables for 2020 are:
		- P2_001N=!!Total:
		- P2_002N=!!Total:!!Hispanic or Latino
		- P2_005N=!!Total:!!Not Hispanic or Latino:!!Population of one race:!!White alone
		- P2_006N=!!Total:!!Not Hispanic or Latino:!!Population of one race:!!Black or African American alone

#. The **ACS Date** dropdown is where the ACS vintage is provided. Currently, the 2010, 2015, and 2020 ACS dates are supported.

#. The **ACS Variables** input box is where the user can provide custom variables to download from the ACS API.

	For the 2010, 2015, and 2020 5-year ACS vintage the default variables are:
		- B19001_001E - Estimate!!Total
		- B19001_002E - Estimate!!Total!!Less than $10,000
		- B19001_003E - Estimate!!Total!!$10,000 to $14,999
		- B19001_004E - Estimate!!Total!!$15,000 to $19,999
		- B19001_005E - Estimate!!Total!!$20,000 to $24,999
		- B19001_006E - Estimate!!Total!!$25,000 to $29,999
		- B19001_007E - Estimate!!Total!!$30,000 to $34,999
		- B19001_008E - Estimate!!Total!!$35,000 to $39,999
		- B19001_009E - Estimate!!Total!!$40,000 to $44,999
		- B19001_010E - Estimate!!Total!!$45,000 to $49,999
		- B19001_011E - Estimate!!Total!!$50,000 to $59,999
		- B19001_012E - Estimate!!Total!!$60,000 to $74,999
		- B19001_013E - Estimate!!Total!!$75,000 to $99,999
		- B19001_014E - Estimate!!Total!!$100,000 to $124,999
		- B19001_015E - Estimate!!Total!!$125,000 to $149,999
		- B19001_016E - Estimate!!Total!!$150,000 to $199,999
		- B19001_017E - Estimate!!Total!!$200,000 or more
		- B19013_001E - Estimate!!Median household income in the past 12 months (in 2016 inflation-adjusted dollars)


#. The **Output Folder** is where the program will save the GIS files that are downloaded from the US Census API. 

#. The **Download Census Data Button** runs the process that extracts counties from the building inventory, calls the US Census and ACS APIs to download data for the extracted counties, and saves the data as GIS files to the output folder.

#. The **Census Block-level GIS File** and **American Community Survey Block Group Level GIS File** box provides the file paths to the respective GIS files. These paths will be populated automatically after the download process described above completes. Alternatively, you can provide their own Census and ACS layers to join to the building inventory. Clicking on the **Browse** button will open a dialog where you can select the appropriate file.

#. The **Extract Census Data Button** runs the process that extracts the Census and ACS data from the GIS files and appends that information to each asset in the asset layer copy. Users can now save the newly augmented layer by right-clicking on the layer in the layer tree and selecting the ``Export->Save As`` option.

.. _fig-R2DHUAPanel:

.. figure:: figures/R2DHUAPanel.png
  :align: center
  :figclass: align-center

  Housing Unit Allocation input panel.

