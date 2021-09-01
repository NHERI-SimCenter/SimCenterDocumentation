.. _lbl-testbed_LC_best_practices:

**************************
Best Practices
**************************

Recommended best practices are summarized as follows:

#. Inventories are based upon building footprint data which may be sourced from state/local authorities or 
   third parties, which should be selected based on known accuracy. State/local data is often the most accurate 
   as they have been quality assured through human oversight. In the absence of such data, select third-party 
   data that is hand drawn, when possible: 2017 Microsoft footprint data is preferable since it is hand-digitized 
   vs. 2018 Microsoft footprint data which is computer-generated. 
#. Note that footprint data may still contain skewed buildings, offset outlines, individual buildings whose 
   close proximity caused them to be treated as a single building outline, or outlines that include 
   non-structural features. Thus footprint data may require additional processing to rectify such issues and 
   any adjustments to the footprints further requires recalculation of coordinates and coordinate-dependent 
   information. 
#. Triangulate data sources to improve data quality, e.g., sanity-checking building classifications in tax 
   assessor data by using zoning or land use/land cover data, cross-checking state tax assessor data against 
   county tax assessor data. 
#. Footprints need to be assigned parcel data from the local tax assessor. If a footprint falls within parcel, 
   the footprint should receive that parcel’s attributes, noting that a parcel may have multiple footprints 
   within it: If footprint falls between multiple parcels, assign it the parcel information with a higher level of 
   flood risk based on the FEMA-designated flood zone, where risk goes from highest to lowest according to: VE, 
   AE, AO, AH, A, X. If footprint falls between multiple parcels and both with the same FEMA flood zone, 
   it receives the parcel information for the parcel with the highest overlapping area. If a footprint falls 
   outside a parcel, it is assigned the attributes of the nearest parcel.
#. Once footprints are identified, assign default values for each required attribute in the Building Inventory. 
   These default values should be selected using engineering judgment to represent the most common/likely 
   attribute expected or conservatively from the perspective of anticipated losses (i.e., picking the more 
   vulnerable attribute option). These initial assignments are then updated if additional data is available 
   to make a more faithful attribute assignment. As part of the default assignment class, pick a building 
   typology that is prevalent in the locale as your default building. For example, implementers may select Single 
   Family Dwelling/Residence, made of Wood (stud-framed) with Slab-on-Grade foundation, shingles as its roof 
   covering, and siding as its wall covering (specific material types may be specified, e.g., asphalt shingle 
   or vinyl siding, depending on the granularity of the damage/loss models). 
#. Elevation certificates may be available from local authorities and can be consulted to establish the 
   elevation of the lowest horizontal structural member for food risk assessments. Most risk assessments will 
   require the top of the bottom occupied floor, which will be defined relative to the lowest adjacent (finished) 
   grade (LAG). Digital Elevation Models (DEMs) can also be consulted to establish building elevations. Note that 
   the SimCenter’s image processing tools minimize the need for these data sources.
#. Extend the trained models to new regions where construction practices may differ.






