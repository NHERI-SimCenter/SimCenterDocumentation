
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
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/Loading.csv
  :include: {0: 'EL.*'}
  :exclude: {6: 'NA'}


.. include:: key.rst

UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/Uncertainty.csv
  :exclude: {6: 'NA'}

.. include:: key.rst

Modeling Requirements
---------------------

..
        .. csv-table:: Requirements - Modeling
          :header: "#", "Description", "Source", "Priority", "Status"
          :file: Modeling.csv

.. csv-filter:: Requirements - Modeling
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/Modeling.csv
  :exclude: {6: 'NA'}

.. include:: key.rst

Analysis Requirements
---------------------

..
        .. csv-table:: Requirements - Analysis
          :header: "#", "Description", "Source", "Priority", "Status"
          :file: Analysis.csv

.. csv-filter:: Requirements - Analysis
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/Analysis.csv
  :exclude: {6: 'NA'}

.. include:: key.rst


RV Requirements
---------------

..
        .. csv-table:: Requirements - Random Variables
          :header: "#", "Description", "Source", "Priority", "Status"
          :file: RV.csv

.. csv-filter:: Requirements - Random Variables
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/RandomVariables.csv
  :exclude: {6: 'NA'}

.. include:: key.rst

Common Research Application Requirements
----------------------------------------

.. csv-filter:: Requirements - CR
  :header: "#", "Description", "Source", "Priority", "Status"
  :file: _json/out/Common.csv

.. include:: key.rst
