Reliability Analysis
<<<<<<< Updated upstream
=======================================

If the user is interested in the probability that a particular response measure will be exceeded, an alternate strategy is to perform a reliability analysis. To obtain reliability results using the Second-Order Reliability Method (SORM) for the truss problem the user would follow the same sequence of steps as previously. In the figure the user is specifying that they are interested in the probability that the displacement will exceed certain response levels.

.. figure:: figures/trussSORM-UQ.png
   :align: center
   :figclass: align-center

After the user fills in the rest of the tabs as per the previous section, the user would then press the **RUN** button. The application (after spinning for a while with the wheel of death) will present the user with the results.

.. figure:: figures/trussSORM-RES.png
   :align: center
   :figclass: align-center

=======
============================================================

This example uses quoFEM to perform a second-order reliability analysis (SORM) of an OpenSees FE model.

Consider the stochastic response of a two-dimensional truss structure shown in the following figure with uncertain section dimensions, material moduli, and loading magnitude. Two input scripts are used to define a `local reliability </common/user_manual/usage/desktop/DakotaReliability.html>`__ procedure to be coordinated by quoFEM which will estimate response magnitudes whose probabilities of exceedance are 0.02, 0.2, 0.4, 0.6, 0.8, and 0.99.


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

None

.. figure:: truss/trussSORM-RES.png

   :align: center
   :figclass: align-center
>>>>>>> Stashed changes
