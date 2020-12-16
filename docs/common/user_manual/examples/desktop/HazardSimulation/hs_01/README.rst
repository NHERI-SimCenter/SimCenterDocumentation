.. _lblHS-Example1:

Northern San Andreas Earthquake Scenario
========================================

This example will use a simulation of one Northern San Andreas (NSA) Earthquake to work through the basic functions of |short tool name| and user inputs. In this example, we are interested in the ground motion intensities in the Bay Area subjected to a large-magnitude earthquake from NSA. For the demonstration, 16 sites are selected in a grid roughly covering San Francisco County.

.. figure:: figures/fault_sites.png
   :align: center
   :width: 600
   :figclass: align-center

   Northern San Andreas fault and example sites

Users are expected to provide a csv file that defines the Longitude and Latitude values of interested sites. For instance, the locations of 16 example sites are shown in the table below.

+----------+-------------+-------------+
| Station  | Latitude    | Longitude   |
+----------+-------------+-------------+
| 1        | 37.80161    | -122.40500  |
+----------+-------------+-------------+
| 2        | 37.78161    | -122.40500  |
+----------+-------------+-------------+
| 3        | 37.76161    | -122.40500  |
+----------+-------------+-------------+
| ...      | ...         | ...         |
+----------+-------------+-------------+

To create the earthquake scenario, |short tool name| first reads the user's configuration of the fault. In this case, we want to select **1** realization from existing Earthquake Rupture Forecast (**ERF**) models (e.g., **WGCEP (2007) UCERF2 - Single Branch**), and the resulting earthquake has a magnitude between **7.8** and **8.0**.

.. literalinclude:: input/fault_config.json
   :language: JSON

.. note::
   |short tool name| currently support the following **"ERF"** **"Model"**:
       1. "WGCEP (2007) UCERF2 - Single Branch"
       2. "Mean UCERF3"
       3. "Mean UCERF3 FM3.1"
       4. "Mean UCERF3 FM3.2"

Then users are expected to provide ground motion information including number of simulations per site (**"NumberPerSite"**), ground motion prediction equation type (**"GMPE"**), intensity measure correlation models (**"CorrelationModel"**), and interested intensity measures (**"IntensityMeasure"**).

.. literalinclude:: input/event_config.json
   :language: JSON

.. note::
  |short tool name| currently support the following **"GMPE"**:
      1. "Abrahamson, Silva & Kamai (2014)"
      2. "Boore, Stewart, Seyhan & Atkinson (2014)"
      3. "Campbell & Bozorgnia (2014)"
      4. "Chiou & Youngs (2014)"

  And, the following **"CorrelationModel"** are available:
      1. "Baker & Jayaram (2008)" (inter-event)
      2. "Jayaram & Baker (2009)" (intra-event)
      3. "Loth & Baker (2013)" (intra-event)
      4. "Markhvida et al. (2017)" (intra-event)

  For more information about the spatial correlation models, please see :ref:`lblCorrelation`


|short tool name| then computes user-defined intensity measures for all given sites. For instance, in this example, response spectra are computed for the 16 example sites.

.. figure:: figures/site_psa.png
   :align: center
   :width: 1200
   :figclass: align-center

   Simulated response spectra (100 per site)

Users can provide their account information to |short tool name| which will download and parse PEER NGA-West records to local directory.

.. literalinclude:: input/peernga_config.json
   :language: JSON

Users can specify this output directory as well as input and working file directories.

.. literalinclude:: input/directory_config.json
   :language: JSON

For instance, given the directories defined above, |short tool name| will prepare and save outputs in the following data structure.

::

    HazardSimulation
    └── test
        └── records             # output directory
            ├── EventGrid.csv   # site map file
            ├── RSN63.json      # ground motion time history
            ├── RSN169.json
            .
            .
            .
            └── scenario1       # scenario folder
                ├── site0.csv   # site ground motion list
                ├── site1.csv
                .
                .
                .
                └── site15.csv
