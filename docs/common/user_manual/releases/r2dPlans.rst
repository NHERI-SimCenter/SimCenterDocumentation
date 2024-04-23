.. _lbl-future_r2d:

.. role:: blue

*************
Release Plans
*************

The following features are planned to be developed for upcoming releases of |app|. We are actively working on the features in the next release. Farther development priorities may change depending on feedback from the community. If you have any suggestions, we encourage you to contribute and contact us through the SimCenter Forum.


June 2024
----------
#. Water Distribution Network, buried pipelines.(1.3.4.3)

#. Efficient forward propagation using Multi-Fidelity Monte-Carlo (1.2.3.1) - Use a few realizations of the output calculated with expensive, high-fidelity models to evaluate and correct the bias in efficient, approximate models, such as surrogates. With little extra computational demands, this method provides a substantial improvement in surrogate model performance if you have the high-fidelity models available that were used to train the surrogates.

#. Add datasets to simulate subassembly damage and losses under wind demands (1.3.5.1) - Data from recent publications in the Performance-Based Wind Engineering literature is collected to enable high-resolution performance assessment under wind hazard, add data to DB-DamegeAndLoss.

#. Probabilistic asset inventories (1.3.6.2) - Calibrate, store, and propagate uncertainties in building features at the regional scale. For example, we have some but not all information for all buildings in an area, fill in the gaps using information we do know.

      
Sep 2024
----------
#. Automatic access to physics-based ground motion simulation results (1.1.1.3)

#. Add datasets to simulate subassembly damage and losses under water demands (1.3.5.2)

#. Add datasets to simulate high-resolution damages and losses in buried pipeline networks (1.3.5.4)
   

Dec 2024
---------
#. Develop methods to model interdependencies between physical components, housing, socio-economic functions, and lifelines (1.3.4.6)

#. Add datasets to simulate high-resolution damages and losses in transportation networks (1.3.5.3)

#. Develop and implement metrics and their visualization to inform recovery and community resilience (1.4.3.2)

#. Look at aspects related to recovery. Housholds (1.4.3.2), Infrastructure (1.4.2.4), Business operations (1.4.2.5)


Sept 2025
---------
#. Multi-fidelity models in regional simulations (1.3.3.1)
#. Multi-scale models for wind and water (1.3.3.2)

 .. note::

    The numbers in parentheses are for internal tracking purposes.

