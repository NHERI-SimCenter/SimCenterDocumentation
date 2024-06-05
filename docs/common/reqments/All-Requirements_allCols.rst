The following is the list of application requirements across all the SimCenter tools. It is helpful to view an abstract hierarchy of the tools, showing **R2D** at the top and the components at the bottom. Each tool can pull in requirements from other applications lower on the hierarchy. For example, **PBE** builds upon **EE-UQ**. It has its own requirements, i.e. **DL**, but includes the loading, modeling, and analysis requirements from **EE-UQ**. It specializes the **UQ** requirement, in that it only incorporates the sampling option. One set of requirements not shown in the figure is **CR**, the list of common research functionalities required in all the applications.


.. .. raw:: latex

..     \begin{landscape}
    
R2D Requirements
----------------

.. csv-filter:: Requirements - R2D
  :header: "#", "Description", "Source", "Priority", "Status", "R2D"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalR2D.csv
  :class: longtable

.. include:: key.rst

PBE Requirements
----------------

.. csv-filter:: Requirements - PBE
  :header: "#", "Description", "Source", "Priority", "Status", "PBE"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalPBE.csv
  :class: longtable

.. include:: key.rst

WE-UQ Requirements
------------------

.. csv-filter:: Requirements - WE
  :header: "#", "Description", "Source", "Priority", "Status", "WE-UQ"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalWE.csv
  :class: longtable

.. include:: key.rst

Hydro-UQ Requirements
---------------------

.. csv-filter:: Requirements - H
  :header: "#", "Description", "Source", "Priority", "Status", "Hydro-UQ"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalHydro.csv
  :class: longtable
	 

.. include:: key.rst

EE-UQ Requirements
------------------

.. csv-filter:: Requirements - EE
  :header: "#", "Description", "Source", "Priority", "Status", "EE-UQ"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalEEUQ.csv
  :class: longtable	 

.. include:: key.rst

quoFEM Requirements
-------------------

.. csv-filter:: Requirements - QF
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalQUO-FEM.csv
  :class: longtable	 

.. include:: key.rst

Earthquake Loading Requirements
-------------------------------

.. csv-filter:: Requirements - EL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 55, 8, 10, 15, 10, 10, 10
  :file: Loading.csv
  :include: {0: '\**EL.*|#'}
  :included_cols: 0, 1, 2, 3, 4, 6, 9, 10
  :class: longtable		  		  
  
.. include:: key.rst

Wind Loading Requirements
-------------------------

.. csv-filter:: Requirements - WL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 10, 55, 8, 10, 15, 10, 10, 10
  :file: Loading.csv
  :include: {0: '\**WL.*|#'}
  :included_cols: 0, 1, 2, 3, 4, 7, 9, 10
  :class: longtable		  		  

.. include:: key.rst

Surge/Tsunami Loading Requirements
----------------------------------

.. csv-filter:: Requirements - HL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 10, 65, 8, 10, 15, 25, 6, 6
  :included_cols: 0, 1, 2, 3, 4, 8, 9, 10
  :file: Loading.csv
  :include: {0: '\**HL.*|#'}
  :class: longtable

.. include:: key.rst

UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 35, 10, 10, 15, 10, 10, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  :file: Uncertainty.csv
  :class: longtable

.. include:: key.rst

RV Requirements
---------------

.. csv-filter:: Requirements - Random Variables
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 40, 10, 10, 15, 10, 10, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  :file: RandomVariables.csv
  :class: longtable

.. include:: key.rst

Modeling Requirements
---------------------

.. csv-filter:: Requirements - MOD
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 50, 10, 10, 15, 10, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 6, 7, 8, 9, 10
  :file: Modeling.csv
  :class: longtable

.. include:: key.rst

Analysis Requirements
---------------------

.. csv-filter:: Requirements - ANA
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 50, 10, 10, 15, 10, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 6, 7, 8, 9, 10
  :file: Analysis.csv
  :class: longtable

.. include:: key.rst

Damage & Loss Requirements
--------------------------

.. csv-filter:: Requirements - DL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 50, 8, 8, 12, 10, 20
  :included_cols: 0, 1, 2, 3, 4, 9, 10
  :file: Damage.csv
  :class: longtable

.. include:: key.rst

Recovery Requirements
---------------------

.. csv-filter:: Requirements - REC
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 50, 10, 10, 15, 10
  :included_cols: 0, 1, 2, 3, 4, 10
  :file: Recovery.csv
  :class: longtable

.. include:: key.rst

Common Research Application Requirements
----------------------------------------

.. csv-filter:: Requirements - CR
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "Hydro-UQ", "PBE", "R2D"
  :widths: 8, 45, 8, 8, 12, 10, 10, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  :file: Common.csv
  :class: longtable

.. include:: key.rst

BRAILS Requirements
-------------------

.. csv-filter:: Requirements - BR
  :header: "#", "Description", "Source", "Priority", "Status", "BRAILS"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalBRAILS.csv
  :class: longtable

.. include:: key.rst

PELICUN Requirements
--------------------

.. csv-filter:: Requirements - P
  :header: "#", "Description", "Source", "Priority", "Status", "PELICUN"
  :widths: 8, 55, 8, 8, 12, 15
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalPELICUN.csv
  :class: longtable

.. include:: key.rst

BE Database Requirements
------------------------

.. csv-filter:: Requirements - BE
  :header: "#", "Description", "Source", "Priority", "Status", "DB-BE"
  :widths: 8, 55, 10, 10, 12, 10
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalBE.csv
  :class: longtable

.. include:: key.rst

DL Database Requirements
------------------------

.. csv-filter:: Requirements - DLD
  :header: "#", "Description", "Source", "Priority", "Status", "DB-DL"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4, 5
  :file: generalDBDL.csv
  :class: longtable

.. include:: key.rst


.. .. raw:: latex

..     \end{landscape}
	     
