.. _lblDLApp:

DL Applications
===============

The **DL application** performs the damage and loss assessment for the buildings subject to the regional event(s).
It takes as input the building properties used for determining damages and losses (building occupancy, structure type, replacement cost, number of stories), specified in the BIM.json file, as well as the response simulation output recorded in the EDP.json file.
It returns component damage probabilities in a "DM.csv" file and decision variable estimates in a "DV.csv" file for each simulation, saved in its corresponding **simulation working directory**.

The following options for DL applications vary in the software package used to perform the damage and loss assessment.
