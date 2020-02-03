RV: Random Variables
====================

The RV panel allows the user to specify the probabilistic distribution for the random problem at hand. The following probabilistic distributions for the random variables are currently supported: 

#. `Gaussian <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-normal_uncertain.html>`_
#. `Lognormal <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-lognormal_uncertain.html>`_
#. `Beta <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-beta_uncertain.html>`_
#. `Uniform <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-uniform_uncertain.html>`_
#. `Weibull <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-weibull_uncertain.html>`_
#. `Gumbel <https://dakota.sandia.gov//sites/default/files/docs/6.9/html-ref/variables-gumbel_uncertain.html>`_


Each distribution has different parameters, and the user needs to select accordingly the parameters for the distribution selected for each random variable. Once the user selects the distribution of the random variable, the
corresponding input boxes for the parameters will show. 

:numref:`figRV` shows the panel for a problem with four Random Variables with all random input following Gaussian distributions. 


.. _figRV:

.. figure:: figures/rv.png
   :align: center
   :figclass: align-center

   Random Variable specification
