.. _lbl-testbed_AC_example_outputs:

**************************
Example Outputs
**************************

Regional Results (NSI-Based Year Built)
========================================

The estimated wind damage states and losses under the Hurricane Laura
are shown in :numref:`dl_1` and :numref:`dl_2`.

.. figure:: figure/ExpectedDS.png
   :name: dl_1
   :align: center
   :figclass: align-center
   :figwidth: 800

   Estimated regional damage state map.

.. figure:: figure/ExpectedLoss.png
   :name: dl_2
   :align: center
   :figclass: align-center
   :figwidth: 800

   Estimated loss ratio map.


SURF-Zilow Year Built Results
=============================

As discussed in :ref:`lbl-testbed_LC_asset_description`, the National Structural Inventory (NSI) is used for 
deriving the year built formation. Because not all buildings in the testbed inventory can be mapped exactly to 
the NSI dataset, `SURF <https://github.com/NHERI-SimCenter/SURF>`_ is employed to construct and train a neural 
network and used it to predict year built information based on the spatial patterns in the NSI dataset.

In parallel to this exploration, `Zillow <https://www.zillow.com/>`_ also provides the year built information for 
many of the residual buildings in the studied region. <<Describing scraper and if the data csv could be shared here>>.

Similar to the implementation of NSI dataset, the 1182 data points of year built from Zillow are used to train a 
neural network, :numref:`surf_ yb_test` shows the verification of the trained neural network (predicted vs. true values,
Zillow dataset). More than :math:`85%` buildings have prediction errors less than 20 years.  

.. figure:: figure/SURF_YearBuiltTest.png
   :name: surf_yb_test
   :align: center
   :figclass: align-center
   :figwidth: 700

   SURF-predicted vs. original year built from Zillow dataset.

The neural network is used to predict the year built information for the entire Lake Charles inventory. :numref:`surf_yb_comp`
contrast the resulting SURF-Zillow and the SURF-NSI year built spatial distribution. The difference in year built is relatively 
small for the downtown buildings (~1960s) but increases at the bounds with a maximum of 80 years. The year built information 
from SURF-Zillow dataset is used for an extra round of simulation, the spatial disribution of damage states of SURF-Zillow set 
is shown in :numref:`ds_zillow_comp` and contrasted against the SURF-NSI result (:numref:`dl_1`). Note that the difference is not 
prominent in the downtown Lake Charles. The major spot of divergent results are seen in southwest of the city where the SURF-Zillow set 
predicts relatively lower damage states. Provided in :numref:`pds_cdf` are the CDF distributions of probability of exceeding DS-2 
and DS-3. 

.. figure:: figure/YearBuilt_NSI_SURFZS.png
   :name: surf_yb_comp
   :align: center
   :figclass: align-center
   :figwidth: 1200

   SURF-NSI vs. SURF-Zillow: year built information.

.. figure:: figure/DS_Zillow_Comp.png
   :name: ds_zillow_comp
   :align: center
   :figclass: align-center
   :figwidth: 1000

   SURF-NSI vs. SURF-Zillow: expected damage state.

.. figure:: figure/PDS_cdf.png
   :name: pds_cdf
   :align: center
   :figclass: align-center
   :figwidth: 700

   SURF-NSI vs. SURF-Zillow: CDFs of probability of exceeding DS-2 and DS-3.



Validation: StEER
==================

For the Hurricane Laura, the StEER has released the report of the visual inspection and damage estimation 
for sample buildings in Lake Charles (refered as StEER buildings). There are 99 StEER buildings also 
included in this testbed, which offers an opportunity to validate the workflow. In the meantime, the relatively 
small sample size also offers the convenience of investigating the influence of different modeling parameters 
on the estimated damage states and related them to corresponding field observations to help understand the 
dominant trends in the data. As will be illustrated, some of these trends validate the effectiveness of the 
methodology and others indicate potential measures to improve the wind resistance.

:numref:`influential_var` plots the estimated damage states against key building attributes that are found
to influence the resulting damage state under the hurricane wind hazard. Major obsered trends are as follows:

#. In general, the damage state is negatively correlated to the year built. Buildings with built year after 2000 
   are found to have prominant improvement in the wind resistance and have lower damage states. This is reasoned 
   by the authors to be led by the assumption in the ruleset that the post-2000 buildings would have shutter 
   measures and stronger roof deck attachment.
#. The surface roughness, i.e., terrain feature, is found to be a key variable when considering the potential 
   damage from the hurricane to the building. Even moving from open terrain to light suburban, following the 
   damage fuctions in HAZUS, we see about 50% reduction in the average damage state.
#. Shutters could significantly help reduce the potential wind-induced damage: average damage state is reduced 
   from 2.2 to 1.2
#. Garage type also would influence the building performance against the wind hazard: garages per SFBC 1994 are 
   found to have much better behaviors than the standard and wake garages.
#. Roof deck attachement using a tighter nail spacing (6 in vs. 12 in) is found to perform much better.
#. Gable roof is found to have slightly worse performance than the hip and flat roofs.

.. figure:: figure/InflVari.png
   :name: influential_var
   :align: center
   :figclass: align-center
   :figwidth: 900

   Influential building attributes on the wind-induced damage state.

It is noted that the trends observed in :numref:`influential_var` is based on a so-called "median" model representing 
our best estimates of building attributes. However, in reality, because of the lack of high-resolution or multiple 
data resources, we may not have 100% confidence about certain building attributes or hazard fields, e.g., year built 
or peak wind speed at a specific site. Hence, the esimated "median" damage state from the "median: model may not give 
the full representation of the real damage potential.  As illustrated in :numref:`ds_uq`, if considering the uncertainty 
in the year built (instead of a deterministic value, asssuming it follows a normal distribution with a standard devidation 
of 10 years), we could sample year built from the distribution and repeat the damage assessment by sufficient times to 
estimated the distrbution of damage state.

.. figure:: figure/DS_uq.png
   :name: ds_uq
   :align: center
   :figclass: align-center
   :figwidth: 600

   Uncertainty in the estimated damage state.

Following this idea, for each of the 99 StEER buildings, we sampled 100 year built from a distribution with the mean of 
the given year built value and a standard deviation of 10 years and run the damage assessment for each sampled case.
:numref:`ds_uq_yb` summarizes the comparison between the mean and 95-precentile of estimated damage state and the 
StEER damage state. Similar exercises (:numref:`ds_uq_pws`) are conducted for the peak wind speed where we sampled 100 PWS from a disribution 
with a standard deviation of 20 mph.

.. figure:: figure/DS_uq_yb.png
   :name: ds_uq_yb
   :align: center
   :figclass: align-center
   :figwidth: 600

   Influence of uncertainty in year built on the estimated damage state.


.. figure:: figure/DS_uq_pws.png
   :name: ds_uq_pws
   :align: center
   :figclass: align-center
   :figwidth: 600

   Influence of uncertainty in PWS on the estimated damage state.


Validation: FEMA Historical Geospatial Damage Assessment
========================================================

FEMA and the Department of Interior lead the development of the 
`Geospatial Platform <https://communities.geoplatform.gov/disasters/>`_, an internet-based service environment that 
provides a suite of well-manged geospatial data, services, applications, and tools. The 
`FEMA Historical Damage Assessment Database <https://communities.geoplatform.gov/disasters/historical-damage-assessment-database/>`_ 
is a repository of geospatial damage assessments from past National Disaster events where 
damage assessments were conducted either using high-resolution imagery or by means of geospatial modeling. 

For the Hurricane Laura, the damage categories of 112,571 buildings in the Louisiana were modeled from flood depths at the 
structure as characterized based on modeled wind, flood or surge data. Five damage categories are 
used: No Damage, Affected, Minor, Major, and Destroyed. Out of the 112,571 buildings, 573 buildings, located in 
the west bound of the Lake Charles city at the waterfront of the Prein Lake, are also investigated 
in this testbed. :numref:`fema_damage_subset` is a subset of data obtained from 
`FEMA Public Data <http://disasters.geoplatform.gov/publicdata/National/Data/HistoricalDamageAssessmentDatabase/PublicRelease_20210622/>`_.
:numref:`fema_damage_bim` is the building inventory for this subset.

.. figure:: figure/fema_damage_webpage.png
   :name: fema_ds_webpage
   :align: center
   :figclass: align-center
   :figwidth: 800

   FEMA Historical Geospatial Damage Assessment Database (2020 Hurricane Laura).

.. csv-table:: FEMA Damage Assessment of 573 buildings in Lake Charles (available in this testbed).
   :name: fema_damage_subset
   :file: data/FEMA_DamageDatabase_LakeCharles_Sample.csv
   :header-rows: 1
   :align: center

.. csv-table:: BIM inventory of 573 buildings in this testbed overlapped with the FEMA Damage Assessment Database.
   :name: fema_damage_bim
   :file: data/BIM_LakeCharles_FEMA.csv
   :header-rows: 1
   :align: center

:numref:`fema_dc` shows the damage categories collected from the FEMA Damage Assessmet Database, where most buildings 
are in low damage levels, i.e., No Damage or Affected. Also noted from :numref:`fema_damage_subset` is that all these 
buildings are subject to CAT-4 gust wind speed, which is consistent with our input wind field where the 3-s gust peak 
wind speed is about 130 :math:`mph` (please see :ref:`lbl-testbed_LC_hazard_characterization`).

To compare these damage categories with the estimated damage states by the workflow in this testbed, we assume that the 
five damage categories are mapped to the five damage states in the HAZUS wind damage functions, assuming the inudation is 
not cause prominent flood-induced damage to the buildings. While this assumption is subjected to future validation, 
:numref:`fema_ds_comp` summarizes (1) the expected damage states of the 573 buildings, (2) the spatial distribution of difference between the FEMA 
Damage Categories and esitmated damage states, and (3) the statistic distribution of the difference between the two.
Given the FEMA set is based on a discrete (category-based) description while the testbed set is based on probabilistic 
estimates, the two results have fairly good agreement except the FEMA set has buildings predicted as no damage (DS-0). 
This overprediction of DS-0 is also seen in StEER set resuls (:numref:`ds_uq_yb` and :numref:`ds_uq_pws`). The uncertainty 
in the year built and wind speed, to some extent, can help explain this overprediction. Future investigations are still 
needed to consider other possible factors causing this mismatch in predicted DS-0, e.g., the surface roughness (for these 573 buildinsg, 
the terrain inferred from LULC and used to determine the fragility function is "Open").

.. figure:: figure/FEMA_DC.png
   :name: fema_dc
   :align: center
   :figclass: align-center
   :figwidth: 700

   FEMA Damage Category in the Geospatial Damage Assessment Database (for the 573 buildings).

.. figure:: figure/FEMA_DS_comp.png
   :name: fema_ds_comp
   :align: center
   :figclass: align-center
   :figwidth: 1200

   Comparison: FEMA Damage Category vs. expected damage state by the workflow (for the 573 buildings).