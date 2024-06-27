.. _lblOutputs:

Outputs
=======

After the DL assessment is complete, the workflow collects the EDP.csv, DM.csv, and DV.csv files produced for each building asset and aggregates the results into single output files. When run locally, the workflow returns the output in CSV format, which is located in the *results* folder. When run remotely, the workflow returns the output in HDF format, which is located in the job archive. The HDF files can be converted into CSV format as a post-processing step.

.. jsonschema:: File_Schema.json#/properties/Outputs/outputEDP

The header schema, followed by an example output, is provided:

.. csv-table:: OutputEDPSchema.csv
   :file: files/OutputEDPSchema.csv
   :header-rows: 4
   :align: center

.. jsonschema:: File_Schema.json#/properties/Outputs/outputDM

The header schema, followed by an example output, is provided:

.. csv-table:: OutputDMSchema.csv
   :file: files/OutputDMSchema.csv
   :header-rows: 3
   :align: center

.. jsonschema:: File_Schema.json#/properties/Outputs/outputDV

The header schema, followed by an example output, is provided:

.. csv-table:: OutputDVSchema.csv
   :file: files/OutputDVSchema.csv
   :header-rows: 4
   :align: center
