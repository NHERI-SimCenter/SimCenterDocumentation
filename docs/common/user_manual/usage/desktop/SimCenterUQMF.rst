.. _lblSimForwardMF:

Multi-fidelity Monte Carlo
==========================

.. only:: quoFEM_app

   SimCenter UQ supports a multi-fidelity Monte Carlo option, where the user can import both high-fidelity and low-fidelity simulation models to estimate the statistics of high-fidelity models. See more information in the technical manual.

   .. figure:: figures/SimCenterUQ/Sampling_MF1.png
      :align: center
      :width: 900px
      :figclass: align-center

      Multi-fidelity Monte Carlo

   The users should define **Max Computation time** and **Seed**

   * **Max Computation Time (minutes)**: The target computation time for the analysis. Note that this is a "soft" target, meaning the analysis may not necessarily be completed within the specified time limit. The total number of simulations is decided after a few pilot runs of simulations considering the remaining budgets (time), and the process is not enforced to finish even if the target time is exceeded. Therefore, there could be a few minutes of estimation error in the max computation time. Note that, even if the specific time is exceeded, the analysis will not end until the minimum number of specified simulations (default is 40) is reached.
   * **Seed**: a positive integer that is used to reproduce the exact sequence of the pseudo-random number generator. The seed is to ensure the reproducibility of the results.

   Additionally, advanced options can be selected by checking the option at the bottom

   .. figure:: figures/SimCenterUQ/Sampling_MF2_quoFEM.png
      :align: center
      :width: 900px
      :figclass: align-center

      Advanced options

   Using the advanced options, the user can define the minimum number of simulations per model and an option to Perform log-transform

   * **Minimum # simulations per model**: The number of pilot samples. The pilot samples are used to estimate the correlations between the high- and low-fidelity models and decide the optimal number of simulations given the time limit. See here for more details. By default, the minimum number of simulations is 40.
   * **Perform log-transform**: Estimate the mean and variance of the log-transformed value (natural logarithm or :math:`ln()` instead of :math:`log_{10}()`). In |short tool id|, the default is unchecked.
	


.. only:: EEUQ_app

	SimCenter UQ supports a multi-fidelity Monte Carlo option, where the user can import both high-fidelity and low-fidelity simulation models to estimate the statistics of high-fidelity responses. See more information in the :ref:`technical manual<lbluqSimTechnical_MFMC>`.

	.. figure:: figures/SimCenterUQ/Sampling_MF1.png
	   :align: center
	   :width: 900px
	   :figclass: align-center

	   Multi-fidelity Monte Carlo

	The users should define **Max Computation time** and **Seed**

	* **Max Computation Time (minutes)**: The target computation time for the analysis. Note that this is a "soft" target, meaning the analysis may not necessarily be completed within the specified time limit. The total number of simulations is decided after a few pilot runs of simulations considering the remaining budgets (time), and the process is not enforced to finish even if the target time is exceeded. Therefore, there could be a few minutes of estimation error in the max computation time. Note that, even if the specific time is exceeded, the analysis will not end until the specified minimum number of simulations (default is 40) is reached.
	* **Seed**: a positive integer that is used to reproduce the exact sequence of the pseudo-random number generator. The seed is used to ensure the reproducibility of the results.

	Additionally, advanced options can be selected by checking the option at the bottom

	.. figure:: figures/SimCenterUQ/Sampling_MF2_EEUQ.png
	   :align: center
	   :width: 900px
	   :figclass: align-center

	   Advanced options

	Using the advanced options, the user can define the minimum number of simulations per model and choose to get statistics in log-transformed space

	* **Minimum # simulations per model**: The number of pilot samples. The pilot samples are used to estimate the correlations between the high- and low-fidelity models and decide the optimal number of simulations given the time limit. See :ref:`technical manual<lbluqSimTechnical>` for more details. By default, the minimum number of simulations is 40.
	* **Perform log-transform**: Estimate the mean and variance of the log-transformed values (natural logarithm or :math:`log_{e}(\bullet)`). In |short tool id|, the default is **checked**.
	

	.. note::

	   The multiple models should be specified in the SIM and FEM tabs, the lower value of the model index corresponds to a higher fidelity model. Therefore, the high-fidelity model should always be imported as model 1 for both SIM and FEM tabs. The model order in the SIM tab should follow that of the FEM tab. The **Belief** field will be ignored.

