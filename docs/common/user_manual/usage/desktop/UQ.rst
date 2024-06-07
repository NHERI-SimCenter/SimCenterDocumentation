.. _lblUQ:

==============================
UQ: Uncertainty Quantification
==============================

The **UQ** tab is the panel where users select the **UQ Engine** for uncertainty quantification calculations. The **UQ Engine** encompasses algorithms for various uncertainty analysis and optimization problems.

.. role:: uqblue

.. only:: quoFEM_app
     
   The **UQ Engine** options currently available are Dakota, SimCenterUQ, and UCSD-UQ. Users can also configure |appName| to use their own UQ methods and algorithms in the |appName| workflow by selecting the CustomUQ option.

   UQ Features At-a-Glance
   -------------------------

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_forward.png
                :width: 100%

     .. grid-item-card:: Forward propagation
            :columns: 9

            | Forward propagation generates sample realizations of input random variables (RVs) and output quantity of interests (QoIs) to provide statistics such as mean, variance, skewness, and kurtosis. See Dakota user manual for theory details.

             | ▪ :ref:`lblDakotaForward` in Dakota   :bdg-link-primary:`Example1 <../../examples/desktop/qfem-0001/README.html>` :bdg-link-primary:`Example2 <../../examples/desktop/qfem-0002/README.html>`
             | ▪ :ref:`lblSimForward` in SimCenterUQ   :bdg-link-success:`Example <../../examples/desktop/qfem-0015/README.html>`
             | ▪ :ref:`lblSimForwardMF` in SimCenterUQ  

            | See Dakota user manual for theory details.


   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_sensitivity.png
               :width: 100%

     .. grid-item-card:: Global Sensitivity Analysis
            :columns: 9

            | Global sensitivity analysis is used to quantify the contribution of each input RV to the uncertainty in an output QoI. Dakota engine provides classical non-parametric estimation based on a smart sampling approach and the SimCenterUQ engine provides a probabilistic model-based approximation. 

             | ▪ :ref:`lblDakotaSensitivity` in Dakota   :bdg-link-primary:`Example <../../examples/desktop/qfem-0001/README.html>`
             | ▪ :ref:`lblSimSensitivity` in SimCenterUQ   :bdg-link-success:`Example1 <../../examples/desktop/qfem-0009/README.html>` :bdg-link-success:`Example2 <../../examples/desktop/qfem-0023/README.html>`

            | See Dakota user manual and :ref:`here<lbluqSimTechnical_Sensitivity>` for theory details.

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_reliability.png
                :width: 100%

     .. grid-item-card:: Reliability Analysis
            :columns: 9

            | Reliability Analysis is performed to estimate the probability of failure, i.e. the probability that a system response (QoI) exceeds a certain threshold level. 

             | ▪ :ref:`lblDakotaReliability` in Dakota   :bdg-link-primary:`Example <../../examples/desktop/qfem-0001/README.html,>`

            | See Dakota user manual for theory details.

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_Bayesian.png
                :width: 100%

     .. grid-item-card:: Bayesian Calibration
            :columns: 9

            | Bayesian Calibration is used to calibrate model parameters probabilistically based on Bayesian inference. The probability distributions of the input parameters (RVs) are updated by experimental data. 

             | ▪ :ref:`lblDakotaBayesianCalibration` in Dakota
             | ▪ :ref:`lblUCSDTMCMC` in UCSD-UQ   :bdg-link-danger:`Example1 <../../examples/desktop/qfem-0014/README.html>` :bdg-link-danger:`Example2 <../../examples/desktop/qfem-0019/README.html>`

            | Theory details can be found in the Dakota user manual and :ref:`here<lbluqUCSDSimTechnical>`.

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_deterministic.png
                :width: 100%

     .. grid-item-card:: Deterministic Calibration
            :columns: 9

            | Deterministic Calibration estimates the best parameter values of a simulation model that best fit the experimental data, using deterministic optimization algorithms, e.g. Gauss-Newton least squares, pattern search, etc. 

             | ▪ :ref:`lblDakotaDeterministicCalibration` in Dakota   :bdg-link-primary:`Example1 <../../examples/desktop/qfem-0007/README.html>` :bdg-link-primary:`Example2 <../../examples/desktop/qfem-0019/README.html>`
             | ▪ :ref:`lblDakotaGradientFreeEstimation` in Dakota

            | See Dakota user manual for theory details. 

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3

         .. thumbnail:: figures/UQtab/method_surrogate.png
                :width: 100%

     .. grid-item-card:: Surrogate Modeling
            :columns: 9

            | |app| can be used to train a surrogate model that substitutes expensive computational simulation models or physical experiments. 

             | ▪ :ref:`lblSimSurrogate` in SimCenterUQ   :bdg-link-success:`Example1 <../../examples/desktop/qfem-0015/README.html>` :bdg-link-success:`Example2 <../../examples/desktop/qfem-0016/README.html>`
             | ▪ :ref:`lblSimCenterUQPLoM` in SimCenterUQ

            | Theory details can be found in :ref:`here<lbluqSimTechnical>`.

   .. grid:: 2
     :gutter: 1

     .. grid-item-card::
         :columns: 3
        
         .. thumbnail:: figures/UQtab/method_custom.png
                :width: 100%

     .. grid-item-card:: Custom UQ
           :columns: 9

           | Custom UQ helps the user plug in a user-defined UQ algorithm in SimCenter workflow.

            | ▪ :ref:`lblCustomUQ` in CustomUQ engine   :bdg-link-success:`Example <../../examples/desktop/qfem-0017/README.html>`


.. only:: notQuoFEM

   The **UQ Engine** options currently available are Dakota and SimCenterUQ.

Dakota UQ Engine
----------------

This UQ engine utilizes the `Dakota Software <https://dakota.sandia.gov/>`_, a state-of-the-art research application that is robust and provides many methods for optimization and UQ, a selection of which we utilize in this application. **Dakota** provides the user with several methods for different kinds of analyses. For this reason, we have divided the methods into categories through a pull-down menu, as shown below. Once the category has been selected, a few different methods are made available to the user.

* By checking the ``Parallel Execution``, the UQ analysis will be performed in parallel. It will try to use all the processors available on the machine. 

* By checking the ``Save Working dirs``, individual working directories will be saved in the Local Jobs Directory. Local Jobs Directory is defined at ``File``-``Preference`` in the menubar. Otherwise, individual simulation files will be deleted after each simulation run. Users might uncheck this box when a large number of simulations is requested, to manage driver space.

.. _figDakota:

.. figure:: figures/dakotaUQ.png
   :align: center
   :figclass: align-center
   :width: 1200

   Dakota engine and category selection.

The following categories are available:

.. toctree-filt::
   :maxdepth: 1

   DakotaSampling
   DakotaSensitivity
   DakotaReliability
   :quoFEM:DakotaDeterministicCalibration
   :quoFEM:DakotaBayesianCalibration
   :quoFEM:DakotaGradientFreeOptimization

SimCenter UQ Engine
-------------------

The **SimCenterUQ** engine is a UQ engine developed in-house at the SimCenter that accommodates different UQ methods, which are organized into categories that can be accessed through a pull-down menu, as shown below:

.. _figSimCenterUQ:

.. figure:: figures/SimCenterUQ.png
   :align: center
   :figclass: align-center
   :width: 1200

   SimCenterUQ engine and category selection.

The following category options are available:

.. toctree-filt::
   :maxdepth: 1

   SimCenterUQSampling
   :quoFEM:SimCenterUQSensitivity
   :quoFEM:SimCenterUQSurrogate
   :quoFEM:SimCenterUQPLoM
   :quoFEM:SimCenterUQMF
   :EEUQ:SimCenterUQSensitivity
   :EEUQ:SimCenterUQSurrogate
   :EEUQ:SimCenterUQPLoM
   :EEUQ:SimCenterUQMF
   :WEUQ:SimCenterUQSensitivity
   :WEUQ:SimCenterUQMF
   :Hydro:SimCenterUQSensitivity
   :Hydro:SimCenterUQMF
   
.. only:: quoFEM_app

   UCSD UQ Engine
   --------------

   The **UCSD-UQ** engine is a module developed at the SimCenter in collaboration with UCSD. It provides algorithms for Bayesian estimation, which can be accessed through a pull-down menu, as shown in :numref:`figUCSDUQ`.

   .. _figUCSDUQ:

   .. figure:: figures/UCSDUQ.png
      :align: center
      :figclass: align-center
      :width: 1200

      UCSD-UQ engine and category selection.

   This module currently offers support for Bayesian estimation of the parameters of a traditional (non-hierarchical) model using the Transitional Markov chain Monte Carlo (TMCMC) algorithm and of a hierarchical model using an adaptive Metropolis-within-Gibbs sampling algorithm.

   .. toctree-filt::
     :maxdepth: 1

     UCSD_UQ_TMCMC
     UCSD_UQ_Hierarchical

   Custom UQ Engine
   ----------------

   The **CustomUQ** option enables users to switch out the UQ engine in the |appName| workflow such that different methods and tools can be applied within the SimCenter framework with minimal effort on the part of the user. The CustomUQ option can be accessed as shown below:
   
   .. _figCustomUQ:

   .. figure:: figures/customUQ.png
      :align: center
      :figclass: align-center
      :width: 1200

      CustomUQ engine selection.

   In order to use the CustomUQ engine option, two steps are required:

   * Configuring the UQ tab to accept the required inputs
   * Adding UQ engine to customized UQ backend

   These steps are described in more detail here:

   .. toctree-filt::
      :maxdepth: 1

      Configuring_CustomUQ

.. only:: quoFEM_app

   Video Resources
   -------------------

   Recorded in tool training, 2022.

   .. raw:: html

      <div style="text-align: center;">
         <video controls src="../../../../_static/videos/quoFEM/youtube_UQ_Day1_TestClip.mp4" width="560" height="315"> </video>   
      </div>