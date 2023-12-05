
.. _SurrogateDoEInputWidget User Inputs:

SurrogateDoEInputWidget
=======================


.. _SurrogateDoEInputWidget Number of Samples:

Number of Samples
	When the number of simulation runs reaches the limit, the analysis will be terminated.

	Default: 150

	Key in JSON file: samples


.. _SurrogateDoEInputWidget Max Computation Time (minutes):

Max Computation Time (minutes)
	When the tolerance limit of the computation time is reached, the analysis will be terminated. There will be a few minutes of error.

	Default: 60

	Key in JSON file: timeLimit


.. _SurrogateDoEInputWidget Target Accuracy (normalized err):

Target Accuracy (normalized err)
	The target accuracy is defined in terms of normalized root-mean-squared error (NRMSE) estimated by leave-out-one cross-validation (LOOCV).

	Default: 0.02

	Key in JSON file: accuracyLimit


.. _SurrogateDoEInputWidget Random Seed:

Random Seed
	Seed of the random number generator

	Default: a random integer

	Key in JSON file: seed


.. _SurrogateDoEInputWidget Parallel Execution:

Parallel Execution
	This engine implemented multiprocessing (local) or mpi4py (remote) python packages to run parallel execution.

	Default: checked

	Key in JSON file: parallelExecution


.. _SurrogateDoEInputWidget Advanced Options for Gaussian Process Model:

Advanced Options for Gaussian Process Model
	If unchecked, default values will be used

	Default: unchecked

	Key in JSON file: advancedOpt


.. _SurrogateDoEInputWidget Kernel Function:

Kernel Function
	Correlation function for Gaussian process regression. Matern5/2 function is the default, and Matern3/2, Radial Basis, and Exponential functions (exponent) are additionally supported. 

	Default: Matern5/2

	Key in JSON file: kernel


.. _SurrogateDoEInputWidget Add Linear Trend Function:

Add Linear Trend Function
	When increasing or decreasing trend is expected over the variables domain, a linear trend function may be introduced. 

	Default: unchecked

	Key in JSON file: linear


.. _SurrogateDoEInputWidget Log-space Transform of QoI:

Log-space Transform of QoI
	When the user can guarantee that the response quantities are always greater than 0, user may want to introduce a surrogate model in log-transformed space of QoI. 

	Default: unchecked

	Key in JSON file: logTransform


.. _SurrogateDoEInputWidget DoE Options:

DoE Options
	Design of Experiment method

	Default: none

	Key in JSON file: DoEmethod


.. _SurrogateDoEInputWidget Initial DoE #:

Initial DoE #
	The number of the initial DoE

	Default: 4 x #RV

	Key in JSON file: initialDoE


.. _SurrogateDoEInputWidget Nugget Variances:

Nugget Variances
	User may define nugget variances or bounds of the nugget variances if needed. 

	Default: Optimize

	Key in JSON file: nuggetOpt


.. _SurrogateDoEInputWidget Nugget Values/Bounds:

Nugget Values/Bounds
	User-defined nugget variances or bounds

	Key in JSON file: nuggetString


.. _SurrogateDoEInputWidget # samples to be replicated (A):

# samples to be replicated (A)
	From the number of unique samples specified in the 'Number of Samples' field, decide how many of them will have replications.

	Default: 8 x #RV

	Key in JSON file: numSampToBeRepl


.. _SurrogateDoEInputWidget # replications per sample (B):

# replications per sample (B)
	Specify how many replications will be generated for the number of samples specified in A.

	Default: 10

	Key in JSON file: numRepl


.. _SurrogateDoEInputWidget Start with Existing Dataset:

Start with Existing Dataset
	If unchecked, no existing dataset is utilized

	Default: checked

	Key in JSON file: existingDoE


.. _SurrogateDoEInputWidget Training Points (Input RV):

Training Points (Input RV)
	Full path to the file containing training points (samples of RV)

	Key in JSON file: inpFile

	.. seealso::

		`Training Points File Format <https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html>`_


.. _SurrogateDoEInputWidget System Responses (Output QoI):

System Responses (Output QoI)
	Full path to the file containing system responses (samples of QoI) corresponding to the specified training points

	Key in JSON file: outFile

	.. seealso::

		`System Responses File Format <https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html>`_


.. _SurrogateDoEInputWidget Advanced Options (Earthquake specific):

Advanced Options (Earthquake specific)
	If unchecked, default values will be used

	Default: unchecked

	Key in JSON file: none


.. _SurrogateDoEInputWidget Input postprocess:

Input postprocess
	Ground motion pre-processing for surrogate model training

	Default: Ground Motion Intensity

	Key in JSON file: none


.. _SurrogateDoEInputWidget IM:

IM
	The user can select intensity measures (IMs) that will be used as auxiliary inputs of the surrogate model, in addition to those specified in the RV tab.

	Default: Pseudo Spectral Velocity (in/sec)

	Key in JSON file: IntensityMeasure


.. _SurrogateDoEInputWidget Periods:

Periods
	Specify period(s) corresponding to IM

	Default: 0.5 or 0.1,1.0,1.5

	Key in JSON file: Periods


.. _SurrogateDoEInputWidget Geometric mean:

Geometric mean
	If ground motions have more than one directional component, either each component's IM can be added as a separate surrogate input parameter, or they can be aggregated by using their geometric mean. 

	Default: checked

	Key in JSON file: useGeoMean



