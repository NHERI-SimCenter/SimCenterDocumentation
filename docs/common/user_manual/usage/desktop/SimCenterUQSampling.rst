.. _lblSimForward:


Forward Propagation
**********************************************

The forward propagation provides a probabilistic understanding of output variables by producing sample realizations and statistical moments (mean, standard deviation, skewness, and kurtosis). Currently, only the Monte Carlo Sampling (MCS) method is available in the SimCenterUQ engine and the other sampling methods (Latin hypercube sampling, Surrogate model-based efficient sampling) are available in the Dakota engine.


Sampling from dataset
========================

SimCenterUQ uniquely provides an option to define the distribution of random variables (RVs) directly from the samples of the RVs (See :ref:`rv`). This feature is useful when the user does not know the actual distribution of an RV but has sample realizations. When a dataset is provided, quoFEM either treats the data as a discrete distribution (when ``Discrete`` distribution option is selected) or fits a parametric distribution to the data (when another distribution option is selected). For the former case, quoFEM uniformly samples the discrete index of the dataset provided by the user and uses the value corresponding to the index for the forward propagation analysis. The index is sampled either **with** replacement if the data size is smaller than the number of samples to draw or **without** replacement if the data size is larger than the number of samples to draw. Further, when the user provides coupled samples of *correlated* RVs, vector-wise resampling can be performed instead of independent resampling. In particular, a single index is sampled and shared in multiple variables for each realization. 

.. _figSimSamp3:

.. figure:: figures/SimUQ_sampling3.png
	:align: center
	:figclass: align-center
	:width: 1200


Click the check box to import correlated datasets

To enable this feature, the user can explicitly define the group of RVs that will share the index samples in the UQ tab using the ``Resample RVs from correlated dataset``:

	* The actual datasets of the RVs written in this field should be imported in the RV tab, through the ``parameters``-``discrete`` option. 
	* The RVs inside each group should be provided with the same length of the samples (e.g. in :numref:`figSimSamp3`, :math:`w` and :math:`wR` should have the same sample size :math:`N_1` and :math:`alp` and :math:`F_y` should have the same sample size :math:`N_2`)

.. note::
	Any correlation values for this coupled datasets **additionally specified in the RV tab** will be **ignored**. Note that the correlation of the data is already reflected in the analysis by introducing the same resampling index.

For example, consider the case where two variables :math:`w` and :math:`wR` are provided as 10 discrete data points in the RV tab as in :numref:`figSimSamp4`. 


.. _figSimSamp4:

.. figure:: figures/SimUQ_sampling4.png
	:align: center
	:figclass: align-center
	:width: 1200

  	Example RV tab. The RVs :math:`w` and :math:`wR` have the same sample size when they are specified to be coupled as shown in :numref:`figSimSamp3`.

Below is an example of 100 realizations of the two variables when they are considered to be *independent*, i.e. without checking the "Resample RVs from correlated dataset" option.

.. _figSimSamp1:

.. figure:: figures/SimUQ_sampling2.png
	:align: center
	:figclass: align-center
	:width: 1200

  	Example of correlated samples (when the "Resample ..." option in the UQ tab is enabled).

On the other hand, if the two datasets are considered correlated, i.e. if "Resample RVs from correlated dataset" are checked and the group {w,wR} is reported in the field as shown in :numref:`figSimSamp3`, 100 realization pairs of the RVs will be stacked on top of the provided 10 data points.

.. _figSimSamp2:

.. figure:: figures/SimUQ_sampling1.png
	:align: center
	:figclass: align-center
	:width: 1200

  	Example of uncorrelated samples (when the "Resample ..." option in the UQ tab is enabled).

This feature is especially useful when the user wants to perform a forward UQ analysis directly using the posterior samples obtained from Markov Chain Monte Carlo or other Bayesian sampling approaches. 


.. Tip::
	
	Summary of capabilities and limitations

	* :bdg-primary:`o` Run Monte Carlo simulation for 12 different kinds of probability distributions with correlations.
	* :bdg-primary:`o` Use data samples as discrete distribution (especially useful when propagating samples from Bayesian updating)
	* :bdg-danger:`x` Run advanced sampling algorithms including Latin hypercube and surrogate-aided sampling. **[Available in Dakota engine]**


.. only:: quoFEM_app
 
	.. include:: SimCenterUQMF.rst

.. only:: EEUQ_app
 
	.. include:: SimCenterUQMF.rst
