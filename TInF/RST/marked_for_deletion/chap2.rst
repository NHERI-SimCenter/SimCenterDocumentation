Introduction
==============

The Turbulence Inflow Tool (TInF) is designed to collect all required properties and parameters
needed for various turbulence inflow models in OpenFOAM, and to augment an existing wind-around-a-building model by adding the necessary sections to respective parameter definition files.

The generic workflow involved is as follows.

(#)
   Build your OpenFOAM model as you would without using a turbulence inflow model.  Use a generic patch with a suitable name for you will need to identify that patch by its name inside TInF.
   
(#)
   Run TInF following, identify your model folder, adjust the parameters as desired, and export to your model definition.
   Consult Chapter :ref:`sec_TInF-usage` for details on those steps.
   
(#)
    Run OpenFOAM using the updated model definition.
    

The tool also provides a Save to file and Open from file functionality that will allow you to
define and share complex sets of settings and parameters for the supported turbulence inflow models and, such, efficiently and reliably apply the same parameters to several different models.


The following Chapter :ref:`sec_TInF-installation` explains the installation of the tool and how
to update your local OpenFOAM copy to implement the supported turbulence inflow models.
Chapter :ref:`sec_TInF-usage` will walk you through the steps required to add a turbulence inflow condition to your model.
Chapter :ref:`sec_TInF-theory` provides a detailed theoretical background on the provided turbulence models.
