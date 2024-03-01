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



GeoJSON to Asset
****************
The **GeoJSON to Asset** application, shown in :numref:`fig-R2DGeoJsonInputBeforeLoad`, is SimCenter's preferred method to load regional infrastructure inventory.
:numref:`fig-R2DGeoJSONInputExampleBuilding` is an example of a ``.geojson`` formatted database for buildings. 
It follows the format convention of the official ``.geojson`` structure as described `here <https://geojson.org/>`_. 
A "CRS" key-item pair is necessary to define the coordinate reference system, and the building stock information is described in the `"features"` array.
Each feature in the features array stands for one asset. Each feature must include a `{"type":"Feature"}` key-item pair, a `"geometry"` item, and a `"properties"` item.
`It can also contain an optional "id" item <https://datatracker.ietf.org/doc/html/rfc7946#section-3.2>`_, and the value of this item is either
a JSON string or number. 
The building information needed in later workflow should be included in the `"properties"` item. All information needed in the 
subsequent workflow (e.g., IMasEDP asset analysis and HAZUS-MH EQ damage and loss analysis) must be provided, otherwise, R2D may return errors.
The information required for typical analysis workflows can be found in :ref:`File Types and Schemas <lblUserDefInputs>` and in :ref:`R2D examples <lbl-examples>`. 
A special SimCenter convention is an attribute **"type"** must be included in the `"properties"` items. The value of **"type"**
describes the component type of this feature. For building inventory, the component type is always
**"Building"**, i.e., `{"type":"Building"}`. For other infrastructure, such as transportation 
infrastructure, the value of `"type"` could be `Bridge`, `Roadway`, and `Tunnel`.
Depending on the component type, the asset will be managed differently in later simulation workflow.
More descriptions can be found at :ref:`lbl-ASDTransport` and example 14 in :ref:`R2D examples <lbl-examples>`. 

:numref:`fig-R2DGeoJsonInputAfterLoadBuilding` is the panel after a ``.geojson`` buidling inventory database is loaded in R2D.
Users should select the buildings they want to analyze in the **Building Selection Filtering** box.
The selected buildings can be visualized in the **VIZ** panel.

.. _fig-R2DGeoJsonInputBeforeLoad:

.. figure:: figures/R2DGeoJsonInputBeforeLoad.png
  :align: center
  :figclass: align-center

  GeoJSON to Asset input panel.


.. literalinclude:: figures/R2DGeoJSONInputExampleBuilding.json
   :language: json
   :linenos:
   :caption: GeoJSON formatted database for buildings.
   :name: fig-R2DGeoJSONInputExampleBuilding

.. _fig-R2DGeoJsonInputAfterLoadBuilding:

.. figure:: figures/R2DGeoJsonInputAfterLoadBuilding.png
  :align: center
  :figclass: align-center
  
  GeoJSON to Asset input panel after loading a building ``.geojson`` database.
  

Regional Water Distribution Networks
-------------------------------------

The water distribution network input panel, as shown in :numref:`fig-wdnInputPanel`, allows a user to input the nodes and pipelines of a water distribution network. The **Regional Water Network Selection** combo box is where the user selects the application for the import of water distribution networks, and for the generation of a asset information model (AIM).

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

.. _lbl-ASDTransport:

Regional Transportation Infrastructure
-------------------------------------
The transportation infrastructure input panel allows users to input the inventory of a transportation network. The **Transportation Network Selection** combo box is where users select the application for importing transportation network inventory generating asset information models (AIM).  

GeoJSON to Asset
****************
The **GeoJSON to Asset** application, shown in :numref:`fig-R2DGeoJsonInputBeforeLoad`, is SimCenter's preferred method to load regional infrastructure inventory.
:numref:`fig-R2DGeoJSONInputExampleBuilding` is an example of a ``.geojson`` formatted database for transportation infrastructure. 
It follows the format convention of the official ``.geojson`` structure as described `here <https://geojson.org/>`_. 
A "CRS" key-item pair is necessary to define the coordinate reference system, and the infrastructure information is described in the `"features"` array.
Each feature in the features array stands for one asset. Each feature must include a `{"type":"Feature"}` key-item pair, a `"geometry"` item, and a `"properties"` item.
`It can also contain an optional "id" item <https://datatracker.ietf.org/doc/html/rfc7946#section-3.2>`_, and the value of this item is either
a JSON string or number. 
The information needed in later workflow should be included in the `"properties"` item. All information needed in the 
subsequent workflow (e.g., IMasEDP asset analysis and HAZUS-MH EQ damage and loss analysis) must be provided. Otherwise, R2D may return errors.
The information required for typical analysis workflows can be found in :ref:`File Types and Schemas <lblUserDefInputs>` and in :ref:`R2D examples <lbl-examples>`. 
A special SimCenter convention is an attribute **"type"** must be included in the `"properties"` items. The value of **"type"**
describes the component type of this feature. For transportation 
infrastructure, the value of `"type"` could be `Bridge`, `Roadway`, `Tunnel`, or other values. Assets with the same `"type"` (e.g., all bridges)
will be visualized in the same visualization layer. Assets with the same `"type"` will also be placed in the 
same working directory in the **Results** folder is in the **Output Directory** folder that is specified in R2D preferences. For each bridge (or other component type),
there can be other identification keys (such as, `"assetSubtype": "HwyBridge"` in :numref:`R2DGeoJSONInputExampleTransport`). The key `"assetSubtype"` is 
used by the R2D built-in Damage and Loss (DL) application **Pelicun3** when the HAZUS-MH damage and loss methods are selected. `"HwyBridge"` stands for highway bridge as classified in the
`Hazus Inventory Technical Manual <https://www.fema.gov/sites/default/files/documents/fema_hazus-6-inventory-technical-manual.pdf>`_ and the
`Hazus Earthquake Model Technical Manual <https://www.fema.gov/sites/default/files/documents/fema_hazus-earthquake-model-technical-manual-5-1.pdf>`_.
If a user selected to use **User-provided Fragilities** in **Pelicun3**, the key `"assetSubtype"` is not needed.
More descriptions can be found in example 14 in :ref:`R2D examples <lbl-examples>`. 

:numref:`fig-R2DGeoJsonInputAfterLoadTransport` is the panel after a ``.geojson`` transportation infrastructure inventory database is loaded in R2D.
Users should switch the viewing panel with the **component selection panel** and select the assets they want to analyze in the **Asset Selection Filtering** box.
The selected assets can be visualized in the **VIZ** panel.

.. note:: The outputs of the BRIALS Transportation tool use the default units of the inventory databse described in :numref:`lbl-BrailsTransportation`. Users need to convert the units to those defined in the :ref:`General Information <lblGI>` panel before loading the units to this Asset panel.

.. literalinclude:: figures/R2DGeoJSONInputExampleTransport.json
   :language: json
   :linenos:
   :caption: GeoJSON formatted database for buildings.
   :name: R2DGeoJSONInputExampleTransport

.. _fig-R2DGeoJsonInputAfterLoadTransport:

.. figure:: figures/R2DGeoJsonInputAfterLoadTransport.png
  :align: center
  :figclass: align-center

  GeoJSON to Asset input panel after loading a transportation infrastructure ``.geojson`` database.
  

GIS to Transportation Network AIM
*****************************

The **GIS to Transportation Network AIM** application imports a transportation network from user-provided GIS files that contain information on highway bridges, tunnels, and/or roadways.  The input panel is shown in :numref:`fig-R2DTransportGISInputPanel`. The GIS files can be in one of many common GIS file formats, e.g., shp, gdb, etc.

The Path to Roadways/Bridges/Tunnels box is where the user supplies the file path to the GIS file that contains the roadways/bridges/tunnels features in the transportation network. At a minimum, the GIS file must contain a field providing the identification numbers (id), in **sequential order**. Any number of attributes can be added to the features to provide information that may be required by other applications in the workflow. R2D will load all feature attributes as columns in a table in a similar way to :numref:`fig-R2DWDNgisInputPanel`. Only the Roadways/Bridges/Tunnels selected in the corresponding selection box will be analyzed in the later part of the workflow. 

Example GIS files for roadways, bridges, and tunnels that can be loaded to R2D with **GIS to Transportation Network AIM** can 
be found in the `github data repository <https://github.com/NHERI-SimCenter/R2DExamples>`_ of example 14 of :ref:`R2D examples <lbl-examples>`

.. _fig-R2DTransportGISInputPanel:

.. figure:: figures/R2DTransportGISInputPanel.png
  :align: center
  :figclass: align-center

  GIS to regional transportation network input panel.