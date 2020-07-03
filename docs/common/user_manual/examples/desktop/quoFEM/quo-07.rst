


Conventional Calibration - Steel Frame
============================================================


| In this example, which has been provided by Professor Joel Conte and his doctoral students Maitreya Kurumbhati and Mukesh Ramancha from UC San Diego, a simplified finite element model of a steel building is being developed.
  |image0|
| Consider the two-story building structure shown above. Each floor slab of the building is made of composite metal deck and is supported on four steel columns. Story heights of 10’ are measured as are the lengths of the building along the X and Y direction, which are measured at :math:`33'-4"` and :math:`30'`. For the steel columns, elastic modulus is measured to be :math:`29,000 \mathrm{ksi}`, :math:`Area=110 \mathrm{in}^2`, and :math:`I_{xx}=1190 \mathrm{in}^4`. For modelling purposes, the four columns are assumed fixed at the base and the beams connecting them are assumed to be rigid.
  What is unknown is the mass of the building. However from data collected the periods of the structure are determined to be 0.19 sec and 0.09 sec. For this exercise the unknown quantities, ``m1`` and ``m2``, the mass of first and second floors to be used in the model will be considered our unknown variables. We will assume some bounds on these variables and provide initial estimates as shown in following table:

.. |image0| image:: frame/joelFrame.png


.. figure:: 
   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:






Model Definition
^^^^^^^^^^^^^^^^


The following input files must be placed in an *empty* folder:

#. ``frame/fem.tcl``: This file is an OpenSees Tcl script that defines a FE model for a given realization, runs an analysis, and creates a `results.out` fils. As a consequence, no postprocessing script is needed. The values placed in `results.out` file are the difference between computed and observed values. Expressed another way, the function `f(m1,m2)` computed and written to the `results.out` file is `f(m1,m2) = ObservedPeriods - ComputedPeriods(m1,m2)`. The UQ algorithm when running is searching for values of the random variable parameters (`m1` and `m2`) that minimize this loss function. The user must take this fact into account when formulating the output from their own scripts for their own problems.





.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

Once the analysis is complete the **RES** tab will be automatically selected and the results will be displayed as shown in the figure below. The figure shows that Dakota returned estimates of our unknown parameters to be :math:`m1=0.515549` and :math:`m2=0.256492`.


.. figure:: frame/joelRES.png

   :align: center
   :figclass: align-center