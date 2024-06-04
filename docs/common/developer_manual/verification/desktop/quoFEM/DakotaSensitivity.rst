.. _lblDakotaSensitivityVeri:

Global Sensitivity Analysis (Dakota)
=====================================

Global Sensitivity Analysis in Dakota Engine is based on Eqs. (8) and (9) of [Weirs12]_. Using the raw analysis samples shown in "RES" tab - "Data Values" tab after running a sensitivity analysis, one can reproduce the sensitivity indices as follows. 

According to [Weirs12]_, the main and total Sobol indices of :math:`i`-th random variable for a quantity of interest (QoI) are computed by

.. math::
   :label: Si
   
   S_i=\frac{\frac{1}{n}\sum^n_{j=1} f(\boldsymbol{A})_j (  f(\boldsymbol{B_A}^{(i)})_j - f(\boldsymbol{B})_j ) }{ \frac{1}{2n}\sum^{2n}_{j=1} f(\boldsymbol{C})_j f(\boldsymbol{C})_j  - <f(\boldsymbol{C})>^2}
   

.. math::
   :label: STi
   
   S^T_i=\frac{\frac{1}{2n}\sum^n_{j=1} (  f(\boldsymbol{B})_j - f(\boldsymbol{B_A}^{(i)})_j )^2 }{ \frac{1}{2n}\sum^{2n}_{j=1} f(\boldsymbol{C})_j f(\boldsymbol{C})_j  - <f(\boldsymbol{C})>^2}
   
See [Weirs12]_ for notation details. Note that, the second formulation looks slightly different from Eq. (9) of the original paper, becuase :math:`\boldsymbol{A}` is switched with :math:`\boldsymbol{B}`. This is to reuse :math:`f(\boldsymbol{B_A}^{(i)})` in the main index for computing the total index.

To reproduce the main and total sensitivity indices of :math:`i`-th random variable, one can substitute :math:`n` with the simulation number specified in the user interface, :math:`f(\boldsymbol{A})` with the vector of first :math:`n` QoI sample values (sample id from :math:`1` to :math:`n`), :math:`f(\boldsymbol{B})` with that of subsequent :math:`n` QoI samples (sample id from :math:`n+1` to :math:`2n`), and :math:`f(\boldsymbol{B_A}^{(i)})` with that of sample id from :math:`(i+1)n+1` to :math:`(i+2)n`.

.. [Weirs12]
   V. G. Weirs, J. R. Kamm, L. P. Swiler, M. Ratto, S. Tarantola, B. M. Adams, W. J. Rider, and M. S Eldred. Sensitivity analysis techniques applied to a system of hyperbolic conservation laws. *Reliability Engineering and System Safety*, 107:157–170, 2012
