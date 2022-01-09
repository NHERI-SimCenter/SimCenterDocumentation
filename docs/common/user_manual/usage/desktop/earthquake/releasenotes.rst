.. _lbl-release_eeuq:

***************************
Release Notes
***************************

This section is initialized at EE-UQ v2.2.5 and would focus on archive new features and fixes in new releases.

Version 2.2
=================

Version 2.2.6
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
    #. Specifying the fault type, pulse-like feature, and duration filter in ground motion selection
    #. Adding the option of "Geometric" suite average for the PEER NGA West2 ground motion selection

#. **Fixes and Patches**: 
    #. Fixing the bug of exporting ground motion names in the "Save Data"
    #. Fixing the bug of using user-specified EDP names


Version 2.3.0
----------------

**Release plan**: Mar. 2022

*Planned features*

#. UQ: New surrogate modeling methods (e.g., PLoM, SAF-IDA)
#. EVT: New feature to use USGS deaggregation information and ground motion prediction equation to generate target spectrum
#. EVT: Invoking OpenQuake to generate scenario-based or classical PSHA ground motion spectral targets
#. SAM: Invoking the iterative seismic design and pushover analysis in AutoSDA as a pre-processing step
#. ...\*

\*: Users are welcome to contact us on `forum <http://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0>`_ for new feature requests.
