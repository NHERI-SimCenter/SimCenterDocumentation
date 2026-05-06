.. _lbl-release_pbe:
.. role:: blue

*************
Release Notes
*************

Version 4
=========

   .. dropdown::    Version 4.5 (:blue:`Current`)
      :open:

      **Release date:** May 2026

      **Major updates:**

      - **ATC-138 Functional Recovery Assessment:** Integrated the
        `ATC-138 functional recovery methodology <https://femap58.atcouncil.org/fr-methodology>`_
        as a new option in the Performance (PRF) tab. The underlying atc138
        Python package implements the Cook et al. (2022) probabilistic
        framework, extending FEMA P-58 damage simulation outputs into recovery
        timelines via fault-tree analysis, impeding factors, and repair
        scheduling. The Results panel reports Reoccupancy, Functional Recovery,
        and Full Recovery time statistics. A new Example 4 demonstrates the
        simulation capabilities and can be used as a template.

      - Update to Pelicun 3.9, which brings numpy 2 compatibility, broader
        pandas/scipy dependency ranges, and a number of internal robustness
        and warning-cleanup fixes.

      - **Migration to Qt 6:** the desktop application now builds
        against Qt 6 (previously Qt 5.15), aligning PBE with modern Qt
        support.

      - **Native Apple Silicon (arm64) builds:** the macOS distribution
        now ships an arm64 binary in addition to x86_64, so users on
        Apple Silicon Macs can expect significantly faster simulations.

   .. dropdown::    Version 4.4

      **Release date:** October 2025

      **Major updates:**

      - Update to Pelicun 3.8, which adds a new interface to the SimCenter
        Damage and Loss Model Library (DLML) from the Pelicun package
        for easier maintenance and more flexible access to new model data.

      - Inherited event-handling enhancements from EE-UQ:

        - Femora input support, enabling multiple OpenSeesMP simulations
        - Soil-Structure Interaction (SSI) widget for custom buildings
          supported on piles or mat foundations

      - HPC usability improvements for jobs launched on DesignSafe:

        - **Share Job** -- share remote simulation jobs across
          DesignSafe projects and users
        - **Open Job Folder** -- jump directly to a remote job's output
          files on DesignSafe
        - **View Job Metadata** -- open DesignSafe's metadata page for
          the job

   .. dropdown::    Version 4.3

      **Release date:** May 2025

      **Major updates:**

      - Update to Pelicun 3.6 and rework of the DL/Pelicun input panel
        to fully leverage the SimCenter Damage and Loss Model Library,
        exposing all available methods (including new Hazus Hurricane
        wind variants and storm-surge support) directly in the user
        interface.

   .. dropdown::    Version 4.2

      **Release date:** February 2025

      **Major updates:**

      - Update to Pelicun 3.5 and the underlying SimCenter Damage and
        Loss Model Library (DLML).

      - New damage and loss models available via DLML:

        - Several Hazus models developed for portfolio-type studies
          (also used in R2D), included primarily for educational use.
        - First release of the SimCenter Wind Component Library, a
          major enhancement collecting high-resolution component-level
          models for wind-pressure-induced damage from the literature.

      - References for damage and loss models are now shown in the
        user interface to encourage recognition of model developers'
        work. The DLML will be extended in future releases to provide
        comprehensive references for all included models. The Wind
        Component Library currently has references for every model
        in it.

      - **Optional loss calculations:** users can opt out of loss
        calculation by selecting "None" under component repair
        consequence databases and turning all loss outputs off.

   .. dropdown::    Version 4.1

      **Release date:** September 2024

      **Major updates:**

      - Domain Reduction Method option added in tools to create events for buildings given large physics- based simulations.

      - ShakerMaker option added to tool to perform earthquake rupture simulations.

      - OpenSees@DesignSafe option added in tools to allow users to run OpenSees, OpenSeesMP, OpenSeesSP, and OpenSeesPy simulations utilizing TACC HPC resources from their desktop.

   .. dropdown::    Version 4.0

      **Release date:** August 2024

      **Major updates:**

      - A needed release for changes required to interact with DesignSafe and new TapisV3 interface.

      - Due to AI generated spam on message board, users now directed to post questions using github discussions.

Version 3
=========

   .. dropdown::    Version 3.5

      **Release date:** June 2024

      **Major updates:**

      - Ability to include different events in multi-model and multi-fidelity simulations
	
   .. dropdown::    Version 3.4

      **Release date:** March 2024

      **Major updates:**

      - Ability to select from Physics based ground motions generated by M9 project

      - Update the Pelicun3 Damage and Loss engine to v3.3:

          - Changes affecting backwards compatibility

              - Remove "bldg" from repair consequence output filenames: The increasing scope of PBE now covers simulations for transportation and water networks. Hence, labeling repair consequence outputs as if they were limited to buildings no longer seems appropriate. The bldg label was dropped from the following files: DV_bldg_repair_sample,DV_bldg_repair_stats,DV_bldg_repair_grp, DV_bldg_repair_grp_stats, DV_bldg_repair_agg, DV_bldg_repair_agg_stats.

              - Decision variable types in the repair consequence outputs are named using CamelCase: Earlier they used all capitals. This change was made to be consistent with other parts of the codebase. For example, we use "Cost" instead of "COST". This might affect post-processing scripts.

              - "ea" units were replaced with "unitless" where appropriate for clarity: There should be no practical difference between the calculations due to this change. Interstory drift ratio demand types are one example.

              - Weighted component block assignment is no longer supported: We recommend using more versatile approach of defining the same component type multiple times to achieve the same effect.

              - Damage functions are no longer supported: Damage functions were used to assign quantity of damage as a function of demand. Contrast this with fragility curves that assign probability of limit state exceedance as a function of demand. We recommend using the new multilinear CDF type fragility functions to develop theoretically equivalent, but more efficient models.

          - Deprecation warnings

              - Remove Bldg from repair settings label in DL configuration file: Following the changes above, we dropped Bldg from BldgRepair when defining settings for repair consequence simulation in a configuration file. The previous version (i.e., BldgRepair) will keep working until the next major release, but we encourage everyone to adopt the new approach and simply use the Repair keyword in the input files.

	  - New features

              - Location-specific damage processes: This new feature is useful when you want damage to a component type to induce damage in another component type at the same location only. For example, damaged water pipes on a specific story can trigger damage in floor covering only on that specific story. Location-matching is performed automatically without you having to define component pairs for every location using the following syntax: '1_CMP.A-LOC', {'DS1': 'CMP.B_DS1'} , where DS1 of CMP.A at each location triggers DS1 of CMP.B at the same location.

              - Multilinear CDF random variable: allows using a multilinear approximation of any CDF in the tool.
      
              - Allow multiple definitions of the same component type at the same location and direction in the asset model. (If needed, we can later add a feature to propagate these as separate instances to model, e.g., components used by various tenants.)

              - Update JSON outputs to follow new standard SimCenter output format

              - Include unit information in every CSV and JSON output file.

              - Several minor efficiency improvements that lead to faster runtimes - major improvments in that area are coming in the next minor release

              - Several error and warning messages added to provide more meaningful information when something goes wrong in a simulation.

              - A lot of minor bugs fixed and robustness of the Pelicun engine ensured by bringing back continuous integration.

   .. dropdown::    Version 3.3 

      **Release date:** Jan 2024

      **Major updates:**

      - Allow multiple definitions of the same component type at the same location and direction in the asset model. (If needed, we can later add a feature to propagate these as separate instances to model, e.g., components used by various tenants.)

      - Update JSON outputs to follow new standard SimCenter output format

      - Include unit information in every CSV and JSON output file.

      - Several minor efficiency improvements that lead to faster runtimes - major improvments in that area are coming in the next minor release

      - Several error and warning messages added to provide more meaningful information when something goes wrong in a simulation.

      - A lot of minor bugs fixed and robustness of the Pelicun engine ensured by bringing back continuous integration.

   .. dropdown::    Version 3.2
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



Users are welcome to contact us on the |messageBoard| for new feature requests.
