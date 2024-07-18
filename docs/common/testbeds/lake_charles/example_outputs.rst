.. _lbl-testbed_LC_getting_started:

**************************
Getting Started
**************************

Running the Testbed
===================

R2D Interface
---------------

One approach to running the testbed simulation is via the 
`R2D application <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/R2Dt>`_.
After successfully downloading and launching, the major steps for setting up the run are listed as follows:

#. Set the **Units** in the **GI** panel as shown in :numref:`r2d_gi_lc` and check the desired output files.

   .. figure:: figure/R2D_GI.png
      :name: r2d_gi_lc
      :align: center
      :figclass: align-center
      :width: 500

      R2D GI setup.
#. Download and unzip the `HurricaneLaura_MappedPWS <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/02.%20Input:%20HAZ%20-%20Hazard%20Characterization>`_. 
   Set the **Event File Listing Wind Field** in the **HAZ** panel to the "EventGrid.csv" in the unzipped "IMs" folder.
   The app will automatically load the directory (:numref:`r2d_haz_lc`). The **Units of Event Input File** should be 
   "Miles per hour".

   .. figure:: figure/R2D_HAZ.png
      :name: r2d_haz_lc
      :align: center
      :figclass: align-center
      :width: 500

      R2D HAZ setup.
#. Download the `BIM_LakeCharles_Full.csv <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/01.%20Input:%20BIM%20-%20Building%20Inventory%20Data>`_ (under **01. Input: BIM - Building Inventory Data** folder). 
   Select **CSV to BIM** in the **ASD** panel and set the **Import Path** to "BIM_LakeCharles_Full.csv" (:numref:`r2d_asd_lc`). 
   Specify the building IDs that you would like to include in the simulation (e.g., 1-26516 for the entire inventory - note that this may take a very long time to run 
   on a local machine, so it is suggested to first test with a small sample like 1-100 locally and then submit the entire run to DesignSafe - see more details in :numref:`r2d_run_ds_lc`).

   .. figure:: figure/R2D_ASD.png
      :name: r2d_asd_lc
      :align: center
      :figclass: align-center
      :width: 500

      R2D ASD setup.
#. Set the **Regional Mapping** and **SimCenterEvent** in the **HTA** panel (e.g., :numref:`r2d_hta`).

   .. figure:: figure/R2D_HTA.png
      :name: r2d_hta
      :align: center
      :figclass: align-center
      :width: 500

      R2D HTA setup.
#. Set the "Building Modeling" in the **MOD** panel to "None". 

   .. figure:: figure/R2D_MOD.png
      :name: r2d_mod
      :align: center
      :figclass: align-center
      :width: 500

      R2D MOD setup.
#. Set the "Building Analysis Engine" in the **ANA** panel to "IMasEDP". 

   .. figure:: figure/R2D_ANA.png
      :name: r2d_ana
      :align: center
      :figclass: align-center
      :width: 500

R2D ANA setup.
#. Set the "Damage and Loss Method" in the **DL** panel to "HAZUS MH HU". Download the ruleset scripts from `DesignSafe PRJ-3207 <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/03.%20Input:%20DL%20-%20Rulesets%20for%20Asset%20Representation/scripts>`_ 
   (under the **03. Input: DL - Rulesets for Asset Representation/scripts** folder) and 
   set the **Auto populate script** to "auto_HU_LA.py" (:numref:`r2d_dl_lc`). Please note, place the ruleset scripts 
   in an individual folder so that the application can copy and load them later. 

   .. figure:: figure/R2D_DL.png
      :name: r2d_dl_lc
      :align: center
      :figclass: align-center
      :width: 500

      R2D DL setup.
#. Set the "UQ Application" in the **UQ** panel to "None". 

   .. figure:: figure/R2D_UQ.png
      :name: r2d_uq_lc
      :align: center
      :figclass: align-center
      :width: 500

      R2D UQ setup.

After setting up the simulation, click the **RUN** button to execute the analysis. Once the simulation is completed, 
the app will direct you to the **RES** panel (:numref:`r2d_res_lc`) where you can examine and export the results.

.. figure:: figure/R2D_RES.png
   :name: r2d_res_lc
   :align: center
   :figclass: align-center
   :width: 500

   R2D RES panel.

For simulating the damage and loss for a large region of interest (remember to reset the building IDs in **ASD**), it would be efficient to submit and run the job 
to `DesignSafe <https://www.designsafe-ci.org/>`_ on `Frontera <https://www.tacc.utexas.edu/systems/frontera>`_. 
This can be done in R2D by clicking **RUN at DesignSafe** (you would need to have a valid 
`DesignSafe account <https://www.designsafe-ci.org/account/register/>`_ for login and access to the computing resource). 
:numref:`r2d_run_ds_lc` provides an example configuration to run the analysis (see `R2D User Guide <https://nheri-simcenter.github.io/R2D-Documentation/common/user_manual/usage/desktop/usage.html#figremjobpanel>`_ for detailed descriptions).
The individual building simulations are parallelized when conducted on Frontera, which accelerates the process. It is suggested for the entire building 
inventory in this testbed to use 15 minutes with 96 Skylake (SKX) cores (e.g., 2 nodes with 48 processors per node) to complete 
the simulation. You would receive a job failure message if the specified CPU hours are not sufficient to complete the run. 
Note that the product of the node number, processor number per node, and buildings per task should be greater than the 
total number of buildings in the inventory to be analyzed.

.. figure:: figure/R2D_RUN.png
   :name: r2d_run_ds_lc
   :align: center
   :figclass: align-center
   :width: 300

   R2D - Run at DesignSafe (configuration).

Users can monitor the job status and retrieve result data by clicking the **GET from DesignSafe** button (:numref:`r2d_get_ds_lc`). The retrieved data includes
four major result files, namely, *BIM.hdf*, *EDP.hdf*, *DM.hdf*, and *DV.hdf*. R2D also automatically converts the hdf files to csv files, which are easier to work with.
While R2D provides basic visualization functionalities (:numref:`r2d_res_lc`), users can access the data downloaded under the remote work directory, e.g., 
*/Documents/R2D/RemoteWorkDir* (this directory is machine-specific and can be found in **File->Preferences->Remote Jobs Directory**).
Once these result files are obtained, users can extract and process the information of interest. The next section will use 
the results from this testbed as an example to discuss more details.

.. figure:: figure/get_from_designsafe.png
   :name: r2d_get_ds_lc
   :align: center
   :figclass: align-center
   :width: 400

   R2D GET from DesignSafe.


Regional Results (NSI-Based Year Built)
========================================

The specific entries included in the *BIM.hdf* file are explained in the Asset Description and specifically 
:numref:`tab-bldg_inv_data_model_lc`. It is important to note that this *BIM.hdf* file is an enhanced version of 
the input BIM file, including additional information necessary for the loss estimation (fields added through 
rulesets explained in :ref:`lbl-testbed_LC_asset_representation`). Additionally, the *BIM.hdf* file includes 
only the buildings in the original inventory file that could be successfully executed by the workflow, e.g., 
satisfied conditions in the rulesets necessary to assign requisite attributes. If there are errors in the 
assignment process, the output *BIM.hdf* file will have fewer buildings than the original input BIM file. 
As such, this expanded inventory file output by R2D should be used for subsequent analyses, rather than 
the original inventory used to run the simulation in Step 3 above. The *EDP.hdf* file summarizes the EDP realizations. The *DM.hdf* and 
*DV.hdf* files summarize the statistics of damage states and estimated loss metrics. The results of this testbed
can be accessed in the `DesignSafe project <https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published//PRJ-3207v4/04.%20Output:%20Results>`_, along with the Jupyter 
notebook used to visualize them. The zip file consists of (1) four result hdf files (*BIM.hdf*, *EDP.hdf*, *DM.hdf*, and *DV.hdf*), (2) 
four parsed result files (in .csv), (3) the input inventory csv file, (4) two Jupyter notebook scripts, and (5) a requirement txt file listing the 
dependencies. *post-process.ipynb* can be run locally and first-time users are suggested to run the first cell to install necessary packages, and 
*post-processing_designsafe.ipynb* can be run on DesignSafe Jupyter Notebook if one uploads the entire folder to the Data Depot.
Users are suggested to find more detailed descriptions about the data attributes in the *DV.csv* in the 
`pelicun documentation <https://nheri-simcenter.github.io/pelicun/common/user_manual/usage/pelicun/outputs.html>`_.

:numref:`terrain_swr` (a) and (b) show sample figures for the geospatial distribution of populated 
terrain types and the secondary water resistance of the building inventory. The influence of different building 
attributes on the damage and loss results will be investigated in :ref:`lbl-testbed_LC_validation_results`.
The geospatial distribution of estimated wind damage states and losses under Hurricane Laura
is shown in :numref:`dl_and_cdf_lc` (a) and (b), respectively. As per :numref:`dl_and_cdf_lc` (c), most of the buildings 
in the studied region (75%) have relatively low to moderate damage (expected Damage State less than 2.0) 
due to the wind hazard. According to :numref:`dl_and_cdf_lc` (c), about 5% of buildings would have expected damage states lower than 
DS-1 and only about 5% of buildings would expect to have damage states exceeding DS-3. 
The CDF of resulting loss ratios is shown in :numref:`dl_and_cdf_lc` (d), where about 20% of buildings would expect 
a loss less than 10% of the total reconstruction cost, and about 30% of buildings could see a loss more than 35% of the total 
reconstruction cost. 

.. figure:: figure/BIM_data.png
   :name: terrain_swr
   :align: center
   :figclass: align-center
   :width: 600

   Terrain and secondary water resistance features populated and used in the simulation.

.. figure:: figure/DS_LS_CDF.png
   :name: dl_and_cdf_lc
   :align: center
   :figclass: align-center
   :width: 700

   Estimated regional damage states and loss ratios.