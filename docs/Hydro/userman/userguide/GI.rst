.. _lbl-GIGenInfo:

GI: General Information
=======================

The **GI** tab allows the user to provide information about the building and the units the user will work with. The widget contains the following four frames, as shown in :numref:`figGI`.

#. **Building Information**: Collects general information about the building. This includes the name of the building.

#. **Properties**: Collects information about the number of stories, width, depth, plan area and height of the building.

#. **Location**: Collects information about the location of the building. This information is used by some event widgets to characterize events that are specific to the building location. 

	.. note::   

		#. For the events where the geometry is defined using bathymetry, the location is specified using the latitude and longitude

		#. For events where geometry is a wave flume or STL files are used, then the location should be specified as :math:`x` and :math:`y`

#. **Units**: Collects information about the units used in the inputs and outputs. Some widgets will require inputs in different units. Those widgets will display units beside those special entry fields.

.. _figGI:

.. figure:: figures/gi.png
	:align: center
	:figclass: align-center
	:height: 500px

	General information input panel.