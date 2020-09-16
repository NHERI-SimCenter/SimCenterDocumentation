
.. _lblDamping

Methods in SimCenterUQ Engine 
==============

Variance-based global sensitivity indices
--------------------------------------

Global sensitivity analysis is performed to quantify contribution of each input variable to the uncertainty in QoI. Using the global sensitivity indices, users can set preferences between random variables considering both inherent randomness and its propagation through the model. Global sensitivity analysis helps users to understand the overall impact of different sources of uncertainties, as well as to accelerate UQ computations by focusing on dominant dimensions or screening out trivial input variables.

	
	
Sobol indices are widely used variance-based global sensitivity measures. It has two types: main effect and total effect sensitivity indices. The **main effect index** quantifies the fraction of variance in QoI that can be attributed to specific input random variable(s) but without considering interactive effect with other input variables. The **total effect index**, on the other hand, additionally takes the interactions into account.

Given the output of model :math:`y=g(\boldsymbol{x})` and input random variables :math:`\boldsymbol{x}=\{x_1,x_2, \cdots ,x_d\}`, the first-order main and total effect indices of each input variable is defined as

