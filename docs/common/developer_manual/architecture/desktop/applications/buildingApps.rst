.. _lblBuildingApp:

Building Applications
=====================


The **building application** creates *building information model* (BIM) files for each building. It takes as input the range of asset IDs selected for simulation (expressed as "min" and "max" ID, specified in the :ref:`configuration file <lblUserDefInputs>`) and the building-specific parameters for each simulation (specified in the :ref:`building source file <lblUserDefInputs>`).
The inputs are parsed into ``#-BIM.json`` files in the **results** folder.

.. _figContext:

.. figure:: _static/images/backendapps_Building.png
   :align: center
   :figclass: align-center


The following options for building applications vary in the file type of the input building source file it processes.


.. only:: RDT_app
  
   .. raw:: html
     :file: _static/html/RDT/createBIM.html


