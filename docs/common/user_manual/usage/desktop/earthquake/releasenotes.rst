.. _lbl-release_eeuq:

***************************
Release Notes
***************************

This section is initialized at EE-UQ v2.2.5 and would focus on archive new features and fixes in new releases.

Version 2.2
=================

Version 2.2.5
----------------

**Release date:** Oct. 4th, 2021

*Current Availability*

#. **Structural Information Model**
    a. MDOF: creating idealized multi-degree-of-freedom models
    b. OpenSees: user-defined OpenSees models
    c. Steel Building Model: automating steel frame design and modeling

#. **Ground Motion Event**
    a. Stochastic Ground Motion: simulating stochastic ground motion recordings
    b. PEER NGA Records: selecting and scaling PEER NGA West2 ground motions
    c. Site Response: propagating rock motions to the surface
    d. Multiple PEER: using multiple PEER recordings
    e. Multiple SimCenter: using multiple SimCenter-format recordings
    f. User Specified Database: selecting and scaling ground motions from the user-specified flatfile

#. **Finite Element Application**
    a. OpenSees: Open System for Earthquake Engineering Simulation

#. **Engineering Demand Parameter Generator**
    a. Standard Earthquake: maximum story drift ratio, lateral story displacement, peak floor acceleration
    b. User Defined: user-specified EDP

#. **Uncertainty Quantification**
    a. Dakota
        - Forward Propagation
        - Sensitivity Analysis
        - Reliability Analysis

*Major Updates in this Version*

#. **Features**:
    #. Uploading a text file to define "User Specified" target spectrum in ground motion selection (:download:`example spectrum file <figures/UserSpecificSpectrum.csv>`)
    #. Specifying the fault type, pulse-like feature, and duration filter in ground motion selection
    #. Adding the option of "Geometric" suite average for the PEER NGA West2 ground motion selection
    #. New message board UI

#. **Fixes and Patches**: 
    #. Resolving load configuration json file for PEER NGA Records
    #. Relaxing the tolerance in the example eeuq-0004
    #. Correcting the input ground motion file in the example eeuq-0002
    #. Fixing the bug of exporting ground motion names in the "Save Data"


Version 2.2.6
----------------

**Release plan**: Dec. 2021

*Planned features*

#. SAM: Invoking the iterative seismic design and pushover analysis in AutoSDA as a pre-processing step
#. RES: Retrieving the periods.out file in AutoSDA runs from DesignSafe from EE-UQ interface
#. EVT: Invoking OpenQuake to generate scenario-based or classical PSHA ground motion spectral targets
#. ...\*

\*: Users are welcome to contact us on `forum <http://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0>`_ for new feature requests.
