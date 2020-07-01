
|quo-01|
============================================================

This example will use quoFEM to estimate the first and second central moments of a FE model's response, given the marginal distributions of various random parameters.

Consider the problem of uncertainty quantification in a two-dimensional truss structure shown in the following figure.

.. figure:: figures/truss.png
   :align: center
   :width: 600
   :figclass: align-center


The structure has uncertain properties that all follow a normal distribution as follows:

1. Elastic modulus(E): mean :math:`\mu_E=205 \mathrm{ kN}/\mathrm{mm}^2` and standard deviation :math:`\sigma_E =15 \mathrm{ kN}/\mathrm{mm}^2` (COV = 7.3%)
2. Load (P): mean :math:`\mu_P =25 kN` and a standard deviation of :math:`\sigma_P = 3 \mathrm{ kN}`, (COV = 12%).
3. Cross sectional area for the upper three bars (Au): mean :math:`\mu_{Au} = 500 \mathrm{mm}^2`, and a standard deviation of :math:`\sigma_{Au} = 25\mathrm{mm}^2`  (COV = 5%)
4. Cross sectional area for the other six bars (Ao): mean :math:`\mu_{Ao} = 250 \mathrm{mm}^2`, and :math:`\sigma_{Ao} = 10\mathrm{mm}^2` (COV = 4%)

Two input files are used to define a forward propagation procedure with quoFEM which will estimate the mean and standard deviation of the vertical displacement at node 3 using Monte-Carlo simulation. The relevant problem files may be downloaded from **LINK**

Pre-processing
^^^^^^^^^^^^^^^^^

The following input files must be placed in an *empty* folder:

.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!

1. `TrussTemplate.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/TrussTemplate.tcl>`_ . The first lines containing ``pset`` will be read by the application when the file is selected and the application will autopopulate the Random Variables input panel with these same variable names. It is of course possible to explicitly use Random Variables without the ``pset`` command as is demonstrated in the verification section. 

.. 
   .. literalinclude:: TrussTemplate.tcl
      :language: tcl


2. `postprocess.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/postprocess.tcl>`_. 
This script will accept as input any of the 6 nodes in the domain and for each of the two dof directions. The user has the option to provide no postprocess script (in which case the main script must create a results.out file containing a single line with as many space separated numbers as QoI or the user may provide a python script that also performs the postprocessing. An example of a postprocessing python script is `postprocess.py <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/postprocess.py>`_. 

.. 
   .. literalinclude:: postprocess.tcl
      :language: tcl 

   .. literalinclude:: postprocess.py
      :language: python


To perform a Sampling or Forward propagation uncertainty analysis the user would perform the following steps:

1. Start the application and the UQ Selection will be highlighted. In the panel for the UQ selection, keep the UQ engine as that selected, i.e. Dakota, and the UQ Method Category as Forward Propagation, and the Forward Propagation method as LHS (Latin Hypercube). Change the #samples to 1000 and the seed to 20 as shown in the figure.

.. 
   .. figure:: figures/trussUQ.png
      :align: center
      :figclass: align-center

2. Next select the FEM tab from the input panel. This will default in the OpenSees FEM engine. For the main script copy the path name to TrussSelection.tcl or select choose and navigate to the file. For the postprocess script, repeat the same procedure for the postprocess.tcl script.

.. 
   .. figure:: figures/trussFEM.png
      :align: center
      :figclass: align-center

3. Next select the RV tab from the input panel. This should be pre-populated with four random variables with same names as those having ``pset`` in the tcl script. For each variable, from the drop down menu change them from having a constant distribution to a normal one and then provide the means and standard deviations specified for the problem.

.. 
   .. figure:: figures/trussRV.png
      :align: center
      :figclass: align-center

4. Next select the QoI panel. Here enter 'Node_3_Disp_2' for the one variable. 

.. 
   .. figure:: figures/trussQoI.png
      :align: center
      :figclass: align-center

.. note::   

   The user can add additional QoI by selecting add and then providing additional names. As seen from the postprocess script any of the 6 nodes may be specified and for any node either the 1 or 2 dof direction.

5. Next click on the 'Run' button. This will cause the backend application to launch dakota. When done the RES panel tab will be selected and the results will be displayed. The results show the values the mean and standard deviation.

.. 
   .. figure:: figures/trussRES1.png
      :align: center
      :figclass: align-center

Post-processing
^^^^^^^^^^^^^^^

If the user selects the "Data" tab in the results panel, they will be presented with both a graphical plot and a tabular listing of the data.

.. figure:: figures/trussRES2.png
   :align: center
   :figclass: align-center

Various views of the graphical display can be obtained by left and right clicking in the columns of the tabular data. If a singular column of the tabular data is pressed with both right and left buttons a frequency and CDF will be displayed, as shown in figure below.

.. figure:: figures/trussRES5.png
   :align: center
   :figclass: align-center
