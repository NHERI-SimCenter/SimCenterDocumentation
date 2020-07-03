Forward Propagation - OpenSeesPy
============================================================

This example illustrates how quoFEM interacts with OpenSeesPy. A simple forward propagation procedure is run to estimate the first and second central moments of a FE model’s response, given the marginal distributions of various random parameters.

Consider the problem of uncertainty quantification in a two-dimensional truss structure shown in the following figure. Two input scripts are used to define a forward propagation procedure to be coordinated by quoFEM which will estimate the mean and standard deviation of the vertical displacement at node 3 using Latin hypercube sampling.


.. figure:: truss/truss.png

   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

#. ``E``

#. ``P``

#. ``Ao``

#. ``Au``



Problem Workflow
^^^^^^^^^^^^^^^^

Workflow

Model Definition
^^^^^^^^^^^^^^^^

The following input files must be placed in an *empty* folder:




.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

If the user selects **Data** in the **RES** tab, they will be presented with both a graphical plot and a tabular listing of the data.

.. figure:: figures/trussRES2.png
   :align: center
   :figclass: align-center

Various views of the graphical display can be obtained by left- and right-clicking the columns of the tabular data. If a singular column of the tabular data is selected with simultaneous right and left clicks, a frequency and CDF will be displayed, as shown in figure below.


.. figure:: truss/trussRES5.png

   :align: center
   :figclass: align-center