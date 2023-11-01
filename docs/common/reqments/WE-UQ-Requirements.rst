

General Requirements
--------------------

.. csv-table:: Requirements - General
  :header: "#", "Description", "Source", "Priority", "Version", "WBS"
  :widths: 10, 60, 10, 10, 10, 10
  :file: generalWE.csv

.. include:: key.rst

Loading Requirements
--------------------

.. csv-table:: Requirements - Wind Loading
  :header: "#", "Description", "Source", "Priority", "Version"
  :widths: 10, 60, 10, 10, 10
  :file: WindLoading.csv


.. .. csv-filter:: Requirements - Earthquake Loading
  :file: _out/Loading.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,7
  :include: {0: 'WL*'}


.. include:: key.rst

UQ Requirements
---------------


.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :file: _out/Uncertainty.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,7
  :exclude: {7: 'NA'}



.. include:: key.rst

Modeling Requirements
---------------------


.. csv-filter:: Requirements - Modeling
  :file: _out/Modeling.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,7
  :exclude: {7: 'NA'}

.. include:: key.rst


Analysis Requirements
---------------------

.. csv-filter:: Requirements - Analysis
  :file: _out/Analysis.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,7
  :exclude: {7: 'NA'}


.. include:: key.rst

Common Research Application Requirements
----------------------------------------

..
  .. csv-table:: Requirements - CR
    :header: "#", "Description", "Source", "Priority", "Status"
    :widths: 10, 60, 10, 10, 10
    :file: commonR.csv

.. csv-filter:: Requirements - CR
  :file: _out/Common.csv
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation", "Implementation", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,7


.. include:: key.rst
