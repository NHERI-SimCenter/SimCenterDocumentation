Non-structural problems with Python
============================================================

This example illustrates how Python scripting can be used with quoFEM to express general mathematical models without the use of a dedicated finite element analysis engine.

The Rosenbrock function is a *test function* that is often used to evaluate numerical optimization algorithms.

.. math::  f(x, y)=(a-x)^{2}+b\left(y-x^{2}\right)^{2} 


.. figure:: None
   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

#. ``x``

#. ``y``



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

None

.. figure:: None
   :align: center
   :figclass: align-center