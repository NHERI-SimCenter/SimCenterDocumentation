.. _lbl-testbed_AC_asset_representation:

********************
Asset Representation
********************

Level 1
=======

Following HAZUS building type classification and the diversity of the collected
data in the building inventory. For wind damage and loss, this testbed groups
buildings into 5 main types by the major building material
(wood, masonry, concrete, steel, manufactured home). In specific, this testbed
adapts the HAZUS building classifications to a catalog of 36 building classes
are created by the story number or/and footprint size, which
are summarized in :numref:`bldg_class`. For flood damage and loss, this testbed
groups buildings based on the building occupancy class as summarized in
:numref:`flood_bldg_class`.

.. csv-table:: Building classification for wind loss assessment.
   :name: bldg_class
   :file: data/bldg_class.csv
   :header-rows: 1
   :align: center

.. csv-table:: Building classification for flood loss assessment.
   :name: flood_bldg_class
   :file: data/flood_bldg_class.csv
   :header-rows: 1
   :align: center

At the Level 1, for each building class, HAZUS further differentiates buildings
to subclasses by asset attributes. These asset attributes are used to developed
the unique damage fragility and loss functions for a class of buildings based on
data and statistics from previous hurricane and flood events. For instance, the
wind-induced damage on wood frames are influenced by the roof shape and the
connection strength between the roof and walls. However, because of the incompleteness
of the building inventory data, not all asset attributes are directly available,
and many of them are not easy to be acquired in general. To address this
lack-of-information issue, this testbed developed and implemented a set of rulesets
to infer the HAZUS required asset properties based on the available attributes
in the building inventory. :numref:`flood_attri_rule` lists the major attributes for
flood loss assessment and their rulesets. And the following sections summarizes the
attributes for wind loss assessment and presents examples of the rulesets.

.. csv-table:: Attributes and rulesets for flood loss assessment.
   :name: flood_attri_rule
   :file: data/HazusAttributesRuleset-FLOOD.csv
   :header-rows: 1
   :align: center

Wooden buildings
-----------------

The wooden buildings have 5 building classes: two Wood Single Family (WSF1 and WSF2) classes and
three Wood Multi-Unit Home (WMUH1, WMUH2, and WMUH3). Their key attributes that influence the
fragility functions are listed in :numref:`wsf_attri` and :numref:`wmuh_attri`.

.. csv-table:: HAZUS Wood Singe Family (WSF) attributes.
   :name: wsf_attri
   :file: data/wsf_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Wood Multi-Unit Home (WMUH) attributes.
   :name: wmuh_attri
   :file: data/wmuh_attributes.csv
   :header-rows: 1
   :align: center

Taking the Second Water Resistance (SWR) as an example, the SWR is determined
by four input variables of the asset from the building inventory including
the built year, roof shape, roof slope, and average temperature in January.
:numref:`swr_attri` provides the detailed rules that map these four variables
to the Second Water Resistance (SWR) attribute. The complete rulesets can be
found in :download:`HazusAttributesRulesets-WIND.xlsx <data/HazusAttributesRulesets-WIND.xlsx>`.

.. csv-table:: Ruleset for determining the Second Water Resistance attribute.
   :name: swr_attri
   :file: data/example_wood_ruleset.csv
   :header-rows: 1
   :align: center

Masonry buildings
------------------

The masonry buildings have 14 building classes: two Masonry Single Family (MSF1 and MSF2) classes,
three Masonry Multi-Unit Home (MMUH1, MMUH2, and MMUH3), two Masonry Low-Rise Strip Mall
(MLRM1 and MLRM2) classes, three Masonry Engineered Residential Building (MERBL, MERBM,
and MERBH) classes, three Masonry Engineered Commercial Building (MECBL, MECBM,
and MECBH) classes, and one Masonry Low-Rise Industrial Building (MLRI) class.
Their key attributes that influence the fragility functions are listed in
:numref:`msf_attri`, :numref:`mmuh_attri`, :numref:`mlrm_attri`,
:numref:`merb_attri`, :numref:`mecb_attri`, and :numref:`mlri_attri`.

.. csv-table:: HAZUS Masonry Singe Family (MSF) attributes.
   :name: msf_attri
   :file: data/msf_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Masonry Multi-Unit Home (MMUH) attributes.
   :name: mmuh_attri
   :file: data/mmuh_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Masonry Low-Rise Strip Mall (MLRM) attributes.
   :name: mlrm_attri
   :file: data/mlrm_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Masonry Engineered Residential Building (MERB) attributes.
   :name: merb_attri
   :file: data/merb_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Masonry Engineered Commercial Building (MECB) attributes.
   :name: mecb_attri
   :file: data/mecb_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Masonry Low-Rise Industrial Building (MLRI) attributes.
   :name: mlri_attri
   :file: data/mlri_attributes.csv
   :header-rows: 1
   :align: center

Steel buildings
---------------

The steel buildings have 6 building classes: three Steel Engineered Residential
Building (SERBL, SERBM, and SERBH) classes and three Steel Engineered Commercial
Building (SECBL, SECBM, and SECBH) classes. Their key attributes that influence
the fragility functions are listed in :numref:`serb_attri` and :numref:`secb_attri`.

.. csv-table:: HAZUS Steel Engineered Residential Building (SERB) attributes.
   :name: serb_attri
   :file: data/serb_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Steel Engineered Commercial Building (SECB) attributes.
   :name: secb_attri
   :file: data/secb_attributes.csv
   :header-rows: 1
   :align: center

Concrete buildings
------------------

The concrete buildings have 6 building classes: three Concrete Engineered Residential
Building (CERBL, CERBM, and CERBH) classes and three Concrete Engineered Commercial
Building (CECBL, CECBM, and CECBH) classes. Their key attributes that influence
the fragility functions are listed in :numref:`cerb_attri` and :numref:`cecb_attri`.

.. csv-table:: HAZUS Concrete Engineered Residential Building (CERB) attributes.
   :name: cerb_attri
   :file: data/cerb_attributes.csv
   :header-rows: 1
   :align: center

.. csv-table:: HAZUS Concrete Engineered Commercial Building (CECB) attributes.
   :name: cecb_attri
   :file: data/cecb_attributes.csv
   :header-rows: 1
   :align: center

Manufactured homes
------------------

The Manufactured Homes (MH) have five building classes (MHPHUD,
MH76HUD, MH94HUD-I, MH94HUD-II, and MH94HUD-III) classes.
Their key attributes that influence the fragility functions are listed in
:numref:`mh_attri`.

.. csv-table:: HAZUS Manufactured Homes (MH) attributes.
   :name: mh_attri
   :file: data/mh_attributes.csv
   :header-rows: 1
   :align: center

Level 2
=======

To be extended in the future.

Level 3
=======

To be extended in the future.
