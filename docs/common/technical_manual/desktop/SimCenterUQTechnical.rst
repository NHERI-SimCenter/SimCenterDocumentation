

Methods in SimCenterUQ Engine 
*****************************

Nataf transformation
====================

Nataf transformation is introduced to convert the samples in the physical space (X-space) into the standard normal samples (U-space), :math:`T:\rm{X} \rightarrow \rm{U}`, and vice versa, during UQ computations ([Liu_1986]_). Specifically, the latter transformation, called inverse Nataf :math:`T^{-1}`, is performed each time when UQ engine generates sample points and calls external workflow applications, so that the main UQ algorithms would face only the standard normal random variables. Among various standardization transformations, Nataf is one of the most popular methods which exploits **marginal distributions** of each physical variables and their **correlation coefficients**.

.. _figNataf1:

.. figure:: figures/SimCenterNataf1.png
   :align: center
   :figclass: align-center

   Standardization of random variables using Nataf transformation

For the Nataf trasformation, the SimCenterUQ engine borrows a part of the distribution class structure developed by ERA group in the Technical University of Munich [ERA_2019]_ 

.. [Liu_1986]
   Liu, P.L. and Der Kiureghian, A. (1986). Multivariate distribution models with prescribed marginals and covariances. *Probabilistic Engineering Mechanics*, 1(2), 105-112.

.. [ERA_2019]
   Engineering Risk Analysis Group, Technische Universität München: https://www.bgu.tum.de/era/software/eradist/ (Matlab, python programs and documentations)


Global sensitivity analysis
===========================

Variance-based global sensitivity indices
-----------------------------------
Global sensitivity analysis (GSA) is performed to quantify the contribution of each input variable to the uncertainty in QoI. Using the global sensitivity indices, users can set preferences between random variables considering both inherent randomness and its propagation through the model. GSA helps users to understand the overall impact of different sources of uncertainties, as well as to accelerate UQ computations by focusing on dominant dimensions or screening out trivial input variables.

.. _figSensitivity1:

.. figure:: figures/SimCenterSensitivity1.png
   :align: center
   :figclass: align-center

   Concept of global sensitivity analysis
	
	
Sobol indices are widely used variance-based global sensitivity measures. It has two types: main effect and total effect sensitivity indices. The **main effect index** finds the fraction of variance in QoI that can be attributed to specific input random variable(s) but without considering interactive effect with other input variables. The **total effect index**, on the other hand, additionally takes the interactions into account.

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
	
where :math:`\boldsymbol{x}_{\sim ij}` indicates the set of all input variables except :math:`x_i` and :math:`x_j`. The higher-order indices are derived likewise. Theoretically, When all the input variables are uncorrelated to each other, the following equality holds.

.. math::

	\sum^d_{i=1} S_i + \sum^d_{i<j} S_{ij} + \cdots + S_{12 \cdots d} = 1 


Estimation of Sobol indices
----------------------------

GSA is typically computationally expensive. High computation cost attributes to the multiple integrations (:math:`d`-dimensional) associated with the variance and expectation operations shown in Eqs. :eq:`Si` and :eq:`SiT`. To reduce the computational cost, efficient Monte Carlo methods, stochastic expansion methods, or meta model-based methods can be employed. Among different approaches, the SimCenterUQ engine supports the probability model-based GSA (PM-GSA) framework developed by [Hu_2019]_. 

The framework first conducts ordinary MCS to obtain input-output data pairs. Then by extracting only a subset dimension of the dataset, the probability distribution of a reduced dimension can be approximated and used for estimating the Sobol index. Among different probability distribution models introduced in [Hu_2019]_  the Gaussian mixture model is implemented in this engine to approximate this lower dimension distribution. For example, to identify 1st order main Sobol index for a variable :math:`x_i`, a bivariate Gaussian mixture model is fitted for the joint probability distribution of :math:`x_i` and :math:`y`, i.e.

.. math::
	:label: GM

	f_{x_i,y}(x_i,y) \simeq f_{x_i,y}^{GM} (x_i,y)
	

using expectation-maximization (EM) algorithm. The mean operation Eq. :eq:`Si` is then derived analytically from the Gaussian mixture model, while variance is approximated to be the sample variance. Therefore, the accuracy of the method depends on the quality of the base samples as well as the fitness of the mixture model. The below figure summarizes the procedure of Gaussian mixture model-based PM-GSA introduced in [Hu_2019z]_. The number of mixture components is optimized along with the mixture parameters during expectation-maximization iterations. 

.. _figSensitivity2:

.. figure:: figures/SimCenterSensitivity2.png
	:align: center
	:figclass: align-center

  	Data-driven global sensitivity analysis by Hu and Mahadevan (2019)

.. [Hu_2019]
   Hu, Z. and Mahadevan, S. (2019). Probability models for data-driven global sensitivity analysis. *Reliability Engineering & System Safety*, 187, 40-57.

