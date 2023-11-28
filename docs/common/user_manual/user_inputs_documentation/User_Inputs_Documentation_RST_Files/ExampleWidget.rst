
.. _ExampleWidget User Inputs:

ExampleWidget
=============


.. _ExampleWidget compound_widget:

Compound Widget
	Follow the link for a description of the inputs to Compound Widget

	Key in JSON file: compound_widget

	.. seealso::

		:ref:`Compound Widget <UCSD_InputTMCMC User Inputs>`
			User inputs for Compound Widget


.. _ExampleWidget sample_size:

Sample Size
	Number of samples from the posterior probability distribution

	Default: 2000

	Constraints: gt=0

	Key in JSON file: sample_size


.. _ExampleWidget seed:

Seed
	State of pseudo-random number generator for reproducibility

	Constraints: ge=0

	Key in JSON file: seed

	.. seealso::

		:ref:`seed <UCSD_InputTMCMC seed>`
			Compare with this parameter too


.. _ExampleWidget calibration_data_file:

Calibration Data File
	Full path to the file containing the calibration data

	Key in JSON file: calibration_data_file


.. _ExampleWidget log_likelihood_script:

Log Likelihood Script
	Full path to the file containing the log-likelihood function

	Default: probability density of multivariate normal with independent components

	Key in JSON file: log_likelihood_script

	.. seealso::

		:ref:`log_likelihood_script <UCSD_InputTMCMC log_likelihood_script>`
			This is also relevant to this parameter and adds some context 


.. _ExampleWidget dummy:

Dummy Variable
	This is a dummy variable

	Default: check_default

	Constraints: check_constraint

	Key in JSON file: dummy


.. seealso::

	`Defining the log-likelihood function <https://nheri-simcenter.github.io/quoFEM-Documentation/common/user_manual/usage/desktop/UCSD_UQ_TMCMC.html#defining-the-log-likelihood-function>`_
		Can link to external webpages too

	`Calibration data file <https://nheri-simcenter.github.io/quoFEM-Documentation/common/user_manual/usage/desktop/UCSD_UQ_TMCMC.html#usage>`_
		Look at the requirements of how to define the calibration data file



