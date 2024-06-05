Stochastic Wind
---------------

This option allows users to generate synthetic wind velocity time histories for target wind loading. To do so, the stochastic wind model is selected from the drop-down menu, as shown in :numref:`fig-stochasticwindloading`.

Depending on the model selected, the user will be asked to enter the parameters describing the wind-loading scenario that the synthetic time history should emulate. In the current release, users can only select the model derived by [wittig1975simulation]_.

Additionally, users can provide a seed for stochastic wind generation if they desire the same suite of synthetic time histories to be generated on multiple occasions. If the seed is not specified, a different realization of the time history will be generated for each run based on the input parameters. The backend application that generates the stochastic wind loads relies on ``smelt``, a modular and extensible C++ library for generating stochastic time histories. Users interested in learning more about the implementation and design of ``smelt`` are referred to its `GitHub repository <https://github.com/NHERI-SimCenter/smelt>`_.

All input parameters can be specified as random variables by entering a string in the parameter field. Please note that the information for the
inputs that are identified as random variables need to be provided in the **UQ** panel.

.. _fig-stochasticwindloading:
.. figure:: figures/stochastic_wind_loading.png
	:align: center
	:figclass: align-center

	Stochastic wind loading event.

References

.. [wittig1975simulation] Wittig, L. E. and Sinha, A. K., "Simulation of multicorrelated random processes using the FFT algorithm," The Journal of the Acoustical Society of America, vol. 58 (3), pp. 630-634 (1975)
