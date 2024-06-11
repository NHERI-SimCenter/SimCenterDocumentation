.. toctree-filt::
   :maxdepth: 4

   overview
   :Hydro:c4model
   :WEUQ:c4model
   :EEUQ:c4model
   :PBE:c4model
   :R2D:c4model
   backendApplications
   :R2D:workflows
   :R2D:run-manually
   file-types

.. Within the natural hazards engineering community, there exist several widely used open-source applications, e.g., OpenFOAM, and online datasets, e.g., PEER NGA, that researchers are currently using. Consequently, to avoid duplication, SimCenter applications incorporate many widely used applications, such as OpenFOAM. To achieve this, SimCenter develops pre- and post-processors for these existing applications and utilizes web technologies for accessing online services.

.. 
   #. DL: An application to determine the damage and loss to the building/infrastructure given the event.
   #. EDP: An application to determine the response parameter given the event, building/lifeline, and damage and loss application.
   #. BRAILS: A framework of applications for creating regional-level building inventories using machine learning.   
   #. Databases containing information on building inventories for regional simulations, consequence functions for the DL applications, and experimental and corresponding simulation models for future machine learning-based AI algorithms.

.. .. note:: **Definitions**

..    #. **Workflow**: “The automation of a business process, in whole or part, during which documents, information, or tasks are passed from one participant to another for action, according to a set of procedural rules.” [Workflow Management Coalition].

..    #. **Application**: A software application that performs operations on data residing in a computer for a user or another program; it can be self-contained, typically termed a program or part of a group of programs.

..    #. **Scientific Workflow**: A sequence of steps propagating input data through various applications to produce output. It is a loosely coupled application performing workflows in which each coordinated task is performed using an individual application. Each of the individual applications takes some data inputs and produces data outputs, which are then consumed by subsequent tasks according to the workflow definition. They are termed scientific because they are typically used by scientists to process, manage, and visualize ever-increasing amounts of data using "scientific" applications. 

..    #. **Scientific Workflow System**: One or more applications that aid a user in setting up, scheduling, running, and monitoring a user-defined scientific workflow. 

..    #. **Software Framework**: A collection of software for building applications in a specific domain. The framework defines the interfaces between the software components, provides example applications that can be developed using the provided software, and represents a clear set of interfaces. The software can be extended to build other applications.
