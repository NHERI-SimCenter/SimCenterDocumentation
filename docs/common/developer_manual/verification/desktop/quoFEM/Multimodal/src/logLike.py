import numpy as np


def log_likelihood():
    params = np.loadtxt("results.out")

    log_posterior = -0.1 * params
    log_prior = np.log(1 / (10 * 10))

    log_like = log_posterior - log_prior
    
    return log_like
