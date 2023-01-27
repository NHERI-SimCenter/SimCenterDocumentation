.. _lbl-future_ee:

.. role:: blue

*************
Release Plans
*************

The following features are planned to be developed for upcoming releases of |app|. We are actively working on the features in the next release. Farther development priorities may change depending on feedback from the community. If you have any suggestions, we encourage you to contribute and contact us through the SimCenter Forum.

Febuary 2023
------------
   #. Quantify epistemic uncertainty in structural response by considering multiple models to represent various candidates for events, structural models, or simulation methods (1.2.4.1) - Define weights for each model candidate and propagate epistemic uncertainty by randomly selecting a model for each realization according to these weights.
   #. Use any simulation engine with the CustomPy feature - CustomPy allows you to execute a Python script that can serve as a wrapper for any other application. After preparing a wrapper, you can take leverage the applications in the SimCenter backend while running the FEM engine of your choice - OpenSeesPy, ETABS, Perform3D, ANSYS, Abaqus, etc.

      
Sept 2023
---------
   #. New, state-of-the-art surrogate methods - Heteroscedastic Gaussian Process Surrogates (1.2.2.2) - First, train a GP surrogate to capture the mean response, then train another GP surrogate the capture the variance using the residuals. This approach is especially powerful when large differences are observed in the variance of the output in different parts of the input space. 
   #. Automatically generate ground motion records that represent a pre-defined intensity-measure input space - Select IMs and corresponding ranges of interest and select ground motions that cover the specified IM space. Such ground motion sets are helpful to train general-purpose surrogate models.
   #. Train and export surrogates for regional simulations (1.3.6.1) - Surrogates developed in EE_UQ can be exported, shared, and directly used to represent structural behavior in large regional seismic risk assessments in R2D.

      

March 2024
----------
   #.  Automatic access to physics-based ground motion simulation results (1.1.1.3)


 .. note::

    The numbers in parentheses are for internal tracking purposes.
