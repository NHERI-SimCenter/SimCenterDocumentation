from scipy.stats import multivariate_normal as mvn
from scipy.stats import norm
import numpy as np


def log_likelihood():
    mu = np.array([0, 0])
    cov = np.diag([100, 1])
    params = np.loadtxt("results.out")
    vec = np.array(params).reshape(2, ) - mu
    a = mvn(mean=mu, cov=cov)
    log_posterior = a.logpdf(vec)

    uniform = False
    if uniform:
        log_prior = np.log(1 / (60 * 60))
    else:
        prior_mu = np.array([0, 100])
        prior_cov = np.diag([400, 400])
        prior_norm = mvn(mean=prior_mu, cov=prior_cov)
        log_prior = prior_norm.logpdf(vec)

    log_like = log_posterior - log_prior
    return log_like
