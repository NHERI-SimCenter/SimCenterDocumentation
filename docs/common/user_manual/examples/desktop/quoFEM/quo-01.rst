


Forward Propagation - OpenSees/Tcl
============================================================

This example uses quoFEM to estimate the first and second central moments of a FE model’s response, given the marginal distributions of various random parameters.

Consider the problem of uncertainty quantification in a two-dimensional truss structure shown in the following figure. Two input scripts are used to define a forward propagation procedure to be coordinated by quoFEM which will estimate the mean and standard deviation of the vertical displacement at node 3 using Latin hypercube sampling.


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

If the user selects **Data** in the **RES** tab, they will be presented with both a graphical plot and a tabular listing of the data.Various views of the graphical display can be obtained by left- and right-clicking the columns of the tabular data. If a singular column of the tabular data is selected with simultaneous right and left clicks, a frequency and CDF will be displayed, as shown in figure below.


.. figure:: truss/trussRES5.png

   :align: center
   :figclass: align-center