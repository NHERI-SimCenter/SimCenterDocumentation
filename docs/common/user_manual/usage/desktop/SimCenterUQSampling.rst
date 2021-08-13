.. _lblSimSurrogate:


Forward Propagation Methods
***************************

The forward propagation analysis provides a probabilistic understanding of output variables by producing sample realizations and statistical moments (mean, standard deviation, skewness, and kurtosis). Currently, only the Monte Carlo Sampling (MCS) method is available in the SimCenterUQ engine and the other sampling methods (Latin hypercube sampling, Gaussian process regression-based efficient sampling) are available in the Dakota engine.


.. _figSimSamp3:

.. figure:: figures/SimUQ_sampling3.png
	:align: center
	:figclass: align-center

  	UQ panel: Import correlated dataset.

The forward propagation in the SimCenterUQ engine additionally allows the user to import correlated data samples, i.e. N correlated dataset from the datasheet will be considered as N-tuple and it's index will be uniformly sampled without replacement. The tuples are imported in the RV tab, through **parameters-discrete** option using drop down menu. RVs inside each same group should be provided with the same length of the samples. 


.. _figSimSamp4:

.. figure:: figures/SimUQ_sampling4.png
	:align: center
	:figclass: align-center

  	RV panel.

.. note::
	If the direct tuple resampling is introduced, correlation value will be ignored. But if the 

For example, consider the case where two variables (w and wR) are provided as 10 discrete datasets in RV tab, below is the an example realization of 100 samples when they are considered to be independent

.. _figSimSamp1:

.. figure:: figures/SimUQ_sampling1.png
	:align: center
	:figclass: align-center

  	Correlated samples.

If the samples are considered to be tuples, 100 sample pairs will be stacked on top of provided 10 samples.

.. _figSimSamp2:

.. figure:: figures/SimUQ_sampling2.png
	:align: center
	:figclass: align-center

  	Uncorrelated samples.

This feature is especially useful when the user wants to perform forward UQ analysis directly using the posterior samples obtained from Markov Chain Monte Carlo or other Bayesian sampling approaches. 
