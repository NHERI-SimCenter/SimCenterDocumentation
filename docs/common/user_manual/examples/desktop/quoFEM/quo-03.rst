


Reliability Analysis
============================================================

This example uses quoFEM to perform a second-order reliability analysis (SORM) of an OpenSees FE model.

Consider the stochastic response of a two-dimensional truss structure shown in the following figure with uncertain section dimensions, material moduli, and loading magnitude. Two input scripts are used to define a `local reliability </common/user_manual/usage/desktop/DakotaReliability.html>`__ procedure to be coordinated by quoFEM which will estimate response magnitudes whose probabilities of exceedance are 0.02, 0.2, 0.4, 0.6, 0.8, and 0.99.


.. figure:: truss/truss.png

   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

#. Elastic modulus, ``E``: Weibull distribution with a  scale parameter :math:`(\lambda)` of 210,  shape parameter :math:`(k)` of 20, .

#. Load magnitude, ``P``: Beta distribution with a  first shape parameter :math:`(\alpha)` of 2,  second shape parameter :math:`(\beta)` of 2,  lower bound :math:`(L_B)` of 20,  upper bound :math:`(U_B)` of 30, .

#. Cross sectional area for the other six bars, ``Ao``: Lognormal distribution with a  mean :math:`(\mu)` of 250,  standard deviation :math:`(\sigma)` of 50, .

#. Cross sectional area for the upper three bars, ``Au``: Normal distribution with a  mean :math:`(\mu)` of 500,  standard deviation :math:`(\sigma)` of 100, .






Model Definition
^^^^^^^^^^^^^^^^


The following input files must be placed in an *empty* folder:

#. ``truss/model.tcl``: This file is an OpenSees Tcl script that constructs and runs a finite element analysis of the truss for a given realization of the problem's random variables. It is supplied to the **Input File** field of the **FEM** tab.

#. ``truss/post.tcl``: This file is an OpenSees Tcl script that processes the QoI identifiers supplied in the **QoI** tab, and writes the relevant response quantities to `results.out` from an OpenSees process. It is supplied to the **Postprocess File** field of the **FEM** tab.





.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

None

.. figure:: truss/trussSORM-RES.png

   :align: center
   :figclass: align-center