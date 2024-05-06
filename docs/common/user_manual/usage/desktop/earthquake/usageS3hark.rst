.. _lbl-usageS3hark:

Site Response Analysis
--------------------------

|s3harkName| allows users to determine the event at the base of the building by performing an effective free-field site response analysis of a soil column. 
In this panel, the user specifies a ground motion at the bottom of the soil column. 
After the soil layers have been properly defined, the motion at the ground surface is given at the end of the analysis 
and that motion can be used in the simulation of the building response.

The full user graphic interface looks like what is shown in :numref:`ui`

.. _ui:

.. figure:: ./figures/s3harkFigures/editing.png
	:align: center
	:figclass: align-center

	Full Graphic Interface

Clicking the arrow between the :ref:`Soil Column Graphic <profileColumn>` and the :ref:`FE Mesh Graphic <mesh>` will hide the FE Mesh Graphic, 
which makes the UI look like what is shown in :numref:`ui2`.

.. _ui2:

.. figure:: ./figures/s3harkFigures/editing2.png
	:align: center
	:figclass: align-center

	Collapse Graphic Interface 



The UI of |s3harkName| consists of the following components:

.. _profileColumn:

Soil Column Graphic
^^^^^^^^^^^^^^^^^^^

The first graphic on the left of the panel shows a visualization of the soil column created. 
Each layer has a different randomly generated color.
When the user adds or deletes a soil layer, this graphic will refresh. 

.. _mesh:

FE Mesh Graphic
^^^^^^^^^^^^^^^
The second graphic on the left shows the finite element mesh and profile plots. 
Upon the finish of the analysis, select any of the tabs on the right inside this graphic (i.e., PGA, :math:`\gamma max`, maxDisp, maxRu, maxRuPWP) 
will show various results from the simulation at the mesh points.

Operations Area
^^^^^^^^^^^^^^^
The right side of this area shows some information on the created soil column, such as the total height and number of soil layers.
The user also finds the Ground Water Table (GWT) input field, plus and minus buttons in this area.
If the user presses the plus button, a layer will be added below a currently selected layer. 
If the minus button is pressed the currently selected layer will be removed. 
The GWT input field allows the user to specify the level of the groundwater table.

.. note:: 

   - Variables are assumed to have m, kPa, and kN units in |s3harkName|.

Soil Layer Table
^^^^^^^^^^^^^^^^
This table is where the user provides the characteristics of soil layers, such as layer thickness, density, Vs30, material type, and element size in the finite element mesh. Single click at a cell will make a soil layer, which will highlight the layer using green color in the table. Also the layer will be highlighted by a red box in the :ref:`Soil Column Graphic <profileColumn>`. Meanwhile the :ref:`Layer Properties Tab <layerPropertiesTab>` will be activated. Double-click a cell to edit it in the table. If you change the ``Material`` cell of a layer, the :ref:`Layer Properties Tab <layerPropertiesTab>` will change correspondingly.

Tabbed Area
^^^^^^^^^^^
This area contains the three tabbed widgets described below.

Configure Tab
"""""""""""""
This tab allows the user to specify the paths to the OpenSees executable and a ground motion file that represent the ground shaking at the
bedrock. The rock motion file must follow the SimCenter event format. 
Examples of SimCenter event files are available in the :download:`motion demos <https://nheri-simcenter.github.io/s3hark-Documentation/_downloads/4aad74c55afc9d112aa4bb1963afa7f7/DemoGM.zip>`. 
|s3harkName| will determine whether to use a 2D column or 3D column based on the ground motion file provided. 
When a ground motion file is selected from the local computer or the path of the ground motion file is typed in, 
|s3harkName| will figure out if it’s a 1D or 2D shaking file. If it’s 1D shaking, all elements will be 2D. If it’s 2D shaking, 
all elements will be 3D. 
The definitions of 2D and 3D slope are different. See :numref:`slope-2d` and :numref:`slope-3d`.

More details about this tab can be found in :ref:`configure`.

.. _layerPropertiesTab:

Layer Properties Tab
""""""""""""""""""""
This tab allows the user to enter additional material properties for the selected soil layer :numref:`layerEditing`.

.. _layerEditing:

.. figure:: ./figures/s3harkFigures/editing.png
	:align: center
	:figclass: align-center

	Layer properties

.. _responseTab:

Response Tab
""""""""""""
Once the site response analysis has been performed, this tab provides information about element and nodal time varying response quantities. See :numref:`response`.

.. _response:

.. figure:: ./figures/s3harkFigures/response.png
	:align: center
	:figclass: align-center

	Response


Analyze Button
^^^^^^^^^^^^^^
This **Analyze** button is located at the top-right corner of the UI and shall be used to run the simulation locally on your computer. 
A progress bar will show up at the bottom of the application indicating the status of the analysis. 
Upon the finish of the simulation, a message will be displayed (:numref:`done`). 

.. _done:

.. figure:: ./figures/s3harkFigures/analysis.png
	:align: center
	:figclass: align-center

	Analysis is done

View Results
^^^^^^^^^^^^
Click the button to dismiss the message window, the response tab will be activated. The user can click on any element in the mesh graphic, the selected element will be highlighted in red and the selected nodes will be pointed out by blue arrows. The time history of the selected element/node will be shown in the :ref:`Response Tab <responseTab>`. This allows the user to review the ground motion predicted at selected nodes :numref:`responseNode`.

.. _responseNode:

.. figure:: ./figures/s3harkFigures/noderesponse.png
	:align: center
	:figclass: align-center

	Response at a selected node


.. note:: 

   - If the Analyze button is not pressed, no simulation will be performed, therefore no simulation is performed and there will be no ground motions provided to the building if you are using |s3harkName| inside other SimCenter applications.



.. _configure:

Configure
^^^^^^^^^

.. _configure-1d:

.. figure:: ./figures/s3harkFigures/configure-1d.png
	:align: center
	:figclass: align-center

	Configuration with a 1D shaking motion

In the configure tab, two paths need to be specified. You can either type them or click the '+' button to select them from your computer. If you don't have OpenSees installed, the instruction can be found :ref:`here <https://nheri-simcenter.github.io/s3hark-Documentation/common/user_manual/quickstart/quickstart.html#download-and-install-opensees>`. If you don't have a ground motion file, demos can be downloaded :download:`here <https://nheri-simcenter.github.io/s3hark-Documentation/_downloads/4aad74c55afc9d112aa4bb1963afa7f7/DemoGM.zip>`.

.. note:: 

   - Variables are assumed to have m, kPa, and kN units in |s3harkName|.    

The first demo is SRT-GM-Input-Style3.json, which contains the shaking motion in one direction (1D shaking). 
If you select this file as the input motion, your tab will look like the one shown in :numref:`configure-1d`. 
You can edit the slope degree :math:`\alpha`. For flat ground, the value should be set as 0. 
If 1D shaking motion provided, |s3harkName| automatically treats the problem as a 2D plane strain problem. 
2D elements will be used. The slope diagram is plotted in :numref:`slope-2d`.

.. _slope-2d:

.. figure:: ./figures/s3harkFigures/slope2d.png
	:align: center
	:figclass: align-center

	Slope definition for 2D Column

The second demo is SRT-GM-Input-Style3-2D.json, which contains the shaking motion in two directions (2D shaking). 
If you select this file as the input motion, your tab will look like the one shown in :numref:`configure-2d`.


.. _configure-2d:

.. figure:: ./figures/s3harkFigures/configure-2d.png
	:align: center
	:figclass: align-center

	Configuration with a bi-directional shaking motion

You can see |s3harkName| detected the file you provided is a 2D shaking, 
|s3harkName| automatically treats the problem as a 3D problem. 
3D elements will be used. The slope diagram is plotted in :numref:`slope-3d`:


.. _slope-3d:

.. figure:: ./figures/s3harkFigures/slope3d.png
	:align: center
	:figclass: align-center

	Slope definition for 3D Column

For flat ground :math:`\alpha` and :math:`\beta` should be set as 0. 


Modeling Spatial Variability Uncertainty of Soil
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most recent version of |s3harkName| allows the user to include spatial variability in the definition of soil profile.
This functionality is achieved using several newly added SimCenter backend python scripts.

Generating Gaussian Random field
""""""""""""""""""""""""""""""""

Physical properties of soils vary from place to place within a soil deposit due to varying geologic formation
and loading histories such as sedimentation, erosion, transportation, and weathering processes.
This spatial variability in the soil properties cannot be simply described by a mean and variance since
the estimation of the two statistic values does not account for the spatial variation of the soil property
data in the soil profile. Spatial variability is often modeled using two separated components: a known deterministic
trend and a residual variability about the trend. These components are illustrated in :numref:`fig_InherentVariability`.

.. _fig_InherentVariability:

.. figure:: ./figures/s3harkFigures/InherentVariability.png
    :scale: 60 %
    :align: center
    :figclass: align-center

    Inherent soil variability (after :cite:`Phoon1999`).

This simplified spatial variability proposed by :cite:`Phoon1999` can be expressed as,

.. math::

  \xi (z) = t(z) \; + \; w(z)\,,

where :math:`\xi(z)` = soil property at location :math:`z`, :math:`t(z)` = deterministic trend at :math:`z`, and :math:`w(z)` =
residual variation. The trend is a smooth deterministic function that can be obtained from a regression analysis of measured data.
The residuals are characterized statistically as random variables, usually with zero mean and non-zero variance.
The pattern of the residuals depends on the local spatial variability of a property. The residual about a trend
does not change erratically in a probabilistically independent way. Rather, similar property values (positive or
negative residuals around a trend) occur together in adjacent locations characterizing the scale of fluctuation
(or wavelength of a residual along the trend) as shown in :numref:`fig_InherentVariability`.

Gaussian stochastic random fields are generated for the liquefiable soil layer by randomizing the assigned
soil strength parameter over the soil layers with a certain spatial probability density.
:cite:`Shin2007` introduced a procedure for generating stochastic random field based on the method outlined in
:cite:`Yamazaki1988` considering uncertainties in soil properties. As explained earlier, the stochastic random
field for a soil property consists of a trend (or mean) field and a residual field,

.. math::
  F_{stochastic} = F_{trend} \; + \; F_{residual} \,.

The trend field (:math:`t(z)`) represents the deterministic mean field assigned by the user. To obtain the
residual field (:math:`w(z)`), a Gaussian random field can be generated using the algorithm proposed by :cite:`Yamazaki1988`.
A normal distribution with a coefficient of variation, *COV*, is required. The scale of fluctuation is defined by correlation
length. The values obtained using :cite:`Yamazaki1988`'s method are interpolated according to the soil element center locations.

A summary of the random field preparation procedure for the site response event analysis is summarized here:
Enumerated lists:

1. Generate mean field using mean target soil property, e.g., relative density or shear wave velocity
2. Generate Gaussian random field for target soil property using *Gauss1D.py* with mean = 0.0 and :math:`\sigma` = 1.0
3. Interpolate Gaussian field to FEM mesh
4. Combine the mean field and Gaussian field to obtain a stochastic field using the following equation:

.. math::
  F_{stochastic} = F_{mean} \; + \; F_{residual} \, = F_{mean} \; + \; COV \; F_{mean} \; F_{Gaussian}\,

.. note::
   - A reasonable mesh resolution is recommended. The selection of element size should consider several factors, including but not limited to, layer shear wave velocity (for frequency resolution), correlation length (for random field resolution), and computation efficiency.

Calibration of Constitutive Model
"""""""""""""""""""""""""""""""""

Since soil properties, instead of material input parameters, are randomized, it is imperative to choose representative input parameters for constitutive models based on the random variable chosen by the user.
An independent calibration process of the constitutive model should be carried out carefully. Currently, a couple of pre-calibrated correlations are included in |s3harkName|, including PM4Sand and PDMY03 based on relative
density (:math:`D_R`). The detailed correlation can be found in *calibration.py*. The user is also encouraged to modify the script to include their own calibration of constitutive models.

Currently, three constitutive models are supported in |s3harkName| to have random fields, namely, Elastic Isotropic (Elastic_Random), PM4Sand (PM4Sand_Random), and PDMY03 (PDMY03_Random). When these models are selected,
the analysis will be carried out using SimCenter workflow. As a result, profile and response plots are not updated inside |s3harkName|.

.. figure:: ./figures/s3harkFigures/Random_All.png
    :scale: 60 %
    :align: center
    :figclass: align-center

.. note::
   - Currently only **2D** plain-strain materials (including PDMY03 and ElasticIsotropic) are supported when using random field. Therefore, 1-component motion is required.

Elastic Isotropic
"""""""""""""""""
Shear wave velocity (Vs) can be selected to be randomized for this material. Subsequently, Young's modulus is calculated based the stochastic shear velocity profile at the center of each element. No special calibration is required.

.. figure:: ./figures/s3harkFigures/Elastic_Random.png
    :scale: 60 %
    :align: center
    :figclass: align-center

.. note::
   - Vs is bounded between 50 and 1500 m/s in *calibration.py*


PM4Sand
"""""""
.. figure:: ./figures/s3harkFigures/PM4Sand_Random.png
    :scale: 60 %
    :align: center
    :figclass: align-center


The calibration of the PM4Sand model is based on a parametric study using quoFEM :cite:`Chen2020a`. The calibration procedure for PM4Sand is straightforward for general sand-like soil behaviors as intended by the model developers.
When detailed laboratory test results are available, the apparent relative density :math:`D_R` can be estimated using void ratio and measured :math:`e_{max}` and :math:`e_{min}`. However, as discussed in :cite:`boulanger2015pm4sand`,
:math:`D_R` is defined to bound the model response rather than a strict measured of relative density from maximum and minimum density tests. Therefore, the user can adjust its value as part of the calibration process, and the default
critical state line might need to be re-positioned by adjusting secondary parameters :math:`Q` and :math:`R`, as well. Nevertheless, the estimated :math:`D_R` provides a reasonable value, such that the resulting model response is also
reasonable. :math:`G_o` can be estimated using small-strain shear modulus estimation methods for different confining pressures. Once :math:`D_R` and :math:`G_o` are determined, :math:`h_{po}` can be calibrated iteratively by matching:
1) excess pore pressure evolution for a range of individual laboratory tests, and/or 2) specific values of :math:`CRR`. Additional secondary parameters can also be adjusted to fine-tune the model response. For example, adjusting :math:`h_o`
can result in different modulus reduction curves.

On the other hand, when comprehensive laboratory tests are not available for specific sites, model calibration needs to be based on in-situ test data such as SPT blow count, CPT penetration resistance, or shear wave velocity (Vs).
For example, :math:`D_R` can be estimated by correlations to penetration resistances. :cite:`Idriss2008` recommended the following correlation to SPT,


.. math::
	D_R = \sqrt{\frac{(N_1)_{60}}{C_d}}\,,

where :math:`C_d` is recommended to be 46. For CPT, the following correlation can be used,


.. math::
	D_R = 0.465\Big(\frac{q_{c1N}}{C_{dq}}\Big)^{0.264} - 1.063\,,

where :math:`C_{dq}` is recommended to be 0.9.
The second primary input parameter :math:`G_o` can also be estimated from in-situ data. :cite:`boulanger2015pm4sand` modified the correlation by :cite:`Andrus2000` to constraint the extrapolation to very small :math:`(N_1)_{60}` values, as


.. math::
	V_{s1} = 85[(N_1)_{60} + 2.5] ^{0.25}\,.

Alternatively, a simpler expression can be used when combined with a range of typical densities as,


.. math::
	G_o = 167\sqrt{(N_1)_{60} + 2.5}\,.

Subsequently, :math:`h_{po}` can be calibrated to reproduce a specific value of :math:`CRR` that can be computed using liquefaction triggering models. Numerous liquefaction triggering models incorporating the simplified cyclic stress approach
have been proposed in the past such as :cite:`Youd2001`, :cite:`Cetin2004`, and :cite:`Idriss2008`. Once :math:`D_R`, :math:`G_o`, and :math:`CRR` are chosen, the modeler should iteratively vary the value of :math:`h_{po}` until the simulated
:math:`CRR` matches the targeted value. Interpolation and extrapolation are common when the variables are within or close to the range of existing calibrated sets of parameters. Secondary parameters are less common to be modified when only
in-situ data are available. This calibration process can become cumbersome when in-situ data show a large degree of variability and calibration has to be performed for each soil unit. To shed light on the calibration process under this circumstance,
a parametric study was conducted to establish a correlation among :math:`D_R`, :math:`G_o`, :math:`h_{po}`, and CRR, i.e., :math:`CRR = f(D_R, G_o, h_{po})`. The function, :math:`f`, should be solvable for :math:`h_{po}` when the other variables
are known and eventually yield :math:`h_{po} = g(CRR, D_R, G_o)`. This correlation is intended to provide a preliminary estimation of :math:`h_{po}` and simplify the iterative calibration process under selected :math:`D_R`, :math:`G_o`, and CRR,
especially when both SPT and :math:`V_s` data are available and the user wants to make :math:`G_o` independent to :math:`D_R`. For this purpose, the Dakota platform, run through the uqFEM (now quoFEM) tool was used in this parametric study.
uqFEM was modified to include UW MixedDriver tool. All the simulations were performed on the Texas Advanced Computing Center (http://www.tacc.utexas.edu) Frontera supercomputer made available through DesignSafe-ci.

Using this tool, :math:`D_R`, :math:`G_o`, and :math:`h_{po}` were varied while all the secondary parameters were kept of their default values (predefined by primary parameters and initial stresses). The Latin Hypercube Sampling (LHS) method was
used to generate near-random variables. Each of these three variables was assigned an independent uniform distribution between minimum and maximum values. The range of these variables was chosen to cover a reasonable range of scenarios and can be
extended in future studies. :math:`D_R` was set to be between 0.2 to 0.9, :math:`G_o` between :math:`250` to :math:`1200`, and :math:`h_{po}` between :math:`0.05` to :math:`1.2`. A total of one million samples were generated. For each set of parameters,
Dakota ran MixedDriver to simulate undrained cyclic simple shear tests for 15 different CSRs ranging from :math:`0.05` to :math:`0.8` to produce smooth cyclic strength curves. A total of three initial conditions were
considered: initial effective vertical stress :math:`\sigma_v' = 1 ~atm.` with :math:`K_0` equal to 0.5 and 1.0, respectively, and :math:`\sigma_v' = 2~atm.` with :math:`K_0` equal to 0.5. The analyses were capped at 350 uniform cycles. Once all 15 simulated
CDSS tests were done, a python script was called by Dakota to calculate the number of cycles to reach liquefaction; which was defined as the number of cycles required to reach a single amplitude (SA) shear strain of 3\% as recommended by :cite:`Ishihara1993`.
Number of cycles to reach 1\% and 2\% SA and the slope (-b) and intercept (a) of the CSR curves (:cite:`Idriss2008`) in logarithmic scale were also recorded. The number of cycles were rounded up to the nearest half. Then a cyclic strength curve was
interpolated to calculate the Cyclic Resistance Ratio, CRR, which was determined as the CSR corresponding to 15 cycles. CRRs were bounded between 0.05 and 0.5 for interpolation accuracy.

The results were processed through linear regression analysis using *Matlab* to find the correlation between the input, :math:`D_R`, :math:`h_{po}` and :math:`G_o`, and the output CRR. Different combinations of terms were explored and the following
format produced the largest :math:`R^2`,

.. math::
  \begin{split}
  CRR_{3\%, K_0 = 0.5}  = & 0.1282 - 0.4952D_R - 5.0565\times10^{-5}G_o + 0.0749h_{po} + 1.4665\times10^{-4}D_RG_o \\
 & + 0.1323D_Rh_{po} + 0.7252D_R^2 - 0.0636h_{po}^2 \,,
  \end{split}

with :math:`R^2 = 0.989`. In this equation :math:`D_R` is in fraction. CRRs using criteria of :math:`1\%` and :math:`2\%` SA as well as for other :math:`\sigma_v'` and :math:`K_0` were also analyzed. More results can be found in :cite:`Chen2020a`.
It should be noted that the magnitude of these coefficients depends directly on the scale of the selected variables and smaller coefficients don't necessary imply less important features. For example, :math:`G_o` is approximately three orders
of magnitude larger than :math:`D_R`, which leads to much smaller coefficients for it.

Then this equation can be rearranged to isolate :math:`h_{po}`,

.. math::
    ah_{po}^2 + bh_{po}+c = 0\,,

where :math:`a = 0.0636`, :math:`b =  -0.0749 - 0.1323D_R`, and :math:`c = - 0.1282 + 0.4952D_R + 5.0565\times10^{-5}G_o - 1.4665\times10^{-4}D_RG_o - 0.7252D_R^2 + CRR_{3\%, K_0 = 0.5}`. This correlation becomes a quadratic equation for
:math:`h_{po}` that can be solved for two real roots for :math:`h_{po}` when values of :math:`D_R`, :math:`G_o`, and :math:`CRR` are given. The lesser root is the one that can be paired with :math:`D_R` and :math:`G_o` to yield the desired
CRR in a calibration process. The predictive equation can be used to provide good initial :math:`h_{po}` values and speed up the calibration process.

.. note::
   - :math:`D_R` is bounded between 0.2 and 0.95 in *calibration.py*


PressureDenpendentMultiYield03
""""""""""""""""""""""""""""""
.. figure:: ./figures/s3harkFigures/PDMY03_Random.png
    :scale: 60 %
    :align: center
    :figclass: align-center

PressureDenpendentMultiYield03 is updated from PressureDenpendentMultiYield02, which was developed for liquefaction and cyclic mobility, to comply with the established guidelines on the dependence of liquefaction triggering to the number of loading cycles,
effective overburden stress (:math:`K\sigma`), and static shear stress (:math:`K\alpha`). The model has been improved with new flow rules to better capture contraction and dilation in sands and has been implemented as PDMY03 in OpenSees. In |s3harkName|, the calibration of PDMY03
model is based on interpolating pre-calibrated parameter sets for various of relative densities.


.. figure:: ./figures/s3harkFigures/Pdmy03_parameters.png
    :scale: 100 %
    :align: center
    :figclass: align-center

    Calibrated parameters for PDMY03 (after :cite:`Khosravifar2018`).

.. note::
   - :math:`D_R` is bounded between 0.33 and 0.87 in *calibration.py*
