.. _lblArchitecture:

*********************
Software Architecture
*********************

The SimCenter is developing a number of computational applications: quoFEM, EE-UQ, WE-UQ, HydroUQ, PBE, and RDT. These applications are intended to advance the field of natural hazard engineering (NHE) at both the building level scale and regional level scale. These applications link together existing open-source software applications, databases and software libraries by employing scientific workflows. The SimCenter applications are as such scientific workflow systems. In contrast to more general purpose scientfic workflow systems (Taverna[Oinn2003], Kepler[Goecks2010], PegasuspDeelman2015]), the SimCenter workflows that are launched are constrained in complexity and have been designed specifically for researchers in natural hazards engineering. Unlike these more powerful scientific workflow systems, the primary focus of SimCenter scientific workflow systems is for creating workflows that run multiple times inside applications that generate responses that include uncertainty quantification (UQ) measures. A consequence outputting uncertainty quantification (UQ) measures, is the need to utilize high performance computers for most any thing but trivial example problems which can be done using Cloud services. 

To facilitate the development of a number of applications and to encourage their reuse and extension by other NHE researchers, the SimCenter is providing the NHE community with a software framework for building such applications. From this framework the SimCenter is building the applications, of which |app| is but one, that it releases. These individual applications are built from the components of the framework. The components of the SimCenter are grouped, as shown in  figure below, into the following components:

#. Cloud: applications/libraries for communicating with remote web services to launch and monitor applications on HPC resources and to upload and download files from the filesystems of such resources.

#. UQ: applications for performing sampling, sensitivity, reliability and optimization methods.

#. SAM: applications for creating finite element models.

#. EVENT: applications for creating loads on buildings and infrastructure given a natural hazard event.

#. FEM: application for determining the response parameter of the building/lifeline given applied loads.

#. DL: application to determine the damage & loss to the builing/infrastructure given the event.

#. EDP: application to determine the response parameter given the event, building/lifeline, and damage and loss application.

#. BRAILS: a framework of applications for creating regional level building inventories using machine learning.   

#. Databases containing information on building inventories for regional simulatioons, consequence functions for the DL applications, and experimental and corresponding simulation models for future machine learning based AI algorithms.


 Within the natural hazards engineering community, there exists a number of widely used open-source applications, e.g. OpenFOAM, and online datasets, e.g. PEER NGA, that researchers are currently using. As a consequence, and to avoid duplication, SimCenter applications incorprate many of the widely used appliecations, e.g. OpenFOAM. To do this SimCenter develops pre- and post-processors to these existing applications and utilize web-technologies for accessing online services.

   
.. _figFramework:

.. figure:: figures/SimCenterFramework.png
   :align: center
   :width: 800
   :figclass: align-center

   SimCenter Software Framework

The SimCenter scientific workflow systems are aimed at facilitating the use, reuse and extension of common workflows encoutred in NHE by a broad range of natural hazards engineering researchers with varying levels of software skills. In order to encourage this use and adoption, this chapter presents the software architecture for the SimCenter framework and |app| using the `C4 model <https://c4model.com>`_. The **C4** model is graphical approach for documenting software architecture through diagrams that describe and communicate the software architecture at different levels of abstraction. It is a top-down approach which starts at a high level (level 1) showing how a user would interact with the software and drills down through three more levels, with level 4 containing the typical UML diagrams. The choice of the **C4** model was made to provide NHE researchers with a diverse range of software architecture knowledge an understanding of the software architecture behind SimCenter applications that fits their skill level. The four levels:

- Level 1: The level one diagram is a system diagram that shows how the software system fits in the real world in terms of people who use it and other software systems it intercat with.
- Level 2: The level two is a container diagram show the the containers (applications, databases, etc.) that  make up the software system.
- Level 3: Level three diagram are component diagrams, showing how the componets pf the individual containers.
- Level 4: The level 4 diagrams show how the individual components are implemented. They are typically UML class diagrams.

The following sections present the architecture of SimCenter the SimCenter to level 3:

.. note::

   1. **Workflow**: “The automation of a business process, in whole or part, during which documents, information or tasks are passed from one participant to another for action, according to a set of procedural rules.” [Workflow Management Coalition].

   2. **Scientific Workflow**: "A large scale loosely coupled application consisting of commodity off-the-shelf software components" [Benchmarking Grid Applications for Performance and Scalability Predictions] for performing an in-silico workflow. "The simplest computerized scientific workflows are scripts that call in data, programs, and other inputs and produce outputs that might include visualizations and analytical results".[Wikipedia, https://en.wikipedia.org/wiki/Scientific_workflow_system]

   3. **Scientific Workflow System**: software to set-up, schedule, run, and monitor a user defined scientific workflow.

   4. **Software Framework**: A software framework provides a foundation on which software developers can build programs for a specific domain. For example, a framework may include predefined classes and functions that can be used to process input, manage hardware devices, and interact with system software. This streamlines the development process since programmers don't need to reinvent the wheel each time they develop a new application.
      
      
Overview
========

A Level 1 diagram showing the system context for the SimCenter applications, i.e. how it fits in the world, is shown in :numref:`figContext`. It shows SimCenter applications (EE-UQ, WE-UQ, PBE, RDT) as a box in the center surrounded by the user and the systems it and the user interact with. The SimCenter applications allows user to create and run scientific workflow applications, the data for the applications may be obtained from the web or DataDepot, the workflow applications are run on either the local desktop or on some HPC at |DesignSafe|.

.. _figContext:

.. figure:: figures/context.png
   :align: center
   :width: 800
   :figclass: align-center

   System context diagram for SimCenter applications.

Given how SimCenter applications fit in with the environment, a level 2 diagrams now demonstrates how the SimCenter applications are broken into high level components. The SimCenter applications are, as shown in :numref:`figContainer`, broken into two components: A front end UI and a back end application that runs the workflow. The front end applications are desktop applications written using the cross-platform Qt framework. The back end is an application that processes the input from the front end, which comes in the form of a JSON file, creates a workflow and runs it. The workflow applications, written in Python, C, or C++, utilize existing applications were possible and run on either the local desktop machine or on a HPC utilizing resources made available to NHE community through DesignSafe.

.. _figContainer:

.. figure:: figures/container.png
   :align: center
   :width: 800
   :figclass: align-center

   System container diagram for SimCenter applications.

Two level 3 diagrams are now presented which break up the two containers into the major building blocks or components in C4 terminology. In :numref:`figComponentFront` the component diagram for the front end UI is presented. It outlines the interaction between the user and the individual graphical elements (widgets) of the UI. Given the analogy of a jigsaw puzzle, the user selects which piece of the jigsaw puzzle they are working on in the component selection widget. The widget for the jigsaw piece will then be displayed on the desktop. The user for each jigsaw piece then selects which application to run for that piece, and for the chosen application, they provide the inputs. When the inputs are all provided, the user can select to run the simulations locally or remotely. For jobs that run remotely, the user can download and review previously run simulations. As seen the widgets may subsequently interact with web services through HTTPS requests, or with DesignSafe utilizing TAPIS Restful API through the RemoteService container.

.. _figComponentFront:

.. figure:: figures/componentFront.png
   :align: center
   :width: 800
   :figclass: align-center

   Component diagram for front end UI.

The component diagram for the backend application shown in :numref:`figComponentBack`, shows that the backend is made up of a number of component applications. The application ``femUQ.py`` is the application that parses the input from the front end, sets up the workflow by creating a ``workflow_driver`` script and then launchin the UQ engine. Which UQ Engine and which applications to run in the workflow, is determined from the data passed from the UI and information contained in a file, ``WorkflowApplication.json``. The ``WorkflowApplication.json`` file is a file that maps the applications specified in the output from the UI with a specific application contained on the users local machine or at the remote HPC resource, as such it allow the researchers to modify the applications that may be run in the workflow w/o the need to recompile the application. Once the ``workflow_driver`` file is created, control is passed to a UQ engine, which repeatedly runs the ``workflow_driver`` to generate the results. In running the workflow some of the applications will invoke applications not developed to meet the API. For such applications pre- and post-processors are provided.
The figure shows the backend application running locally or remotely on a HPC at DesignSafe.


.. _figComponentBack:

.. figure:: figures/componentBack.png
   :align: center
   :width: 800
   :figclass: align-center

   Component diagram for backend application.

To better understand the flow of control for the backend
   
.. only:: RDT

   .. include:: RDTbackend.rst


