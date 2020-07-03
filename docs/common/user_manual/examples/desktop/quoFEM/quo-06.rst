


Optimization
============================================================

In this example, quoFEM is used to solve a classical optimization problem, for which an analytic solution is known.

The Rosenbrock function is a *test function* that is often used to evaluate numerical optimization algorithms.

.. math::  f(x, y)=(a-x)^{2}+b\left(y-x^{2}\right)^{2} 


.. figure:: None
   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

#. , ``x``: Uniform distribution with a  lower bound :math:`(L_B)` of -2,  upper bound :math:`(U_B)` of 2, .

#. , ``y``: Uniform distribution with a  lower bound :math:`(L_B)` of 1.4,  upper bound :math:`(U_B)` of 1.6, .






Model Definition
^^^^^^^^^^^^^^^^


The following input files must be placed in an *empty* folder:

#. ``rosen/rosen.py``: This file is a Python script which implements the Rosenbrock function. It is supplied to the **Input Script** field of the **FEM** tab. Because this file write directly to `results.out`, it obviates the need for supplying a **Postprocess Script**. When invoked in the workflow, the Python routine is supplied a set of random variable realizations through the star-import of the script supplied to the **Parameters File** field.

#. ``rosen/params.py``: This file is a Python script which defines the problem's random variables as objects in the Python runtime. It is supplied to the **Parameters File** field of the **FEM** tab. *The literal values which are assigned to variables in this file will be varied at runtime by the UQ engine.*





.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

None

.. figure:: None
   :align: center
   :figclass: align-center