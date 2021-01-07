.. _lbl-testbed_AC_damage_and_loss:

**************************
Damage and Loss Estimation
**************************

The initial implementation of the hurricane testbed, which is described here, is limited to
consideration of wind and storm surge (i.e., flood) damage and losses.
Further, the calculation of wind effects does not require structural analysis to estimate EDPs,
but rather adopts an approach where damage and losses are calculated directly from the wind speed.
Similarly, the flood-induced loss calculation is based on the peak water depth.
Damage and loss functions from the HAZUS Multi-hazard Loss Estimation Methodology ([FEMA18a]_, [FEMA18b]_)
were implemented in `PELICUN <https://pelicun.readthedocs.io/en/latest/>`_ to support the damage and loss assessment.

For the **wind loss assessment**, the HAZUS functions consist of tabular data to
describe the fragility or expected losses as a function of peak wind speed (PWS). These
data were used to calibrate coupled damage and loss models to estimate the damage
state and the corresponding expected loss ratio for each building configuration in PELICUN.
Continuous functions (Normal or Lognormal cumulative density functions) were fit to the synthetic
data by maximizing the likelihood of the observations assuming a Binomial distribution of outcomes
at each discrete wind speed in the HAZUS database. Only data up to 200 mph wind speeds were used
because the substantial reduction in the number of observations introduces significant measurement
error above that level (:numref:`wind_df`). Coupling the damage and loss models in this way ensures more realistic
outcomes (e.g., a building with no damage cannot have total loss when the two models are coupled),
and the parameterized models allow for more efficient storage and computations within the
workflow.

.. figure:: figure/wind_damage_functions.png
   :name: wind_df
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Fitted HAZUS wind damage functions for example building classes.

The HAZUS damage and loss functions are grouped into five main classes by building material, with
additional subclasses by building type. For each building class, e.g., wood single-family homes 1-2+
stories, a collection of attributes are used to define key features of the load path and components
(e.g., roof shape, secondary water resistance, roof deck attachment, roof-wall connection, shutters,
garage) as well as the exposure (terrain roughness previously estimated in the Wind Hazard Model)
to assign the corresponding fragility. A rules engine was developed using a combination of historical
New Jersey model building codes, surveys capturing owner-driven mitigation actions (e.g., [Javeline19]_),
and market data to assign these attributes to each parcel based on age and
other available building information (e.g., MOD IV data). Libraries of damage and loss functions
associated with storm surge from the USACE and other recent studies in the literature are planned for
future releases of PELICUN. Eventually, these damage and loss descriptions will be supplemented
with more advanced models as the testbed is progressively refined to include component-based
fragilities and fault-trees that capture cascading damage sequences resulting from breaches of the
building envelope.

For the **flood loss assessment**, the HAZUS functions are in the form of depth-damage ratio curves, relating
the peak water depth (PWD) of flooding (in feet), as measured from the top of the first finished floor,
to a percent of the total replacement cost of the asset. These depth-damage ratio curves are provided
for each building class as listed in :numref:`flood_bldg_class`. :numref:`flood_ddc` shows the depth-damage
ratio curves.

.. figure:: figure/flood_depth_damage_curves.png
   :name: flood_ddc
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Depth-damage ratio curves for the flood loss assessment.

The **total loss** from wind and flood damages are estimated by combining the "wind-only" and "flood-only"
losses following the combination rule in [FEMA18a]_. The primary motivation for the combined wind and
flood loss methodology is to avoid “double counting” of damage. At a minimum, the combined wind and
flood loss must be at least the larger of the wind-only or the flood-only loss. At a maximum, the combined
loss must be no larger than the lesser of the sum of the wind-only and flood-only losses
or 100% of the building (or contents) replacement value. These constraints can be written
as:

.. math::

   max(L_{wind}, L_{flood}) \leq L_{combined} \leq min(L_{wind}+L_{flood}, 1.00)

where :math:`L_{wind}` is the wind-only loss ratio, :math:`L_{flood}` is the flood-only loss ratio, and :math:`L_{combined}`
is the combined loss ratio. The HAZUS combination rule first assumes that the wind-induced damage and flood-induced damage
are spread uniformly and randomly over a building. In this idealized case, the two damage mechanisms can be treated as
independent, and the expected combined loss ratio is simply as:

.. math::

   L_{combined} = L_{wind} + L_{flood} - L_{wind} \times L_{flood}

However,  it is nonetheless clear that neither wind nor storm surge damages are
uniformly and randomly distributed throughout a structure. Wind damage is most
frequently initiated at the roof and fenestrations (i.e., windows,
doors, or other openings in the building envelope), whereas flood damage is most
frequently initiated at the lowest elevations of the structure (e.g., basement or first
finished floor) and progresses upward through the structure as the depth of flooding
increases. HAZUS used an approach for incorporating the non-uniformity of
wind and flood damage into the combined loss methodology, which is based on
allocating wind and flood losses to building *sub-assemblies* as a function of the building
type and the overall wind-only and flood-only loss estimate.

This so-called building sub-assembly approach can more accurately apply the combination calculation above
to each sub-assembly instead of applying it to the entire building. Specifically, HAZUS groups the loss
components into a consistent set of building sub-assemblies:

.. note::
   HAZUS building sub-assemblies ([FEMA18a]_):
      1. Foundation: Includes site work, footings, and walls, slabs, piers or piles.
      2. Below First Floor: Items other than the foundation that are located below the first floor of the structure such as mechanical equipment, stairways, parking pads, break away flood walls, etc.
      3. Structure Framing: Includes all of the main load carrying structural members of the building below the roof framing and above the foundation.
      4. Roof Covering: Includes the roof membrane material and flashing.
      5. Roof Framing: Includes trusses, rafters, and sheathing.
      6. Exterior Walls: Includes wall covering, windows, exterior doors, and insulation.
      7. Interiors: Includes interior wall and floor framing, drywall, paint, interior trim, floor coverings, cabinets, counters, mechanical, and electrical

Hence, the combination is conducted at each sub-assembly level and the total combined loss ratio is the
sum of combined sub-assembly loss ratios:

.. math::

   L_{combined} = \sum\limits_{i=1}^7 L_{wind,i} + L_{flood,i} - L_{wind,i} \times L_{flood,i}

where :math:`L_{wind,i}` is the wind-only loss ratio of the :math:`i^{th}` sub-assembly, and
:math:`L_{flood,i}` is the flood-only loss ratio of the :math:`i^{th}` sub-assembly. These sub-assembly
loss ratios are computed as a percent of the total building loss ratio. The percentages are based on the
:numref:`wind_comp` and :numref:`flood_comp` that are developed per the HAZUS methodology and data table ([FEMA18a]_).

.. csv-table:: Sub-assembly wind-only loss contribution ratio table.
   :name: wind_comp
   :file: data/wind_sub.csv
   :header-rows: 1
   :align: center

.. csv-table:: Sub-assembly flood-only loss contribution ratio table.
   :name: flood_comp
   :file: data/flood_sub.csv
   :header-rows: 1
   :align: center

The estimated wind-only, flood-only, and total losses under the four hurricane
scenarios (:numref:`hurricane_cat`) are shown in :numref:`dl_c2` to :numref:`dl_c5`.

.. figure:: figure/DL_category2.png
   :name: dl_c2
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Estimated regional loss maps for the **Category 2** hurricane.

.. figure:: figure/DL_category3.png
   :name: dl_c3
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Estimated regional loss maps for the **Category 3** hurricane.

.. figure:: figure/DL_category4.png
   :name: dl_c4
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Estimated regional loss maps for the **Category 4** hurricane.

.. figure:: figure/DL_category5.png
   :name: dl_c5
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Estimated regional loss maps for the **Category 5** hurricane.

Average expected loss ratios are also computed for individual cities, which are
summarized in :numref:`cl_c2` to :numref:`cl_c5`

.. figure:: figure/city_loss_c2.png
   :name: cl_c2
   :align: center
   :figclass: align-center
   :figwidth: 100%

   City-wise average expected loss ratios (**Category 2** hurricane).

.. figure:: figure/city_loss_c3.png
   :name: cl_c3
   :align: center
   :figclass: align-center
   :figwidth: 100%

   City-wise average expected loss ratios (**Category 3** hurricane).

.. figure:: figure/city_loss_c4.png
   :name: cl_c4
   :align: center
   :figclass: align-center
   :figwidth: 100%

   City-wise average expected loss ratios (**Category 4** hurricane).

.. figure:: figure/city_loss_c5.png
   :name: cl_c5
   :align: center
   :figclass: align-center
   :figwidth: 100%

   City-wise average expected loss ratios (**Category 5** hurricane).

For the top five cities with most assets in the building inventory, the average
expected wind losses are computed for different built eras. Buildings before 1980s generally
have relatively higher wind loss ratios where 1970s is found to be the worst decade for
Atlantic City, Brigantine, and Galloway. Since 1980, the building performance is improved
where the post-2000 buildings are found to behave much better than buildings in the other groups. 

.. figure:: figure/atlantic_wind_loss.png
   :name: wl_atlantic
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Average expected wind loss ratios (Atlantic City).

.. figure:: figure/brigantine_wind_loss.png
   :name: wl_brigantine
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Average expected wind loss ratios (Brigantine).

.. figure:: figure/galloway_wind_loss.png
   :name: wl_galloway
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Average expected wind loss ratios (Galloway).

.. figure:: figure/margate_wind_loss.png
   :name: wl_margate
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Average expected wind loss ratios (Margate City).

.. figure:: figure/ventor_wind_loss.png
   :name: wl_ventor
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Average expected wind loss ratios (Ventor City).

.. [FEMA18a]
   FEMA (2018), HAZUS – Multi-hazard Loss Estimation Methodology 2.1, Hurricane Model Technical Manual, Federal Emergency Management Agency, Washington D.C., 718p.

.. [FEMA18b]
   FEMA (2018), HAZUS – Multi-hazard Loss Estimation Methodology 2.1, Flood Model Technical Manual, Federal Emergency Management Agency, Washington D.C., 569p.

.. [Javeline19]
   Javeline, D. and Kijewski-Correa, T. (2019) “Coastal Homeowners in a Changing Climate,” Climatic Change. 152(2), 259-276 https://doi.org/10.1007/s10584-018-2257-4
