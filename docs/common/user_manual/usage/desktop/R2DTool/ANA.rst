ANA: Asset Analysis
===================

In this panel, users can select specific applications for analyzing different asset classes. To choose an asset type, such as Buildings or Transportation Network, users interact with the **Asset Selection Ribbon** on the left side of the interface as depicted in :numref:`fig-R2DANAInputPanel`. This ribbon is initially hidden and becomes visible when multiple asset types are selected in the **GI: General Information** panel. Only assets marked in the **GI** panel will be listed in the **Asset Selection Ribbon**. Switching between assets updates the **Input Panel** to display the relevant analysis applications for the selected asset type.

.. contents::
   :local:

.. _fig-R2DANAInputPanel:

.. figure:: figures/R2DANAInputPanel.png
  :align: center
  :figclass: align-center

  Buildings analysis input panel.


.. _lbl-ANABuildings:

Buildings
---------

For building analysis, the following applications are supported: 

  - OpenSees
  - OpenSeesPy
  - IMasEDP
  - PreTrained Surrogate Models
  - CustomPy-Simulation
  - None

OpenSees Analysis Model
***********************

The **OpenSees** option performs structural analysis using OpenSees. If an "Analysis Script" argument is provided, the quantities defined with the graphical user interface will be ignored.

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

The **OpenSeesPy** application utilizes OpenSeesPy for structural analysis.

IMasEDP Analysis Model
*************************

The IMasEDP application directly uses the hazard intensity measure (IM) as the engineering demand parameter (EDP), bypassing structural analysis.

Pre-trained surrogate models
****************************

The **Pre-trained surrogate model** is used to import the surrogate models trained using `EE-UQ <https://simcenter.designsafe-ci.org/research-tools/overview/>`_. The surrogate model can take the parameters of structure (e.g. initial stiffness, post-yield stiffness, yield drift, construction year etc) and the intensity measures of recorded or stochastically generated ground motions (e.g. peak ground acceleration, peak spectral acceleration, significant duration etc.) as its input. 

.. panels::
   :column: col-lg-12 col-md-12 col-sm-12 col-xs-12 p-2

   .. figure:: figures/R2DANASurrogateWorkflow.png
      :align: center
      :figclass: align-center
      :width: 1200

Refer to `Step 1 <https://nheri-simcenter.github.io/EE-UQ-Documentation/common/user_manual/usage/desktop/SimCenterUQSurrogate.html>`_ in the EE-UQ documentation for initial steps. Users must complete the *Surrogate Models* and *Default Analysis* tabs to use pre-trained surrogate models.

.. _fig-R2DANASurrogateInputPanel:

.. figure:: figures/R2DANASurrogateInput.png
  :align: center
  :figclass: align-center

  Buildings analysis input panel.


.. role:: uqblue

:uqblue:`Surrogate Models`

* **Filter script**: A Python script provided by the user to assign surrogate models to buildings when multiple surrogate models representing different building types are provided. The script should contain a function named ``model distributor`` that processes dictionary inputs for general information (``GI``) and structural analysis model parameters (``SAM``), returning the surrogate model name or "Default". Below is an example of the filter script.

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

   2. Structural properties - variables from the modeling (MOD) application (example for a 2-story building using MDOF-LU) 

      .. csv-table:: Structural parameters estimated by structural modeling app (specified in the MOD tab)
         :file: src/ANA_surrogate_SAM.csv
         :header-rows: 1
         :align: center
         :widths: 2, 1, 2, 7

Refer to :ref:`lbl-MODMDOFLu` for more details. Custom modeling apps should follow the specified format for "SAM.json". See :download:`here <src/ANA_SAM.json>` for an example of SAM.json file.

   3. Ground motion parameters (automatically named internally both in EE-UQ and R2D)

      .. csv-table:: Ground motion parameters
         :file: src/ANA_surrogate_GM.csv
         :header-rows: 1
         :align: center
         :widths: 2, 1, 2, 7

R2D ensures only the intensity measures specified during the training of the surrogate model are computed and utilized.

:uqblue:`Default Analysis`
   Choose the analysis engine for cases where the **filter script** returns "Default".

.. _lbl-ANATransport:

Transportation Infrastructure Analysis
---------------------------------------


IMasEDP Analysis Model
*************************

Similar to buildings, the IMasEDP application for transportation infrastructure uses the hazard intensity measure (IM) directly as the engineering demand parameter (EDP), bypassing structural analysis.