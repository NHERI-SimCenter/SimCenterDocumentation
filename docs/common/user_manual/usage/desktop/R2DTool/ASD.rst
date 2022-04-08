ASD: Asset Definition
=====================

In this panel the user can import the databases of different asset classes. The user can select the type of asset from the **Asset Selection Ribbon**, e.g., Buildings and Gas Network, as shown on the left-hand side of :numref:`fig-buildingInputPanel`. The **Asset Selection Ribbon** appears when more than one type of asset is selected in the **GI: General Information** panel. Moreover, only the assets that are checked in the **GI: General Information** panel will appear in the **Asset Selection Ribbon**. As the user switches between assets, the main panel changes to reflect the applications available for the import of each type of asset. 

.. contents::
   :local:

Buildings
---------

The buildings input panel, as shown in :numref:`fig-buildingInputPanel`, allows a user to input a building inventory database. The **Building Import Selection** combo box is where the user selects the application for the import of buildings, and for the generation of a building information model (BIM).

CSV to BIM
**********

The **CSV to BIM** application imports a building inventory database from a user provided .csv file. 

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

The **Building Information** table, shown in :numref:`fig-buildingInputPanel`, provides a user-editable spreadsheet containing the information provided by the building inventory database file. When a subset of buildings is selected for analysis, only the selected buildings will appear in the **Building Information** table. Pressing the **Clear Selection** button will clear the list of buildings that will be analysed and show all buildings in the **Building Information** table again. 

.. _fig-buildingInputPanel:

.. figure:: figures/R2DBuildingsInputPanel.png
  :align: center
  :figclass: align-center

  CSV to BIM input panel.

GIS to BIM
**********

The **GIS to BIM** application imports a building inventory database from a user-provided GIS file (e.g., shapefile, geodatabase). The input panel is shown in :numref:`fig-R2DGISBuildingsInputPanel`.

#. The **GIS Input File** box is where the user supplies the file path to the GIS file that contains the building inventory. Clicking on the **Browse** button will open a dialog where you can select the appropriate file. 

#. The **Building Selection Filtering** box is where the user can select a subset of buildings for analysis. There are two ways to select and filter buildings:

	#. Input a string of numbers that correspond to the building IDs that you want to analyze. A range of buildings is specified with a dash, and multiple buildings are separated with a comma, e.g., 2-8, 9, 13, 15, 21, 34-38.
	#. Employ the Advanced Filtering capabilities by clicking on the **Advanced Filter** button. The **Query Builder** dialog will appear, as seen in :numref:`fig-R2DQueryBuilderDialog`. You can create a custom filter expression (SQL format) using operators, e.g., ``<, =, OR``, and fields available in the imported building inventory, e.g., ``BuildingType``. Operators and fields can be combined to perform complex filtering expressions such as ``"YearBuilt" < 1970  AND  "BuildingType"  =  'Wood'``. When the **Select** button is pressed, the buildings that are specified in the **Building Selection** box are added to the list of buildings that will be analyzed. Pressing the **Clear Selection** button will clear the list of buildings that will be analyzed.

#. The **Building Information** table provides a user-editable spreadsheet containing the information provided by the building inventory database file. When a subset of buildings is selected for analysis, only the selected buildings will appear in the **Building Information** table. 

.. _fig-R2DGISBuildingsInputPanel:

.. figure:: figures/R2DGISBuildingsInputPanel.png
  :align: center
  :figclass: align-center

  GIS to BIM input panel.

Housing Unit Allocation
***********************

The **Housing Unit Allocation** application can be employed to augment an existing building inventory (supplied in a GIS format, e.g., shapefile, geodatabase) with census demographic information. The input panel is shown in :numref:`fig-R2DHUAPanel`. Given a building inventory, the **Housing Unit Allocation** application will download demographic data from the US Census website. First, the application cross-references the building inventory with a US counties map (2021), generating a set of unique US county codes that overlap with the building inventory. Next, the US census API is queried and the population demographic information within each county is downloaded at the block level and saved locally as GIS files to the output folder. The download of census data employs a modified version of the ``censusutil.py`` script from the `pyincore-data <https://github.com/IN-CORE/pyincore-data>`_ module, a component of IN-CORE. Lastly, the demographic information from the downloaded GIS files can be extracted and saved to a new layer that is a copy of the original building inventory. Each building within the new building inventory layer will contain the population demographics (percent inhabitants that are of black, hispanic, white, and other races), extracted from the downloaded census block level layer.

#. The **Building GIS File** box is where the file path to the GIS file that contains the building inventory is specified. Clicking on the **Browse** button will open a dialog where you can select the appropriate file. When a building GIS file is loaded, a copy of the original building inventory layer is automatically created. Going forward, the copied building inventory layer is employed, as to keep the original building inventory file intact. 

#. The **Coordinate Reference System (CRS)** dropdown is where the coordinate reference system for a particular GIS file is specified. Each GIS file should have an accompanying CRS that will need to be specified. 

#. The **Census Date** dropdown is where the census vintage is provided. Currently, the 2000 and 2010 census dates are supported. 

#. The **Output Folder** is where the program will save the GIS files that are downloaded from the US Census API. 

#. The **Download Census Data Button** runs the process that extracts counties from the building inventory, calls the US Census API to download demographic data for the extracted counties, and saves the data as GIS files to the output folder. 

#. The **Census Block-level GIS File** box provides the file path to the GIS file that should contain the block-level census data. This will be populated automatically if the **Download Census Data** process from above is run. Otherwise, users can supply their own data.  Clicking on the **Browse** button will open a dialog where you can select the appropriate file. 

#. The **Extract Census Data Button** runs the process that extracts the demographics data from the block-level GIS file and appends that information to each building in the building inventory layer copy. Users can now save the newly augmented layer by right-clicking on the layer in the layer tree and selecting the ``Export->Save As`` option.

.. _fig-R2DHUAPanel:

.. figure:: figures/R2DHUAPanel.png
  :align: center
  :figclass: align-center

  Housing Unit Allocation input panel.
