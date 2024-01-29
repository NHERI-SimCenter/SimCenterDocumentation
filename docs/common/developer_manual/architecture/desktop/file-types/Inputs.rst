.. _lblUserDefInputs:

Inputs
===================

The following files must be provided by the user to execute the workflow.

.. jsonschema:: File_Schema.json#/properties/Inputs/configurationFile


.. jsonschema:: File_Schema.json#/properties/Inputs/buildingSourceFile

The header schema, followed by an example input, is provided. Definitions for the keywords are given in the `Custom Inventory sheet <https://docs.google.com/spreadsheets/d/1bYV48cSmjQ6DUpc9eTKy2jrWLVEHMAuqjJnkYIsKetQ/edit#gid=0>`_.

.. csv-table:: InputDataSchema.csv
   :file: files/InputDataSchema.csv
   :header-rows: 2
   :align: center

.. _lblTransportationInputOption1:

.. jsonschema:: File_Schema.json#/properties/Inputs/transportationSourceFile1

A JSON file containing highway transportation roadways, bridges, and tunnels for the response simulation and damage/loss estimation steps of the workflow. This file contains all the information necessary for constructing AIM files for each bridge, tunnel, and roadway. The JSON file must contain the "nodes" object and at lease one of the "hwy_bridges", "hwy_tunnels", and "roadways" object. Involved key-item pairs are:

* "hwy_bridges": A JSON array of JSON Objects, each containing the following key/item pairs

.. csv-table:: InputDataSchemaBridge.csv
   :file: files/InputDataSchemaBridge.csv
   :header-rows: 2
   :align: center


* "hwy_tunnels": A JSON array of JSON Objects, each containing the following key/item pairs

.. csv-table:: InputDataSchemaTunnel.csv
   :file: files/InputDataSchemaTunnel.csv
   :header-rows: 2
   :align: center


* "roadways": A JSON array of JSON Objects, each containing the following key/item pairs

.. csv-table:: InputDataSchemaRoadway.csv
   :file: files/InputDataSchemaRoadway.csv
   :header-rows: 2
   :align: center


* "nodes": A long JSON Objects containing the following key/item pairs

.. csv-table:: InputDataSchemaTransportNode.csv
   :file: files/InputDataSchemaTransportNode.csv
   :header-rows: 1
   :align: center


.. jsonschema:: File_Schema.json#/properties/Inputs/modelFile


.. jsonschema:: File_Schema.json#/properties/Inputs/EDPspecs


.. jsonschema:: File_Schema.json#/properties/Inputs/eventFiles


