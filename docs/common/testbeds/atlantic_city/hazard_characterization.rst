.. _lbl-testbed_AC_hazard_characterization:

***********************
Hazard Characterization
***********************

Both the wind and flood hazards affect the building inventory in this testbed.
As the initial implementation of the regional assessment workflow, the testbed mainly
adapted the HAZUS Hurricane Damage and Loss Assessment methodology to quantify the
hazards by two intensity measures: Peak Wind Speed (PWS), and Peak Water Depth (PWD).
The PWS refers to maximum wind speed average over a 3-second gust and measured at 10m height
and under the open terrain surface condition (equivalent to the Exposure C in ASCE 7-16).
The PWD is the maximum depth of flooding during the time period of the hurricane event.
The following sections will introduce the wind and flood fields used in this testbed.

Wind Modeling
==============

The initial implementation of the testbed utilizes the highly efficient, linear analytical
model for the boundary layer winds of a moving hurricane developed by ([Snaiki17a_], [Snaiki17b_]) as
implemented in the NJcoast Storm Hazard Projection (SHP) Tool ([NJCoast20_]). To account for the exposure in each New Jersey county, an
effective roughness length (weighted average) of the upwind terrain is used based on the Land
Use/Land Cover data reported by the state’s Bureau of GIS. While the model is fully height-resolving
and time-evolving, for a given five parameter hurricane scenario, the wind hazard is characterized by
the maximum 10-minute mean wind speed observed during the entire hurricane track. This is
reported at the reference height of 10 m over a uniform grid (0.85-mile spacing, 1.37 km), which is
then accordingly adjusted for compatibility with the averaging interval assumed by the HAZUS
Hurricane Damage and Loss Model. Note the wind speed (:math:`V(600s, 10m, z_0)`) from the
NJcoast SHP Tool is averaged over the time window of 1 hour, so the following conversions
was conducted for parsing the wind speed to the 3-second and open-terrain PWS (i.e., :math:`V(3s, 10m, Exposure C)`):

1. Computing :math:`\alpha` and :math:`z_g` by ASCE 7-16 ([ASCE16_]) Equation C26.10-3 and C26.10-4
taking :math:`c_1 = 5.65, c_2 = 450` for units in m):

.. math::

   \alpha_{SHP} = c_1z_0^{-0.133}

   z_{g,SHP} = c2z_0^{0.125}

2. Computing the gradient height :math:`V(600s, z_g, z_0)` using the power law expression:

.. math::

   V(600s, z_g, z_0) = V(600s, 10m, z_0) \times (\frac{z_{g,SHP}}{10m})^{1/\alpha_{SHP}}

3. Computing the Exposure C (open-terrain) wind speed at 10m height :math:`V(600s, 10m, Exposure C)`, with
:math:`\alpha_C = 9.5` and :math:`z_{g,C} = 274.32 m` ([ASCE16_]):

.. math::

   V(600s, 10m, Exposure C) = V(600s, z_{g,C}, z_0) \times (\frac{10m}{z_g})^{1/\alpha_C}

4. Converting the result to 3s-gust wind speed using the ESDU conversion [ESDU02_]:

.. math::

   V(3s, 10m, Exposure C) = V(600s, 10m, Exposure C) \times \frac{C(3s)}{C(600s)}

where :math:`C(3s) = 1.52` and :math:`C(600s) = 1.05` are the Gust Factor from the ESDU conversion.

Wind fields described by either approach are then locally interpolated to the site of each parcel in the inventory.
The resulting 3s-gust peak wind speed (PWS) ranges from 178 mph to 191 mph given the simulated Category-5 hurricane event (:numref:`pws`).
Because the SPH model tracks the maximum wind speed over the entire hurricane time history - so the inland cities are subjected to
slightly higher wind speed than the coastal cities.

.. figure:: figure/pws.png
   :name: pws
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Interpolated peak wind speed (3s-gust) for each asset in the inventory.

Storm Surge Modeling
=====================

Coastal hazard descriptions use the outputs of the aforementioned SHP Tool, which estimates storm
surge and total run up due to the breaking of near-shore waves for an arbitrary hurricane scenario
using surrogate modeling techniques ([Jia13]_, [Jia15]_). The SHP Tool
leverages the US Army Corps of Engineers (USACE) NACCS: North Atlantic Coastal
Comprehensive Study ([NadalCaraballo15]_), which contains over 1000 high-fidelity
numerical simulations of hurricanes using the ADCIRC ([Luettich92]_) storm surge model,
coupled with STWAVE ([Smith01]_) to capture the additional effects of waves offshore. The
NACCS database was further enhanced with wave run-up simulations that capture the interaction of
the waves with site-specific bathymetry/topography (2015 USGS CoNED Topobathy DEM: New
Jersey and Delaware (1888 - 2014) dataset) to project the total run up inland, along transects spaced
0.5 km apart along the New Jersey coast. This results in a prediction of storm surge height at the
USACE-defined save points along the New Jersey coast that are, on average, 200 m apart, with finer
resolution in areas with complex topographies. The SHP Tool was executed for the testbed scenario
to estimate the depth of storm surge above ground, geospatially interpolated to 110,000 nearshore
locations at approximately 120 m spacing, accompanied by the Limit of Moderate Wave Action
(LiMWA) and wet-dry boundary respectively defining the extent of damaging waves and inundation
over land at each of the transect points. These are then interpolated to the location of the coastal
parcels to express the property exposure to storm surge (:numref:`pwd`). In the initial implementation, as demonstrated
in this test, only the peak water depth (PWD) was considered, which will be used in the HAZUS
Flood Damage and Loss Assessment.

.. figure:: figure/pwd.png
   :name: pwd
   :align: center
   :figclass: align-center
   :figwidth: 100%

   Interpolated peak water depth for each asset in the inventory.

Multiple Category Analysis (MCA)
=================================

Note that the resulting 3s-gust PWS values by this Category-5 hurricane is much higher than
the design wind speed specified by ASCE 7-16 ([ASCE16]_) for the Atlantic County which ranges
from 105 mph to 115 mph. Since this extreme scenario bears a small likelihood, this testbed
also scales the wind and flood water field down to lower categories to conduct the so-called
Multiple Category Analysis to exam the building performance under different intense scenarios.
The PWS and PWD were scaled to Categories 2, 3, and 4 as summarized in :numref:`hurricane_cat`.

.. table:: Scaled peak wind speed and peak water depth for different hurricane categories.
   :name: hurricane_cat

   +-----------------------+-----------+-----------+-----------+-----------+
   | Hurricane Category    |     2     |     3     |     4     |     5     |
   +-----------------------+-----------+-----------+-----------+-----------+
   | Peak Wind Speed (mph) | 101 - 108 | 119 - 127 | 136 - 145 | 178 - 191 |
   +-----------------------+-----------+-----------+-----------+-----------+
   | Peak Water Depth (ft) |   0 - 7   |   0 - 11  |   0 - 15  |   0 - 18  |
   +-----------------------+-----------+-----------+-----------+-----------+



.. [Snaiki17a]
   Snaiki, R. and Wu, T. (2017a) “Modeling tropical cyclone boundary layer: Height-resolving
   pressure and wind fields,” Journal of Wind Engineering and Industrial Aerodynamics, 170, 18-27.

.. [Snaiki17b]
   Snaiki, R. and Wu, T. (2017b) “A linear height-resolving wind field model for tropical
   cyclone boundary layer,” Journal of Wind Engineering and Industrial Aerodynamics, 171, 248-260.

.. [ATC20]
   ATC (2020b), ATC Hazards By Location, https://hazards.atcouncil.org/, Applied Technology Council, Redwood City, CA.

.. [NJCoast20]
   NJ Coast (2020), Storm Hazard Projection Tool, NJ Coast, https://njcoast.us/resources-shp/

.. [ASCE16]
   ASCE (2016), Minimum Design Loads for Buildings and Other Structures, ASCE 7-16,
   American Society of Civil Engineers.

.. [ESDU02]
   Engineering Sciences Data Unit (ESDU). (2002). “Strong winds in the atmospheric boundary
   layer—Part 2: Discrete gust speeds.” ESDU International plc, London, U.K.

.. [Jia13]
   Jia G. and A. A. Taflanidis (2013) "Kriging metamodeling for approximation of high-dimensional
   wave and surge responses in real-time storm/hurricane risk assessment," Computer Methods in
   Applied Mechanics and Engineering, V(261-262), 24-38.

.. [Jia15]
   Jia G., A. A. Taflanidis, N. C. Nadal-Caraballo, J. Melby, A. Kennedy, and J. Smith (2015) "Surrogate
   modeling for peak and time dependent storm surge prediction over an extended coastal region using
   an existing database of synthetic storms," Natural Hazards, V81, 909-938

.. [Nadal‐Caraballo15]
   Nadal‐Caraballo N.C, J. A. Melby, V. M. Gonzalez, and A. T. Cox (2015), North Atlantic Coast
   Comprehensive Study – Coastal Storm Hazards from Virginia to Maine, ERDC/CHL TR-15-5, U.S.
   Army Engineer Research and Development Center, Vicksburg, MS.

.. [Luettich92]
   Luettich R.A, J. J. Westerink, and N. W. Scheffner (1992), ADCIRC: An advanced three-dimensional
   circulation model for shelves, coasts, and estuaries. Report 1. Theory and methodology of ADCIRC-
   2DDI and ADCIRC-3DL, Dredging Research Program Technical Report DRP-92-6, U.S Army
   Engineers Waterways Experiment Station, Vicksburg, MS.

.. [Smith01]
   Smith J.M, A. R. Sherlock, and D. T. Resio (2001) "STWAVE: Steady-state spectral wave model user's
   manual for STWAVE, Version 3.0," Defense Technical Information Center, US Army Corps of
   Engineering, Vicksburg, MS.
