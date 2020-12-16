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


Documentation of the software architecture is detailed in the following pages:


.. toctree-filt::
   :maxdepth: 1

   file-types.rst
   backendApplications.rst
   :RDT:workflows
   :RDT:run-manually


For additional reading into the software design philosophy, refer to the *C4 model* diagrams:


.. toctree-filt::
   :maxdepth: 1

   c4model
