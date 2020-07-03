


Forward Propagation - OpenSeesPy
============================================================

This example illustrates how quoFEM interacts with OpenSeesPy. A simple forward propagation procedure is run to estimate the first and second central moments of a FE model’s response, given the marginal distributions of various random parameters.

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

#. ``truss/model.py``: This file is a Python script which takes a given realization of the problem's random variables, and runs a finite element analysis of the truss with OpenSeesPy. It is supplied to the **Input Script** field of the **FEM** tab, and obviates the need for supplying a **Postprocess Script**. When this script is invoked in the workflow, it receives the list of the identifiers supplied in the **QoI** tab through the operating system's `stdout` variable, and a set of random variable realizations by star-importing the **Parameters File** from the **FEM** tab.

#. ``truss/params.py``: This file is a Python script which defines the problem's random variables as objects in the Python runtime. It is supplied to the **Parameters File** field of the **FEM** tab. *The literal values which are assigned to variables in this file will be varied at runtime by the UQ engine.*





.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

Various views of the graphical display can be obtained by left- and right-clicking the columns of the tabular data. If a singular column of the tabular data is selected with simultaneous right- and left-clicks, a frequency and CDF will be displayed, as shown in figure below.


.. figure:: truss/trussRES5.png

   :align: center
   :figclass: align-center