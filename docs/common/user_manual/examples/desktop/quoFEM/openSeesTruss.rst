
Forward Propagation in Two-Dimensional Truss
============================================

Consider the problem of uncertainty quantification in a two-dimensional truss structure, as shown in figure Figure 4.1. The structure has uncertain properties that all follow normal distribution such that:

1. Elastic modulus(E): mean :math:`\mu_E=205 kN/{mm^2}` and standard deviation :math:`\sigma_E =15 kN/{mm^2}`
2. Load (P): mean :math:`\mu_P =25 kN` and a standard deviation of :math:`\sigma_P = 3 kN`
3. Cross sectional area for the upper three bars (Au): mean :math:`\mu_{Au} = 500 mm^2`, and a standard deviation of :math:`\sigma_{Au} = 25mm^2` 
4. Cross sectional area for the other six bars (Ao): mean :math:`\mu_{Ao} = 250mm^2`, and :math:`\sigma_{Ao} = 10mm^2`

The goal of the exericise is to estimate the mean and standard deviation of the vertical displacement at node 3. The exercise requires two files: `TrussTemplate.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/TrussTemplate.tcl>`_ and `postprocess.tcl <https://github.com/NHERI-SimCenter/quoFEM/blob/master/examples/exampleOpenSeesForward/postprocess.tcl>`_. These file need to be saved and places in a NEW folder on your computer.


.. note::
   
   1. The first lines containing pset will be read by the application when the file is selected and the application will autopopulate the Random Variables input panel with these same variable names.

   2. The postprocess script is passed the QoI provided by the user and will provide results for any of the 6 nodes in any of their 2 dof directions.

.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containig these files multiple times. If you are like me, your root, Downloads or Documents folders contains and awful lot of files.

The steps involved:

1. Start the application and the UQ Selection will be highlighted. In the panel for the UQ selection, keep the UQ engine as that selected, i.e. Dakota, and the UQ Method as Forward Propogation, and the Forward Propagarion method as LHS (Latin Hypercude). Change the #samples to 1000 and the seed to 500 as shown in the figure.

2. Next select the FEM tab from the input panel. This will default in the OpenSees FEM engine. For the main script copy the path name to TrussSelection.tcl or select choose and navigate to the file. For the postprocess script, repeat the same procedure for the postpropcess.py script.

3. Next select the RV tab from the input panel. This should be prepopulated with four random variables with same names as those having pset in the tcl script. For each variable, from the drop down menu change them from having a constant disatribution to a lognormal one and then provide the means and standard deviations specified for the problem.

4. Next select the QoI panel. Here enter 'Node_3_Disp_2' for the one variable. 

.. note::
   
   The user can add additional QoI by selecting add and then providing additional names. As seen from the postprocess script any of the 6 nodes may be specified and for any node either the 1 or 2 dof direction.

5. Next click on the 'Run' button. This will cause the backend application to launch dakota. When done the RES panel tab will be selected and the results will be displayed. The results show the values dor the mean and standard deviation.





With the 'RES' panel selected the user can also select the Data tab. With the data tab slected the use can visually look at the results of each of all the deterministic simulations.


In this example, we will use the Latin Hypercube Sampling available in the Dakota UQ Engine's Forward Sampling mewthods in conjunction with OpenSees. 







