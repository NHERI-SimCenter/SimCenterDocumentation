.. _lblUserDefInputs:

Inputs
===================

The following files must be provided by the user to execute the workflow. Illustrations of the file format are obtained from Example 1.

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


A suggested directory structure for the user-defined inputs is:

::

    cantilever_example
    ├── rWHALE_config.json
    └── input_data
        ├── model
            ├── cantilever.py
        ├── records
            ├── EventGrid.csv
            ├── RSN30.json
            ├── RSN63.json
            .
            .
            .
            ├── site0.csv
            ├── site1.csv
            .
            .
            .
            └── site8.csv
        └── input_params.csv
