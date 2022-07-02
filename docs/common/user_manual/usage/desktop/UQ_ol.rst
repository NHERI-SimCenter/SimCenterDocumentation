
UQ: Uncertainty Quantification
==============================

The first selection panel the user must select from and enter data into is the **UQ** tab. It is in this panel that the user selects the **UQ Engine** to use for performing the uncertainty quantification calculations. The **UQ Engine** provides algorithms for solving various types of uncertainty analysis and optimization problems. 

.. only:: quoFEM_app
	  
	The **UQ Engine** options currently available are Dakota, SimCenterUQ, and UCSD-UQ. Users can also configure quoFEM to use their own UQ methods and algorithms in the quoFEM workflow by selecting the CustomUQ option.

	**UQ features at-a-glance**:

	.. role:: uqblue

	.. list-table:: 
	   :class: tight-table
	   :widths: 30 10 

	   * - :uqblue:`Forward Propagation`
	         | Forward propagation generates sample realizations of input random variables (RVs) and output quantity of interests (QoIs) to provide statistics such as mean, variance, skewness, and kurtosis. 

			   | * :ref:`lblDakotaForward` in Dakota (:ref:`Example1<qfem-0001>`, :ref:`Example2<qfem-0002>`)
			   | * :ref:`lblSimForward` in SimCenterUQ (:ref:`Example<qfem-0015>`)

	     - .. thumbnail:: figures/UQtab/method_forward.png

	   * - :uqblue:`Global Sensitivity Analysis`
	         | Global sensitivity analysis is used to quantify contribution of each input RV to the uncertainty in an output QoI. Dakota engine provides classical non-parametric estimation based on smart sampling approach and SimCenterUQ engine provides probabilistic model-based approximation. See Dakota user manual and :ref:`here<lbluqSimTechnical>` for theory details.

			   | * :ref:`lblDakotaSensitivity` in Dakota (:ref:`Example<qfem-0001>`)
			   | * :ref:`lblSimSensitivity` in SimCenterUQ (:ref:`Example1<qfem-0009>`, :ref:`Example2<qfem-0023>`)
	     - .. thumbnail:: figures/UQtab/method_sensitivity.png

	   * - :uqblue:`Reliability Analysis`
	         | Reliability Analysis is performed to estimate the probability of failure, i.e. the probability that a system response (QoI) exceeds a certain threshold level. 

			   | * :ref:`lblDakotaReliability` in Dakota (:ref:`Example<qfem-0001>`)
	     - .. thumbnail:: figures/UQtab/method_reliability.png

	   * - :uqblue:`Inverse Problem (Bayesian Calibration)`
	         | Inverse Problem (Bayesian Calibration) is used to calibrate model parameters probabilistically based on Bayesian inference. The probability distributions of the input parameters (RVs) are updated by experimental data. Theory details can be found in Dakota user manual and :ref:`here<lbluqUCSDSimTechnical>`

			   | * :ref:`lblInverseProblem` in Dakota
			   | * :ref:`lblUCSDTMCMC` in UCSD-UQ (:ref:`Example1<qfem-0014>`, :ref:`Example2<qfem-0019>`)
	     - .. thumbnail:: figures/UQtab/method_Bayesian.png

	   * - :uqblue:`Parameter Estimation (Deterministic Calibration)` 
	         | Parameter Estimation (Deterministic Calibration) estimate the best parameter values of a simulation model that best fit the experimental data, using deterministic optimization algorithms, e.g. Gauss-Newton least squares

			   | * :ref:`lblDakotaParameterEstimation` in Dakota (:ref:`Example1<qfem-0007>`, :ref:`Example2<qfem-0019>`)
	     - .. thumbnail:: figures/UQtab/method_deterministic.png

	   * - :uqblue:`Surrogate Modeling`
	         | |app| can be used to train a surrogate model model that substitutes expensive computational simulation models or physical experiments. Theory details can be found in :ref:`here<lbluqSimTechnical>`.

			   | * :ref:`lblSimSurrogate` in SimCenterUQ (:ref:`Example1<qfem-0015>`, :ref:`Example2<qfem-0016>`)
			   | * :ref:`lblSimCenterUQPLoM` in SimCenterUQ

	     - .. thumbnail:: figures/UQtab/method_surrogate.png

	   * - :uqblue:`Custom UQ`
	         | Custom UQ helps user to plug-in an user-defined UQ algorithm in SimCenter workflow.

			   | * :ref:`lblCustomUQ` in CustomUQ engine (:ref:`Example<qfem-0017>`)

	     - .. thumbnail:: figures/UQtab/method_custom.png



.. only:: notQuoFEM
	  
	The **UQ Engine** options currently available are Dakota and SimCenterUQ


Dakota UQ Engine
----------------

This UQ engine utilizes the `Dakota Software <https://dakota.sandia.gov/>`_, a state-of-the-art research application that is robust and provides many methods for optimization and UQ, a selection of which we utilize in this application. **Dakota** provides the user with a large number of methods for different kinds of analyses. For this reason we have divided the methods into categories though a pull-down menu, as shown in :numref:`figDakota`. Once the category has been selected, a number of different methods are made available to the user.

.. _figDakota:

.. figure:: figures/dakotaUQ.png
   :align: center
   :figclass: align-center

   Dakota engine and category selection.

The following categories are available:

.. toctree-filt::
   :maxdepth: 1

   DakotaSampling
   :EEUQ:DakotaSensitivity
   :EEUQ:DakotaReliability
   :Hydro:DakotaSensitivity
   :Hydro:DakotaReliability	 
   :quoFEM:DakotaSensitivity
   :quoFEM:DakotaReliability
   :quoFEM:DakotaParameterEstimation
   :quoFEM:DakotaInverseProblems

.. only:: EEUQ_app
	   
	  SimCenter UQ Engine
	  -------------------
	  
	  The **SimCenterUQ** engine is a UQ engine developed in-house at the SimCenter that accommodates different UQ methods, which are organized into categories that can be accessed through a pull-down menu, as shown in :numref:`figSimCenterUQ`.
	  
	  .. _figSimCenterUQ:
	  
	  .. figure:: figures/SimCenterUQ.png
	  	:align: center
		:figclass: align-center
		
		SimCenterUQ engine and category selection.
	  
	  Currently the following category options are available:

	  .. toctree-filt::
	     :maxdepth: 1

             SimCenterUQSampling
             SimCenterUQSensitivity
             SimCenterUQPLoM

.. only:: quoFEM_app
	   
	  SimCenter UQ Engine
	  -------------------
	  
	  The **SimCenterUQ** engine is a UQ engine developed in-house at the SimCenter that accommodates different UQ methods, which are organized into categories that can be accessed through a pull-down menu, as shown in :numref:`figSimCenterUQ`.
	  
	  .. _figSimCenterUQ:
	  
	  .. figure:: figures/SimCenterUQ.png
	  	:align: center
		:figclass: align-center
		
		SimCenterUQ engine and category selection.
	  
	  Currently the following category options are available:

	  .. toctree-filt::
	     :maxdepth: 1

             SimCenterUQSampling
             SimCenterUQSensitivity
             SimCenterUQSurrogate
             SimCenterUQPLoM


	  UCSD UQ Engine
	  --------------

	  The **UCSD-UQ** engine is a module developed at the SimCenter in collaboration with UCSD. It provides algorithms for Bayesian estimation, which can be accessed through a pull-down menu, as shown in figure :numref:`figUCSDUQ`.
	  
	  .. _figUCSDUQ:
	  
	  .. figure:: figures/UCSDUQ.png
	  	:align: center
		:figclass: align-center
		
		UCSD-UQ engine and category selection.
		
	  This module currently offers support for Bayesian estimation using the Transitional Markov chain Monte Carlo (TMCMC) algorithm:

	  .. toctree-filt::
	     :maxdepth: 1

	     UCSD_UQ_TMCMC

	  Custom UQ Engine
	  ----------------
	  
	  The **CustomUQ** option enables users to switch out the UQ engine in the quoFEM workflow such that different methods and tools can be applied within the SimCenter framework with minimal effort on the part of the user. The CustomUQ option can be accessed as shown in figure :numref:`figCustomUQ`.
	  
	  .. _figCustomUQ:
	  
	  .. figure:: figures/customUQ.png
	  	:align: center
		:figclass: align-center
		
		CustomUQ engine selection.
	
	  In order to use the CustomUQ engine option, two steps are required:
	  
	  * Configuring UQ tab to accept the required inputs
	  * Adding UQ engine to customized UQ backend
	  
	  These steps are described in more detail here:
	  
	  .. toctree-filt::
	  	:maxdepth: 1
		
		Configuring_CustomUQ
