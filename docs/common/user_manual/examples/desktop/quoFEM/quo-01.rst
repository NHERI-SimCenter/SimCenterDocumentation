Forward Propagation - OpenSees/Tcl
==================================

This example uses quoFEM to estimate the first and second central moments of a FE model’s response, given the marginal distributions of various random parameters.

Consider the problem of uncertainty quantification in a two-dimensional truss structure shown in the following figure. Two input scripts are used to define a forward propagation procedure to be coordinated by quoFEM which will estimate the mean and standard deviation of the vertical displacement at node 3 using Latin hypercube sampling.

|image0|

The following parameters are defined in the **RV** tab:

1. Elastic modulus, ``E``: **Weibull** distribution with a scale parameter :math:`(\lambda)` of 210.0, shape parameter :math:`(k)` of 20.0,

2. Load magnitude, ``P``: **Beta** distribution with a first shape parameter :math:`(\alpha)` of 2.0, second shape parameter :math:`(\beta)` of 2.0, lower bound :math:`(L_B)` of 20.0, upper bound :math:`(U_B)` of 30.0,

3. Cross sectional area for the other six bars, ``Ao``: **Lognormal** distribution with a mean :math:`(\mu)` of 250.0, standard deviation :math:`(\sigma)` of 50.0,

4. Cross sectional area for the upper three bars, ``Au``: **Normal** distribution with a mean :math:`(\mu)` of 500.0, standard deviation :math:`(\sigma)` of 100.0,

UQ Workflow
-----------

To define the uncertainty workflow in quoFEM, select **Forward Propagation** for the **Dakota Method Category**, and enter the following inputs:

=========== ===
**Method**  LHS
**Samples** 100
**Seed**    949
=========== ===

Model Files
-----------

The following files make up the **FEM** model definition.

#. ``truss/model.tcl``: This file is an OpenSees Tcl script that constructs and runs a finite element analysis of the truss for a given realization of the problem’s random variables. It is supplied to the **Input File** field of the **FEM** tab.

#. ``truss/post.tcl``: This file is an OpenSees Tcl script that processes the QoI identifiers supplied in the **QoI** tab, and writes the relevant response quantities to ``results.out`` from an OpenSees process. It is supplied to the **Postprocess File** field of the **FEM** tab.

.. warning::

Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!

Results
-------

If the user selects **Data** in the **RES** tab, they will be presented with both a graphical plot and a tabular listing of the data.Various views of the graphical display can be obtained by left- and right-clicking the columns of the tabular data. If a singular column of the tabular data is selected with simultaneous right and left clicks, a frequency and CDF will be displayed, as shown in figure below.

.. figure:: %22truss/trussRES5.png%22
   :alt: Stochastic truss results.

   Stochastic truss results.

.. |image0| image:: truss/truss.png
