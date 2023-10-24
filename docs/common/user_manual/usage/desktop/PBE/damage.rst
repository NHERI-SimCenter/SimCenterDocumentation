.. _lblPelicun_damage:

Damage Model
============

This tab configures the damage simulation (:numref:`fig-dl-pelicun-damage`). Note that components were already assigned to the asset in the earlier :ref:`lblPelicun_asset` tab. These components have their fragility functions defined in the specified component vulnerability data files and they do not need to be further configured here. This tab provides a convenient way to create additional components that represent global vulnerabilities and allows you to specify a damage process that describes the interdependencies in damage simulation. These features are described in detail below.

.. _fig-dl-pelicun-damage:

.. figure:: figures/dl_pelicun_damage.png
   :align: center
   :figclass: align-center

   The Damage model inputs.


Global Vulnerabilities
----------------------

We use the term Global Vulnerabilities for damages that are at the building-level and usually affect multiple components in the building. In high-resolution assessments (e.g., FEMA P-58), the vulnerabilities listed below require building-specific fragility functions that are typically not part of a standard damage and loss model library. The data you provide here is used the automatically generate additional components for the analysis that can capture these types of vulnerabilities.

.. note::
   In analyses with building-level resolution (e.g., Hazus Earthquake Methodology), these vulnerabilities are typically handled with components that provide a holistic model for the entire building. In such cases, we recommend assinging those components to the building in the Asset tab and not include these vulnerabilities.

Irreparable Damage
^^^^^^^^^^^^^^^^^^
Irreparable damage is assumed to be triggered by excessive Residual Interstory Drift (RID) values. The corresponding limit state capacity is assumed to have a lognormal distribution with user-defined parameters.

.. note:: 
   FEMA P-58 recommends using this model with a median of 0.01 and a logarithmic standard deviation of 0.3.

.. note::
   Exceedance events are managed by creating an ``excessiveRID`` component and assigning it to every story and direction where RID values are provided in the demand sample. Then, the drift capacity distribution is sampled for every excessiveRID component and the realized capacities are checked against the corresponding RID demand realizations. If any RID exceeds the capacity of the corresponding story, the entire building is considered irreparable. 

   Damage experienced by the excessiveRID components is recorded in the output files for every realization. This can help evaluate the contribution of individual floors to the irreparable damage outcomes.

.. note::
   The above approach typically results in higher probability of irreparable damage than the widely used alternative where a single RID demand is checked against a single capacity realization. If you wish to achieve that behavior, see the Residual Drifts section at the bottom of the :ref:`lblPelicun_demands` page for information on how to provide demands that have one RID value for the entire building.

Collapse
^^^^^^^^

Collapse is assumed to be triggered by a particular demand exceeding the structure's capacity for that demand. This generic approach allows you to consider collapse fragility curves that are typically controlled by intensity measures. It also supports modeling non-simulated collapses where exceeding a certain level of structural response is considered to result in collapse. For the latter, make sure the collapsed cases are not already filtered out by setting a collapse limit in the :ref:`lblPelicun_demands`. Currently, only one demand type can be specified. Let us know if your work would benefit from having multiple collapse limits in an assessment.

The following settings are available for the global collapse component:

:Demand:
   Identifies the demand type using the standard SimCenter demand naming convention. See the section on standard demand data in :ref:`lblPelicun_demands` for a detailed description of demand labels.

   All demands of the selected type will be evaluated against the capacity specified by the following parameters. For example, if PID is specified here, the peak interstory drift ratio on all floors and in all directions is checked against capacity realizations sampled for every location.

   .. note::
      When demands at multiple locations can trigger collapse capacity exceedance, these are managed by creating an ``excessive.coll.DEM`` component and assigning it to every story and direction where the demand type specified here is available. Damage experienced by these components is recorded in the output files for every realization. This can help evaluate the contribution of individual floors to the collapse outcomes.

:Capacity:
   Specifies the median capacity of the building, that is, the intensity of the given demand type that triggers the collapse limit state in 50% of the realizations.

   If you use a deterministic approach to collapse modeling, this capacity is a hard limit that will directly be applied to all realizations. Otherwise, the following two parameters are used to define a random collapse capacity variable through a probability density function. That capacity variable is sampled for every realization and every location (if there are multiple locations with collapse demands) to capture the uncertainty in the collapse capacity.

   The unit of the collapse capacity is based on the length unit in the General Information panel of the PBE app.        

:Distribution:
   Specifies the type of distribution, if any, to model the uncertainty in the collapse capacity. Currently, lognormal and normal distributions are supported. You can use a determinsitic model by selecting ``N/A``. 

:θ₁:
   Specifies the second parameter of the probability density function of the distribution selected above. The second parameter is the coefficient of variation for normal and the log-standard deviation for lognormal distributions. This input is not used if you selected ``N/A`` for the distribution.

.. note::
   A conventional lognormal collapse fragility function can be defined with its median and log-standard deviation. The corresponding demand type is typically an intensity measure. In an earthquake context, this is often the spectral acceleration at the fundamental period of vibration. Such a demand can be provided as "SA_1.03", for example, for a T₁=1.13 case.

.. note::
   Another typical use case is to take a demand type from one of the measured response quantities and assume that the building collapses when it exceeds a certain value. For example, in an earthquake context, use PID as the demand type and set the capacity as a deterministic 0.1. This will check the peak interstory drift ratio on every story of the building and trigger a collapse if it exceeds 10% in any story.

.. note:: 
   These automatic component generators were designed to handle the typical use cases mentioned above. Pelicun can model more complex global vulnerabilities and such models can be used in the PBE app too as long as the corresponding components are prepared and provided as part of the Asset model. Let us know if you are interested in such advanced modeling.

Damage Process
--------------

Damage processes characterize the interdependencies between various component damages. They allow modeling complex cascading damage phenomena and models where multiple different probabilistic events can trigger the same damage state.

Damage processes are a list of tasks described using a JSON file. Each task identifies a source component and how a damage event in the source component triggers one or more damage events in target components. The following example illustrates the general notation::
   
   "27_sourceComp": {
      "DS3": "targetComp1_DS2",
      "DS4": [
          "targetComp1_DS3", 
          "targetComp2_DS1"
      ],
      "DS5": "ALL_NA"
   }

Task identifiers shall start with a positive integer (``27`` in the example above). They are sorted at the beginning and executed in ascending order. Although it is not mandatory, we recommend adding tasks to the JSON file in ascending order and using a sequence of integers starting with ``1`` for the sake of clarity.

``sourceComp`` should be replaced with the component ID of the source component and ``targetComp1`` and ``targetComp2`` are placeholders for the component IDs of different target components. Each task assigns a dictionary to the source component and allows you to specify one or more damage states that trigger damage events. In the example above, ``DS3``, ``DS4``, and ``DS5`` are used to trigger other damages.

Each damage state can be linked to one or more damage events. In the example above, ``DS3`` in the source component triggers ``DS2`` in ``targetComp1``, while ``DS4`` in the source component affects two components. It triggers ``DS3`` in ``targetComp1`` and ``DS1`` in ``targetComp2``. Note how multiple target events can be linked to a source damage event by using an array of strings.

The ``DS5`` damage state triggers events using two special keywords. When ``ALL`` is used for the target component, it affects all but the source component. This is helpful to model how global events affect damages of all components. When ``NA`` is used as a target damage state, it removes all damage information from the target component. 

.. note:: 
   This is not the same as assigning ``DS0`` because it signals an undefined damage state rather than no damage. This option is typically helpful when certain component damages are conditioned on other events and need not be evaluated otherwise. For example, if we are interested in detailed component damage statistics conditioned on no collapse, we assign an ``ALL_NA`` target event to collapse cases to remove component damages from those realizations.

.. note::
   If a source or target component is not among the components assigned to the building, the corresponding task is simply skipped during the simulation. This allows for creating general damage process files with tasks that are only triggered when the corresponding components are available in the building. 

In a future update we plan to include more specific component identification that lets you restrict tasks to linking co-located components (i.e., sourceComp and targetComp located at the same story). This will allow for tasks that can, for example, link a damage to a pipe component in the ceiling to water-induced damage to a component on the floor.

The following options are available for damage processes in the PBE app:

:FEMA P-58:
   Automatically loads a pre-defined damage process based on the second edition of the FEMA P-58 methodology::

      {
          "1_excessive.coll.DEM": {
              "DS1": "collapse_DS1"
          },
          "2_collapse": {
              "DS1": "ALL_NA"
          },
          "3_excessiveRID": {
              "DS1": "irreparable_DS1"
          }
      }

   This process performs the following tasks:

   #. If the collapse capacity of any story is exceeded by the demand (see Collapse in the Global Vulnerabilities section above for details) trigger a global collapse event through the ``collapse``  component's ``DS1``. Note that this task is only applied if there are multiple locations with collapse checks. Otherwise, there are no excessive.coll.DEM components assigned and this task is skipped.

   #. Make sure that no other component damages are evaluated when the building collapses. This is important to avoid double counting consequences and to get appropriate component damage statistics conditioned on no collapse.

   #. If any of the residual interstory drifts exceeds the assigned capacity, trigger an irreparable damage event using ``DS1`` of the ``irreparable`` component.

:Hazus Earthquake:
   Automatically loads a pre-defined damage process based on the Hazus Earthquake methodology::

      {
          "1_STR": {
              "DS5": "collapse_DS1"
          },
          "2_LF": {
              "DS5": "collapse_DS1"
          },
          "3_excessive.coll.DEM": {
              "DS1": "collapse_DS1"
          },
          "4_collapse": {
              "DS1": "ALL_NA"
          },
          "5_excessiveRID": {
              "DS1": "irreparable_DS1"
          }
      }

   This process performs the following tasks:

   #. If any of the structural components (there is typically only one ``STR`` component) is in Collapse damage state (``DS5``), trigger a global collapse damage state. Note that ``STR`` is automatically replaced by the PBE app with the component ID of the structural component assigned to the building. If there is no ``STR`` component assigned to the building, this task is skipped.

   #. If any of the lifeline-facility components (there is typically only one ``LF`` component) is in a collapse damage state (``DS5``), trigger a global collapse damage state. Note that ``LF`` is automatically replaced by the PBE app with the component ID of the lifeline-facility component assigned to the building. Also note that despite Hazus's recommendation to use ``LF`` components only for lifeline facilities where very little information is available about the structural system, these are often applied in literature more broadly to a general building inventory. If there is no ``LF`` component assigned to the building, this task is skipped.

   #. If the collapse capacity of any story is exceeded by the demand (see Collapse in the Global Vulnerabilities section above for details) trigger a global collapse event through the ``collapse``  component's ``DS1``. Note that this task is only applied if there are multiple locations with collapse checks. Otherwise, there are no excessive.coll.DEM components assigned and this task is skipped.

   #. Make sure that no other component damages are evaluated when the building collapses. This is important to avoid double counting consequences and to get appropriate component damage statistics conditioned on no collapse.

   #. If any of the residual interstory drifts exceeds the assigned capacity, trigger an irreparable damage event using ``DS1`` of the ``irreparable`` component. This last task extends the concept of irreparable damage to the Hazus methodology. It is removed from the damage process if there are no such vulnerabilities assigned to the model.

:User Defined:
   This option allows you to load a custom damage process for the calculation from a JSON file.

:None:
   Do not consider interdependencies between damages. If this option is selected, all component damages are evaluated independently.

