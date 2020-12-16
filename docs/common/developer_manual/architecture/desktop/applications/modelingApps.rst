.. _lblmodelingApp:

Modeling Applications
=====================

The **modeling application** consolidates information on the *structural analysis model* (SAM) used to represent the building on each site.
It takes as input the :ref:`BIM file <lblBuildingApp>`, the :ref:`EVENT file <lblEventApp>`, and information on the structural model used for response simulation, specified in the :ref:`configuration file <lblUserDefInputs>`.
The input structural model information is parsed into a "SAM.json" file, located in its corresponding **simulation working directory**.

.. _figContext:

.. figure:: _static/images/backendapps_Modeling.png
   :align: center
   :figclass: align-center


The following options for modeling applications vary in the type of model and finite element program used for response simulation.

.. only:: EEUQ_App
   
   .. raw:: html
      :file: _static/html/EE-UQ/createSAM.html 

.. only:: WEUQ_App
   
   .. raw:: html
      :file: _static/html/WE-UQ/createSAM.html 

.. only:: RDT_App
   
   .. raw:: html
      :file: _static/html/RDT/createSAM.html
