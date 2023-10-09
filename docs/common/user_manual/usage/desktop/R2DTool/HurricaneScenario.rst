.. _hurricane_scenario_tool:

Hurricane Scenario
------------------

This tool dialog is where user can enter data for a specific Hurricane and it will generate a wind field for a specific region..

The **Hurricane Scenario Simulation**, seen in :numref:`fig-R2DHurricaneMainPanel`, is an tool that calculates a wind field over a user defined grid. The application is implemented based on the method proposed by [SnaikiWu2017a]_ and [SnaikiWu2017b]_. The GIS visualization window, seen at the bottom of :numref:`fig-R2DHurricaneMainPanel`, is used to interactively define hurricane inputs. At a minimum, a user needs to specify a set of hurricane track points, landfall location and parameters, and a wind field grid. The individual input panes are discussed below.

.. _fig-R2DHurricaneMainPanel:

.. figure:: figures/R2DHurricaneMainPanel.png
  :align: center
  :figclass: align-center

  Hurricane Scenario Simulation Application.

**Hurricane Definition**

A user has the option to specify a hurricane track and associated landfall parameters, or select a historical hurricane from a built-in database.

    #. **Specify Hurricane Track**

	To manually input a hurricane track, the user needs to supply a ``.csv`` file with rows that contain the latitude and longitude coordinates of the points along the track. To input the hurricane track file, the user needs to specify the file path in the **Path to Hurricane Track File** input shown in :numref:`fig-R2DHurricaneTrackSelectPane`. A successfully loaded track is shown at the top of :numref:`fig-R2DHurricaneTrackSelectPane`. The circles represent a measurement point along the track and the arrow head shows the direction of the hurricane. Clicking on a circle will produce a dialog with the available information at that point.

	.. _fig-R2DHurricaneTrackSelectPane:

	.. figure:: figures/R2DHurricaneTrackSelectPane.png
	  :align: center
	  :figclass: align-center

	  Manually defined hurricane track.
	  	  
	An example hurricane track input file is given below in  :numref:`fig-R2DHurricaneTrackSelectExData`. The track data should be in temporal order, i.e., the first measurement should be in the first row of the input file.
	
	.. _fig-R2DHurricaneTrackSelectExData:

	.. figure:: figures/R2DHurricaneTrackSelectExData.png
	  :align: center
	  :figclass: align-center

	  Example data for hurricane track input.
	  
	Users also have the option to specify a terrain roughness file in the ``.geojson`` format. Users need to provide the path to the terrain roughness file in the **Path to Terrain Roughness File** input, given in :numref:`fig-R2DHurricaneTrackSelectPane`. When loaded, the terrain roughness file will be visualized in the GIS window, as highlighted at the bottom of :numref:`fig-R2DHurricaneTrackSelectPane`. If a terrain roughness is not specified, a default value of 0.03 m is used (assuming open/flat terrain few isolated obstacles). 
		  
    #. **Select Hurricane from Database**

	The panel to select a historical hurricane is shown in :numref:`fig-R2DHurricaneTrackDB`. Clicking on the **Load Hurricane Database** button will load the database and all of the hurricanes in the database will appear in the GIS window, as shown at the bottom of :numref:`fig-R2DHurricaneTrackDB`. The database that is pre-bundled with the application is the International Best Track Archive for Climate Stewardship (IBTrACS) v04r00 database, listing storms that have occurred in the last three years. Users can modify the ``.csv`` database file, e.g., update it or add their own storm information, if the same header format and file name (ibtracs.last3years.list.v04r00.csv) is retained. Users can find this file in the ``Databases`` folder that is in the R2D installation directory. 

	.. _fig-R2DHurricaneTrackDB:

	.. figure:: figures/R2DHurricaneTrackDB.png
	  :align: center
	  :figclass: align-center

	  Hurricane selection from database.
			  
	To load a specific hurricane, a user needs to navigate to a hurricane of their choice in the GIS window and click on the hurricane to select it. The selected hurricane will be highlighted, as shown in :numref:`fig-R2DHurricaneTrackDB2`, and a dialog will appear providing the hurricane track metadata. Clicking on the **Select Hurricane Button** in :numref:`fig-R2DHurricaneTrackDB2` will finalize the selection. The selected hurricane's metadata will appear in the box that is given in the middle of :numref:`fig-R2DHurricaneTrackDB`.
			
  	.. _fig-R2DHurricaneTrackDB2:

  	.. figure:: figures/R2DHurricaneTrackDB2.png
  	  :align: center
  	  :figclass: align-center

  	  Selecting a hurricane from the map.
			
	After selecting a hurricane, a user will see the final hurricane track, similar to what is shown in :numref:`fig-R2DHurricaneTrackDB3`. The circles represent a measurement point along the track. Clicking on a circle will produce a dialog with the available information at that point. The blue diamond represents the first point of hurricane landfall, i.e., the first point at which the distance to land is equal to zero. If a landfall location is found, the landfall parameters are programmatically filled in with the measurements at the landfall location. In the case where a hurricane makes landfall more than once, the user has the option to clear the initial landfall point, and select another landfall point, the procedure of which is described below. Note that if a new landfall location is selected by the user, except for the latitude and longitude which is updated programmatically, users should manually update the landfall parameters to agree with the expected parameter values at new location.
	
  	.. _fig-R2DHurricaneTrackDB3:

  	.. figure:: figures/R2DHurricaneTrackDB3.png
  	  :align: center
  	  :figclass: align-center

  	  Output after hurricane selection.	

**Hurricane Landfall Parameters**

This is where the user inputs the hurricane landfall parameters. Hurricane landfall occurs when the center of the storm moves across a coastline after traversing open water. Shown in :numref:`fig-R2DHurricaneLandfallParams`, the user must supply the following parameter values:

	- Latitude in degrees North
	- Longitude in degrees East
	- Landing, or approach angle, in degrees
	- Speed in knots (kts)
	- Pressure in millibars (mb)
	- Radius in nautical miles (nmile)
	- Exposure category to classify terrain roughness
	- Gust duration in seconds (s)
	- Reference height in meters (m). 
	
Note that if a track is selected from the database, the landfall parameters will be automatically filled in based on the first encountered landfall. The **Perturbation** input boxes allow the user to specify uncertainty in the parameter values.  

.. _fig-R2DHurricaneLandfallParams:

.. figure:: figures/R2DHurricaneLandfallParams.png
  :align: center
  :figclass: align-center

  Hurricane Landfall Parameters.
	  
**Specify Landfall Location**

The hurricane landfall location is manually defined using the buttons in :numref:`fig-R2DHurricaneLandfallSelect`. Clicking on the **Define Landfall on Map** button causes a blue circle to appear in the GIS window, as seen in the righthand side of the window in :numref:`fig-R2DHurricaneLandfallParams`. A user can click on and drag this circle to any location on the map. When the user is satisfied with their new landfall location, they need to click on the **Select Landfall** button to finalize the selection. The landfall will then appear as a blue diamond symbol in its own layer in the GIS window. If a user wants to erase an existing landfall location, they need to click on the **Clear Landfall** button and start over. 

.. _fig-R2DHurricaneLandfallSelect:

.. figure:: figures/R2DHurricaneLandfallSelect.png
  :align: center
  :figclass: align-center

  Specify Hurricane Landfall.

**Truncate Hurricane Track**

R2D allows users to truncate hurricane tracks to save time in the wind field computations. This is also useful when a user requires only a portion of a hurricane track in their region of interest. The buttons for truncating a hurricane track are shown in :numref:`fig-R2DHurricaneTruncateTrack`. Clicking on the **Select Area on Map** button in the figure will turn on the selection procedure. Clicking on any point in the GIS window will start the selection process. Continuing the point selection procedure by clicking elsewhere on the map will form the boundary of the selection polygon, an example of which is provided in :numref:`fig-R2DHurricaneTruncateTrack`. Right-clicking anywhere on the map, or my pressing the escape key, will clear the polygon and select the points within the polygon. The selected points will be highlighted in yellow.The selection points can be cleared at any time by pressing the **Clear** button. Clicking on the **Apply** button will finalize the selection. The yellow-highlighted track points that are selected will be kept and all other points will be discarded. Note that once the **Apply** button is pressed, the procedure cannot be undone. An example truncated track is given in the left-hand side of the GIS window in :numref:`fig-R2DHurricaneTruncateTrack`.
	
.. _fig-R2DHurricaneTruncateTrack:

.. figure:: figures/R2DHurricaneTruncateTrack.png
  :align: center
  :figclass: align-center

  Truncate Hurricane Track.
  
**Specify Wind Field Grid**

To select the wind field grid on a map, the user needs to click on the **Define Grid on Map** button. A new grid will appear in the GIS window, as seen in :numref:`fig-R2DHurricaneDefineGrid`. A user can click and drag the **Resize** and **Move** handles, shown in :numref:`fig-R2DHurricaneDefineGrid`, to resize the grid extents and to move the grid. Changing the grid discretization along the latitude and longitude directions will change the number of grid divisions on the map. Once a grid is defined on the map, the user needs to click on the **Select Grid** button to finalize grid selection. When grid selection is finalized, a new layer is added to the GIS widget. Shown on the right-hand side of :numref:`fig-R2DHurricaneDefineGrid`, the wind field grid points are represented with a cross symbol. Clicking on the **Clear Grid** button will clear the existing grid, allowing for the selection of a new grid. 
	
.. _fig-R2DHurricaneDefineGrid:

.. figure:: figures/R2DHurricaneDefineGrid.png
  :align: center
  :figclass: align-center

  Hurricane Wind Field Grid.

**Run Simulation Button**

Shown on the right-hand side of :numref:`fig-R2DHurricaneMainPanel`, the **Run Simulation** button starts the hurricane simulation application. The results from the simulation are in the **Output Directory** folder specified in R2D preferences. The final output is a ``.csv`` file called ``EventGrid.csv``. The ``EventGrid.csv`` file contains the grid point locations and file names. Each grid point is assigned a ``.csv`` file containing a list of the peak wind speeds at the grid point. The ``EventGrid.csv`` is post-processed and the grid points created in the **Specify Wind Field Grid** step will be updated with the Peak Wind Speed values that are calculated in the simulation. Clicking on a grid point will produce a popup listing the wind speeds at that point. 

User-specified Hurricane
--------------------------

The **User-specified Hurricane** application loads the results of a **Hurricane Scenario Simulation** that was shown previously. The **User-specified Hurricanes** application input pane is given in :numref:`fig-R2DUserSelectWindField`. As seen in the figure, the user is required to input the file path to the ``EventGrid.csv`` file. If the wind and/or inundation field stations are not in the same folder as the ``EventGrid.csv`` file, then the user needs to input the directory path to the folder containing the wind and/or inundation field station files. The user also needs to specify the units of the intensity measure field. 

.. _fig-R2DUserSelectWindField:

.. figure:: figures/R2DUserSelectWindField.png
  :align: center
  :figclass: align-center                     




