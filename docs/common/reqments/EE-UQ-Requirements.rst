
General Requirements
--------------------

.. csv-table:: Requirements - General
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 60, 10, 10, 10
  :file: generalEEUQ.csv

.. include:: key.rst

Loading Requirements
--------------------

..
        .. csv-table:: Requirements - Earthquake Loading
          :header: "#", "Description", "Source", "Priority", "Status"
          :widths: 10, 60, 10, 10, 10	   
          :file: EarthquakeLoading.csv

.. csv-filter:: Requirements - Earthquake Loading
  :file: _out/Loading.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6
  :include: {0: 'EL.*'}
  :exclude: {6: 'NA'}


.. include:: key.rst

UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :file: _out/Uncertainty.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6
  :exclude: {6: 'NA'}

.. include:: key.rst

Modeling Requirements
---------------------

.. csv-filter:: Requirements - Modeling
  :file: _out/Modeling.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6
  :exclude: {6: 'NA'}

.. include:: key.rst

Analysis Requirements
---------------------

.. csv-filter:: Requirements - Analysis
  :file: _out/Analysis.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6
  :exclude: {6: 'NA'}

.. include:: key.rst


RV Requirements
---------------


.. csv-filter:: Requirements - Random Variables
  :file: _out/RandomVariables.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6
  :exclude: {6: 'NA'}

.. include:: key.rst

Common Research Application Requirements
----------------------------------------

.. csv-filter:: Requirements - CR
  :file: _out/Common.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,6

.. include:: key.rst

