.. _lblDakotaSensitivity:


Global Sensitivity Analysis
***************************

``******This section is being modified -- SY******``

Global sensitivity analysis is used to quantify contribution of each input variable to the uncertainty in QoI. Using the global sensitivity indices, users can set preferences between random variables considering both inherent randomness and its propagation through the model. Global sensitivity analysis helps users to understand the overall impact of different sources of uncertainties and their intersections, as well as to accelerate UQ computations by focusing on dominant dimensions or screening out trivial input variables. This can also be useful identifying the input variables for which extra experimentation/research may be useful in reducing the uncertainty in the initial specification.

**Sobol indices** are widely used variance-based global sensitivity measures which has two types: main effect and total effect sensitivity indices. The **main effect index** quantifies the fraction of variance in QoI that can be attributed to specific input random variable(s) but without considering interactive effect with other input variables. The **total effect index**, on the other hand, additionally takes the interactions into account.

Given the output of model :math:`y=g(\boldsymbol{x})` and input random variables :math:`\boldsymbol{x}=\{x_1,x_2, \cdots ,x_d\}`, the first-order main and total effect indices of each input variable is defined as

.. _figSensitivity:

.. figure:: figures/SensitivityAnalysisSimUQ.png
	:align: center
	:figclass: align-center

  	Sensitivity analysis input panel.
	
	
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
	:label: Sbound

	\sum^d_{i=1} S_i + \sum^d_{i<j} S_{ij} + \cdots + S_{12 \cdots d} = 1 

When correlation is not zero, the value may be greater or smaller than one.

In SimCenterUQ engine, Sensitivity indices are estimated by Gaussian mixture model-based probability distribution approximation framework presented in Hu and Mahadevan (2018) [Hu19]_. The user has to specify the number of samples and a seed. 


In the bottom of QoI panel, user may activate the option to specify advanced outputs. By default, the analysis results are first-order sensitivity indices of each random variable. By manually specifying groups of the random variables in this option, user can get group-wise Sobol indices. It is particularly useful when user wants to obtain sensitivity measure corresponding to categorized groups (e.g. separating to each structural and excitation properties) or when user expects interacted contribution of random variables those which in nature cannot be separated.



.. _figSensitivity2:

.. figure:: figures/SensitivityAnalysis2SimUQ.png
	:align: center
	:figclass: align-center

  	Group-wise sobol indicies
	

.. note::

   - The numerical results of global sensitivity analysis may show negative values due to the sampling variability.
   - The numerical results of Eq. :eq:`Sbound` may not hold due to the sampling variability and approximation errors. If this error is high, the sensitivity index may not be accurate. However, the rank between variable is relatively robust, so that it provides useful informations.

.. note::

   - When multiple outputs are considered, global sensitivity analysis is done separately for each QoI. 
   - When constant variable is defined, sensitivity analysis will ignore the variable.
   - When random variables defined in RV panel is not sufficient, i.e. if model contains additional randomness, total Sobol index value may be underestimated by omitting the intersections with the missing variable informations.

.. warning::
   - When number of variable increase, the approximation may not be accurate. In such cases, caution should be taken checking the validity of results


.. [Hu19]
   Hu, Z. and Mahadevan, S. (2019). Probability models for data-driven global sensitivity analysis. *Reliability Engineering & System Safety*, 187, 40-57.

