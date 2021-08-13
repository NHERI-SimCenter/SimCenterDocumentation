
UQ: Uncertainty Quantification
==============================

The first selection panel the user must select from and enter data into is the **UQ** tab. It is in this panel where the user selects the **UQ Engine** to use for performing the uncertainty quantification calculations.

.. only:: quoFEM_app
	  
	  Presently the **UQ Engine** option supports Dakota, SimCenterUQ, UCSD-UQ and users' own custom UQ engines.

.. only:: notQuoFEM
	  
	  Presently the only **UQ Engine** option is Dakota.


Dakota UQ Engine
----------------

This UQ engine utilizes the `Dakota Software <https://dakota.sandia.gov/>`_, a state-of-the-art research application that is robust and provides many methods for optimization and UQ, a selection of which we utilize in this application. **Dakota** provides the user with a large number of different methods. For this reason we have divided the methods into categories though a pull-down menu, as shown in :numref:`figDakota`. Once the category has been selected, a number of different methods are made available to the user.

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

.. only:: quoFEM_app
	   
	  SimCenter UQ Engine
	  -------------------
	  
	  The **SimCenterUQ** engine is a UQ engine developed in-house at the SimCenter that accommodates different UQ methods, which are organized into categories that can be accessed through a pull-down menu, as shown in :numref:`figSimCenterUQ`.
	  
	  .. _figSimCenterUQ:
	  
	  .. figure:: figures/SimCenterUQ.png
	  	:align: center
		:figclass: align-center
		
		SimCenterUQ engine and category selection.
	  
	  Currently the category option is limited to global sensitivity analysis:

	  .. toctree-filt::
	     :maxdepth: 1

             SimCenterUQSampling
             SimCenterUQSensitivity
             SimCenterUQSurrogate


	  UCSD UQ Engine
	  --------------

	  The **UCSD-UQ** engine is a module developed at the SimCenter in collaboration with UCSD. It provides algrithms for Bayesian estimation, which can be accessed through a pull-down menu, as shown in figure :numref:`figUCSDUQ`.
	  
	  .. _figUCSDUQ:
	  
	  .. figure:: figures/UCSDUQ.png
	  	:align: center
		:figclass: align-center
		
		UCSD-UQ engine and category selection.
		
	  This module currently offers support for Bayesian estimation using the Transitional Markov chain Monte Carlo (TMCMC) algorithm, which is also known as the Sequential Monte Carlo algorithm:

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
