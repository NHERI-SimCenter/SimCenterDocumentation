
.. _UQpyStretch User Inputs:

UQpyStretch
===========


.. _UQpyStretch burn length:

burn length
	Burn length of the Markov Chain Monte Carlo algorithm

	Default: 0

	Key in JSON file: burn_in


.. _UQpyStretch jump:

jump
	Jump parameter of the Markov Chain Monte Carlo sampling

	Default: 1

	Key in JSON file: jump


.. _UQpyStretch method:

method
	String that defines the MCMC algorithm to be used

	Default: ModifiedMetropolisHastings

	Key in JSON file: method


.. _UQpyStretch # Chains:

# Chains
	Number of chains to be used in the MCMC sampling algorithm

	Default: 1

	Key in JSON file: n_chains


.. _UQpyStretch # Dimension:

# Dimension
	Number of parameters to be sampled

	Default: 1

	Key in JSON file: n_dimension


.. _UQpyStretch Scale:

Scale
	Parameter specific to the Stretch sampling aglorithm

	Default: 2

	Key in JSON file: scale



