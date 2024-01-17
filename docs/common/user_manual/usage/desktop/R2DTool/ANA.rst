ANA: Asset Analysis
===================

In this panel, the user can select the applications that will be employed in the analysis of each asset class. The user can select the type of asset from the **Asset Selection Ribbon**, e.g., Buildings and Gas Network, as shown on the left-hand side of :numref:`fig-R2DANAInputPanel`. The **Asset Selection Ribbon** is hidden by default, and appears when more than one type of asset is selected in the **GI: General Information** panel. Additionally, only the assets that are checked in the **GI: General Information** panel will appear in the **Asset Selection Ribbon**. As the user switches between assets, the **Input Panel** in :numref:`fig-buildingModelingPanel` will change to reflect the applications that are available for analyzing each type of asset.

.. _fig-R2DANAInputPanel:

.. figure:: figures/R2DANAInputPanel.png
  :align: center
  :figclass: align-center

  Buildings analysis input panel.

.. contents::
   :local:

Buildings
---------

The applications available for the modeling of buildings are: 

  - OpenSees
  - OpenSeesPy
  - IM as EDP

Currently, the inputs, scripts, commands, etc., for the analysis applications are provided by the modeling applications. Future implementation will allow for the user to customize the analysis applications, e.g., specify the type of solver and convergence test in an OpenSees analysis. 

OpenSees Analysis Model
***********************

The **OpenSees** analysis application employs OpenSees to conduct the structural analysis. Note that when the optional argument "Analysis Script" is provided, the quantities above will be ignored.

.. _fig-R2DANAOpenSees:

.. figure:: figures/R2DANAOpenSees.png
  :align: center
  :figclass: align-center
  :width: 800

  OpenSees analysis option

Following is an example of user-provided :download:`analysis script <src/ANA_OpenSees.tcl>` (.tcl) that additionally sets the "-fullGenLapack 1" flag on top of the selections shown in the above image.

  .. literalinclude:: src/ANA_OpenSees.tcl
      :language: tcl
  
OpenSeesPy Analysis Model
*************************

The **OpenSeesPy** analysis application employs OpenSeesPy to conduct the structural analysis.

IM as EDP Analysis Model
*************************

The **IM as EDP** application forgoes a structural analysis altogether. In this case, the hazard intensity measure (IM) is considered the engineering demand parameter (EDP). 

Pre-trained surrogate models
****************************

The **Pre-trained surrogate model** is used to import the surrogate models trained using `EE-UQ <https://simcenter.designsafe-ci.org/research-tools/overview/>`_. The surrogate model can take the parameters of structure (e.g. initial stiffness, post-yield stiffness, yield drift, construction year etc) and the intensity measures of recorded or stochastically generated ground motions (e.g. peak ground acceleration, peak spectral acceleration, significant duration etc.) as its input. 

.. panels::
   :column: col-lg-12 col-md-12 col-sm-12 col-xs-12 p-2

   .. figure:: figures/R2DANASurrogateWorkflow.png
      :align: center
      :figclass: align-center
      :width: 1200

Step 2 is covered below and `Step 1 <https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html>`_ can be found in EE-UQ documentation. The user needs to fill in two tabs: *Surrogate Models* and *Default Analysis*.


.. _fig-R2DANAInputPanel:

.. figure:: figures/R2DANASurrogateInput.png
  :align: center
  :figclass: align-center

  Buildings analysis input panel.


.. role:: uqblue

:uqblue:`Surrogate Models`

* **Filter script**: a user-provided python script used to assign the surrogate model to individual buildings when multiple surrogate models representing different building types are available. In the script, the user needs to provide a python function named ``model distributor`` that takes two dictionary variables, general information (``GI``) and structural analysis model parameters (``SAM``), as inputs. The function should return either the name of the surrogate model (the name is defined in the user interface) or the string "Default". Below is an example of the filter script.

  .. literalinclude:: src/ANA_surrogate_filter.py

  Below are example keys and values of GI and SAM dictionaries that will be provided to the model.

  .. tabs::

      .. tab:: GI

          .. literalinclude:: src/ANA_GI.json 
              :language: json


      .. tab:: SAM (MDOF-Lu)

          .. literalinclude:: src/ANA_SAM.json
              :language: json

* **Surrogate models**: surrogate model files in JSON (.json) format. Each surrogate model can be separately trained and exported in JSON format through EE-UQ. The surrogate models will take structural parameters (**structure information** and **structural analysis parameters computed in the modeling app** (specified in the MOD tab)), and **ground motion intensity parameters** as inputs. Below, we list the names of the parameters that will be passed to the surrogate model and its example values. When training a surrogate model through EE-UQ, make sure it only expects a subset of the structural variables listed below as inputs (The ground motion parameters are processed automatically internally, so users do not need to be concerned about naming rules on those variables).

   1. Structure information - user-provided inventory data

      .. csv-table:: User-provided structure information
         :file: src/ANA_surrogate_GI.csv
         :header-rows: 1
         :align: center
         :widths: 2, 1, 2,7

   2. Structural properties - the variables created in the modeling (MOD) application (an example of MDOF-LU module for 2 story building) 

      .. csv-table:: Structural parameters estimated by structural modeling app (specified in the MOD tab)
         :file: src/ANA_surrogate_SAM.csv
         :header-rows: 1
         :align: center
         :widths: 2, 1, 2, 7

      See :ref:`lbl-MODMDOFLu` for details. If other custom modeling apps (other than MDOF-LU) are used, "SAM.json" should be manually created by the user with the specified format. See :download:`here <src/ANA_SAM.json>` for an example of SAM.json file.

   3. Ground motion parameters (automatically named internally both in EE-UQ and R2D)

      .. csv-table:: Ground motion parameters
         :file: src/ANA_surrogate_GM.csv
         :header-rows: 1
         :align: center
         :widths: 2, 1, 2, 7

   In R2D workflow, only the intensity measures that were specified when **training** the surrogate model (in EE-UQ) will be automatically computed and passed on to the surrogate model. 

:uqblue:`Default Analysis`
   Select the engine that will be used when "Default" is returned from the **filter script.**