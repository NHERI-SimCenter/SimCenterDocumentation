.. _lbl-geometry:

***********************************************
Geometry
***********************************************

There are four aspects related to the definition of geometry, namely geometry of the ocean floor or wave flume, buildings or specimens, floating bodies, and shallow water to CFD interface. This section discusses the setup of all aspects of geometry.

Bathymetry
==============

The geometry can be provided either in terms of the bathymetry of the ocean floor, an STL file, or the wave flume digital twin. The geometry definition is based on the type of ``Simulation type`` chosen in the :ref:`lbl-projsett`. The geometry definition for each of the simulation types has been outlined below.

.. dropdown:: Shallow-water to CFD coupling

    .. include:: Geometry/Geom_SWCFD.rst

.. dropdown:: Bathymetry

    .. include:: Geometry/Geom_Bathy.rst

.. dropdown:: STL file

    .. include:: Geometry/Geom_STL.rst

.. dropdown:: Wave flume

    .. include:: Geometry/Geom_WFlume.rst


SW-CFD interface
===================

The shallow-water to CFD interface can only be defined for the simulation type where CFD is used to resolve the shallow-water solutions. The interface is specified using a ``.csv`` file and uploaded as shown in :numref:`SWCFDInter`.

.. _SWCFDInter:

.. figure:: Geometry/figures/swcfd_Interface.png
   :align: center
   :width: 400
   :figclass: align-center

   Uploading the ``.csv`` file that defines the interface

Consider the problem description as shown in the :numref:`SWCFDInter2`. Consider an event (earthquake on a fault or low-pressure due to a hurricane) represented by the red line on the left. The shallow-water solvers are used over the Ocean domain. In order to provide a high-fidelity solution for the structural response, the shallow-water domain is further refined using 3D CFD. The yellow boxes represent the shallow water to CFD interfaces. This interface information is provided in a ``.csv`` file. 

.. _SWCFDInter2:

.. figure:: Geometry/figures/SWCFD02.png
   :align: center
   :width: 400
   :figclass: align-center

   Visual depiction of the shallow water to CFD interface

A typical interface file is shown below.

.. literalinclude:: Geometry/SWCFDInter.csv

The ``.csv`` needs four patches to be explicitly defined. The first is the patch name, followed by the ``x`` and ``y`` coordinates of the first and second points. The order of the points or the patches do not matter. The physical meaning of the patch names are as given below:

#. **Entry** - This is the patch for the inlet of the fluid from the shallow water to the CFD domain.
#. **Exit** - This is the patch for the fluid outlet from the CFD domain. 
#. **Right** - This is generally a patch on the right. Here, if one were to stand at the inlet and face the outlet, this is the boundary on the right. 
#. **Left** - This is generally a patch on the left. Here, if one were to stand at the inlet and face the outlet, this is the boundary on the left. 

.. note::

    #. It is necessary that the point provided to define the interface needs to be closed and a quadrilateral.

    #. The patch names need to be provided to identify appropriate boundaries.

Buildings/specimens
========================

Buildings or specimens can be defined in the ``EVT``. It is important here to note that there can be two types of buildings: (a) Building of interest for which the structural response is measured (b) Other neighboring buildings that impact the flow fields.

These can either be defined manually in a tabular format or parametrically as shown in :numref:`BuildDef`.

.. _BuildDef:

.. figure:: Geometry/figures/Building.png
   :align: center
   :width: 500
   :figclass: align-center

   Building definition in the ``EVT``

For the manual definition of the building, a tabular format is used for the user to specify:

#. **Building type (type):** This refers to the shape and type of building. An index is used to identify the type of building:

    #. **-2**: This is the building on which the structural response is required. The building definition is as provided in the ``GI`` widget tab earlier. Here the building shape is generally cuboid.

    #. **-1**: This is the building on which the structural response is required. However, this is provided in the ``SIM`` tab as an OpenSees script for complicated building shapes. For this type of building, please also upload the ``STL`` file, in ASCII format, for the building shape. This is required to accurately capture the flow fields around the building.

    #. **1**: This is a building on which structural response is not desired. However, this is present in the neighborhood and can significantly affect the flow fields. The shape of the building is cuboid here.

    #. **2**: This is a building on which structural response is not desired. However, this is present in the neighborhood and can significantly affect the flow fields. The shape of the building is more complex and provided through an ``STL`` file in ASCII format.

    .. note::

        At present, HydroUQ only supports one type of building to be defined using a ``STL`` geometry. This file needs to be in ASCII format. This limitation will be removed in the upcoming versions.

#. **Center:** This refers to the location of the building/specimen. This is defined in terms of the coordinates (``x`` , ``y`` , ``z``) or latitude-longitude depending on the type of simulation chosen earlier in :ref:`lbl-projsett`. Suppose the simulation is based on shallow-water to CFD or bathymetry settings. In that case, the latitude and longitude need to be specified. Else, the position is input in terms of the coordinates.

    .. note::

        Here, the building position refers to the center of the bottom surface of the building. Thus, one needs to appropriately calculate the position of the building.

#. **Parameters:** This refers to the building's length, breadth, and height definition. This is required only for building types **1**. The parameters for the other types will be extracted either from the ``STL`` files or the ``GI`` widget tab.

The parametric definition of the building is recommended for usage mainly for the flume. This is recommended for usage when all the buildings are of the same shape and size. Here, the buildings are automatically generated based on a set of parametric inputs. The building of interest is directly determined by the |app| by using the coordinate information from the ``GI`` tab and matching it with the nearest building. The set of parameters include:

#. **Number of buildings along the coast:** This refers to the number of building in the direction orthogonal to the flow, i.e., between right and left interfaces or walls of the CFD domain.

#. **Number of buildings into the coast:** This refers to the number of buildings in the flow direction, i.e., between entry and exit of the CFD domain.

#. **Distance from coast:** This refers to the distance of the first building from (0,0).

#. **Distance between buildings (Side):** This refers to the center-to-center distance between the buildings in the direction orthogonal to the flow. 

#. **Distance between buildings (Front):** This refers to the center-to-center distance between the buildings in the flow direction. 

#. **Building size:** Here, it is required to specify the building's length - breadth - height. This information can be the size of the building (for those with a cuboidal shape). Alternatively, this is the box into which an irregular building can be fitted.

#. **Coordinate of coastline center:** This refers to the center of the coastline from the global (0,0) of the domain.

#. **Building shape:** Here, two-building shapes are possible, i.e., cuboid or user-defined as shown in :numref:`BuildShape`. If the building shape is user-defined, then an ``STL`` file in ASCII format needs to be uploaded. 

    .. _BuildShape:

    .. figure:: Geometry/figures/BuildShape.png
        :align: center
        :width: 400
        :figclass: align-center

        Building shape definition in the ``EVT``

#. **Distribution of buildings:** This refers to the distribution of the buildings. At present, this can be simple or staggered, as shown in :numref:`BuildDist`.

    .. _BuildDist:

    .. figure:: Geometry/figures/BuildDist.png
        :align: center
        :width: 400
        :figclass: align-center

        Building distribution definition in the ``EVT``

Floating bodies
===================

The present version of the HydroUQ does not facilitate floating bodies. These would be added to the upcoming versions of |app|.