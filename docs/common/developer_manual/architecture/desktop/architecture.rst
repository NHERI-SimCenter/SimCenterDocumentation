.. _lblArchitecture:

*********************
Software Architecture
*********************

The |app| is one of the SimCenter's computational applications, which are `scientific workflow systems <https://en.wikipedia.org/wiki/Scientific_workflow_system>`_ that executes a sequence of computational tasks specialized for natural hazard engineering (NHE) problems. In contrast to more general-purpose scientific workflow systems (such as `Taverna <https://taverna.incubator.apache.org/>`_, `Kepler <https://kepler-project.org/>`_, and `Pegasus <https://pegasus.isi.edu/>`_), SimCenter workflow systems include the following features:

   - access to high-performance computing resources, available on the cloud through |DesignSafe|, to enable parallel workflows for non-trivial large-scale NHE problems;
   - uncertainty quantification capabilities using `Dakota <https://dakota.sandia.gov/>`_, which allows users to introduce input uncertainties that are propagated through the workflow with random variables;
   - streamlined interfaces between existing software applications and datasets that are widely used by the NHE community, such as `OpenFOAM <https://openfoam.org/>`_, |OpenSeesLink|, `ADCIRC <http://adcirc.org/>`_, and `PEER Strong Ground Motion Databases <https://peer.berkeley.edu/peer-strong-ground-motion-databases>`_. To do this, the SimCenter develops pre- and post-processors for these existing applications and utilizes web technologies for accessing online services;
   - additional custom software applications produced by the SimCenter. Among these are applications that automate the acquisition of building inventory data (`BRAILS <https://nheri-simcenter.github.io/BRAILS-Documentation/>`_), applications that simulate hazard events and generate corresponding input files for passing through the workflow system (RegionalEvent Applications), applications for damage and loss assessment (`pelicun <https://nheri-simcenter.github.io/pelicun/>`_), and more.
   - a modular framework that allows developers to incorporate their own software applications as components to the workflow system, so long as it meets the input-output structure at component interfaces.


.. _figFramework:

.. figure:: figures/SimCenterFramework.png
   :align: center
   :width: 1000
   :figclass: align-center

   SimCenter Software Framework

The SimCenter scientific workflow systems aim to facilitate the use, reuse, and extension of common workflows encountered in NHE by a broad range of natural hazards engineering researchers with varying software skills. This chapter presents the software architecture for the SimCenter framework and |app| using the `C4 model <https://c4model.com>`_ to encourage this use and adoption. The **C4** model is a graphical approach for documenting software architecture through diagrams describing and communicating the software architecture at various levels of abstraction. It is a top-down approach that starts at a high level (level 1), showing how a user would interact with the software, and drills down through three more levels, with level 4 containing the typical UML diagrams. The **C4** model was chosen to provide NHE researchers with a diverse range of software architecture knowledge to understand the software architecture behind SimCenter applications that fit their skill level. The four levels:

- Level 1: The level one diagram is a system diagram that shows how the software system fits in the real world in terms of people who use it and other software systems it interacts with.
- Level 2: Level 2 is a container diagram showing the containers (applications, databases, etc.) that make up the software system.
- Level 3: Level three diagrams are component diagrams, showing how the components of the individual containers.
- Level 4: The level four diagrams show how the individual components are implemented. They are typically UML class diagrams.

The following sections present the architecture of SimCenter the SimCenter to level 3:


Documentation of the SimCenter software architecture is detailed in the following pages:


.. toctree-filt::
   :maxdepth: 2

   overview.rst
   file-types.rst
   backendApplications.rst
   :R2D:workflows
   :R2D:run-manually
   :notQuoFEM:c4model


Within the natural hazards engineering community, there exist several widely used open-source applications, e.g., OpenFOAM, and online datasets, e.g., PEER NGA, that researchers are currently using. Consequently, and to avoid duplication, SimCenter applications incorporate many widely used applications, e.g., OpenFOAM. To do this, SimCenter develops pre- and post-processors for these existing applications and utilizes web technologies for accessing online services.

.. 
   #. DL: application to determine the damage and loss to the building/infrastructure given the event.
   #. EDP: application to determine the response parameter given the event, building/lifeline, and damage and loss application.
   #. BRAILS: a framework of applications for creating regional-level building inventories using machine learning.   
   #. Databases containing information on building inventories for regional simulations, consequence functions for the DL applications, and experimental and corresponding simulation models for future machine learning-based AI algorithms.


.. note:: **Definitions**

   #. **Workflow**: “The automation of a business process, in whole or part, during which documents, information or tasks are passed from one participant to another for action, according to a set of procedural rules.” [Workflow Management Coalition].

   #. **Application**: A software application performs operations on data residing in a computer for a user or another program; it can be self-contained, typically termed a program or part of a group of programs.

   #. **Scientific Workflow**: A sequence of steps propagating input data through various applications to produce output. It is a loosely coupled application performing workflows in which each coordinated task is performed using an individual application. Each of the individual applications takes some data inputs and produces data outputs, which are then consumed by subsequent tasks according to the workflow definition. They are termed scientific because they are typically used by scientists to process, manage, and visualize ever-increasing amounts of data using "scientific" applications. 

   #. **Scientific Workflow System**: One or more applications that aid a user in setting up, scheduling, running, and monitoring a user-defined scientific workflow. 

   #. **Software Framework**: A collection of software for building applications in a specific domain. The framework defines the interfaces between the software components, provides example applications that can be developed using the provided software, and represents a clear set of interfaces. The software can be extended to build other applications.


