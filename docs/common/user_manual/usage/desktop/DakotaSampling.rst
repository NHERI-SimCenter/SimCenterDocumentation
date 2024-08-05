
.. _lblDakotaForward:

Forward Propagation
**********************************************
 
The forward propagation analysis provides a probabilistic understanding of output variables by producing sample realizations and statistical moments (mean, standard deviation, skewness, and kurtosis) of the quantities of interest. Currently, four sampling methods are available: 

1. **Monte Carlo Sampling (MCS)**
2. **Latin Hypercube Sampling (LHS)**

and sampling based on surrogate models, including: 

3. **Gaussian Process Regression (GPR)**
4. **Polynomial Chaos Expansion (PCE)**

Depending on the option selected, the user must specify the appropriate input parameters. For instance, for MCS, the number of samples specifies the number of simulations to be performed, and providing a seed value for the pseudo-random number generator will produce the same sequence of random numbers allowing the user to reproduce the sampling results multiple times. The user selects the sampling method from the dropdown ``Dakota Method Category`` menu. Additional information regarding sampling techniques offered in Dakota can be found `here <https://snl-dakota.github.io/docs/6.20.0/users/usingdakota/studytypes/uq.html#sampling-methods>`_. 

Monte Carlo Sampling (MCS) 
^^^^^^^^^^^^^^^^^^^^^^^^^^

MCS is among the most robust and universally applicable sampling methods. Moreover, the convergence rate of MCS methods is independent of the problem dimensionality, albeit the convergence rate of such MCS methods is relatively slow at :math:`N^{-1/2}`. In MCS, a sample drawn at any step is independent of all previous samples. 

:numref:`figMCS` shows the input panel corresponding to the Monte Carlo Sampling setting. Two input parameters need to be specified: (1) the number of samples of the output to be produced, which is equal to the number of times the model is evaluated, and (2) the seed for the pseudo-random number generator.

.. _figMCS:

.. figure:: figures/fwMC.png
	:align: center
	:figclass: align-center

  	Monte Carlo Sampling input panel.


Latin Hypercube Sampling (LHS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The conventional Monte Carlo method generates each sample independently, which may produce undesired clusters and gaps between the samples arising from the sampling variability. On the other hand, Latin hypercube sampling (LHS) aims to prevent those gaps and clusters by 'evenly' spreading out the samples throughout the whole input domain. This can significantly reduce the sampling variability and facilitate faster convergence of the probabilistic statistics. In particular, LHS divides the input domain of each variable into N intervals with equal probability and locates the samples such that only one sample lies on each interval. This strategy forces the samples to be more uniformly spread across the domain. In general, LHS is encouraged over MCS as it provides unbiased estimation with a smaller standard error. For example, `this article <https://old.analytica.com/blog/latin-hypercube-vs.-monte-carlo-sampling>`_ suggests that the convergence rate of a sample mean is about quadratically faster with LHS than with Monte Carlo simulation. However, it is noted that one drawback of LHS is that there is no closed-form expression to quantify the error level of the estimators. This means that the user may need to perform multiple batch samplings to quantify the error from the sample variability


.. _figLHS1:

.. figure:: figures/dakota/Sampling_LHS1.png
	:align: center
	:width: 600px
	:figclass: align-center

	Monte Carlo sampling vs. Latin hypercube sampling

:numref:`figLHS2` shows the input panel corresponding to the Latin hypercube sampling (LHS) scheme. Two input parameters need to be specified: (1) the number of samples of the output to be produced, which is equal to the number of times the model is evaluated, and (2) the seed for the pseudo-random number generator.


.. _figLHS2:

.. figure:: figures/fwLHS.png
	:align: center
	:figclass: align-center

	Latin Hypercube Sampling input panel.



Gaussian Process Regression (GPR)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the problems in which computationally expensive models are involved, conventional sampling schemes such as LHS and MCS can be extremely time-consuming. In this case, a surrogate model can be constructed based on a smaller number of simulation runs, and then the surrogate model can be used to efficiently generate a larger number of samples replacing the expensive simulations.

Gaussian Process Regression (GPR), also known as Kriging is one of the well-established surrogate techniques, which constructs an approximated response surface based on Gaussian process modeling and covariance matrix optimizations. :numref:`figGPR` shows the input panel for the GPR model that consists of training and sampling panels. 


.. _figGPR:

.. figure:: figures/fwGP.png
	:align: center
	:figclass: align-center

  	GPR forward propagation input panel.

In the **Surrogate Training Data** panel, the users specify the number of samples of the output of the computationally expensive model to be either Monte Carlo Sampling or Latin Hypercube Sampling to generate sample output values from the computationally expensive model, which, along with the corresponding input values are used to train the surrogate models.

Other surrogate models, different from Gaussian process regression are also available in the drop-down menu titled **Surface Fitting Method**. All these surrogate models utilize either Monte Carlo Sampling or Latin Hypercube Sampling to generate sample output values, which, along with the corresponding input values are used to train the surrogate models. 


Polynomial Chaos Expansion (PCE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Polynomial Chaos Expansion (PCE) is another surrogate model that can replace the expensive simulation model. Similar to the input GPR panel, the input panel for the PCE model shown in :numref:`figPCE` consists of training and sampling parts. The input parameters in the *surrogate training data* set specify the dataset used for training the surrogate model, while the parameters in the *surrogate sampling data* are related to the samples generated using the surrogate. Extreme care must be taken in specifying the parameters of the training dataset to result in an accurate approximation. 


.. _figPCE:

.. figure:: figures/fwPCE.png
	:align: center
	:figclass: align-center

	PCE forward propagation input panel.


If the user is not familiar with the training parameters of the surrogates, it is recommended to refrain from using the surrogates (PCE in particular) and to instead use conventional sampling approaches such as MCS and LHS, despite a higher computational cost. 


