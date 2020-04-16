.. _lblDakotaParameterEstimation:


Parameter Estimation
********************

Parameter Estimation involves the calculation of the parameters that best fits the experimental results, that is that **minimizes** the QoI, given no prior estimation as to the distribution associaciated with the random variables. As such the processing scripts should leave in the **results.out** file differences between observed response and simulated response. The algorithms employed will find a set of parameters that minimizes these differences. The algorithms themselves are general functional minimization algorithms.

For parameter estimation two different optimization algorithms are currently provided, namely OPT++GaussNewton and NL2SOL:

OPT++
^^^^^

OPT++ Provides a Gauss-Newton least squares capability which, on zero-residual test problems, can exhibit quadratic convergence rates near the solution. As a consequence, a good starting point values for the parameters should be provided. The Hessian is constructed with a Gauss-Newton approximation and the OPT++ Optimization routines are used. 

.. [OPT] 
   J. C. Meza, R. A. Oliva, P. D. Hough, and P. J. Williams, "OPT++: An Object Oriented Toolkit for Nonlinear Optimization", ACM Transactions on Mathematical Software, Volume 33, Number 2, June 2007.

NL2SOL
^^^^^

The NL2SOL method is based on an adaptive nonlinear least-squares algorithm, devised by Dennis and colleagues[Dennis81]. NL2SOL uses a trust region method and adaptivily switches between two Hessian approximations, the Gauss-Newton approximation alone and the Gauss-Newton approximation plus a quasi-Newton approximation to the rest of the Hessian. This later approximation being useful when the starting guess is far from solution. For problems with large number of residuals, this algorithm is known to be more reliable than Gauss-Newton.

.. [Dennis81a]
   J. E. Dennis, D. M. Gay, and R. E. Welsch. An adaptive nonlinear least-squares algorithm. ACM Trans. Math. Softw.. 7(3). 348 - 368. 1981.

.. [Dennis81b]
   J. E. Dennis, D. M. Gay, and R. E. Welsch. Algorithm 573: NL2SOL—An Adaptive Nonlinear Least-Squares Algorithm [E4] ACM Trans. Math. Softw.. 7(3). 369 - 383. 1981.



For both OPT++ and NL2SOL, two input parameters need to be specified: the convergence tolerance and the maximum number of iterations for the optimization subroutine.

.. _figParameterEstimation:

.. figure:: figures/ParameterEstimation.png
	:align: center
	:figclass: align-center

  	Dakota Parameter Estimation Input Panel





