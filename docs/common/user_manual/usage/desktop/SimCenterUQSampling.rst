.. _lblSimSurrogate:


Forward Propagation Methods
***************************

The forward propagation analysis provides probabilistic understanding of output variables by producing sample realizations and statistical moments (mean, standard deviation, skewness, and kurtosis). Currently only the Monte Carlo Sampling (MCS) method is available in SimCenterUQ engine and for the other sampling methods (Latine hyper cube sampling, Gaussian process regression-based efficient sampling) are available in Dakota engine.


Forward propagation in simcenter UQ engine additionally allows users to import ordered (tupled) dataset. It can be especially useful when user has samples of posterior distribution from Markov Chanin Monte Carlo or other Bayesian sampling approach. 
