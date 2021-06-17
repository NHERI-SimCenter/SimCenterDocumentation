.. _lblSimSurrogate:


Forward Propagation Methods
***************************

The forward propagation analysis provides a probabilistic understanding of output variables by producing sample realizations and statistical moments (mean, standard deviation, skewness, and kurtosis). Currently, only the Monte Carlo Sampling (MCS) method is available in the SimCenterUQ engine and the other sampling methods (Latine hypercube sampling, Gaussian process regression-based efficient sampling) are available in the Dakota engine.


The forward propagation in the SimCenterUQ engine additionally allows the user to import correlated data samples. This feature is especially useful when the user wants to run forward UQ analysis using the posterior samples obtained from Markov Chanin Monte Carlo or other Bayesian sampling approaches. 
