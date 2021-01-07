.. _lbl-testbed_AC_overview:

********
Overview
********

This testbed for regional hurricane risk assessment of Atlantic County under multiple hazards adopts an approach
consistent with that developed for earthquake hazards. Its intent is to demonstrate the computational scaffolding
upon which community developers can progressively contribute refinements that increase the
fidelity and capacities of the backend regional resilience assessment workflow. Featured by the workflow
offering a fine resolution of parcel-scale representation (instead of the census-block level), the testbed
was able to investigate the building performance of specific asset.

The major components in this testbed include: (1) asset inventory, (2) hazard characterization, (3) asset
representation, (4) damage and loss model, and (5) sampling results. This testbed
includes 32,828 assets in the 23 cities of Atlantic County with a wide combination of
built year, building material type, and occupancy type. Both the wind and surge hazards were
considered as they were characterized by two intensity measures the Peak Wind Speed (PWS) and
Peak Water Depth (PWD), respectively. Analytical and Numerical models were employed to simulate
the wind and surge field for Atlantic County, while interpolations were conducted to
evaluate the intensity measures at the site of each asset. The description of assets
in the inventory adopts an augmented parcel approach that adapts and maps tax assessor data
via designed rulesets to HAZUS-consistent building classifications. For the initial
implementation of the backend workflow, the HAZUS damage and loss assessment methodology for
hurricane and flood was adopted in this testbed. Multiple runs were conducted with different
hurricane categories to inspect the building performance under various scenarios. Sample results
are presented to verify the workflow and demonstrate its usage.
