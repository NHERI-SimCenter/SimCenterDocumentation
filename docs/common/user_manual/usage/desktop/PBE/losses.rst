.. _lblPelicun_losses

Loss Models
===========

This tab is designed to collect settings for various loss models. Currently, it provides repair cost and repair time modeling capabilities. Extensions with injuries, unsafe placards, and environmental impacts, and functional recovery time are planned for future releases. The following subsections introduce the settings for each type of loss model.


Repair consequences
-------------------

Repair cost and time in pelicun are calculated as a function of the quantity and severity of damage experienced by structural components. There are three settings in this panel that influence these calculations:


Global consequences
^^^^^^^^^^^^^^^^^^^

This area allows you to add a replacement cost and time consequence to the model automatically. If you choose Automatic mapping between damage and consequences (see the subsection on Mapping below for details), collapse and irreparable damage are mapped to this replacement consequence.

If the distribution is set to N/A, the consequence is deterministic. Otherwise, the median and theta_1 are the two parameters that define the uncertain consequence. Theta_1 is the coefficient of variation for a normal distribution and the log-standard deviation for a lognormal distribution.

.. note:: Both the FEMA P-58 and the Hazus methodology use deterministic representation of replacement cost and time.


Database
^^^^^^^^

Consequence data is decoupled from damage data (i.e., component vulnerabilities) and provided in separate datasets for each consequence type (e.g., repairs, injuries) and method in Pelicun. This area provides a drop-down list with the built-in consequence functions and the ability to use custom datasets. The following options are available:

:FEMA P-58:
    Provides the repair consequence data that was released with the second edition of the FEMA P-58 methodology (2018).

    .. note:: A substantial part of the consequence definitions in FEMA P-58 are incomplete. You will have to edit the dataset and provide the missing data if you need to use components with incomplete information. If such components are selected for analysis without fixing these issues, they are recognized and skipped by Pelicun during the calculation.

:Hazus Earthquake:
    Provides the repair consequence data published in the Hazus Earthquake Technical Manual (2011)

:User Defined:
    Allows you to Choose a file that provides your own set of consequence functions. The |PelicunDocs| explains how to prepare a compatible consequence data file.


Mapping
^^^^^^^

Mapping is responsible for linking damaged components with consequence models. The **Automatic** approach is limited to the built-in databases and works with the following assumptions:

:FEMA P-58:
    Assumes that the component vulnerability and consequence IDs are identical. Queries the damageable component IDs and creates a mapping to a list of identical consequence IDs.

:HAZUS:
    For each component, uses the damageable component IDs to extract the relevant information and adds the occupancy type (set in the Asset model panel) to arrive at a corresponding consequence component ID.

You can select the **User Defined** option if you prefer to provide your own mapping. This option allows you to Choose a CSV file that lists the damaged component IDs and the corresponding consequence IDs. The |PelicunDocs| provides more information on the standard structure of these CSV files.
