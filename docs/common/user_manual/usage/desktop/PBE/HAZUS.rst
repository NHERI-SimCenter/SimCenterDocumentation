.. _lblHAZUS:

HAZUS MH
--------

This option implements the loss assessment methodology described in the `HAZUS MH Technical Manual`_ document.

General Settings
^^^^^^^^^^^^^^^^

:numref:`fig-dl-hazus-general` shows the input panel that allows the user to set the response, damage, and loss models for the assessment.

.. _fig-dl-hazus-general:

.. figure:: figures/dl_hazus_general.png
	:align: center
	:figclass: align-center

	The General Damage and Loss Settings panel. (The settings shown in the Figure serve demonstration purposes and are not the suggested inputs.)


Response Model
^^^^^^^^^^^^^^^^^


.. figure:: figures/dl_hazus_general_response.png
    :align: right
    :figwidth: 300px

    Response model settings.


Some text about the model


**Response Description**

    **EDP data**

    Allows you to provide externally calculated EDP results for the assessment. If this field is not empty, we will use the raw results in the file provided and we will not run any response simulations regardless of the settings in other parts of the application.

    **EDP distribution** 

    Specifies the approach to describing the distribution of EDPs. If empirical is selected, the raw EDPs are kept as is and resampled during the assessment. The lognormal setting fits a multivariate lognormal distribution to the EDPs. The truncated lognormal setting can be used to set a truncated multivariate lognormal distribution to the non-collapse results by setting the Basis (the next setting) appropriately.

    **Basis** 

    Specifies the basis of the EDP distribution. The all results setting uses all samples, while the non-collapse results removes the samples that have EDPs beyond the collapse limits (see in a later setting).

    **Realizations**

    The number of EDP and corresponding damage and loss realizations to generate. Depending on the complexity of the model, a few thousand realizations might be sufficient to capture central tendencies. A much larger number is required to get appropriate estimates of the dispersion of results. If the EDP distribution is set to empirical, the EDP realizations are sampled from the set of raw EDP values with replacement. If the EDP distribution is set to lognormal or truncated lognormal, the samples are generated from the distribution that is fit to the raw EDP values.

**Additional Uncertainty** 

  Ground motion and modeling uncertainty per FEMA P58 that is referred to as uncertainty in response due to variability of ground motion demand and variability in the capacity properties of the model building in HAZUS MH. The prescribed logarithmic standard deviation values are added to the dispersion of EDPs to arrive at the description of uncertain building response.

**Detection Limits** 

  These limits correspond to the maximum possible values that the response history analysis can provide. While peak interstory drifts will certainly have an upper limit, peak floor acceleration will not necessarily require such a setting. Leaving any of the fields empty corresponds to unlimited confidence in the simulation results.

  Note: these limits will be used to consider EDP data as a set of censored samples when fitting the multivariate distribution set under Response Description. If the EDP distribution is set to empirical, this setting has no effect.


Damage Model
^^^^^^^^^^^^


.. figure:: figures/dl_hazus_general_damage.png
    :align: right
    :figwidth: 300px

    Damage model settings


**Structure Type and Design Level**

  These two pieces of information are used to select the appropriate fragility and consequence functions from those provided in the HAZUS MH Technical Manual.

  Note: Any fragility or consequences function can be edited by the user and loaded by specifying a directory that contains those custom functions in the Custom DL data box at the bottom right. The loss calculations are performed at the local computer. Consequently, the locally available fragility and population data files can be used to perform the calculations even if the response simulations are done at DesignSafe.


Loss Model
^^^^^^^^^^^^^^^^^


.. figure:: figures/dl_hazus_general_loss.png
    :align: right
    :figwidth: 300px

    Loss model settings


**Replacement Cost and Time**
  
  The cost (in the currency used to describe repair costs, typically US dollars) and the time (in days) it takes to replace the building.

**Decision variables of interest**
  
  These checkboxes allow the user to pick the decision variables of interest and save computation time and storage space by only focusing on those.

**Inhabitants**

	**Occupancy Type**

	  The type of occupancy is used to describe the temporal distribution of the inhabitants. Note: the default HAZUS MH distribution can be overridden by a custom file provided in the Custom distribution box.
	
	**Peak Population**

	  The maximum number of people present at each floor of the building. The example shows a two-story wooden house with a cripple wall, hence the 0 population in the first floor.
	
	**Custom distribution**

	  The loss assessment is performed using population data from the HAZUS Technical Manual. Each data source can be overridden by custom user-defined data.
	
	  Note: the loss calculations are performed at the local computer. Consequently, the locally available fragility and population data files can be used to perform the calculations even if the response simulations are done at DesignSafe.

**Components**

  **Custom DL data**

    The loss assessment is performed using fragility and loss data from the HAZUS Technical Manual. Each data source can be overridden by custom user-defined data.


.. .. bibliography:: ../../../../references.bib

.. _FEMA P58: https://www.fema.gov/media-library/assets/documents/90380
.. _HAZUS MH Technical Manual: https://www.fema.gov/media-library-data/20130726-1820-25045-6286/hzmh2_1_eq_tm.pdf

