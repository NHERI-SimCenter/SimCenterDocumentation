.. _lblHAZ:

HAZ: Hazards
============

In this panel the user can define or simulate hazards over a region. The user can select the type of hazard, such as Earthquakes and Hurricanes, from the **Hazard Selection** combo box, as shown on the top of :numref:`fig-HazMainPanel`. As the user selects between the different hazard applications, the main panel will change to reflect the inputs for each application.

.. contents::
   :local:

.. _fig-HazMainPanel:

.. figure:: figures/R2DHazMainPanel.png
  :align: center
  :figclass: align-center

  Hazard input panel.

User-specified Ground Motions
-----------------------------

The **User-specified Ground Motion** application loads the results of an **Earthquake Scenario Simulation** that was run previously. The **User-specified Earthquakes** application input pane is given in :numref:`fig-UserSelectEQ`. As seen in the figure, the user is required to input the file path to the ``EventGrid.csv`` file in the `Event File Listing Motions Field`. If the ground motions are not in the same folder as the ``EventGrid.csv`` file, then the user needs to input the directory path to the folder containing the ground motions. Users also need to specify the units of the ground motion field.

.. _fig-UserSelectEQ:

.. figure:: figures/R2DUserSelectEQ.png
  :align: center
  :figclass: align-center

  User-defined earthquakes input panel.
  
  

ShakeMap Earthquake Scenarios
-----------------------------

The **ShakeMap Earthquake Scenario** application provides the functionality to import a USGS ShakeMap earthquake hazard. The **ShakeMap Earthquake Scenario** application input pane is given in :numref:`fig-R2DShakeMapPane`. As seen in the figure, the user is required to input a path to a folder on the user's computer that contains the ShakeMap data. At a minimum, the folder must contain a ``grid.xml`` file that provides the ground motion intensity measures, e.g., PGA, PGV, over a geographical grid. To visualize the PGA contours or rupture in the GIS window, a user can also provide the ``cont_pga.json`` file, or ``rupture.json`` file, respectively. Note that more than one ShakeMap can be input. However, the ShakeMap that is selected in the **List of ShakeMaps** tree in :numref:`fig-R2DShakeMapPane`, is the one that is employed in the subsequent analysis. The user also has the option to select the type of intensity measure they want from the ShakeMap grid. 

.. _fig-R2DShakeMapPane:

.. figure:: figures/R2DShakeMapPane.png
  :align: center
  :figclass: align-center

  ShakeMap input panel.
  
After a ShakeMap is loaded, it will appear in the list of ShakeMaps shown above in :numref:`fig-R2DShakeMapPane`. Users can see the grid, contours, etc., ShakeMap visuals by going to the **VIZ** pane, as highlighted in :numref:`fig-R2DShakeMapOutput` below. 
  
.. _fig-R2DShakeMapOutput:

.. figure:: figures/R2DShakeMapOutput.png
  :align: center
  :figclass: align-center

  ShakeMap visualization.
  
.. [SnaikiWu2017a]
   Snaiki, R. and Wu, T. (2017a). Modeling tropical cyclone boundary layer: Height-resolving pressure and wind fields. Journal of Wind Engineering and Industrial Aerodynamics, 170, pp. 18-27.

.. [SnaikiWu2017b]
   Snaiki, R. and Wu, T. (2017b). A linear height-resolving wind field model for tropical cyclone boundary layer. Journal of Wind Engineering and Industrial Aerodynamics, 171, pp. 248-260.
   
  
Raster Defined Hazard
---------------------
   
The **Raster Defined Hazard Widget** allows for the import of raster files to represent hazard intensities. The **Raster Defined Hazard Widget** input pane is given in :numref:`fig-R2DRasterHazardPane`. 

#. To load a raster file, click on the **Browse** button next to the input file box, and then select the raster file in the dialog that will appear. 
#. Next, select the event type in the **Event Type Dropdown**, shown in the :numref:`fig-R2DRasterHazardPane`, e.g., Hurricane or Earthquake. 
#. You then need to specify the coordinate reference system (CRS) that was used to create the raster so that the raster will appear in the correct geographic location. Upon import, a default CRS will be assigned, which will be the CRS that is currently used by the main map.
#. Depending on the number of bands in your raster, the equivalent number of **Unit Selection Dropdowns** will appear. For each raster band, you need to provide the corresponding units. 

.. _fig-R2DRasterHazardPane:

.. figure:: figures/R2DRasterHazardPane.png
  :align: center
  :figclass: align-center

  Raster hazard input pane.
  
.. note:: When the **Raster Defined Hazard Widget** is employed in an analysis, for each asset, the raster will be sampled at the asset location to determine the hazard intensity level. A set of .csv files in the SimCenter event format (EventGrid.csv) will be created where each grid point corresponds to the location of an asset. As a result, the corresponding **Mapping Application** in **HTA** (Hazard to Asset Mapping) should be set to **Site Specified**. 


Regional Site Response
--------------------------

Site response analysis is commonly performed to analyze the propagation of seismic wave through soil. As shown in :numref:`fig_siteResponse`, 
one-dimensional response analyses, as a simplified method, assume that all boundaries are horizontal and that the response of a soil deposit is
predominately caused by SH-waves propagating vertically from the underlying bedrock. Ground surface response is usually the major output from
these analyses, together with profile plots such as peak horizontal acceleration along the soil profile. When liquefiable soils are presenting,
maximum shear strain and excess pore pressure ratio plots are also important.

.. _fig_siteResponse:
.. figure:: figures/siteResponse.png
   :align: center
   :figclass: align-center

   Schematic figure for site response analysis (courtesy of Pedro Arduino)

**Regional Site Response** consists of four major functionalities for site response analysis, each of which is encapsulated in a specific widget:

.. _fig_siteResponsePane:
.. figure:: figures/R2DSiteResponsePane.png
   :align: center
   :figclass: align-center

   Graphic user interface of Regional Site Response

#. **Site information widget**: three options for defining a set of sites for soil response analysis: (1) ``Single Location``, (2) ``Grid of Locations``, and (3) ``Scattering Locations``.
   Users can manually define or select a rectangular grid on map using the ``Grid of Locations``.
   In addition, users can upload a csv site file using the ``Scattering Locations``. 
   The minimum attributes are: ``Station`` ID column, ``Longitude`` and ``Latitude`` columns.
   Users can add extra columns for soil properties or modeling paramters; alternatively, users could use the **Site Data tool widget**
   to generate needed attributes.
#. **Site data toolbox widget**: three Vs30 data sources are available: (1) Wills et al., 2015 ([Wills2015]_), (2) Thompson et al., 2018 ([Thompson2018]_), and (3) Heath et al., 2020 ([Heath2020]_). 
   There are two data sources of bedrock depth: (1) SoilGrid250 ([Hengl2017]_) and (2) National Crustal Model ([Boyd2020]_). Three soil model types will be available: (1) Elastic isotropic, (2) Multiaxial Cyclic plasticity, and (3) User.
   After selecting the desired data sources and model type, a new site information csv site file will be generated and loaded by clicking the ``Fetch Site Data`` button.
#. **Soil model widget**: a soil modeling script is expected, which will be used to create numerical models from the site information csv and run simulations.
#. **Input motion widget**: a ``EventGrid.csv`` csv file along with a directory including ground motion acceleration time history files are expected.  
   Note that the units of the time history and scaling factor should also be provided by users.

.. [Wills2015]
   Wills, C. J., Gutierrez, C. I., Perez, F. G., & Branum, D. M. (2015). A next generation VS 30 map for California based on geology and topography. Bulletin of the Seismological Society of America, 105(6), 3083-3091.

.. [Thompson2018]
   Thompson, E.M., 2018, An Updated Vs30 Map for California with Geologic and Topographic Constraints: U.S. Geological Survey data release.

.. [Heath2020]
   Heath, D. C., Wald, D. J., Worden, C. B., Thompson, E. M., & Smoczyk, G. M. (2020). A global hybrid VS30 map with a topographic slope–based default and regional map insets. Earthquake Spectra, 36(3), 1570–1584.

.. [Hengl2017]
   Hengl T, Mendes de Jesus J, Heuvelink GBM, Ruiperez Gonzalez M, Kilibarda M, Blagotić A, et al. (2017) SoilGrids250m: Global gridded soil information based on machine learning. PLoS ONE 12(2): e0169748.

.. [Boyd2020]
   Boyd, O.S., 2020, Calibration of the U.S. Geological Survey National Crustal Model: U.S. Geological Survey Open-File Report 2020–1052, 23 p., https://doi.org/10.3133/ofr20201052.

.. [Manzour2016]
   Manzour, H., Davidson, R. A., Horspool, N., & Nozick, L. K. (2016). Seismic hazard and loss analysis for spatially distributed infrastructure in Christchurch, New Zealand. Earthquake Spectra, 32(2), 697-712.

.. [Peterson2020]
   Petersen, M. D., Shumway, A. M., Powers, P. M., Mueller, C. S., Moschetti, M. P., Frankel, A. D., ... & Zeng, Y. (2020). The 2018 update of the US National Seismic Hazard Model: Overview of model and implications. Earthquake Spectra, 36(1), 5-41.
