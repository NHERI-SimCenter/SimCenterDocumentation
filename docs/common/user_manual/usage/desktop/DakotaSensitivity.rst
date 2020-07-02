.. _lblDakotaSensitivity:


Global Sensitivity Analysis
***************************

Sensitivity analysis provides information on how uncertainty in the output can be divided/allocated to the uncertainties in the inputs.
It is used to identify most important input variables that influence the model response and their interactions. This can be useful for down-selecting the random variables to use in forward propagation problems, and identifying the input variables for which extra experimentation/research may be useful in reducing the uncertainty in the initial specification.

For Sensitivity Analysis the user has two options to generate the samples on which the statistics are created: Monte Carlo, and Latin Hypercube Sampling (LHS). For both they are required, as shown in figure below, to specify the number of samples and a seed.

.. _figSensitivity:

.. figure:: figures/SensitivityAnalysis.png
	:align: center
	:figclass: align-center

  	Sensitivity analysis input panel.
	
	
Introduction
-------------
Global sensitivity analysis quantifies the contribution of each input variable to the uncertainty in QoI. Using the global sensitivity indices, users can set preferences between random variables considering both inherent randomness and its propagation through the model. Global sensitivity analysis helps users to understand the overall impact of different sources of uncertainties, as well as to accelerate UQ computations by focusing on dominant dimensions or screening out trivial input variables.

.. _figSensitivity2:

.. figure:: figures/SensitivityAnalysis2.png
	:align: center
	:figclass: align-center

  	Concept of global sensitivity analysis
	
	
Sobol indices are widely used variance-based global sensitivity measures. It has two types: main effect and total effect sensitivity indices. The **main effect index** quantifies the fraction of variance in QoI that can be attributed to specific input random variable(s) but without considering interactive effect with other input variables. The **total effect index**, on the other hand, additionally takes the interactions into account.

Given the output of model :math:`y=g(\boldsymbol{x})` and input random variables :math:`\boldsymbol{x}=\{x_1,x_2, \cdots ,x_d\}`, the first-order main and total effect indices of each input variable is defined as


.. math::
	:label: Si
	
	S_i=\frac{\text{Var}_{x_i}[\text{E}_{\boldsymbol{x}_{\sim i}}[y|x_i]]}{\text{Var}[y]}, \qquad i=1, \cdots ,d
	
   
.. math::
	:label: SiT

	S_i^T=\frac{\text{E}_{\boldsymbol{x}_{\sim i}}[\text{Var}_{x_i}[y|\boldsymbol{x}_{\sim i}]]}{\text{Var}[y]},  \qquad  i=1, \cdots ,d


respectively, where :math:`\boldsymbol{x}_{\sim i}` indicates the set of all input variables except :math:`x_i`. It is noteworthy that in both equations, the variance operator :math:`\text{Var}_{x_i}[\cdot]` captures only the part of uncertainty associated with :math:`x_i`, while the mean operator :math:`\text{E}_{\boldsymbol{x}_{\sim i}}[\cdot]` averages out all remaining uncertainties. From the definitions, two indices theoretically have values between zero and one. Eq. :eq:`Si` can also be understood intuitively. For example, if the QoI is insensitive to :math:`x_i`, the term inside :math:`\text{Var}_{x_i}[\cdot]` is nearly constant and :math:`S_i` approaches zero. On the other hand, when one single variable :math:`x_i` dominates QoI, inside :math:`\text{Var}_{x_i}[\cdot]` is approximately the same as :math:`y`, and thus :math:`S_i` approaches one. Eq. :eq:`SiT` can be understood in similar ways. The second-order main effect index that provides the pair-wise interaction effect is defined as

.. math::
	:label: Sij

	S_{ij}=\frac{\text{Var}_{x_i,x_j}[\text{E}_{\boldsymbol{x}\sim ij}[y|x_i,x_j]]}{\text{Var}[y]} - S_i - S_j,  \qquad  i,j=1, \cdots ,d
	
where :math:`\boldsymbol{x}_{\sim ij}` indicates the set of all input variables except :math:`x_i` and :math:`x_j`. The higher-order indices are derived likewise. When all the input variables are uncorrelated to each other, the following equality holds.

.. math::

	\sum^d_{i=1} S_i + \sum^d_{i<j} S_{ij} + \cdots + S_{12 \cdots d} = 1 


Estimation of variance-based global sensitivity indices
--------------------------------------------------------

Typically, global sensitivity analysis requires high simulation cost. It attributes to the multiple integrations (:math:`d`-dimensional) associated with variance and expectation operations shown in Eqs. :eq:`Si` and :eq:`SiT`. To reduce the computational cost, efficient Monte Carlo methods, stochastic expansion methods, or meta model-based methods can be employed. 

**(Explanation of GSA approach we are implementing)**



.. _figSensitivity3:

.. figure:: figures/SensitivityAnalysis3.png
	:align: center
	:figclass: align-center

  	Data-driven global sensitivity analysis by Hu and Mahadevan (2019)


.. [NOTE]
   - The numerical results of global sensitivity analysis may show negative values due to the sampling variability.
   - When multiple outputs are considered, global sensitivity analysis is done separately for each QoI. 

.. [CITATION]
   Hu, Z. and Mahadevan, S. (2019). Probability models for data-driven global sensitivity analysis. *Reliability Engineering & System Safety*, 187, 40-57.

