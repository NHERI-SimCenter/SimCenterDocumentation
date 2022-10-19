.. _Turbulence Inflow Tool:

Turbulence Inflow Tool
======================

.. only:: html

   **Jiawei Wan** [1]_, **Peter Mackenzie-Helnwein** [2]_

   The Turbulence Inflow Tool (TInF) is designed to collect all required properties and parameters
   needed for various turbulence inflow models in OpenFOAM, and to augment an existing wind-around-a-building model by adding the necessary sections to respective parameter definition files.

   The generic workflow involved is as follows.

   1.  Build your OpenFOAM model as you would without using a turbulence inflow model.  Use a generic patch with a suitable name for you will need to identify that patch by its name inside TInF.
   
   2. Run TInF following, identify your model folder, adjust the parameters as desired, and export to your model definition.
   Consult Chapter :ref:`sec_TInF-usage` for details on those steps.
   
   3. Run OpenFOAM using the updated model definition.

   This document covers the features and capabilities of Version |toolVersion|  of the tool. Users are encouraged to comment on what additional features and capabilities they would like to see in future versions of the application through the |messageBoard|.


.. note::

   The first open source release of ``OpenFOAM`` was in 2004. It was based on the ``FOAM`` code, which was originally developed by Henry Weller in 1989. As sometimes happens with open source software when commercial interests get involved, the code forked over time and a number of open source distributions from different entities are available. The two main distributions of the code come from the |openfoam.org| and from |openfoam.com|. Currently |app| compiles and runs with versions **6** and **7** of the code released by the |openfoam.org|.

.. _lblUserManual:

.. toctree::
   :caption: User Manual
   :maxdepth: 1
   :numbered: 4

   acknowledgment
   about
   installation
   userManual
   troubleshooting
   examples/examples
   bugs
   copyright

..
   common/user_manual/requirements/requirements

.. _lblTechnicalManual:

.. toctree::
   :caption: Technical Manual
   :maxdepth: 1
   :numbered: 2

   theory/turbulent_inflow


.. _lblDeveloperManual:

.. toctree::
   :caption: Developer Manual
   :maxdepth: 1
   :numbered: 4

   building
   validation/TinFverification
   codingStyle
..   
   architecture
   howToExtend



Contact
-------

Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna AT berkeley.edu

.. [1] University of Notre Dame
.. [2] University of Washington
