.. _lblQUO_QOI

QoI: Quantaties of Interest
===========================

The QoI panel is where the user specifies the variable names associated with the FEM results. For each result quantatity that the users application generates and places in the results.out file, the user must provide a variable name. A new response quantatity is added by the user slecting the ''Add'' button. Quantaties can be removed by selecting it, this is done by clicking in the circle befor the variable name, and then selecting the ''remove'' button.

.. _figQoI:

.. figure:: figures/QoI.png
	:align: center
	:figclass: align-center

	Input for QoI panel 

In figure shown the user has added two response quantiaites, **Node_2_Disp_2** and **Node_4_Disp_1**. The postprocessing script, if one has been provided, will be passed these 2 values as arguments.

.. warning::

   1. There can be no spaces in variable names, underescores are permitted.
   2. Names cannot begin with a numeral, i.e. 0,1,2,3,4,5,6,7,8,9.
   3. Names cannot be duplicated.
