.. _rv:


RV: Random Variables
====================

The **RV** tab allows the user to specify the probabilistic distribution for the random problem at hand. The following probabilistic distributions for the random variables are currently supported: 

Probability distribution
------------------------

.. note::

   To add a new random variable the user presses the **Add** button. To remove a random variable, the user must first select it by checking the small circle before the random variable, and then pressing the **Remove** button.


Dakota Engine
+++++++++++++

The following six distribution classes are supported for Dakota engine.

1. `Normal (Gaussian) <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-normal_uncertain.html>`_

   User provides the mean (:math:`\mu`) and standard deviation (:math:`\sigma`) of the normal distribution. The density function of the normal distribution, as a function of :math:`\mu` and :math:`\sigma` is:

   .. math::

      f(x) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( -{\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^2} \right)


2. `Lognormal <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-lognormal_uncertain.html>`_



   User provides the mean (:math:`\mu`) and standard deviation (:math:`\sigma`) of the lognormal distribution. The density function of the lognormal distribution, as a function of :math:`\mu` and :math:`\sigma` is:

   .. math::

      f(x) = \frac{1}{\sqrt{2 \pi} \zeta x} \exp \left( -{\frac{1}{2} \left( \frac{\ln x - \lambda}{\zeta} \right)^2} \right)

  where :math:`\zeta^2 = \ln \left( \frac{\sigma^2}{\mu^2} + 1 \right)` and :math:`\lambda = \ln(\mu) - \frac{\zeta^2}{2}`


3. `Beta <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-beta_uncertain.html>`_


   User provides :math:`\alpha`, :math:`\beta`, lower bound (:math:`L_B`), and an upper bound (:math:`U_B`) for the beta distribution. The density function of the normal distribution, as a function of these quantities is:

   .. math::

      f(x) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} \frac{(x - L_B)^{\alpha-1}(U_B-x)^{\beta-1}}{(U_B - L_B)^{\alpha + \beta - 1}}


   where :math:`\Gamma(\alpha)` is the `Gamma function <http://mathworld.wolfram.com/GammaFunction.html>`_.



4. `Uniform <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-uniform_uncertain.html>`_


   User provides the lower bound (:math:`L_B`), and an upper bound (:math:`U_B`) for the uniform distribution. The density function of the normal distribution, as a function of these quantities is:

   .. math::

      f(x) = \frac{1.0}{(U_B - L_B)}

   The mean of the distribution is :math:`\frac{(U_B + L_B)}{2.0}`

5. `Weibull <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-weibull_uncertain.html?highlight=weibull>`_


   User provides shape parameter (:math:`k`) and scale parameter (:math:`a_n`)  for the Weibull distribution. The density function of the Weibull distribution, as a function of these quantities is:

   .. math::

      f(x) = \frac{k}{a_n}\left(\frac{x}{a_n}\right)^{k-1} \exp \left( -(x/a_n)^{k} \right)

   where :math:`k,a_n > 0` and :math:`x \geq 0`. For :math:`x<0`, :math:`f(x) = 0`.


6. `Gumbel <https://snl-dakota.github.io/docs/6.18.0/users/usingdakota/reference/variables-gumbel_uncertain.html>`_


   User provides :math:`\alpha` and :math:`\beta` for the Gumbel distribution, where :math:`\beta` is known as the **location parameter** and :math:`\frac{1}{\alpha}` the **scale parameter**. The density function of the Gumbel distribution, as a function of these quantities is:

   .. math::
   
	f(x) = \alpha e^{-\alpha(x-\beta)} \exp(-e^{-\alpha(x-\beta)})

For each random variable, the user must enter a name and select from the pull down menu the distribution associated with the random variable. For the distribution selected, the user must then provide the input arguments, which are as described above. :numref:`figRV` shows the panel for a problem with four Random Variables with all random input following Gaussian distributions. 

.. _figRV:

.. figure:: figures/rv.png
   :align: center
   :figclass: align-center

   Random variable specification.

.. note::

   To add a new random variable the user presses the **Add** button. To remove a random variable, the user must first select it by checking the small circle before the random variable, and then pressing the **Remove** button.

.. warning::

   Removing a random variable may have unintended consequences and cause the UQ engine to fail. 

.. figure:: figures/rvplot.png
   :align: center
   :width: 800
   :figclass: align-center

   Various distributions offered by the |app| .

.. only:: quoFEM_app

   SimCenterUQ Engine
   +++++++++++++++++

   Five additional distributions are supported in the SimCenter UQ engine. The users can define distributions either by **Parameters**, **Moments** or **Dataset**. (**Note**: Nataf transform module developed by [ERA19]_ is adopted)

   1. Exponential

      User provides the parameter (:math:`\lambda`) of the exponential distribution. The density function of the exponential distribution, as a function of :math:`\lambda` is:

      .. math::

         f(x) = \lambda \exp(-\lambda x)

      where :math:`x>0` and :math:`\lambda>0`. User can alternatively provide the **mean** (:math:`m`) of the exponential distribution. 

      .. math::

   		m = \frac{1}{\lambda}


   2. Discrete 

      User provides the :math:`N` discrete values (:math:`x_i`) and their weights (probability :math:`p_i`) for a multinomial distribution. The probability mass function of the discrete distribution is:

      .. math::

         p(x)=\begin{cases}
      		 p_i, & \text{if $x=x_i$}\\
      	 	 0, & \text{otherwise}
         \end{cases}

      where :math:`p_i>0`. The weights (:math:`p_i`) will be automatically normalized if they do not sum up to one. The option to define by moments is not supported for the discrete distribution.

   3. Gamma

      User provides the shape parameter (:math:`k`) and scale parameter (:math:`\lambda`) of the Gamma distribution. The density function of the Gamma distribution, as a function of :math:`k` and :math:`\lambda` is:

      .. math::

         f(x) = \frac{\lambda^kx^{k-1}\exp(-\lambda x)}{\Gamma(k)}

      where :math:`\lambda>0` and :math:`k>0`. User can alternatively provide the **mean** (:math:`m`) and **standard deviation** (:math:`\sigma`) . 

      .. math::

   		m &= \frac{k}{\lambda} \\
   		\sigma &= \sqrt{\frac{k}{\lambda^2}}

   4. Chi-squared

      User provides the parameter :math:`k` of the Chi-squared distribution. The density function of the Chi-squared distribution, as a function of :math:`k` is

      .. math::

         f(x) = \frac{1}{2^{\frac{k}{2}}\Gamma\left(\frac{k}{2}\right)}x^{\left(\frac{k}{2}-1\right)} \exp\left(-\frac{x}{2}\right)

      where :math:`x>0` and :math:`k` is a natural number. User can alternatively select the moment option where the **mean** (:math:`m`) is 

      .. math::

   		m = k

   5. Truncated exponential

      User provides the parameter :math:`k` and bounds :math:`L_B` and :math:`U_B` for the truncated exponential distribution. The density function of the truncated exponential distribution, as a function is

      .. math::

         f(x) = \frac{\lambda}{c} \exp(-\lambda x), \text{  where $L_B<x<U_B$}

      where :math:`c` is a normalization constant, i.e.

      .. math::

         c = \int_{L_B}^{U_B} \lambda\exp(-\lambda x) dx

      where :math:`x>0` and :math:`\lambda>0`. User can alternatively provide the **mean** of the distribution along with the **truncated bounds**. 

      .. figure:: figures/rv5.png
       :align: center
       :width: 800
       :figclass: align-center

       Extended random variable specification
      

   **Input Type - Dataset**

   User can also define the random variables by providing sample realization data set as shown in the below figure, by selecting ``Dataset`` input type. The data will be fitted to the specified probability distribution model. Note that for some of the bounded distributions, such as beta and truncated exponential, the bounds should additionally be provided through the user interface.  

   .. _figRVdata

   .. figure:: figures/rv3.png
       :align: center
       :width: 800
       :figclass: align-center

       Example of input dataset file

   .. note::

      - Clicking the ``Show PDF`` or ``Show PMF`` button will display probability distribution (or mass) function of each random variable with the specified parameters/moments. If the PDF or PMF is not displayed, we recommend the users to double-check the parameters/moments if they are in a valid range. The plotting button is not activated for the ``Dataset`` input type. 

   .. [ERA19]
      Engineering Risk Analysis Group, Technische Universität München: https://www.bgu.tum.de/era/software/eradist/ (Matlab/python programs and documentations)

.. only:: quoFEM_app

   Correlation matrix
   ------------------------

   Correlation coefficients between each variable can be defined by clicking the ``Correlation Matrix`` button. Default correlations between variables are set to be zero. The diagonal element of the matrix is fixed as one, and symmetry of the correlation matrix is enforced once the entries of the lower triangular part of the matrix are modified. 

   .. figure:: figures/rv4.png
      :align: center
      :width: 800
      :figclass: align-center

      Example of a valid correlation matrix

   Once the ``OK`` button is clicked after setting all required entries, the program will automatically check the validity of the matrix before closing the correlation matrix window. If the matrix is not **positive definite**, an error message will be displayed and the window will not be closed. In such case, user should adjust the correlation coefficients to be positive definite.

   .. note::

      - When ``constant`` variable is introduced instead of probability distributions, the correlation coefficient corresponding to those variables will be ignored. 
      - When more than one random variable is provided as ``Dataset``, correlations between the data pairs will not be incorporated automatically. If correlations exist, user can define them manually at the correlation matrix window.

   .. warning::

       Correlation warping for Nataf variable transformation of **beta** distributions is currently not supported.


.. only:: quoFEM_app

   UCSD-UQ Engine
   ++++++++++++++

   The same set of distributions that are supported by the SimCenterUQ engine are supported in the UCSD-UQ engine. Currently, the distributions can only be defined through their **Parameters**. Correlation between the random variables is not supported in the UCSD-UQ engine. 


.. only:: quoFEM_app

   CustomUQ Engine
   +++++++++++++++

   The same set of distributions and correlation options as that supported by the SimCenterUQ engine can also be selected when the CustomUQ engine is used. Additionally, two options - **User defined** and **User defined vector** are also available. 

   When the **User defined** option is chosen, the user must provide the path to a script file that makes the desired functionality for the CustomUQ engine available, such as methods to draw samples from the user-defined distribution, or to evaluate the probability density of the user-defined distribution at specified sample points, etc. 

   When the **User defined vector** option is chosen, in addition to the path to the script file, the user must also enter the number of components in the random vector.

   .. _figUserDefinedDists

   .. figure:: figures/userDefinedDists.png
       :align: center
       :width: 800
       :figclass: align-center

       Specifying user-defined distributions under CustomUQ engine


.. Tip::
   
   Summary of capabilities and limitations

   * :bdg-primary:`o` Specify 12 different kinds of random distributions either by parameters, moments (mean and variance), or data samples (Specify 7 different kinds of random distributions by parameters when using Dakota instead of SimCenterUQ)
   * :bdg-primary:`o` Draw correlated samples through Nataf transformation (Gaussian-copular) 
   * :bdg-danger:`x` Explicitly specify random fields (planned)
   * :bdg-danger:`x` Specify user-defined random distribution (planned)
   * :bdg-danger:`x` Specify Non-Gaussian copular correlation (upon request)

.. only:: quoFEM_app

   Video Resources
   -------------------

   Recorded in tool training, 2022.

   .. raw:: html

      <div style="text-align: center;">
         <video controls src="../../../../_static/videos/quoFEM/youtube_RV_Day1_TestClip.mp4" width="560" height="315"> </video>   
      </div>
