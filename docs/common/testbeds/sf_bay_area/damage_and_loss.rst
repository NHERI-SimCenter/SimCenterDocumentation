.. _lbl-testbed_SF_damage_and_loss:

**************************
Damage and Loss Estimation
**************************

The building performance assessment was performed on a
story-level basis using **PELICUN** ([Zsarnóczay20]_), where damage and losses are calculated with storylevel
fragility functions based on the peak story drift and
floor acceleration demands. The story-based damage and loss
fragility functions are derived from corresponding building-level
damage and loss functions from the HAZUS earthquake
model ([FEMA18]_) based on the characteristic data for each
building (e.g., year of construction, structure type, occupancy
type). Collapse safety limit states are evaluated directly from the
story drift demands, where a collapse of one or more stories is
considered as partial collapse of the entire building. The story
drift and floor accelerations from 25 non-linear analyses of each
building are used to define multivariate lognormal distributions
of peak drifts and accelerations for each story of the building,
and the dispersion in the drift and acceleration demands is
inflated by 0.22 to account for additional modeling uncertainties
not considered in the non-linear dynamic analyses. Using the
distributions of earthquake demands, and damage and loss
functions, **PELICUN** generates 20,000 realizations of damage and
losses for each building, and stores statistics of the resulting
performance data that are relevant for regional-scale evaluation.
The results are output as HDF5 (Hierarchical Data Format) files
that can be processed and visualized through MatLab, Python,
Jupyter notebooks, or converted to CSV format.


.. [Zsarnóczay20]
   Zsarnóczay, A., and Deierlein, G. G. (2020). “PELICUN – A Computational Framework for Estimating Damage, Loss and Community Resilience,” 
   in Proceedings, 17th World Conference on Earthquake Engineering, (Sendai: WCEE).

.. [FEMA18]
   FEMA (2018), HAZUS – Multi-hazard Loss Estimation Methodology 2.1, Earthquake Model Technical Manual, Federal Emergency Management Agency, Washington D.C.
