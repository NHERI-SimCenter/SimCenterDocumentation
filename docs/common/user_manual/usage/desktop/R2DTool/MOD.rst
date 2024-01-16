MOD: Asset Modeling
===================

In this panel, the user can select the applications that will be used to model each asset class. The user can select the type of asset from the **Asset Selection Ribbon**, e.g., Buildings and Gas Network, as shown on the left-hand side of :numref:`fig-buildingModelingPanel`. The **Asset Selection Ribbon** is hidden by default, and appears when more than one type of asset is selected in the **GI: General Information** panel. Additionally, only the assets that are checked in the **GI: General Information** panel will appear in the **Asset Selection Ribbon**. As the user switches between assets, the **Input Panel** in :numref:`fig-buildingModelingPanel` will change to reflect the applications that are available for the modeling of each type of asset. 

.. _fig-buildingModelingPanel:

.. figure:: figures/R2DMODInputPanel.png
  :align: center
  :figclass: align-center

  Buildings modeling input panel.

.. contents::
   :local:

.. _lbl-MODBuildings:

Buildings
---------

The applications available for the modeling of buildings are: 

	- MDOF-LU Building Model
	- OpenSeesPy Building Model


.. _lbl-MODMDOFLu:

MDOF-LU Building Model
**********************

The **MDOF-LU** building modeling application creates a hysteretic, multi-degree of freedom (MDOF) model from the user-provided high-level building information. The implementation is a variation of work of [Lu2020]_. The module essentially takes the building inventory information (construction year, structural type, plan area, and the number of stories) provided by the user in ASD tab, determines the design code level (e.g. high code, low code), and creates an Opensees model of each building. The following are the needed information.

.. _fig-MDOFLUModelingPanel:

.. figure:: figures/R2DMDOFLUBuildingModel.png
  :align: center
  :figclass: align-center
  :width: 80%

* **Hazus Data File:** The path to a file that contains the ruleset that maps the design code-level & structural types to various structural parameters. :download:`Here <src/MDOF_Lu_HazusData.txt>` is an example file, where the columns are in the order of

    .. collapse:: Column names of HazusData.txt (click)

      .. csv-table:: Column names of HazusData.txt (showing the first 10 rows for high-code) 
         :file: src/MOD_Lu_HazusData_display.csv
         :header-rows: 1
         :align: center


  See :numref:`fig-MDOFLUModelingHys` for the parameter definitions. Note that not all the parameters are being used.

* **Std deviation Stiffness:** The standard deviation of lateral stiffness of the building model. The randomness will be applied by sampling a multiplication factor with the specified standard deviation and mean of 1. The factor is sampled only once per structure and will be applied to all stories.
* **Std deviation Damping:** The standard deviation of the damping ratio of the building model. The randomness will be applied by sampling a multiplication factor with the specified standard deviation and mean of 1. 
* **Default Story Height (optional):** Used to set the mass node coordinates.

Once the analysis is done, the estimated structural parameters are written in ``SAM.json`` and the corresponding opensees model is written in ``example.tcl`` (with  `uniaxialMaterial Hysteretic <https://opensees.berkeley.edu/wiki/index.php/Hysteretic_Material>`_ material model) for the downstream analysis. Both files can be found in the local working directory. 

    .. collapse:: Example of SAM.json (click)

      .. literalinclude:: src/MOD_Lu_SAM.json
          :language: json

    .. collapse:: Example of opensees.tcl (click)

      .. literalinclude:: src/MOD_Lu_example.tcl
          :language: tcl
          :emphasize-lines: 1,2,3,4,5,6,7,8,9,10,11

where the keys of ``SAM.json`` are defined as follows:

.. _fig-MDOFLUModelingHys:

.. figure:: figures/R2DMDOFLU_Hysteresis.png
  :align: center
  :figclass: align-center
  :width: 400

  MDOF-LU Building model.  

.. csv-table:: Structure parameters estimated from MDOF-Lu
  :file: src/MOD_SAM.csv
  :header-rows: 1
  :align: center
  :widths: 2, 1, 7
   \* `see here for details on unloading stiffness <https://portwooddigital.com/2022/04/17/hysteretic-damage-parameters/>`_

.. note:: When the **MDOF-LU** building modeling application is employed, the **OpenSees** simulation application should be used for analysis in the **ANA: Asset Analysis** input panel. 


.. [Lu2020] Lu, X., McKenna, F., Cheng, Q., Xu, Z., Zeng, X., & Mahin, S. A. (2020). An open-source framework for regional earthquake loss estimation using the city-scale nonlinear time history analysis. Earthquake Spectra, 36(2), 806-831.

OpenSeesPy Building Model
*************************

The **OpenSeesPy** building modeling application creates an OpenSeesPy structural model from a user-defined Python script. The input panel, shown in :numref:`fig-R2DOpenSeesPyBuildingModel`, has the following inputs:

	#. **OpenSeesPy Script:** Script containing the code to create the building model. 
	#. **Node Response Mapping:** By default, the workflow assumes X=1, Y=2, Z=3 mapping between the *x,y,z* directions and degrees of freedom, with *x* and *y* being the horizontal directions. This input allows you to define an alternative mapping by providing three numbers separated by commas in a string, such as ‘1, 3, 2’ if you wish to have *y* as the vertical direction.
	#. **Analysis Spatial Dimensions:** Number of dimensions in the OpenSeesPy analysis.
	#. **Degrees-of-Freedom at Node:** Number of degrees-of-freedom at each node. 

.. _fig-R2DOpenSeesPyBuildingModel:

.. figure:: figures/R2DOpenSeesPyBuildingModel.png
  :align: center
  :figclass: align-center

  OpenSeesPy Building model input panel.

.. _lbl-MODTransport:

Transportation Infrastructure
-----------------------------
Only the Intensity Measure as Engineering Demand Parameter (**IMasEDP**) type of analysis is supported for transportation infrastructure analysis now. The asset models should be **None** for **IMasEDP** analyses. 




