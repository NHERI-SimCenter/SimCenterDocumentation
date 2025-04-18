.. _testbed_FortMyers

*******************
Fort Myers, Florida
*******************

Hurricane Ian made landfall Sept. 28, 2022, near Cayo Costa, Florida, as a Category 4 storm with maximum sustained winds of 150 mph. Ian pushed a storm surge of 15 feet above ground level into southwest Florida, resulting in record inundation of coastal locations, especially Sanibel Island and Fort Myers.  "According to the NOAA National Centers for Environmental Information, Ian caused an estimated $112.9 billion worth of total damage in the United States (with a 90% confidence interval of $86.8 to $135.9 billion), making Ian the third-costliest United States hurricane on record." In Fort Myers Beach alone, which experienced peak wind gust of 100mph and surge inundation levels of 10 to 15ft above ground level, an estimated 900 structures were totally destroyed, and 2,200 were damaged. ([AL092022]_, [COAPS22]_).

This testbed estimates the damage and loss associated with Hurricane Ian for the Fort Myers beach. It's intent is to discuss/demonstrates the process of performing such a damage and loss estimation utiling the NHERI SimCenter framework, specifically utiling R2D and BRAIL++. This documentation specifically demonstrates the process of: (1) creating an asset inventory utilizing brails, (2) incorporating the hazard information througth GIS information files (3) performing a damage and loss modeling estimation using R2D given the assets and hazard information utilizing a HAZUS approach within the R2D application. 

.. note::

   The adoption of the HAZUS damage and loss assessment methodology for estimnating  damage and loss due hurricane wind and flood, enables the intensity measures to be related to probabilities of damage and loss, based on the building class and assigned attributes. Supported building classes include residential, commercial and industrial construction, critical facilities, and manufactured homes, constructed of wood, steel, reinforced concrete, and masonry. The adoption of HAZUS loss estimation frameworks constrains the current testbed to buildings 6 stories and under and only the building classes currently supported by HAZUS ([FEMA18a]_, [FEMA18b]_).

.. toctree-filt::
   :maxdepth: 1

   hazards
   inventories
   results

**Acknowledgements**

Several members of the SimCenter Team assisted with the development and documentation of this testbed: 
Frank McKenna, Barbaros Cetiner.
Guidance for the testbed was provided by some members of the SimCenter WG on hurricanes, which included Tracy Kijewski-Correa (University of Notre Dame), Seymour Spence (University of Michigan), Ahsan Kareem (University of NotreDame), Andrew Kennedy (University of Notre Dame).
Inundation and Wind fields were provided by Rick Luettich and a wind field model contributed by Teng Wu (University at Buffalo).
Assest inventories were obtained from the assessors office and DesignSafe, and BRAILS++.

**Versioning**

As this documentation will continue to evolve when features are added and as software capabilities improve, the documentation, associated input files, results, and rulesets will be updated over time. The applications are hosted on NHERI-SimCenter DesignSafe and the versioned source codes are archived via Zenodo. Other related files are maintained in two types of repositories:

#. The DesignSafe Project BLAH contains inputs (inventories, rulesetsm and hazard data).
#. GitHub is used as the home for all software, scripts, and applications engaged by the testbed.

This version history of the documentation is tracked in :numref:`doc_version_AC`
and the versions of all applications and rulesets of the current version of the testbed are reported in :numref:`software_version_AC`.
:numref:`brails_version_AC` provides the versions of BRAILS and its various classifiers used in the generation of results herein.

.. list-table:: Testbed Version History
   :name: doc_version_AC
   :header-rows: 1
   :align: center

   * - Description
     - Version
     - Release Date
   * - Initial release
     - 1.0
     - 05/2025
   * - Files
     - Version
     - DOI/Release
   * - R2D
     - `v1.1.1 <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/R2Dt>`_
     - .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5033626.svg
          :target: https://doi.org/10.5281/zenodo.5033626
   * - AssetRepresentationRulesets
     - `v1.0.0 <https://github.com/NHERI-SimCenter/AssetRepresentationRulesets/releases/tag/v1.0.0>`_
     - .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5496056.svg
          :target: https://doi.org/10.5281/zenodo.5496056
   * - DesignSafe Project PRJ-3314
     - v1.0
     - `Data Depot <https://www.designsafe-ci.org/data/browser/projects/6469761920420942316-242ac114-0001-012/>`_

   
.. [AL092022] "NATIONAL HURRICANE CENTER TROPICAL CYCLONE REPORT HURRICANE IAN (AL092022) 23–30 September 2022", Lisa Bucci, Laura Alaka, Andrew Hagen, Sandy Delgado, and Jack Beven, National Hurricane Center, 3 April 2023.

.. [COAPS22]  "Hurricane Ian: A major hurricane that brought wide-ranging catastrophic impacts to Florida", Emily Powell, Florida Climate Center Center for Ocean-Atmospheric Prediction Studies (COAPS), Florida State University, November 14, 2022.

.. [FEMA18a]
   FEMA (2018), HAZUS – Multi-hazard Loss Estimation Methodology 2.1, Hurricane Model Technical Manual, Federal Emergency Management Agency, Washington D.C., 718p.

.. [FEMA18b]
   FEMA (2018), HAZUS – Multi-hazard Loss Estimation Methodology 2.1, Flood Model Technical Manual, Federal Emergency Management Agency, Washington D.C., 569p.



