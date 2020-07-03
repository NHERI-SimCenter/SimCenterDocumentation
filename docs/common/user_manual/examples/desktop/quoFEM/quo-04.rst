Sensitivity Analysis
============================================================

This example uses quoFEM to perform a global sensitivity analysis of an OpenSees FE model.

Consider a stochastic model of a two-dimensional truss structure like that shown in the following figure. A `sensitivity analysis </common/user_manual/usage/desktop/DakotaSensitivity.html>`__ procedure is coordinated by quoFEM which will estimate the sensitivities of the response quantities of interest with respect to the problem’s random variables.


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


#. ``truss/model.tcl``: This file is an OpenSees Tcl script that constructs and runs a finite element analysis of the truss for a given realization of the problem's random variables. It is supplied to the **Input File** field of the **FEM** tab.

#. ``truss/post.tcl``: This file is an OpenSees Tcl script that processes the QoI identifiers supplied in the **QoI** tab, and writes the relevant response quantities to `results.out` from an OpenSees process. It is supplied to the **Postprocess File** field of the **FEM** tab.





.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

If the user selects **Data** in the **RES** tab, they will be presented with both a graphical plot and a tabular listing of the data.

.. figure:: figures/trussRES2.png
   :align: center
   :figclass: align-center

None

.. figure:: None
   :align: center
   :figclass: align-center