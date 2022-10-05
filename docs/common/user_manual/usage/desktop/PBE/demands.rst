.. _lblPelicun_demands

Demand Model
============

This tab collects information about the demands that control the performance model of the building. There are multiple ways to define the demands using the information provided in the following areas:

Data Source
-----------

The drop-down list in this area identifies how the demands are calculated:

:from Workflow:
    Select this option if the PBE app is used to perform the entire performance assessment workflow, that is, the structural response estimation is also set up an performed by this application. In this case, make sure the workflow you set up provides all of the demand types required by the performance assessment. The demand file will be automatically created in the appropriate format by the backend engine and passed on to Pelicun in the background.

:from File:
    Select this option if the PBE app is only used for the performance assessment step, that is, the structural response estimation is performed outside of the application. In this case, you will need to perform the demand calculations and provide demand data in the standard CSV format used by SimCenter applications, including Pelicun. See the |PelicunDocs| for more information on the corresponding data format.

    When this option is selected, use the **Choose** button to select a file on your computer that contains the demand data.


Stochastic Model
----------------

Robust performance assessment typically requires hundreds or thousands of damage and loss realizations while raw demand data is typically not available for more than a few dozen realizations. Therefore, the raw data is typically used to calibrate a stochastic demand model that is later sampled to obtain the number of realizations required for performance assessment.


This area controls the characteristics of the stochastic demand model that is prepared using the provided raw demand data. The following features are available:

:Distribution:
    Pelicun can fit a multivariate distribution to the raw data. The following options are available:

    :lognormal:
        Fit a multivariate lognormal distribution to the data.

    :truncated log:
        Fit a truncated multivariate lognormal distribution to the data. Truncation allows for limiting the domain for each random demand variable. This is an effective and transparent approach to avoid unrealistically high demands that otherwise are generated from the tails of lognormal distributions. See the details of setting up truncation limits below.

    :empirical:
        Use the raw demand data as-is without fitting a distribution. When this approach is chosen, the empirical data is sampled with replacement to obtain the required number of realizations. This is only recommended if a sufficiently large number of realizations is available.

:Truncation limits:
    This option is only available if the truncated lognormal distribution is selected. The **\+** and **\-** buttons can be used to add or remove definitions to the list. The following information defines each truncation limit:

    :Demand:
        Identifies the demand type using the standard SimCenter demand naming convention. The |PelicunDocs| provides a list of supported demand types that can be easily expanded if needed.

        Currently, all demands of the selected type will be truncated at the provided limits. Let us know if location-specific demand truncation would be helpful for your work.

    :Lower Lim:
        Lower truncation limit for the specified demand type. The unit of this truncation limit is identical to the unit of the demand in the raw demand data. If the demand is from the standard SimCenter workflow, then demand units are based on the unit settings in the GI panel of the PBE app.

    :Upper Lim:
        Upper truncation limit for the specified demand type. Unit considerations are identical to those explained under the Lower Lim. Either of the two limits can be left empty to avoid imposing limits on the given side of the distribution.

:Add Uncertainty:
    This option allows you to quantify the uncertainty that was not included in the simulations used to obtain the raw demand data. Following the FEMA P-58 methodology, the uncertainty is quantified as a log-standard deviation value that is used to increase the dispersion of the raw demand data.

    .. note:: FEMA P-58 disaggregates this uncertainty into several components, but --- from a practical point of view --- only their aggregate value matters for the performance assessment. Please provide the aggregate value here.

    .. note:: Although the FEMA P-58 methodology was developed under the assumption of a multivariate lognormal distribution, Pelicun uses a more general assessment engine that can increase the uncertainty in truncated lognormal distributions as well as in  empirical data. Therefore, this option is not limited to lognormal distributions.

:Remove collapses:
    This option allows you to filter collapsed results from the raw demand data. The filtered data is removed from the raw demands before any other calculation would take place. For example, only the filtered data is passed on to the engine to fit a distribution to the demands. This allows you to remove collapsed cases and prepare a stochastic demand model only for the non-collapsed realizations.

    Use the **\+** and **\-** buttons to prepare a list of demand types and corresponding collapse limits. The |PelicunDocs| provides a list of supported demand types that can be easily expanded if needed.

    Currently, if any of the demands of the selected type exceeds the collapse limit, the building in the given realization will be considered collapsed. Let us know if location-specific collapse limits would be helpful for your work.

    The unit of the collapse limit is identical to the unit of the demand in the raw demand data. If the demand is from the standard SimCenter workflow, then demand units are based on the unit settings in the GI panel of the PBE app.


Sample
------

This area is used to specify the sample size for demands and --- since these realizations are the first step in the uncertainty propagation through the performance assessment workflow --- for the entire performance assessment.

Pelicun uses Latin Hypercube Sampling to provide mean and additive outputs with smaller errors than typical Monte Carlo analysis would. If you are only interested in such outputs, using a few hundred realizations should be sufficient. However, if you are interested in other statistics of the decision variable distributions, we recommend using a sample size of at least 1000.

The **Directly use raw demand data** option allows you to use the raw data without resampling. That is, the data will be used in the same order it was provided. If the requested sample size if larger than the size of the raw demand sample, the demand data will be used multiple times, always re-starting from the beginning and going through in the order it was provided. This option is useful when you want to preserve the order of demands, for example, because a portfolio of buildings is analyzed and the demands were generated to represent spatial correlation in the hazard.


Residual Drifts
---------------

Residual interstory drift ratios are often used as proxies to infer irreparable damage to buildings. However, it is challenging to model such behavior reliably and some experts recommend approximating such drifts from other demands. The drop-down list in this area allows you to choose an approximate method to get residual drift estimates. If you prefer to use a method that is not listed here, let us know and we can include it in a future update. Choose **do not infer** if you do not need residual drifts, or you wish to provide those values as part of the raw demand data yourself.

.. note:: This inference is performed *after* the demands are sampled, hence, the RID values are not limited by the prescribed distribution in the stochastic model.


**FEMA P-58 method**

The inference method in FEMA P-58 uses the yield drift ratio of the structural system to characterize the initiation of inelastic behavior and estimates the residual drifts from the peak interstory drift ratios. Pelicun allows you to use direction-specific yield drift ratios to be able to appropriately model structures that are not identical in the two horizontal directions. Use the **\+** and **\-** buttons to prepare a list of directions and corresponding yield drift ratios.

.. note::
    Pelicun applies this method to every PID (Peak Interstory Drift) demand to get a corresponding RID (Residual Interstory Drift) demand. This allows for any floor to trigger irreparable damage and enables a more realistic and detailed analysis than the typical approach of using a single RID demand as input.

    Nevertheless, if you wish to perform such a calculation, we recommend providing an RID-0-1 value among the raw demand inputs, where 0 as location identifies this as a global (i.e., not specific to a particular location) demand and 1 as direction is an arbitrary choice. The automatic irreparable damage calculation will recognize such input and perform the calculation appropriately.
