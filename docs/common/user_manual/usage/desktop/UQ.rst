

UQ: Uncertainty Quantification
==============================

The first selection panel the user must select from and enter data into is the **UQ** panel. It is this panel where the user selects from the UQ_Engine to use to perform the uncertainty quantification calculuations. Presently the UQ_engine option is limited to The **Dakota Engine** or a user provided **Other**.

Dakota UQ Engine
----------------

This engine utilizes the `Dakota Software <https://dakota.sandia.gov/>`_, a state-of-the-art research and robust, usable software application for optimization and UQ. **Dakota** provides a number of methods which we divide into the following categories though th pull-down menu:

.. toctree-filt::
   :maxdepth: 1

   DakotaSampling
   :quoFEM:DakotaSensitivity
   :quoFEM:DakotaReliability
   :quoFEM:DakotaParameterEstimation
   :quoFEM:DakotaInverseProblems