.. _lbl-testbed_SF_response_simulation:

*******************
Response Simulation
*******************

The non-linear response of buildings to ground shaking is
simulated using OpenSees ([OpenSees20]_) and an application,
**MDOF-LU**, that generates an idealized structural analysis model
based on structure type, height, plan area, year of construction
and the type of occupancy. The **MDOF-LU** application is based
on a method developed by [Lu14]_ that uses the
building configurations in the HAZUS earthquake technical
manual and corresponding capacity curve descriptions to define
a multi-story non-linear shear-column finite element model
with lumped masses.

Each of the 1.84 M building models is analyzed for 25 pairs
of 2D ground motions, where the peak story drift ratios and 
peak floor accelerations are recorded for subsequent damage
and loss analyses. The approximations and uncertainties in the
structural model and behavior are considered by treating the
initial stiffness and the damping ratio as random variables with
a 0.1 coefficient of variation. These uncertainties are propagated
through the analysis using different realizations of the stiffness
and damping parameters for each of the 25 non-linear dynamic
analyses for each building.


.. [OpenSees20]
   OpenSees (2020). Open System for Earthquake Engineering Simulation. Berkeley: OpenSees.

.. [Lu14]
   Lu, X., Han, B., Hori, M., Xiong, C., and Xu, Z. (2014). 
   A coarse-grained parallel approach for seismic damage simulations of urban areas based on refined
   models and GPU/CPU cooperative computing. Adv. Engine. Soft. 70, 90–103. 
   doi: 10.1016/j.advengsoft.2014.01.010

