.. _lblQUO_QOI:

QoI: Quantities of Interest
===========================

The **QoI** tab is where the user specifies the variable names associated with the FEM results. The result quantity might be a scalar (i.e. of length 1) or a vector/field quantity (i.e., of length > 1). For each result quantity that the users' application generates and places in the ``results.out`` file, the user must provide a variable name and specify its length. A new response quantity is added by the user selecting the **Add** button. Quantities can be removed by selecting it, this is done by clicking in the circle before the variable name, and then selecting the **Remove** button.

.. _figQoI:

.. figure:: figures/QoI.png
	:align: center
	:figclass: align-center

	Input for the **QoI** tab.

In :numref:`figQoI`, the user has defined three response quantities, ``Node_2_Disp_2``, ``Node_4_Disp_1`` and ``stress_time_history``. If a postprocessing Python script has been provided, it will be passed these three names as arguments.

.. warning::

   1. There can be no spaces in variable names, underscores are permitted.
   2. Names cannot begin with a numeral, i.e. 0,1,2,3,4,5,6,7,8,9.
   3. Names cannot be duplicated.
