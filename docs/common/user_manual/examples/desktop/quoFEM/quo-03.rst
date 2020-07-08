:page_template: vega.html

Reliability Analysis
====================

+---------------+-----------------------------------------------------+
| Problem files | `quo-03 <https://github.com/claudioper              |
|               | ez/SimCenterDocumentation/tree/examples/docs/common |
|               | /user_manual/examples/desktop/quoFEM/src/quo-03>`__ |
+---------------+-----------------------------------------------------+

This example uses quoFEM to perform a second-order reliability analysis
(SORM) of an OpenSees FE model.

Consider the stochastic response of a two-dimensional truss structure
shown in the following figure with uncertain section dimensions,
material moduli, and loading magnitude. Two input scripts are used to
define a `local
reliability </common/user_manual/usage/desktop/DakotaReliability.html>`__
procedure to be coordinated by quoFEM which will estimate response
magnitudes whose probabilities of exceedance are 0.02, 0.2, 0.4, 0.6,
0.8, and 0.99. |Simple truss model.|

The following parameters are defined in the **RV** tab of quoFEM:

1. Elastic modulus, ``E``: **Weibull** distribution with a scale
   parameter :math:`(\lambda)` of :math:`210.0`, shape parameter
   :math:`(k)` of :math:`20.0`,

2. Load magnitude, ``P``: **Beta** distribution with a first shape
   parameter :math:`(\alpha)` of :math:`2.0`, second shape parameter
   :math:`(\beta)` of :math:`2.0`, lower bound :math:`(L_B)` of
   :math:`20.0`, upper bound :math:`(U_B)` of :math:`30.0`,

3. Cross sectional area for the other six bars, ``Ao``: **Lognormal**
   distribution with a mean :math:`(\mu)` of :math:`250.0`, standard
   deviation :math:`(\sigma)` of :math:`50.0`,

4. Cross sectional area for the upper three bars, ``Au``: **Normal**
   distribution with a mean :math:`(\mu)` of :math:`500.0`, standard
   deviation :math:`(\sigma)` of :math:`100.0`,

UQ Workflow
-----------

To define the uncertainty workflow in quoFEM, select **Reliability
Analysis** for the **Dakota Method Category**, and enter the following
inputs:

====================== ================================
**Integration Method** Second Order
**Level Type**         Probability Levels
**Local Method**       Most Probable Point
**Reliability Method** Local Reliability
**MPP Search Method**  no_approx
**Probability Levels** [0.02, 0.2, 0.4, 0.6, 0.8, 0.99]
====================== ================================

Model Files
-----------

The following files make up the **FEM** model definition.

#. `model.tcl <https://raw.githubusercontent.com/claudioperez/SimCenterExamples/master/static/truss/model.tcl>`__:
   This file is an OpenSees Tcl script that constructs and runs a finite
   element analysis of the truss for a given realization of the
   problem’s random variables. It is supplied to the **Input File**
   field of the **FEM** tab.

#. `post.tcl <https://raw.githubusercontent.com/claudioperez/SimCenterExamples/master/static/truss/post.tcl>`__:
   This file is an OpenSees Tcl script that processes the QoI
   identifiers supplied in the **QoI** tab, and writes the relevant
   response quantities to ``results.out`` from an OpenSees process. It
   is supplied to the **Postprocess File** field of the **FEM** tab.

.. raw:: html

   <!-- <div class="admonition warning">Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!</div> -->

Results
-------

Once the analysis is complete the **RES** tab will be automatically
selected and the results will be displayed as shown in the following
figure:

.. figure:: truss/trussSORM-RES.png
   :alt: Sensitivity analysis results.

   Sensitivity analysis results.

.. raw:: html

   <div id="vis">

.. raw:: html

   </div>

.. raw:: html

   <script>
       // Assign the specification to a local variable vlSpec.
       var vlSpec = {
       $schema: 'https://vega.github.io/schema/vega-lite/v4.json',
       data: {
           values: [
           {a: 'C', b: 2},
           {a: 'C', b: 7},
           {a: 'C', b: 4},
           {a: 'D', b: 1},
           {a: 'D', b: 2},
           {a: 'D', b: 6},
           {a: 'E', b: 8},
           {a: 'E', b: 4},
           {a: 'E', b: 7}
           ]
       },
       mark: 'bar',
       encoding: {
           y: {field: 'a', type: 'nominal'},
           x: {
           aggregate: 'average',
           field: 'b',
           type: 'quantitative',
           axis: {
               title: 'Average of b'
           }
           }
       }
       };

       // Embed the visualization in the container with id `vis`
       vegaEmbed('#vis', vlSpec);
   </script>

.. |Simple truss model.| image:: truss/truss.png
