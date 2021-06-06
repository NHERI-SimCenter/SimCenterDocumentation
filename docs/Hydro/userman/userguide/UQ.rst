.. _lbl-UQ:

***********************************************
UQ: Uncertainty Quantification
***********************************************

The first selection panel, the user, must select from and enter data into is the **UQ** tab. In this panel, the user selects the **UQ Engine** to use for performing the uncertainty quantification calculations. Presently the only **UQ Engine** option available in the |app| is Dakota. `Dakota <https://dakota.sandia.gov/>`_, a state-of-the-art research application that is robust and provides many methods for optimization and UQ, a selection of which we utilize in this application. **Dakota** provides the user with a large number of different ways. For this reason, we have divided the methods into categories through a pull-down menu, as shown in :numref:`figDakota`. Once the type has been selected, several different methods are made available to the user.

.. _figDakota:

.. figure:: figures/dakotaUQ.png
   :align: center
   :figclass: align-center

   Dakota engine and category selection.

The following categories are available:

.. toctree::
    :maxdepth: 1

    DakotaSa
    DakotaSe
    DakotaR
