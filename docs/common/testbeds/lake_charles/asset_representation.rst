.. _lbl-testbed_LC_asset_representation:

********************
Asset Representation
********************

This section discusses the translation of asset descriptions into representations 
of structures suitable for simulation within workflow, in this case consistent with 
the HAZUS description of building classes and associated attributes, which becomes 
the default data schema. Thus the description of assets below is organized according 
to the HAZUS conventions for classifying buildings and organizing damage and loss data 
according to attributes associated with those building classes.

The following discussion will reference a number of rulesets developed for this testbed 
to enable various assignments of these HAZUS building classes and corresponding attributes. 
Details of these rulesets are available to users in one of two forms: 

1. Rulest definition tables (PDFs) curated in DesignSafe that include additional documentation 
   justifying the proposed rule, with provenance information for any sources engaged in that 
   rule’s development.
2. Scripts (in Python) curated in GitHub that implement the ruleset’s logic for this testbed.

Each section provides a table linking the relevant Tables and Scripts. Note that as well 
that all of the rulesets introduced herein are tiered, initiating by assigning all assets 
a default value for its building classification or a given attribute based on the primary 
rule. This ensures that every asset receives a HAZUS building class and related attribute 
assignments, regardless of data sparsity. 

.. _lbl-testbed_LC_asset_representation_building_classification:

Building Classifications
==========================

HAZUS classifies buildings based on a more nuanced interpretation of Occupancy Class 
(see building inventory field **OccupancyClass**) based on other attributes of relevance 
for a given hazard type.

For wind losses, HAZUS groups buildings into 5 main types by primary building material/construction 
mode (wood, masonry, concrete, steel, manufactured home). Buildings must then be sub-classified 
into one of 55 corresponding HAZUS building classes (**HazusClass-W**) based on characteristics 
such as occupancy, number of stories and footprint size, using rulesets that call upon various 
fields in the building inventory. The HAZUS building classifications for wind losses are listed 
in :numref:`bldg_class`, and the corresponding rulesets (PDFs and Python scripts) are cross-referenced 
later in :numref:`addinfo_ruleset`. Note that while rulesets were developed for marginally and non-engineered 
building classes in HAZUS, these classes are not used in the current implementation of this testbed.

.. csv-table:: HAZUS building classification for wind loss assessment.
   :name: bldg_class
   :file: table/bldg_class_new.csv
   :header-rows: 1
   :align: center

.. list-table:: Additional details for rulesets assigning HAZUS building class
   :name: addinfo_ruleset
   :header-rows: 1
   :align: center

   * - Ruleset Name
     - Ruleset Definition Table
     - Python script
   * - Building Class Rulesets - Wind
     - `HAZUS Building Class Rulesets - Wind.pdf <https://berkeley.box.com/s/602imclyqm1ohvfqliqro0bzq4v0wdj3>`_
     - :download:`WindClassRulesets <data/WindClassRulesets.py>`

Building Attributes
======================

Within each of these building classes, e.g., wood single-family homes 1-2+ stories, the HAZUS Hurricane 
Technical Manual (HHTM) further differentiates buildings based on asset attributes and the hazard type 
(e.g., wind vs. flood) for the purpose of loss estimation. These attributes define key features of the 
load path and components (e.g., roof shape, secondary water resistance, roof deck attachment, roof-wall 
connection, shutters, garage), and the number of attributes necessary to describe a given building varies. 

As these attributes are beyond what is typically encompassed in a building inventory, this testbed developed 
and implemented a library of rulesets to infer the HAZUS-required attributes based upon the fields available 
in the Building Inventory, legacy building codes in New Jersey, local construction practices/norms, surveys 
capturing owner-driven mitigation actions (e.g., [Javeline19]_) and market/industry data. 
Where possible, the rulesets are time-evolving, considering the age of construction to determine the governing 
code edition and availability of specific mitigation measures in the market. Though reliant on engineering 
judgement and historical data availability, each rule provides detailed notes cross-referencing the various 
documents and practices that governed that era of construction and thus informed the ruleset formation. 
In cases where engineering judgment was required, rules were assigned based on what was understood to be 
the most common construction practice. In cases where that was not clear, the ruleset assigned the most 
vulnerable configuration for a more conservative approach to loss estimation.

.. csv-table:: Building attributes for wind loss assessment.
   :name: wind_bldg_attri
   :file: table/wind_bldg_attri.csv
   :header-rows: 1
   :align: center

Note that rulesets for assigning wind loss attributes call upon two meta-variables relevant to wind losses 
for any building: “Hazard Prone Region” and “Wind Borne Debris,” which are assigned based the design wind 
speed at the asset location (Building Inventory field “DSWII”) and the flood zone (building inventory field 
**FloodZone**), per New Jersey code. These rules used to assign these meta-variables are provided in 
:numref:`addinfo_ruleset_metavar`. Also note that the roof shape (building inventory field **RoofShape**), 
derived from aerial imagery, and terrain roughness (building inventory field **Terrain**), derived from 
Land Use Land Cover data, are also attributes required by the HAZUS wind loss model. As these were already 
assigned in the :ref:`lbl-testbed_AC_asset_description`, they are not discussed again herein.

.. list-table:: Additional details for rulesets for meta-variables in wind loss attribute assignment in HAZUS
   :name: addinfo_ruleset_metavar
   :header-rows: 1
   :align: center

   * - Ruleset Name
     - Ruleset Definition Table
     - Python script
   * - Attribute Assignment - Wind (Meta-Variable)
     - `Hazus Building Attribute Rulesets - Wind - Meta-Variables.pdf <https://berkeley.box.com/s/l4vdnfoakq8xsv4rmj64x4m2kxqritu7>`_
     - :download:`WindMetaVarRulesets <data/WindMetaVarRulesets.py>`

Finally, all of the rulesets used to assign attributes include a default value that can be updated based 
on available data, ensuring that each asset receives all the attribute assignments necessary to identify 
the appropriate Hazus fragility description. The following sections summarize the rulesets used for 
attribute assignments for specific classes of buildings. Additional attributes assigned to assets are 
discussed in the following subsections, organized by hazard and building class, where applicable.

Wind Loss Attributes for Wood Buildings
------------------------------------------

The wind loss model in HAZUS classifies wooden buildings into five building classes:
   
1. two single family homes (WSF1 and WSF2) and
2. three for multi-unit homes (WMUH1, WMUH2, and WMUH3)

Their required attributes for wind loss modeling, the possible entries (values, terms) that can be 
assigned for those attributes, and the basis for the ruleset developed to make that assignment are 
summarized in :numref:`wsf_attri` and :numref:`wmuh_attri`. Note that these rulesets were developed 
to reflect the likely attributes based on the year of construction and the code editions and 
construction norms at that time. The corresponding time-evolving rulesets (PDFs and Python scripts) 
are cross-referenced in :numref:`addinfo_ruleset_wood`.

.. csv-table:: Additional HAZUS attributes assigned for wood single family (WSF) homes: wind losses.
   :name: wsf_attri
   :file: table/wsf_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: Additional HAZUS attributes assigned for wood multi-unit home (WMUH): wind losses.
   :name: wmuh_attri
   :file: table/wmuh_attributes.csv
   :header-rows: 1
   :align: center

.. list-table:: Additional details for rulesets assigning wind loss attributes for wood buildings
   :name: addinfo_ruleset_wood
   :header-rows: 1
   :align: center

   * - Ruleset Name
     - Ruleset Definition Table
     - Python script
   * - HAZUS Building Attribute Rulesets - Wind (WSF1-2)
     - `Hazus Building Attribute Rulesets - Wind - WSF1-2.pdf <https://berkeley.box.com/s/nod73v7shtj9x7ox7xw7b7nvmrs3e8oc>`_
     - :download:`WindWSFRulesets <data/WindWSFRulesets.py>`
   * - HAZUS Building Attribute Rulesets - Wind (WMUH1-3)
     - `Hazus Building Attribute Rulesets - Wind - WMUH1-3.pdf <https://berkeley.box.com/s/4v7405rit2u475daorayy9w6ssuezbz9>`_
     - :download:`WindWMUHRulesets <data/WindWMUHRulesets.py>`

Taking the attribute Second Water Resistance (SWR) as an example, the SWR attribute is assigned by 
a series of time-evolving rules calling upon four fields in the building inventory: year built, 
roof shape, roof slope, and average temperature in January. :numref:`swr_attri` provides the 
detailed rules that map these four variables to the Second Water Resistance (SWR) attribute. 
This example demonstrates an instance where the attribute is assigned as a random variable, 
based on the fact that secondary water resistance is not required by code, though surveys 
of homeowners in hurricane-prone areas can be used to infer how many may have voluntarily 
adopted this mitigation practice. 

.. csv-table:: Ruleset for determining the Second Water Resistance attribute for WSF homes.
   :name: swr_attri
   :file: table/example_wood_ruleset.csv
   :header-rows: 1
   :align: center


.. [Javeline19]
    Javeline, D., & Kijewski-Correa, T. (2019). Coastal homeowners in a changing climate. Climatic Change, 152(2), 259-274.