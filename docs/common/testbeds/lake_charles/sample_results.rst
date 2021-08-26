.. _lbl-testbed_LC_sample_results:

********************
Verification Results
********************

This page summarizes sample results from the 
testbed runs with the focuse on verifying the estimated loss ratios by hand-calculations.

Building Inventory
===================

From the entire building inventory, 109 buildings (:numref:`sample_table`) are selected.
:numref:`scatter_matrix` shows the data distributions of the built year, surface
roughness (i.e., Terrain), roof shape, number of stories, and occupancy class.

.. csv-table:: Sampled building inventory
   :file: table/veri_sample.csv
   :name: sample_table
   :header-rows: 1
   :align: center

.. figure:: figure/ScatterMatrix.png
   :name: scatter_matrix
   :align: center
   :figclass: align-center
   :figwidth: 700

   Scatter matrix of sampled buildings.

Hand Calculation
==================

Hand calculations of wind loss are conducted using the
input building information and intensity measures for the sampled buildings.
:numref:`hand_calc` compares the hand-calculated loss ratios and the simulated
results which are in good agreement.

.. figure:: figure/SimuVSHandCalc.png
   :name: hand_calc
   :align: center
   :figclass: align-center
   :figwidth: 400

   Hand-calculated results vs. simulated results.