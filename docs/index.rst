|full tool name|
=====================================================================

.. only:: html

   |developers|

   .. only:: R2D_app

      The |full tool name| (|app|) creates and launches simulation workflows to assess the regional impact of natural hazard events. Advanced capabilities facilitate high-resolution simulation. Researchers can investigate disaster scenarios or perform a probabilistic assessment by including uncertainties in both the hazard and the characteristics of the built environment. Assessments can include a comprehensive inventory of assets or focus on a distributed portfolio of structures, subjected to hurricanes, earthquakes, or other hazard events. The application integrates tools and libraries to support the creation of inventories, characterize hazard events, and simulate damage and losses on large inventories of buildings and civil infrastructure. User-defined models and calculation methodologies are also supported. Detailed results are provided in a standardized format to facilitate post-processing and further calculations to evaluate community impacts and recovery. The computations are performed by a simulation workflow that runs on either the user’s local machine or on a high-performance computer made available by |DesignSafe|.

   .. only:: PBE_app

      The |full tool name| (|app|) is an open-source desktop application designed to support the assessment of building performance under natural hazard events. The application quantifies performance in a probabilistic approach. Users can consider uncertainties in event intensity, structural behavior, component quantities and their limit state capacities, as well as the consequences of exceeding component limit states (i.e., experiencing damage). The |app| provides a convenient user interface and uses the settings provided by the user to prepare a simulation workflow description in a JSON file. This workflow description is used to run a simulation workflow on SimCenter's backend engine using sWHALE. The structural response estimation part of the workflow can run on the TACC high-performance computing cluster made available through |DesignSafe|. The performance assessment part runs locally using SimCenter's PELICUN performance assessment engine.

   .. only:: EEUQ_app

      The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to earthquake events. The application is focused on quantifying the uncertainties in the predicted response, given the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the user's local machine or on a high-performance computer made available by |DesignSafe|.


   .. only:: WEUQ_app

      The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to wind loading events. The application is focused on quantifying the uncertainties in the predicted response, given the uncertainties in models, wind loads, and analysis. The computations are performed in a workflow application that will run on either the user's local machine or on a high-performance computer made available by |DesignSafe|.


   .. only:: quoFEM_app

      The |full tool name| is an open-source research application that focuses on providing uncertainty quantification methods (forward, inverse, reliability, sensitivity, and parameter estimation) to researchers in natural hazards who utilize existing simulation software applications, typically Finite Element applications, in their work. The computations are performed in a workflow application that will run on either the user's local machine or on a high-performance computer made available by |DesignSafe|.

   
   .. only:: pelicun

      The |full tool name| is an open-source implementation of the PELICUN framework in a Python package. PELICUN is developed as an integrated multi-hazard framework to assess the performance of buildings and other assets in the built environment under natural hazards. Its foundation is the FEMA P58 performance assessment methodology that is extended beyond the seismic performance assessment of buildings to also handle wind and water hazards, bridges and buried pipelines, and performance assessment using vulnerability functions and damage models based on intensity measures (e.g., Hazus).


   .. only:: HydroUQ_app

      The |full tool name| (|app|) is an open-source research application for predicting the response of a building in a community subjected to water-borne events, namely tsunamis and storm surges. The application is focused on quantifying the uncertainties in the predicted structural response, given the uncertainties in models, loads, and analysis. The computations are performed in a workflow application that will run on a high-performance computer made available by |DesignSafe|.

   
   .. only:: Bootcamp

      The |full tool name| is a short course on programming Python, C, and C++ for personal computers (PC) through high-performance computers (HPC).  It is designed for engineering students who want to integrate SimCenter Workflow Tools with their research, use and extend their capabilities, and hopefully share their contributions with the broader research community.

   
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
   :quoFEM:common/user_manual/about/quoFEM/about  
   :pelicun:common/user_manual/about/pelicun/about
   :Hydro:common/user_manual/about/Hydro/about

   :R2D:common/front-matter/desktop/ack
   :PBE:common/front-matter/desktop/ack_pbe
   :EEUQ:common/front-matter/desktop/ack
   :WEUQ:common/front-matter/desktop/ack
   :quoFEM:common/front-matter/desktop/ack
   :pelicun:common/front-matter/pelicun/ack
   :Hydro:common/front-matter/desktop/ack

   common/front-matter/license
   common/front-matter/cite.rst

   :quoFEM:common/user_manual/releases/quoCapabilities   
   :quoFEM:common/user_manual/releases/quoReleaseNotes
   :quoFEM:common/user_manual/releases/quoPlans

   :EEUQ:common/user_manual/releases/eeCapabilities   
   :EEUQ:common/user_manual/releases/eeReleaseNotes
   :EEUQ:common/user_manual/releases/eePlans	   

   :WEUQ:common/user_manual/releases/weCapabilities
   :WEUQ:common/user_manual/releases/weReleaseNotes
   :WEUQ:common/user_manual/releases/wePlans

   :Hydro:common/user_manual/releases/hydroCapabilities
   :Hydro:common/user_manual/usage/desktop/hydro/releasenotes
   :Hydro:common/user_manual/releases/hydroPlans

   :PBE:common/user_manual/releases/pbeCapabilities
   :PBE:common/user_manual/releases/pbeReleaseNotes
   :PBE:common/user_manual/releases/pbePlans
      
   :R2D:common/user_manual/releases/r2dCapabilities 	 
   :R2D:common/user_manual/releases/r2dPlans 
   :R2D:common/user_manual/releases/r2dReleaseNotes
	    
   common/front-matter/glossary.rst
   common/front-matter/abbreviations.rst
	  
.. _lbl-user-manual:

.. toctree-filt::
   :caption: User Manual
   :maxdepth: 1
   :numbered: 4

   :EEUQ:common/user_manual/installation/desktop/installation
   :WEUQ:common/user_manual/installation/desktop/installation
   :PBE:common/user_manual/installation/desktop/installation
   :quoFEM:common/user_manual/installation/desktop/installation
   :R2D:common/user_manual/installation/desktop/installation
   :Hydro:common/user_manual/installation/desktop/installation
   :pelicun:common/user_manual/installation/pelicun/installation

   :quoFEM:common/user_manual/about/quoFEM/quoFEMtutorial
   .. :Hydro:common/user_manual/about/Hydro/HydroUQtutorial

   :EEUQ:common/user_manual/usage/desktop/usage
   :WEUQ:common/user_manual/usage/desktop/usage
   :Hydro:common/user_manual/usage/desktop/usage

   :PBE:common/user_manual/usage/desktop/usage
   :quoFEM:common/user_manual/usage/desktop/usage
   :R2D:common/user_manual/usage/desktop/usage
   :pelicun:common/user_manual/usage/pelicun/usage


   :R2D:common/user_manual/usage/desktop/R2DTool/tools
   :WEUQ:common/user_manual/usage/desktop/wind/tools
	:Hydro:common/user_manual/usage/desktop/hydro/tools



   :EEUQ:common/user_manual/examples/desktop/examples
   :WEUQ:common/user_manual/examples/desktop/examples
   :PBE:common/user_manual/examples/desktop/examples
   :Hydro:common/user_manual/examples/desktop/examples	
   :quoFEM:common/user_manual/examples/desktop/examples
   :R2D:common/user_manual/examples/desktop/examples
   :pelicun:common/user_manual/examples/pelicun/examples

   :EEUQ:common/user_manual/troubleshooting/desktop/troubleshooting
   :WEUQ:common/user_manual/troubleshooting/desktop/troubleshooting
   :PBE:common/user_manual/troubleshooting/desktop/troubleshooting
   :quoFEM:common/user_manual/troubleshooting/desktop/troubleshooting
   :R2D:common/user_manual/troubleshooting/desktop/troubleshooting
   :pelicun:common/user_manual/troubleshooting/pelicun/troubleshooting
   :Hydro:common/user_manual/troubleshooting/desktop/troubleshooting


   :Hydro:common/user_manual/usage/desktop/hydro/bestpractices

   :EEUQ:common/reqments/EEUQ
   :WEUQ:common/reqments/WEUQ
   :PBE:common/reqments/PBE
   :R2D:common/reqments/R2D
   :quoFEM:common/reqments/reqQUOFE
   :pelicun:common/reqments/reqPelicun
   :Hydro:common/reqments/HydroUQ


   common/user_manual/bugs
   :quoFEM:common/user_manual/dcv/quoFEM/quoFEM
   :quoFEM:common/user_manual/usage/desktop/quoFEM/usage_video
   .. :Hydro:common/user_manual/dcv/Hydro/HydroUQ


   :Hydro:common/user_manual/usage/desktop/hydro/helpvideo
   .. :Hydro:common/user_manual/user_inputs_documentation/User_Input_Documentation_Tables

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
   :docTestbeds:common/testbeds/Alameda/index

.. _lbl-dldb-manual:

.. toctree-filt::
   :caption: Damage and Loss DB
   :maxdepth: 1
   :numbered: 3

   :docDLDB:common/dldb/damage/index
   :docDLDB:common/dldb/repair/index

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
   :Hydro:common/technical_manual/desktop/technical_manual
   :Hydro:common/technical_manual/desktop/hydro/hazards/water
   :Hydro:common/technical_manual/desktop/hydro/mpm/mpm
   :Hydro:common/technical_manual/desktop/hydro/fvm/fvm
   :Hydro:common/technical_manual/desktop/hydro/swsolver/swsolver
   :Hydro:common/technical_manual/desktop/hydro/cfdsolver/cfdsolver
   :Hydro:common/technical_manual/desktop/hydro/verification/verification


   :pelicun:common/technical_manual/pelicun/background/background
   :pelicun:common/technical_manual/pelicun/verification/verification


.. _lbl-developer-manual:

.. toctree-filt::
   :caption: Developer Manual
   :maxdepth: 1
   :numbered: 4

   :desktop_app:common/developer_manual/how_to_build/desktop/how_to_build

   :desktop_app:common/developer_manual/architecture/desktop/architecture

   :EEUQ:common/developer_manual/how_to_extend/desktop/how_to_extend
   :WEUQ:common/developer_manual/how_to_extend/desktop/how_to_extend
   :quoFEM:common/developer_manual/how_to_extend/desktop/how_to_extend
   :R2D:common/developer_manual/how_to_extend/desktop/how_to_extend
   .. :Hydro:common/developer_manual/how_to_extend/desktop/how_to_extend

   :EEUQ:common/developer_manual/verification/desktop/verification
   :WEUQ:common/developer_manual/verification/desktop/verification
   :quoFEM:common/developer_manual/verification/desktop/verification
   :R2D:common/developer_manual/verification/desktop/verification
   .. :Hydro:common/developer_manual/verification/desktop/verification

   :desktop_app:common/developer_manual/coding_style/desktop/coding_style
   :pelicun:common/developer_manual/coding_style/pelicun/coding_style

   :docTestbeds:common/developer_manual/examples/desktop/examples

   :pelicun:common/developer_manual/API/pelicun/API


Contact
=======

|contact person|


References
==========

.. bibliography:: common/references.bib
