.. _lbl-release_pbe:
.. role:: blue

*************
Release Notes
*************

Version 3
=========

   .. dropdown::    Version 3.2 (:blue:`Current`)
      :open:

      **Release date:** Sept 2023

      **Major updates:**

      - Post-disaster Performance and Recovery Simulation
   
         - Extended the PBE simulation workflow with a Performance (PRF) step. Applications in this step use the Damage and Loss (DL) results in models that estimate the post-disaster performance and recovery of an asset
         - Integrated the `ARUP REDi Seismic Downtime Model <https://sgavrilovicarup.github.io/REDi-docs/#>`_ using the open-source `PyREDI package <https://github.com/arup-group/REDi>`_ as the first tool in the PBE App to support functional recovery calculations.
         - Example 3 is added to illustrate this new functionality.

      - All features of EE-UQ up to v3.4, including:
         
         - Multi Fidelity Monte Carlo (MFMC) method for modeling building response


   .. dropdown::    Version 3.1

      **Release date:** May 2023

      **Major updates:**

      - Damage and Loss Database (DBDL)

         - A collection of parameters and metadata for damage and loss models for performance based engineering. The DBDL is available and updated regularly in the `DB_DamageAndLoss <https://github.com/NHERI-SimCenter/DB_DamageAndLoss>`_ GitHub Repository.

         - The initial release of the database includes the damage and repair consequence models from the following publications:
            - FEMA P-58 Second Edition
            - Hazus Earthquake Model for Buildings
            - Hazus Earthquake Model for Transportation Assets   
         
         - This and future releases of the PBE tool have the latest version of DBDL at the time of their release bundled with them.
         
         - Included in documentation

      - Environmental Impacts as per FEMA P-58 included in DBDL and available in the new release.

      - New Outputs tab allows users to select the outputs they need (across asset, demand, damage, and loss information) and if they prefer them in CSV or JSON format. 

      - Support automatic combination of built-in and user-defined databases for damage and loss models.

      - Support running calculations for only a subset of available consequence types.

      - All features of EE-UQ up to v3.3, including:

         - Multi-model uncertainty propagation options that allow multiple candidates for structural models and simulation settings.
         - Program Output Window provides detailed information about calculations and helps find errors.

   .. dropdown::    Version 3.0

      **Release date:** September 2022

      **Major updates:**

      - Built on v4.0 of SimCenter's backend application framework. Major updates in the backend:

         - Redesigned and generalized UQ architecture
         - Generalized workflow managers support non-building assets
         - Surrogate modeling capabilities for characterizing events and earthquake response

      - Redesigned user interface for Performance Assessment with Pelicun 3:

         - Takes advantage of the new databases developed for Pelicun 3 to allow users to use custom components, demands, damage processes, and consequence functions.
         - Decouples and generalizes demand, damage, and loss calculations.
         - Enables performance assessment under any type of natural hazard event
         - Supports modeling cascading damages
         - Supports custom mapping between damage states and consequence functions
         - Supports global consequences with uncertainty (e.g., uncertain replacement cost)
         - Substantial improvement in computational efficiency for large performance models
         - Two redesigned examples demonstrate capabilities

      - All features of EE-UQ up to v3.2.0, including:

         - Advanced options for PEER NGA Event selection
         - Site-specific seismic disaggregation
         - Steel and concrete building model generators
         - MDOF-LU approximate shear column model generator

   .. warning::

      Major releases break compatibility. Input files used for PBE 2.x will need to be converted to work with the PBE 3.x versions.

Version 2
=========

   .. dropdown::    Version 2.0.0

      **Release date:** October 2019

      Major updates:

      - Update DL interface:

          - General settings are organized around Damage, Response, and Loss Models
          - Components tab got a completely new look that facilitates the definition of component groups for each fragility group.
          - Dependencies moved to a new, fourth tab that will eventually house all advanced functionality

      - Support for loading and saving performance model (i.e., component definitions) using standard csv files.

      - Support for loading external EDP files using standard csv files. This enables the user to run a loss assessment without running the response estimation inside PBE.

      - Added damage and loss data from FEMA P58 second edition to the database.

      - Migrated to a new, more readable and flexible damage and loss model description in saved json files - not compatible with earlier versions.

      - All updates in EE-UQ up to v2.0, including:

         - Record selection from PEER NGA ground motion database
         - Nonlinear soil models in site response
         - Additional stochastic ground motion model

   .. warning::

      Major releases break compatibility. Input files used for PBE 1.x will need to be converted to work with the PBE 2.x versions.


Version 1
=========

   .. dropdown::    Version 1.2

      **Release date:** June 2019

      Major updates:

      - Updates to user interface for Damage and Loss assessment

      - All updates in EE-UQ up to v1.2, including:

         - 2D motions for site response
         - Improvements in connections to DesignSafe
         - Preferences window provides convenient access to settings

   .. dropdown::    Version 1.1

      **Release date:** April 2019

      Major updates:

      - Damage and loss estimation using the Hazus Earthquake Model

      - All updates in EE-UQ up to v1.1, including:

         - Idealized Multiple Degrees of Freedom model for structural analysis
         - Stochastic Ground Motions
         - Site Response Analysis
         - User-defined EDPs in structural analyses

   .. dropdown::    Version 1.0

      **Release date:** October 2018

      Initial release with FEMA P-58 damage and loss assessment functionality.

      All features of EE-UQ v1.0 are available for structural response estimation.



Users are welcome to contact us on the `Message Board <http://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0>`_ for new feature requests.
