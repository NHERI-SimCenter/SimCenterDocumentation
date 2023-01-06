.. _lbl-release_pbe:
.. role:: blue

*************
Release Notes
*************

Version 3.0
===========

   .. warning::

      This is a major release and it breaks compatibility. Input files used for PBE 2.x will need to be converted to work with the new version.

   .. dropdown::    Version 3.0.0 (:blue:`Current`)
      :open:

      **Release date:** September 2022

      **Major updates:**

      - Built on v4.0 of SimCenter's backend application framework. Major updates in the backend:

         - Redesigned and generalized UQ architecture
         - Generalized workflow managers support non-building assets
         - Surrogate modeling capabilities for characterizing events and earthquake response

      - All features of EE-UQ up to v3.2.0, including:

         - Advanced options for PEER NGA Event selection
         - Site-specific seismic disaggregation
         - Steel and concrete building model generators
         - MDOF-LU approximate shear column model generator

      - Redesigned user interface for Performance Assessment with Pelicun 3:

         - Takes advantage of the new databases developed for Pelicun 3 to allow users to use custom components, demands, damage processes, and consequence functions.
         - Decouples and generalizes demand, damage, and loss calculations.
         - Enables performance assessment under any type of natural hazard event
         - Supports modeling cascading damages
         - Supports custom mapping between damage states and consequence functions
         - Supports global consequences with uncertainty (e.g., uncertain replacement cost)
         - Substantial improvement in computational efficiency for large performance models
         - Two redesigned examples demonstrate capabilities

Version 2.0
===========

   .. warning::

      This is a major release and it breaks compatibility. Input files used for PBE 2.x will need to be converted to work with the new version.

   .. dropdown::    Version 2.0.0
      :open:

      **Release date:** October 2019

      Major updates:

      - All updates in EE-UQ from version v1.2.0 to v2.0.1 changes
      - Update DL interface:

          - General settings are organized around Damage, Response, and Loss Models
          - Components tab got a completely new look that facilitates the definition of component groups for each fragility group.
          - Dependencies moved to a new, fourth tab that will eventually house all advanced functionality

      - Support for loading and saving performance model (i.e., component definitions) using standard csv files.

      - Support for loading external EDP files using standard csv files. This enables the user to run a loss assessment without running the response estimation inside PBE.

      - Added damage and loss data from FEMA P58 second edition to the database.

      - Migrated to a new, more readable and flexible damage and loss model description in saved json files - not compatible with earlier versions.


Users are welcome to contact us on the `Message Board <http://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0>`_ for new feature requests.