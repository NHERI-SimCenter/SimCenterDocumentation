.. _lblUserDefInputs:

Inputs
===================

The following files must be provided by the user to execute the workflow.

.. jsonschema:: App_Schema.json#/properties/Inputs/configurationFile

An example configuration file is here: :download:`rWHALE_config.json <files/rWHALE_config.json>`


.. jsonschema:: App_Schema.json#/properties/Inputs/buildingSourceFile


.. jsonschema:: App_Schema.json#/properties/Inputs/modelFile


.. jsonschema:: App_Schema.json#/properties/Inputs/EDPspecs


.. jsonschema:: App_Schema.json#/properties/Inputs/eventFiles


Example input files are provided here: :download:`input_data.zip <files/input_data.zip>`, following the suggested directory structure for the user-defined inputs:

::

    cantilever_example
    ├── rWHALE_config.json              # configuration file
    └── input_data
        ├── model
            ├── cantilever.py           # model file
        ├── records
            ├── EventGrid.csv           # event grid file
            ├── RSN30.json              # event IM files
            ├── RSN63.json
            .
            .
            .
            ├── site0.csv               # site files
            ├── site1.csv
            .
            .
            .
            └── site8.csv
        ├── EDPspecs.json               # EDP specifications file
        └── input_params.csv            # building source file
