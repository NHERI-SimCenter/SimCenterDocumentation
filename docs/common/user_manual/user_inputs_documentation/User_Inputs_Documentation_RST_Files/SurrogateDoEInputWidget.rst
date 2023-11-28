
.. _SurrogateDoEInputWidget User Inputs:

SurrogateDoEInputWidget
=======================


.. _SurrogateDoEInputWidget samples:

Number of Samples : *Int*
	When the number of simulation runs reaches the limit, the analysis will be terminated.

	Default: 150

	Key in JSON file: samples


.. _SurrogateDoEInputWidget timeLimit:

Max Computation Time (minutes) : *PositiveDouble*
	When the tolerance limit of the computation time is reached, the analysis will be terminated. There will be a few minutes of error.

	Default: 60

	Key in JSON file: timeLimit


.. _SurrogateDoEInputWidget accuracyLimit:

Target Accuracy (normalized err) : *PositiveDouble*
	The target accuracy is defined in terms of normalized root-mean-squared error (NRMSE) estimated by leave-out-one cross-validation (LOOCV).

	Default: 0.02

	Key in JSON file: accuracyLimit


.. _SurrogateDoEInputWidget seed:

Random Seed : *PositiveInt*
	Seed of the random number generator

	Default: a random integer

	Key in JSON file: seed


.. _SurrogateDoEInputWidget parallelExecution:

Parallel Execution : *Bool*
	This engine implemented multiprocessing (local) or mpi4py (remote) python packages to run parallel execution.

	Default: checked

	Key in JSON file: parallelExecution


.. _SurrogateDoEInputWidget advancedOpt:

Advanced Options for Gaussian Process Model : *Bool*
	If unchecked, default values will be used

	Default: unchecked

	Key in JSON file: advancedOpt


.. _SurrogateDoEInputWidget kernel:

Kernel Function : *ComboBox*
	Correlation function for Gaussian process regression. Matern5/2 function is the default, and Matern3/2, Radial Basis, and Exponential functions (exponent) are additionally supported. 

	Default: Matern5/2

	Key in JSON file: kernel


.. _SurrogateDoEInputWidget linear:

Add Linear Trend Function : *Bool*
	When increasing or decreasing trend is expected over the variables domain, a linear trend function may be introduced. 

	Default: unchecked

	Key in JSON file: linear


.. _SurrogateDoEInputWidget logTransform:

Log-space Transform of QoI : *Bool*
	When the user can guarantee that the response quantities are always greater than 0, user may want to introduce a surrogate model in log-transformed space of QoI. 

	Default: unchecked

	Key in JSON file: logTransform


.. _SurrogateDoEInputWidget DoEmethod:

DoE Options : *ComboBox*
	Design of Experiment method

	Default: none

	Key in JSON file: DoEmethod


.. _SurrogateDoEInputWidget initialDoE:

Initial DoE # : *PositiveInt, optional*
	The number of the initial DoE

	Default: 4 x #RV

	Key in JSON file: initialDoE


.. _SurrogateDoEInputWidget nuggetOpt:

Nugget Variances : *ComboBox*
	User may define nugget variances or bounds of the nugget variances if needed. 

	Default: Optimize

	Key in JSON file: nuggetOpt


.. _SurrogateDoEInputWidget nuggetString:

Nugget Values/Bounds : *IntList or ListList*
	User-defined nugget variances or bounds

	Key in JSON file: nuggetString


.. _SurrogateDoEInputWidget numSampToBeRepl:

# samples to be replicated (A) : *PositiveInt, optional*
	From the number of unique samples specified in the ‘Number of Samples’ field, decide how many of them will have replications.

	Default: 8 x #RV

	Key in JSON file: numSampToBeRepl


.. _SurrogateDoEInputWidget numRepl:

# replications per sample (B) : *PositiveInt, optional*
	Specify how many replications will be generated for the number of samples specified in A.

	Default: 10

	Key in JSON file: numRepl


.. _SurrogateDoEInputWidget existingDoE:

Start with Existing Dataset : *Bool*
	If unchecked, no existing dataset is utilized

	Default: checked

	Key in JSON file: existingDoE


.. _SurrogateDoEInputWidget inpFile:

Training Points (Input RV) : *Str*
	Full path to the file containing training points (samples of RV)

	Key in JSON file: inpFile

	.. seealso::

		:ref:`https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html <>`


.. _SurrogateDoEInputWidget outFile:

System Responses (Output QoI) : *Str*
	Full path to the file containing system responses (samples of QoI) corresponding to the specified training points

	Key in JSON file: outFile

	.. seealso::

		:ref:`https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html <>`


.. _SurrogateDoEInputWidget none:

Advanced Options (Earthquake specific) : *Bool*
	If unchecked, default values will be used

	Default: unchecked

	Key in JSON file: none


.. _SurrogateDoEInputWidget none:

Input postprocess : *ComboBox*
	Ground motion pre-processing for surrogate model training

	Default: Ground Motion Intensity

	Key in JSON file: none


.. _SurrogateDoEInputWidget IntensityMeasure:

IM : *ComboBox*
	The user can select intensity measures (IMs) that will be used as auxiliary inputs of the surrogate model, in addition to those specified in the RV tab.

	Default: Pseudo Spectral Velocity (in/sec)

	Key in JSON file: IntensityMeasure


.. _SurrogateDoEInputWidget Periods:

Periods : *PositiveDouble or PositiveDoubleList*
	Specify period(s) corresponding to IM

	Default: 0.5 or 0.1,1.0,1.5

	Key in JSON file: Periods


.. _SurrogateDoEInputWidget useGeoMean:

Geometric mean : *Bool*
	If ground motions have more than one directional component, either each component’s IM can be added as a separate surrogate input parameter, or they can be aggregated by using their geometric mean. 

	Default: checked

	Key in JSON file: useGeoMean



