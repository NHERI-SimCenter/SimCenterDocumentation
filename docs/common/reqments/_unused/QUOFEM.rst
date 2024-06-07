.. raw:: latex

    \clearpage
    
.. only: requirements

   quoFEM Requirements
   ===================
   
   The following are the requirements for the quoFEM application. quoFEM is an
   application providing uncertainty quantification (UQ) and optimization methods to existing FEM applications. quoFEM
   has a lower-level interface to UQ and optimization methods than the other applications
   (WE-UQ, EE-UQ, and PBE). It is thus a more powerful tool providing more capabilities for
   researchers. All requirements in this section are related to work in sections 1.3.7, 1.3.8,
   and 1.3.9 of the WBS.

.. only: quoFEM

   .. _lblRequirements:

   ************
   Requirements
   ************

   The purpose of presenting these requirements is to inform the community about the present capabilities of the |app| and features that could be added. The original set of requirements has come from a set of grand challenge reports, **GC**. These original requirements have been broken into a smaller set of deliverable features by the senior faculty associated with the project, **SP**. Additional requirements have come from users, **U** See section :ref:`features` if you have additional features you would like to see.


quoFEM Requirements
-------------------

.. csv-filter:: Requirements - quoFEM
  :header: "#", "Description", "Source", "Priority", "Status"
  :widths: 10, 50, 10, 10, 10
  :included_cols: 0,1,2,3,4
  :file: quoFEM.csv


UQ Requirements
---------------

.. csv-filter:: Requirements - Uncertainty Quantification Methods
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2DTool", "HydroUQ"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,5
  :file: Uncertainty.csv



.. csv-filter:: Requirements - Random Variables
  :header: "#", "Description", "Source", "Priority", "Status", "quoFEM", "EE-UQ", "WE-UQ", "PBE", "R2DTool", "HydroUQ"
  :widths: 10, 50, 10, 10, 10, 10
  :included_cols: 0,1,2,3,4,5
  :file: RandomVariables.csv

.. include:: key.rst


