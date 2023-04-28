The following is the list of all requirements across all the tools. It is helpful to view an abstract hierarchy of the tools, showing **R2D** at the top and the components at the bottom. Each application pulls in many of the requirements from the others. For Example PBE, builds upon EE-UQ. It has it;'s own requirements, i.e. DL, but includes the loading, modeling and analysis requirements from EE-UQ. It specializes the UQ requirement, in that it only incorporates the sampling option. One set of requirements not shown in the figure is CR, a listing of all the common functionalty required of all the applications.


R2D
---

.. csv-filter:: Requirements - R2D
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: R2D.csv

.. include:: key.rst

PBE
---

.. csv-filter:: Requirements - PBE
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: generalPBE.csv

.. include:: key.rst

WE-UQ Requirements
------------------

.. csv-filter:: Requirements - WE
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: generalWE.csv

.. include:: key.rst


Hydro-UQ Requirements
---------------------

.. csv-filter:: Requirements - H
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: generalHydro.csv

.. include:: key.rst


EE-UQ Requirements
------------------

.. csv-filter:: Requirements - EE
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: generalEEUQ.csv

.. include:: key.rst

quoFEM Requirements
-------------------

.. csv-filter:: Requirements - QF
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :file: generalQUO-FEM.csv

.. include:: key.rst


Earthquake Loading Requirements
-------------------------------

.. csv-filter:: Requirements - EL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Loading.csv
  :include: {0: 'EL\..*'}
  
.. include:: key.rst


Wind Loading Requirements
-------------------------

.. csv-filter:: Requirements - WL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Loading.csv
  :include: {0: 'WL\..*'}

.. include:: key.rst

Surge/Tsunami Loading Requirements
----------------------------------

.. csv-filter:: Requirements - HL
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :included_cols: 0, 1, 2, 3, 4
  :file: HydroLoading.csv

.. include:: key.rst

UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods and Variables
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Uncertainty.csv


.. include:: key.rst


RV Requirements
---------------

.. csv-filter:: Requirements - Random Variables
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10  
  :file: _out/RandomVariables.csv

.. include:: key.rst


Modeling Requirements
---------------------

.. csv-filter:: Requirements - MOD
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Modeling.csv

.. include:: key.rst

Analysis Requirements
---------------------

.. csv-filter:: Requirements - ANA
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Analysis.csv

.. include:: key.rst


Damage & Loss Requirements
--------------------------

.. csv-filter:: Requirements - DL
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Damage.csv
  :include: {0: 'DL\..*'}

.. include:: key.rst


Recovery Requirements
---------------------

.. csv-filter:: Requirements - REC
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Recovery.csv

.. include:: key.rst


Common Research Application Requirements
----------------------------------------

.. csv-filter:: Requirements - CR
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Common.csv

.. include:: key.rst


BRAILS
------

.. csv-filter:: Requirements - BR
  :header: "#", "Description", "Source", "Priority", "Status", "WBS"
  :widths: 10, 50, 10, 10, 10, 10
  :file: BRAILS.csv

.. include:: key.rst


PELICUN
-------

.. csv-filter:: Requirements - P
  :header: "#", "Description", "Source", "Priority", "Status", "WBS"
  :widths: 10, 50, 10, 10, 10, 10
  :file: requirements_pelicun_general.csv

.. include:: key.rst

BE Database
-----------

.. csv-filter:: Requirements - BE
  :header: "#", "Description", "Source", "Priority", "Status", "WBS"
  :widths: 10, 50, 10, 10, 10, 10
  :file: BE.csv

.. include:: key.rst

DL Database
-----------


.. csv-filter:: Requirements - DLD
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2D"
  :widths: 10, 50, 10, 10, 10, 10, 10, 10, 10, 10, 10
  :file: _out/Damage.csv
  :include: {0: 'DLD.*'}

.. include:: key.rst




