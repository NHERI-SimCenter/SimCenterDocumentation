.. _lblAboutHydroUQ:

*****
About
*****

|full tool name| (|app|) is an open-source software tool developed by the NHERI SimCenter. It allows for utilization of existing simulation software applications, e.g. OpenSees and OpenFOAM, in uncertainty quantification (UQ) workflows. The application provides popular UQ methods (e.g., forward, inverse, reliability, sensitivity, parameter estimation, and surrogate modeling) to engineers, researchers, and students for tsunamis, hurricane storm-surges, and other water-borne hazards. The SimCenter is part of the Natural Hazards Engineering Research Infrastructure (NHERI) program, funded by the National Science Foundation (see :ref:`lblAcknowledgements`). 

To download the HydroUQ desktop application for Windows 8/10/11 or Mac OS X, navigate to |appLink|. For Linux systems, e.g. Ubuntu 18.04-LTS, download the source code at |tool github link| and build the program file by following steps provided in the :ref:`Build Guide <lblHowToBuild>`.  The |app| is released under the **2-Clause BSD** license (see :ref:`lblLicense`).

.. figure:: HydroUQ_MPM_3DViewPort_OSULWF_2024.04.25.gif
     :align: center
     :figclass: align-center

     The HydroUQ Desktop Application's User Interface for Oregon State University's Large Wave Flume Digital Twin.
This is Version |tool version| of the tool. Users are encouraged to comment on what additional features and capabilities they would like to see in this application. These requests and feedback can be submitted through an anonymous |user survey link|. We greatly appreciate any input you have. If there are features you want, chances are many of your colleagues also would benefit from them. We encourage you to review the :ref:`lblHydroRequirements` to see what features are planned.

The additional simulations required for uncertainty quantification can be prohibitively expensive. To overcome this impediment, the user has the option to perform the response simulations on the Frontera and Lonestar6 supercomputers, located at the Texas Advanced Computing Center (TACC). These HPC resources are made available to the user through NHERI DesignSafe-CI, the cyberinfrastructure provider for the distributed NSF-funded Natural Hazards Engineering Research Infrastructure (NHERI) facility.




Capabilities and Limitations
------------------------------

Below are key capabilities and limitations of |short tool id|, categorized by Uncertainty Quantification (UQ), Design Building General Information (GI), Structural Information & Analysis Model (SIM), Natural Hazard Event (EVT), Engineering Demand Parameters (EDP), Finite Element Method (FEM), Random Variables (RV), and Results (RES).


.. list-table:: 
   :widths: 5 50 50 
   :header-rows: 1

   * - Item
     - Capabilities
     - Limitations
   * - UQ
     - Easy access to different :ref:`UQ methods<lblFEM>`. Parallelized UQ algorithms. Multiple alternative algorithms for each method.
     - No support for optimization under uncertainty and local sensitivity analysis.
   * - GI
     - Basic interface for user-provided general building information (e.g. location, age, and building type).
     - No support for user-defined building types.
   * - SIM
     - Easy interface for user-provided structural information and analysis models (e.g. geometry, material properties, and boundary conditions). Provides a multi-degree-of-freedom (MDOF) building model. Allows for OpenSeesPy models defined in user-provided scripts. Supports investigation of multiple potential building models with associated "belief" values for each. 
     - 
   * - EVT 
     - OpenFOAM computational fluid dynamics (CFD) simulations. GeoClaw Shallow-Water Equations (SWE) and OpenFOAM CFD one-way coupled simulations. FOAMySees two-way coupled CFD-FEA simulations. Material Point Method (MPM, ClaymoreUW) simulations. Pre-built and validated digital wave-flume twins. 
     - Most simulation types are limited to remote execution on TACC supercomputers.
   * - FEM
     - Easy interface for user-provided simulation models (not only FEM models but *any model*), including Opensees, python, or any other simulation models (e.g. FEM or non-FEM software) with a python-scripted interface.
     - Support for alternative finite element analysis (FEA) software is limited.
   * - RV
     - 12 different kinds of probability distributions with correlations.
     - No support for random fields, non-Gaussian copular, or user-defined variables.
   * - EDP
     - Scalar and vector EDP parsing. Hazard specific EDP lists (e.g. tsunami and storm-surge). Support for user-defined EDPs.
     - Separate Intensity Measures (IMs) and EDPs is not fully defined yet.
   * - RES
     - Interactive plotting of scatter charts, histograms, and cumulative mass functions. Summary of statistics. Save data into a CSV file.
     - Limited flexibility in in-app visualization. Results must be ported to external plotting software for more advanced visualization.
   * - General
     - Graphical user interface. Free and easy one-click remote running option. 
     - 
