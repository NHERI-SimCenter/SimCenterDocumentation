.. _lblOutputs:

Outputs
===================

After DL assessment is complete, the workflow aggregates the resultant EDP.csv, DM.csv, and DV.csv file for each building asset into the following output files, located in the *results* folder.

.. jsonschema:: App_Schema.json#/properties/Outputs/outputEDP

An example EDP output file is here: :download:`EDP_{min id}-{max id}.csv <doc/EDP_1-19.csv>`, :download:`EDP.hdf <doc/EDP.hdf>`


.. jsonschema:: App_Schema.json#/properties/Outputs/outputDM

An example DM output file is here: :download:`DM_{min id}-{max id}.csv <doc/DM_1-19.csv>`, :download:`DM.hdf <doc/DM.hdf>`


.. jsonschema:: App_Schema.json#/properties/Outputs/outputDV

An example DV output file is here: :download:`DV_{min id}-{max id}.csv <doc/DV_1-19.csv>`, :download:`DV.hdf <doc/DV.hdf>`
