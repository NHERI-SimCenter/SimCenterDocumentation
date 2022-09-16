.. _lbl-testbed_LC_future_refinements:

****************************************
Research Opportunities
****************************************

This testbed and its backing workflows should be viewed as a sandbox and scaffold, 
respectively, within which the community can explore different scenarios and develop 
new capabilities. The following list itemizes some areas where contribution from the 
community is especially welcome: 

#. The current use of HAZUS for damage and loss modeling limits the buildings under 
   consideration to 6 stories and under. Thus the user community is invited to support 
   the extension of PELICUN to buildings taller than 6 stories.

#. Extensions to taller buildings will require further expansion of the building 
   inventory’s fields to capture attributes relevant to those classes of construction. 
   Methods to mine relevant data from imagery or other third party data sources, e.g., 
   Emporis, will provide welcome extensions to the Asset Description approaches described herein.

#. The testbed will benefit from continued validation efforts, mining larger cross-sections 
   of data assembled by StEER and others and spanning a wider range of vintages of construction, 
   i.e., YearBuilt.

#. Currently the workflow calculates damage and monetary loss; coupling the workflow with other 
   social, societal or economic models, will provide opportunities to more robustly explore the 
   impacts of hazard events, mitigation investments and development decisions on community resilience. 
   The creation of techniques to automatically scrape and fuse data from the social, human and behavioral 
   sciences will ensure those datasets can be generated in a manner similar to those used for the 
   building inventory itself. 

#. A number of approximations and assumptions were made in the generation of the building inventory 
   (see :ref:`lbl-testbed_LC_asset_description`)
   There is considerable opportunity to expand, enrich and improve upon 
   methodologies for automated inventory generation, particularly to generate other attributes necessary 
   as the workflow advances to include other classes of construction and eventually component-level 
   damage quantification.

#. The current implementation considers only wind hazards and thus will warrant extension to include flood 
   losses similar to the approach adopted in the `Atlantic County, NJ <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/index.html>`_ testbed. This will also enable a
   more faithful comparison with the multi-hazard assessments conducted by StEER and FEMA (see :ref:`lbl-testbed_LC_getting_started`).

#. The current implementation considers only wood residential construction and thus would benefit from 
   extension to other building classes in a manner similar to that exercised in the 
   `Atlantic County, NJ <https://nheri-simcenter.github.io/R2D-Documentation/common/testbeds/atlantic_city/index.html>`_ testbed.

#. The current pre-trained BRAILS models could be extended to new regions where construction practices may differ. 
   Please refer to the discussion on the `generalization of BRAILS models <https://nheri-simcenter.github.io/BRAILS-Documentation/common/technical_manual/understand.html>`_

#. More importantly, the rulesets used to demonstrate how a hindcast testbed could be swiftly implemented 
   were ported over from New Jersey. The rulesets warrant updating to match the regulatory environment in 
   Louisiana and also to capture the behaviors and norms in this region, e.g., the low rates of window 
   protection observed by StEER ([Roueche21]_).

#. The SimCenter aspires to incorporate increasing levels of fidelity in its characterization of hazards, 
   modeling of buildings (to support application of pressures/loads and structural analysis), and ability 
   to describe damage at the component level, with fault-trees that capture cascading damage sequences 
   resulting from breaches of the building envelope. Thus there is considerable need for community 
   research contributions such as libraries of fragilities, archetype building models, and catalogs 
   of high-fidelity hazard simulations (hindcasts of historical events or synthetic storm data). 
   This is especially the case of coastal hazards. With aspirations to replicate this workflow in other 
   regions, these contributions need not be confined to Lousiana/Gulf Coast. Their integration into 
   the testbed can demonstrate how the contributions of individual researchers can aggregate to evaluate 
   impact on much larger scales.

#. The testbed does not explicitly treat the effects of debris (wind-borne or surge-transported), nor 
   are any of the flow fields translated into pressures acting on individual buildings to enable the 
   execution of structural analyses. Extending the workflow to tall buildings creates opportunities for 
   response simulation to estimate drifts or other EDPs for more dynamically sensitive structures under 
   wind. However, similar opportunities to translate geospatially varying hazards into loads on a given 
   structure can be seized to increase the workflow's overall fidelity.


.. [Roueche21]
   Roueche, D. Kameshwar, S. Vorce, M. Kijewski-Correa, T. Marshall, J. Mashrur, N. Ambrose, K. Brown, C. Childress, O. Fox, D. Morris, 
   K. Rawajfih, H. Rodriguez, L. (2021) "Field Assessment Structural Teams: FAST-1, FAST-2, FAST-3", in StEER - Hurricane Laura. 
   DesignSafe-CI. https://doi.org/10.17603/ds2-dha4-g845