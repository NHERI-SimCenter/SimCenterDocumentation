.. _lblmodelingApp:

Modeling Applications
=====================

The **modeling application** consolidates information on the *structural analysis model* (SAM) used to represent the building on each site.
It takes as input the :ref:`BIM file <lblBuildingApp>`, the :ref:`EVENT file <lblEventApp>`, and information on the structural model used for response simulation, specified in the :ref:`configuration file <lblUserDefInputs>`.
The input structural model information is parsed into a ``SAM.json`` file, located in its corresponding **simulation working directory**.


.. figure:: _static/images/backendapps_Modeling.png
   :align: center
   :figclass: align-center

.. only:: HydroUQ_app

   .. raw:: html
      :file: _static/html/HydroUQ/createSAM.html

.. only:: EEUQ_app

   .. raw:: html
      :file: _static/html/EE-UQ/createSAM.html

.. only:: WEUQ_app

   .. raw:: html
      :file: _static/html/WE-UQ/createSAM.html

