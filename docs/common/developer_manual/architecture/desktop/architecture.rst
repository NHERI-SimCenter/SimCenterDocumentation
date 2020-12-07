.. _lblArchitecture:

*********************
Software Architecture
*********************

The |app| is one of the SimCenter's computational applications, which are `scientific workflow systems <https://en.wikipedia.org/wiki/Scientific_workflow_system>`_ that execute a sequence of computational tasks specialized for natural hazard engineering (NHE) problems. In contrast to more general-purpose scientific workflow systems (such as `Taverna <https://taverna.incubator.apache.org/>`_, `Kepler <https://kepler-project.org/>`_, and `Pegasus <https://pegasus.isi.edu/>`_), SimCenter workflow systems include the following features:

   - access to high performance computing resources, available on the cloud through |DesignSafe|, to enable parallel workflows for non-trivial large-scale NHE problems;
   - uncertainty quantification capabilities using `Dakota <https://dakota.sandia.gov/>`_, which allows users to introduce input uncertainties which are propagated through the workflow with random variables;
   - streamlined interfaces between existing software applications and datasets that are widely used by the NHE community, such as `OpenFOAM <https://openfoam.org/>`_, `OpenSees <https://opensees.berkeley.edu/>`_, `ADCIRC <http://adcirc.org/>`_, and `PEER Strong Ground Motion Databases <https://peer.berkeley.edu/peer-strong-ground-motion-databases>`_. To do this, the SimCenter develops pre- and post-processors to these existing applications and utilize web technologies for accessing online services;
   - additional custom software applications produced by the SimCenter. Among these are applications which automate the acquisition of building inventory data (`BRAILS <https://nheri-simcenter.github.io/BRAILS-Documentation/>`_), applications which simulate hazard evens and generate corresponding input files for passing through the workflow system (RegionalEvent Applications), applications for damage and loss assessment (`pelicun <https://nheri-simcenter.github.io/pelicun/>`_), and more.
   - a modular framework which allows developers to incorporate their own software applications as components to the workflow system, so long as it meets the input-output structure at component interfaces.



.. note:: **Terminology**

   #. **Workflow**: The automation of a business process, in whole or part, during which documents, information or tasks are passed from one participant to another for action, according to a set of procedural rules.” [Workflow Management Coalition].

   #. **Application**: A software application performs operations on data residing in a computer for a user or another program; it can be self contained, typically termed a program, or part of a group of programs.

   #. **Scientific Workflow**: A sequence of steps which propogate input data through a series of applications to produce output files. It is a loosely coupled application performing workflows in which each of the coordinated tasks is performed using an individual application. Each of the individual application taking some data inputs and producing data outputs, which are then consumed by subsequent tasks according to the workflow definition. They are termed scientific because they are typically used by scientists to process, manage, and visualize ever increasing ever increasing amounts of data applied to "scientific" problems.

   #. **Scientific Workflow System**: An application or applications to aid a user to set-up, schedule, run, and monitor a user defined scientific workflow.

   #. **Software Framework**: A software framework defines a set of component interfaces and provides a set of implementations in code of these interfaces which allows developers to build applications for the domain for which the framework has been designed. For example, a C++ framework will provide a set of abstract classes that define interfaces, and a set of concrete classes that implement the interfaces which will allow developers to quickly build and release applications using the concrete classes.  Frameworks allow developers to extend the functionality of the applications by introducing their own components that meet the component interface.


SimCenter Applications Overview
===============================
Documentation of the software architecture is detailed in the following pages.

.. toctree::
   :maxdepth: 1

   c4model
   backendApplications


How to Run
====================

Instructions for how to run the backend applications are detailed in the following pages.

.. toctree::
   :maxdepth: 1

   runLocal
   runRemote
   troubleshooting


.. only:: RDT_app

   .. include:: RDTworkflows.rst
