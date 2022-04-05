|full tool name|
=====================================================================

.. only:: html

   |developers|

   .. only:: R2D_app


      The |full tool name| (|app|) is an open-source research application that can be used to simulate the performance of the built environment subjected to natural hazards. Version 1 will allow users to predict the performance of the buildings in the region when subjected to earthquake events. Version 2, due May 2021, will allow researchers to study the effects given a Hurricane event. Future version will allow users to study effects of lifleines and interdependencies. The computations are performed by a simulation workflow that will run on either the user's local machine or on a high performance computer made available by |DesignSafe|.

   .. only:: PBE_app

      The |full tool name| (|app|) is an open-source research application that can be used to predict the performance of a building subjected to earthquake events. The application is focused on quantifying building performance given the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|.

   .. only:: EEUQ_app

      The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to earthquake events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|.


   .. only:: WEUQ_app

      The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to wind loading events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, wind loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|.


   .. only:: quoFEM_app

      The |full tool name|  is an open-source research application which focuses on providing uncertainty quantification methods (forward, inverse, reliability, sensitivity and parameter estimation) to researchers in natural hazards who utilize existing simulation software applications, typically Finite Element applications, in their work. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|.

   .. only:: pelicun

      The |full tool name| is an open-source implementation of the |short tool name| framework in a Python package. It provides tools for assessment of damage and losses due to natural disasters. Its basis is the stochastic damage and loss model described in FEMA P58. While FEMA P58 aims to assess the seismic performance of a building, with the |app| we provide a more versatile, hazard agnostic tool that can estimate losses for several types of assets in the built environment.

      .. only:: Hydro

      The Water-borne Natural Hazards with Uncertainty Quantification Application (Hydro-UQ app) is an open-source research application that can be used to predict the response of a building a community subjected to events like tsunami and storm-surge. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, loads, and analysis. The computations are performed in a workflow application that will run on a high performance computer made available by |DesignSafe|.


   This document covers the features and capabilities of Version |tool version| of the tool. Users are encouraged to comment on what additional features and capabilities they would like to see in future versions of the application through the |messageBoard|.


.. _lbl-front-matter:

.. toctree-filt::
   :caption: About
   :maxdepth: 1
   :numbered: 4

   :PBE:common/user_manual/about/PBE/about
   :R2D:common/user_manual/about/R2D/about
   :EEUQ:common/user_manual/about/EEUQ/about
   :WEUQ:common/user_manual/about/WEUQ/about
   :quoFEM:common/user_manual/about/quoFEM/aboutQUOFEM
   :pelicun:common/user_manual/about/pelicun/about

   common/front-matter/ack
   common/front-matter/license
   common/front-matter/glossary.rst
   common/front-matter/abbreviations.rst
   :quoFEM:common/user_manual/usage/desktop/quoFEM/releasenotes   
   :R2D:common/user_manual/usage/desktop/releasenotes
   :Hydro:common/user_manual/usage/desktop/hydro/releasenotes
   :EEUQ:common/user_manual/usage/desktop/earthquake/releasenotes

	  
.. _lbl-user-manual:

.. toctree-filt::
   :caption: User Manual
   :maxdepth: 1
   :numbered: 4

   :pelicun:common/user_manual/installation/pelicun/installation
   :EEUQ:common/user_manual/installation/desktop/installation
   :WEUQ:common/user_manual/installation/desktop/installation
   :PBE:common/user_manual/installation/desktop/installation
   :quoFEM:common/user_manual/installation/desktop/installation
   :R2D:common/user_manual/installation/desktop/installation
   :Hydro:common/user_manual/installation/desktop/installation

   :EEUQ:common/user_manual/usage/desktop/usage
   :WEUQ:common/user_manual/usage/desktop/usage
   :Hydro:common/user_manual/usage/desktop/usage	 
   :PBE:common/user_manual/usage/desktop/usage
   :quoFEM:common/user_manual/usage/desktop/usage
   :R2D:common/user_manual/usage/desktop/usage
   :pelican:common/user_manual/usage/pelicun/usage

   :Hydro:common/user_manual/usage/desktop/hydro/resguide
   :Hydro:common/user_manual/usage/desktop/hydro/helpvideo

   :EEUQ:common/user_manual/troubleshooting/desktop/troubleshooting
   :WEUQ:common/user_manual/troubleshooting/desktop/troubleshooting
   :PBE:common/user_manual/troubleshooting/desktop/troubleshooting
   :quoFEM:common/user_manual/troubleshooting/desktop/troubleshooting
   :R2D:common/user_manual/troubleshooting/desktop/troubleshooting
   :pelican:common/user_manual/troubleshooting/pelicun/troubleshooting
   :Hydro:common/user_manual/troubleshooting/pelicun/errors

   :EEUQ:common/user_manual/examples/desktop/examples
   :WEUQ:common/user_manual/examples/desktop/examples
   :PBE:common/user_manual/examples/desktop/examples
   :quoFEM:common/user_manual/examples/desktop/examples
   :R2D:common/user_manual/examples/desktop/examples
   :pelicun:common/user_manual/examples/pelicun/examples


   :Hydro:common/user_manual/usage/desktop/hydro/bestpractices

   :EEUQ:common/reqments/EEUQ		
   :WEUQ:common/reqments/WEUQ
   :PBE:common/reqments/PBE
   :R2D:common/reqments/R2D
   :quoFEM:common/reqments/reqQUOFEM	
   :pelicun:common/user_manual/requirements/pelicun/requirements

   common/user_manual/bugs

.. _lbl-testbeds-manual:

.. toctree-filt::
   :caption: Testbeds
   :maxdepth: 1
   :numbered: 3

   :docTestbeds:common/testbeds/sf_bay_area/index
   :docTestbeds:common/testbeds/atlantic_city/index
   .. :docTestbeds:common/testbeds/memphis/index
   .. :docTestbeds:common/testbeds/anchorage/index
   :docTestbeds:common/testbeds/lake_charles/index

.. _lbl-technical-manual:



.. toctree-filt::
   :caption: Technical Manual
   :maxdepth: 1
   :numbered: 2

   :EEUQ:common/technical_manual/desktop/technical_manual
   :WEUQ:common/technical_manual/desktop/technical_manual
   :PBE:common/technical_manual/desktop/technical_manual
   :quoFEM:common/technical_manual/desktop/technical_manual
   :R2D:common/technical_manual/desktop/technical_manual
   :pelicun:common/technical_manual/pelicun/technical_manual
   :Hydro:common/technical_manual/desktop/hydro/hazards/water
   :Hydro:common/technical_manual/desktop/hydro/fvm/fvm
   :Hydro:common/technical_manual/desktop/hydro/swsolver/swsolver
   :Hydro:common/technical_manual/desktop/hydro/cfdsolver/cfdsolver

.. _lbl-developer-manual:

.. toctree-filt::
   :caption: Developer Manual
   :maxdepth: 1
   :numbered: 4

   :desktop_app:common/developer_manual/how_to_build/desktop/how_to_build

   :desktop_app:common/developer_manual/architecture/desktop/architecture
   :pelicun:common/developer_manual/architecture/pelicun/architecture

   :EEUQ:common/developer_manual/how_to_extend/desktop/how_to_extend
   :WEUQ:common/developer_manual/how_to_extend/desktop/how_to_extend
   :PBE:common/developer_manual/how_to_extend/desktop/how_to_extend
   :quoFEM:common/developer_manual/how_to_extend/desktop/how_to_extend
   :R2D:common/developer_manual/how_to_extend/desktop/how_to_extend

   :pelicun:common/developer_manual/how_to_extend/pelicun/how_to_extend

   :EEUQ:common/developer_manual/verification/desktop/verification
   :WEUQ:common/developer_manual/verification/desktop/verification
   :PBE:common/developer_manual/verification/desktop/verification
   :quoFEM:common/developer_manual/verification/desktop/verification
   :R2D:common/developer_manual/verification/desktop/verification
   :pelican:common/developer_manual/verification/pelicun/verification

   :desktop_app:common/developer_manual/coding_style/desktop/coding_style
   :pelicun:common/developer_manual/coding_style/pelicun/coding_style

   :docTestbeds:common/developer_manual/examples/desktop/examples
   :pelicun:common/developer_manual/examples/pelicun/examples

   :pelicun:common/developer_manual/API/pelicun/API


Contact
=======

|contact person|


References
==========

.. bibliography:: common/references.bib
