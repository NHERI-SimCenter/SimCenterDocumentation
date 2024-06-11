.. _lblDLApp:

DL Applications
===============

The **DL application** assesses the damage and loss for buildings subjected to regional events.It uses building properties, such as building occupancy, structure type, replacement cost, and number of stories, to determine damages and losses. These properties are specified in the :ref:`BIM file <lblBuildingApp>`. The application also uses the response simulation output recorded in the :ref:`EDP file <lblEDPApp>`.

The application returns damage probabilities in a "DM.csv" file and decision variable estimates in a "DV.csv" file for each simulation. These files are saved in their respective **simulation working directories**.

.. figure:: _static/images/backendapps_DL.png
   :align: center
   :figclass: align-center

