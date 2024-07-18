.. _lblBuildingApp:

Building Applications
=====================

The **Building Application** creates *Building Information Model* (BIM) files for each building. It takes as input the range of asset IDs selected for simulation (expressed as "min" and "max" ID, specified in the :ref:`configuration file <lblUserDefInputs>`), and the building-specific parameters for each simulation (specified in the :ref:`building source file <lblUserDefInputs>`).
These inputs are parsed into ``#-BIM.json`` files, which are stored in the **results** folder.

.. figure:: _static/images/backendapps_Building.png
   :align: center
   :figclass: align-center

.. only:: HydroUQ_app

   .. raw:: html
      :file: _static/html/HydroUQ/createBIM.html

.. only:: EEUQ_app

   .. raw:: html
      :file: _static/html/EE-UQ/createBIM.html

.. only:: WEUQ_app

   .. raw:: html
      :file: _static/html/WE-UQ/createBIM.html
