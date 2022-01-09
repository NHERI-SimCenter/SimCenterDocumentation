
.. _R2D_Requirements:

.. raw:: latex

    \clearpage

R2D Requirements
================

**R2D** is the UI for a regional simulation. It uses **rWhale** to run the workflow. The requirements from R2D come from many components.

.. csv-filter:: Requirements - R2D
  :header: "#", "Description", "Source", "Priority", "Version"
  :widths: 10, 50, 10, 10, 10	   
  :file: R2D.csv

.. include:: key.rst

Earthquake Loading Requirements
-------------------------------

.. csv-filter:: Requirements - EL
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :file: _out/Loading.csv
  :included_cols: 0,1,2,3,4,9
  :include: {0: 'EL\..*'}

.. include:: key.rst

Wind Loading Requirements
-------------------------

.. csv-filter:: Requirements - WL
  :header: "#", "Description", "Source", "Priority", "Status", "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,9
  :file: _out/Loading.csv
  :include: {0: 'WL\..*'}

.. include:: key.rst

Surge/Tsunami Loading Requirements
----------------------------------

.. csv-filter:: Requirements - HL
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10	   
  :file: HydroLoading.csv

.. include:: key.rst	     

UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :header: "#", "Description", "Source", "Priority", "Status", _, _, _, _, "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 9
  :file: _out/Uncertainty.csv

.. include:: key.rst


RV Requirements
---------------

.. csv-filter:: Requirements - Random Variables
  :header: "#", "Description", "Source", "Priority", "Status", _, _, _, _, "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 9
  :file: _out/RandomVariables.csv

.. include:: key.rst
	     

Common Research Application Requirements
----------------------------------------

.. csv-filter:: Requirements - CR
  :header: "#", "Description", "Source", "Priority", "Status", _, _, _, _, "Implementation"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 9
  :file: _out/Common.csv

.. include:: key.rst	 


