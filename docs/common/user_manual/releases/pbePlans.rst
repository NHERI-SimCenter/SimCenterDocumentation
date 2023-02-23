.. _lbl-future_pbe:

.. role:: blue

*************
Release Plans
*************

The following features are planned to be developed for upcoming releases of |app|. We are actively working on the features in the next release. Farther development priorities may change depending on feedback from the community. If you have any suggestions, we encourage you to contribute and contact us through the SimCenter Forum.


March 2023
----------
   #. Quantify epistemic uncertainty in structural response by considering multiple models to represent various candidates for events, structural models, or simulation methods (1.2.4.1) - Define weights for each model candidate and propagate epistemic uncertainty by randomly selecting a model for each realization according to these weights.

May 2023
--------
   #. Add datasets to simulate injuries and environmental impacts (1.4.3.1) - Data from Hazus Earthquake and FEMA P58 methodologies will be made available to support these calculations.
   

Sept 2023
----------
   #. New, state-of-the-art surrogate methods - Heteroscedastic Gaussian Process Surrogates (1.2.2.2) - First, train a GP surrogate to capture the mean response, then train another GP surrogate the capture the variance using the residuals. This approach is especially powerful when large differences are observed in the variance of the output in different parts of the input space. 
   #. Efficient forward propagation using Multi-Fidelity Monte-Carlo (1.2.3.1) - Use a few realizations of the output calculated with expensive, high-fidelity models to evaluate and correct the bias in efficient, approximate models, such as surrogates. With little extra computational demands, this method provides a substantial improvement in surrogate model performance if you have the high-fidelity models available that were used to train the surrogates.
   #. Add datasets to simulate subassembly damage and losses under wind demands (1.3.5.1) - Data from recent publications in the Performance-Based Wind Engineering literature is collected to enable high-resolution performance assessment under wind hazard.
      
March 2024
----------
   #. Automatic access to physics-based ground motion simulation results (1.1.1.3)
   #. Add datasets to simulate subassembly damage and losses under water demands (1.3.5.2) 

 .. note::

    The numbers in parentheses are for internal tracking purposes.
