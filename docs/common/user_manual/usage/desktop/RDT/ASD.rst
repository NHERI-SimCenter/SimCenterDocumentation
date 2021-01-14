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

The **CSV to BIM** application imports a building inventory database from a user-provided .csv file. 

#. The **Path to Buildings Database** box is where the user supplies the file path to the .csv file that contains the building inventory. At a minimum, the .csv file must contain columns providing the building identification numbers (ID), in sequential order, and the latitudes and the longitudes of the locations of the buildings. Any number of columns can be added to the file to provide information required by other applications in the workflow.  

#. The **Building Selection** box is where the user can select a subset of buildings to be analyzed. A range of buildings is specified with a dash, and multiple buildings are separated with a comma, e.g., 2-8, 9, 13, 15, 21, 34-38. When the **Select** button is pressed, the buildings that are specified in the **Building Selection** box are added to the list of buildings that will be analysed.

#. The **Building Information** table provides a user-editable spreadsheet containing the information provided by the building inventory database file. When a subset of buildings are selected for analysis, only the selected buildings will appear in the **Building Information** table. Pressing the **Clear Selection** button will clear the list of buildings that will be analysed and show all buildings in the **Building Information** table again. 

.. _fig-buildingInputPanel:

.. figure:: figures/RDTBuildingsInputPanel.png
  :align: center
  :figclass: align-center

  CSV to BIM input panel.




