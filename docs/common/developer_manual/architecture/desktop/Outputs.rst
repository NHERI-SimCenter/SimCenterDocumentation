.. _lblOutputs:

Outputs
===================

After DL assessment is complete, the workflow aggregates the resultant EDP.csv, DM.csv, and DV.csv file for each building asset into the following output files, located in the *results* folder. Illustrations of the file format are obtained from Example 1.

.. jsonschema:: App_Schema.json#/properties/Inputs/configurationFile

An example configuration file is here: :download:`rWHALE_config.json <doc/rWHALE_config.json>`


.. jsonschema:: App_Schema.json#/properties/Inputs/buildingSourceFile

An example building source file is here: :download:`input_params.csv <doc/input_params.csv>`


.. jsonschema:: App_Schema.json#/properties/Inputs/modelFile

An example model file is here: :download:`cantilever.py <doc/cantilever.py>`


.. jsonschema:: App_Schema.json#/properties/Inputs/eventFiles

An example event grid file is here: :download:`EventGrid.csv <doc/EventGrid.csv>`

An example seismic event file is here: :download:`RSN30.json <doc/RSN30.json>`

An example site file is here: :download:`site0.csv <doc/site0.csv>`
