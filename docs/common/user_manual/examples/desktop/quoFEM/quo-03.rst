
|quo-03|
============================================================

Consider the problem of uncertainty quantification in a two-dimensional truss structure shown in the following figure.

.. figure:: figures/truss.png
   :align: center
   :width: 600
   :figclass: align-center

The structure has uncertain properties that all follow a normal distribution:

1. Elastic modulus(E): mean :math:`\mu_E=205 kN/{mm^2}` and standard deviation :math:`\sigma_E =15 kN/{mm^2}` (COV = 7.3%)
2. Load (P): mean :math:`\mu_P =25 kN` and a standard deviation of :math:`\sigma_P = 3 kN`, (COV = 12%).
3. Cross sectional area for the upper three bars (Au): mean :math:`\mu_{Au} = 500 mm^2`, and a standard deviation of :math:`\sigma_{Au} = 25mm^2`  (COV = 5%)
4. Cross sectional area for the other six bars (Ao): mean :math:`\mu_{Ao} = 250mm^2`, and :math:`\sigma_{Ao} = 10mm^2` (COV = 4%)

The goal of the exercise is to estimate the mean and standard deviation of the vertical displacement at node 3. The exercise requires two files. The user is required to download these files and place them in a **NEW** folder. The two files are: 

1. `TrussTemplate.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/TrussTemplate.tcl>`_ 

.. literalinclude:: TrussTemplate.tcl
   :language: tcl

.. note::
   
   1. The first lines containing ``pset`` will be read by the application when the file is selected and the application will autopopulate the Random Variables input panel with these same variable names. It is of course possible to explicitly use Random Variables without the ``pset`` command as is demonstrated in the verification section.

2. `postprocess.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/postprocess.tcl>`_. 

The postprocess.tcl script shown below will accept as input any of the 6 nodes in the domain and for each of the two dof directions.

.. literalinclude:: postprocess.tcl
   :language: tcl

.. note::

   The use has the option to provide no postprocess script (in which case the main script must create a results.out file containing a single line with as many space separated numbers as QoI or the user may provide a python script that also performs the postprocessing. An example of a postprocessing python script is `postprocess.py <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/postprocess.py>`_. 

   .. literalinclude:: postprocess.py
      :language: python

.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!

Reliability Analysis
^^^^^^^^^^^^^^^^^^^^

If the user is interested in the probability that a particular response measure will be exceeded, an alternate strategy is to perform a reliability analysis. In order to perform a reliability analysis the steps above would be repeated with the exception that the user would select a reliability analysis method instead of a Forward Propagation method. To obtain reliability results using the Second-Order Reliability Method (SORM) for the truss problem the user would follow the same sequence of steps as previously. The difference would be in the UQ tab in which the user would select a Reliability as the Dakota Method Category and then choose Local reliability. In the figure the user is specifying that they are interested in the probability that the displacement will exceed certain response levels.


.. figure:: figures/trussSORM-UQ.png
   :align: center
   :figclass: align-center

After the user fills in the rest of the tabs as per the previous section, the user would then press the ''RUN'' button. The application (after spinning for a while with the wheel of death) will present the user with the results.

.. figure:: figures/trussSORM-RES.png
   :align: center
   :figclass: align-center


Global Sensitivity
^^^^^^^^^^^^^^^^^^

In a global sensitivity analysis the user is wishing to understand what is the influence of the individual random variables on the quantities of interest. This is typically done before the user launches large scale forward uncertainty problems in order to limit the number of random variables used so as to limit the number of simulations performed.

To perform a reliability analysis the steps above would be repeated with the exception that the user would select a reliability analysis method instead of a Forward Propagation method. To obtain reliability results using the Second-Order Reliability Method (SORM) for the truss problem the user would follow the same sequence of steps as previously. The difference would be in the UQ tab in which the user would select a Reliability as the Dakota Method Category and then choose Local reliability. In the figure the user is specifying that they are interested in the probability that the displacement will exceed certain response levels.


.. figure:: figures/trussSens-UQ.png
   :align: center
   :figclass: align-center

After the user fills in the rest of the tabs as per the previous section, the user would then press the ''RUN'' button. The application (after spinning for a while with the wheel of death) will present the user with the results.

.. figure:: figures/trussSensitivity-RES.png
   :align: center
   :figclass: align-center


