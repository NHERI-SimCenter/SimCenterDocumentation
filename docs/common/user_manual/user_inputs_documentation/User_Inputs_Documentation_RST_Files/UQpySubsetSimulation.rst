
.. _UQpySubsetSimulation User Inputs:

UQpySubsetSimulation
====================


.. _UQpySubsetSimulation method:

method
	Reliability analysis method to be used

	Default: SubsetSimulation

	Key in JSON file: method


.. _UQpySubsetSimulation Conditional Probabaility:

Conditional Probabaility
	Conditional probability for each conditional level

	Default: 0.1

	Key in JSON file: conditionalProbability


.. _UQpySubsetSimulation Failure Threshold:

Failure Threshold
	Threshold over which it is assume that the simulated system fails

	Default: 0.001

	Key in JSON file: failureThreshold


.. _UQpySubsetSimulation Max. Levels:

Max. Levels
	Maximum number of allowable conditional levels

	Default: 10

	Key in JSON file: maxLevels


.. _UQpySubsetSimulation Initial samples:

Initial samples
	Initial samples to bootstrap the Subset simulation algorithm

	Default: 1000

	Key in JSON file: initialSamples


.. _UQpySubsetSimulation Sampling Method:

Sampling Method
	Specifies the MCMC sampling agorithm to be used 

	Default: MetropolisHastings

	Key in JSON file: samplingMethod

	.. seealso::

		:ref:`MCMC Algorithm <UQpyStretch User Inputs>`



