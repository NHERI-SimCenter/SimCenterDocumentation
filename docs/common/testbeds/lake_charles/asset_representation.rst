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

The following discussion will reference a number of rulesets initially developed for the 
`Atlantic County, NJ <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/index.html>`_ 
testbed to enable various assignments of these HAZUS building classes 
and corresponding attributes. Details of these rulesets are available to users in one of two forms: 

1. Ruleset definition tables (PDFs) curated in DesignSafe that include additional documentation justifying the proposed rule, with provenance information for any sources engaged in that rule’s development.
2. Scripts (in Python) that implement the ruleset’s logic for this testbed. Users wishing to execute the testbed in its current form are recommended to download the Python rulesets from DesignSafe. Users wishing to adapt the rulesets to potentially change the way attributes are assigned to buildings, are encouraged to access the Python implementation of the rulesets in GitHub.

Both of these repositories also include additional documentation (PDFs) justifying the proposed rule, 
with provenance information for any sources engaged in that rule’s development.
Note that all of the rulesets introduced herein are tiered, initiating by assigning all assets a 
default value for its building classification or a given attribute based on the primary rule. 
This ensures that every asset receives a HAZUS building class and related attribute assignments, 
regardless of data sparsity. The sections below detail the ruleset development, 
closing with a table linking the relevant PDFs from DesignSafe and Python scripts from GitHub.

.. _lbl-testbed_LC_asset_representation_building_classification:

Building Classifications
==========================

HAZUS classifies buildings based on a more nuanced interpretation of Occupancy Class 
(see building inventory field **OccupancyClass**) based on other attributes of relevance 
for a given hazard type.

HAZUS groups buildings into five main types by primary building material/construction 
mode for projecting wind losses. Given the focus of this testbed on residential, wood 
construction, the only relevant HAZUS classes are Wood Single Family (WSF) homes and 
Wood, Multi-Unit/Hotel/Model (WMUH). These HAZUS building classifications are listed in 
:numref:`bldg_class`, and the corresponding rulesets (PDFs and Python scripts) are cross-referenced 
later in :numref:`addinfo_ruleset`.

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
     - `HAZUS Building Class Rulesets - Wind.pdf <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/03.%20Input:%20DL%20-%20Rulesets%20for%20Asset%20Representation>`_
     - `WindClassRulesets <https://github.com/NHERI-SimCenter/AssetRepresentationRulesets/blob/main/rulesets/LA/scripts/WindClassRulesets.py>`_

Building Attributes
======================

Within each of these building classes, e.g., wood single-family homes 1-2+ stories, the HAZUS Hurricane 
Technical Manual ([FEMA21]_) further differentiates buildings based on asset attributes and the hazard type 
(e.g., wind vs. flood) for the purpose of loss estimation. These attributes define key features of the 
load path and components (e.g., roof shape, secondary water resistance, roof deck attachment, roof-wall 
connection, shutters, garage), and the number of attributes necessary to describe a given building varies. 

As these attributes are beyond what is typically encompassed in a building inventory, a library of rulesets 
to infer the HAZUS-required attributes was developed and implemented for the `Atlantic County, NJ <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/index.html>`_ testbed, 
based upon the fields available in the building inventory, legacy building codes in New Jersey, local 
construction practices/norms, surveys capturing owner-driven mitigation actions (e.g., [Javeline19]_) 
and market/industry data. Where possible, the rulesets are time-evolving, considering the age of 
construction to determine the governing code edition and availability of specific mitigation measures 
in the market. Though reliant on engineering judgement and historical data availability, each rule provides 
detailed notes cross-referencing the various documents and practices that governed that era of construction 
and thus informed the ruleset formation. In cases where engineering judgment was required, rules were assigned 
based on what was understood to be the most common construction practice. In cases where that was not clear, 
the ruleset assigned the most vulnerable configuration for a more conservative approach to loss estimation. 
The rulesets from the `Atlantic County, NJ <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/index.html>`_ testbed are applied here, without modification as the purpose 
herein is solely to demonstrate the workflow. It is acknowledged that, while also grounded in the 
International Residential Code and International Building Code, Louisiana has a different regulatory 
framework and code eras that would require adaptation of the rulesets. Such adaptations are encouraged 
as part of the community’s use and adaptation of this workflow in its research.

.. csv-table:: Building attributes for wind loss assessment for WSF and WMUH.
   :name: wind_bldg_attri
   :file: table/wind_bldg_attri.csv
   :header-rows: 1
   :align: center
   :widths: 15, 65, 20

Note that rulesets for assigning wind loss attributes call upon two meta-variables relevant to wind losses 
for any building: “Hazard Prone Region” and “Wind Borne Debris,” which are assigned based the design wind 
speed at the asset location (Building Inventory field “DWSII”) and the flood zone (building inventory field 
**FloodZone**). These rules used to assign these meta-variables are provided in 
:numref:`addinfo_ruleset_metavar`. Also note that the roof shape (building inventory field **RoofShape**), 
derived from aerial imagery, and terrain roughness (building inventory field **Terrain**), derived from 
Land Use Land Cover data, are also attributes required by the HAZUS wind loss model. As these were already 
assigned in the `Atlantic County, NJ testbed Asset Representation <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/asset_representation.html>`_, they are not discussed again herein.

.. list-table:: Additional details for rulesets for meta-variables in wind loss attribute assignment in HAZUS
   :name: addinfo_ruleset_metavar
   :header-rows: 1
   :align: center

   * - Ruleset Name
     - Ruleset Definition Table
     - Python script
   * - Attribute Assignment - Wind (Meta-Variable)
     - `Hazus Building Attribute Rulesets - Wind - Meta-Variables.pdf <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/03.%20Input:%20DL%20-%20Rulesets%20for%20Asset%20Representation>`_
     - `WindMetaVarRulesets <https://github.com/NHERI-SimCenter/AssetRepresentationRulesets/blob/main/rulesets/LA/scripts/WindMetaVarRulesets.py>`_

The following sections summarize the rulesets used for wind loss  attribute assignments for WSF and WMUH 
in this testbed. See the `Atlantic County, NJ testbed Asset Representation <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/asset_representation.html>`_, the source of these rulesets, 
for additional rulesets guiding attribute assignments for other building classes and hazards.

Wind Loss Attributes for Wood Buildings
------------------------------------------

The wind loss model in HAZUS classifies wooden buildings into five building classes:
   
1. two for single family homes (WSF1 and WSF2) and
2. three for multi-unit homes (WMUH1, WMUH2, and WMUH3)

Their required attributes for wind loss modeling, the possible entries (values, terms) that can be 
assigned for those attributes, and the basis for the ruleset developed to make that assignment are 
summarized in :numref:`wsf_attri` and :numref:`wmuh_attri`. NNote that these rulesets were developed 
for Atlantic County, NJ to reflect the likely attributes based on the year of construction and the 
code editions and construction norms at that time. They are applied in this testbed for demonstration 
purposes only. The corresponding time-evolving rulesets (PDFs and Python scripts) are 
cross-referenced in :numref:`addinfo_ruleset_wood`.

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
     - `Hazus Building Attribute Rulesets - Wind - WSF1-2.pdf <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/03.%20Input:%20DL%20-%20Rulesets%20for%20Asset%20Representation>`_
     - `WindWSFRulesets <https://github.com/NHERI-SimCenter/AssetRepresentationRulesets/blob/main/rulesets/LA/scripts/WindWSFRulesets.py>`_
   * - HAZUS Building Attribute Rulesets - Wind (WMUH1-3)
     - `Hazus Building Attribute Rulesets - Wind - WMUH1-3.pdf <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/03.%20Input:%20DL%20-%20Rulesets%20for%20Asset%20Representation>`_
     - `WindWMUHRulesets <https://github.com/NHERI-SimCenter/AssetRepresentationRulesets/blob/main/rulesets/LA/scripts/WindWMUHRulesets.py>`_

Taking the attribute Second Water Resistance (SWR) as an example, the SWR attribute is assigned by 
a series of time-evolving rules calling upon four fields in the building inventory: year built, 
roof shape, roof slope, and average temperature in January. :numref:`swr_attri` provides the 
detailed rules that map these four variables to the Second Water Resistance (SWR) attribute. 
This example demonstrates an instance where the attribute is assigned as a random variable, 
based on the fact that secondary water resistance is not required by code, though surveys 
of homeowners in hurricane-prone areas can be used to infer how many may have voluntarily 
adopted this mitigation practice. Practices around SWR, particularly for contemporary 
construction, are likely to be different in Louisiana, warranting further refinements 
to these rulesets by users

.. csv-table:: Ruleset for determining the Second Water Resistance attribute for WSF homes.
   :name: swr_attri
   :file: table/example_wood_ruleset.csv
   :align: center


.. [Javeline19]
    Javeline, D., & Kijewski-Correa, T. (2019). Coastal homeowners in a changing climate. Climatic Change, 152(2), 259-274.

.. [FEMA21]
   FEMA (2021), Hazus Hurricane Technical Manual. Hazus 4.2 Service Pack 3. Federal Emergency Management Agency, Washington D.C. 
   https://www.fema.gov/sites/default/files/documents/fema_hazus-hurricane-technical-manual-4.2.3_0.pdf