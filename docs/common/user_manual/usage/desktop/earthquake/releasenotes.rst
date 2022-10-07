.. _lbl-release_eeuq:
.. role:: blue

*************
Release Notes
*************

Version 3.2
===========

Version 3.2.0 (Current)
-----------------------

**Release date:** Sept. 2022

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **Structural Information Model**
    a. MDOF: creating idealized multi-degree-of-freedom models
    b. OpenSees: user-defined OpenSees models
    c. Steel Building Model: automating steel frame design and modeling
    d. :blue:`Concrete Building Model: automating concrete moment frame design and modeling`
    e. :blue:`MDOF-LU: MDOF shear building model`

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
    b. SimCenterUQ

#. **Results**
    a. Summary Data
    b. Data Values

#. **Others**: Improvements to the message area, and minor bug fixes
    * :blue:`Decoupling the output units defined in GI with the units used in the simulation.`
    * :blue:`Decoupling the Rayleigh damping ratio with the FEM configuration.`


Version 3.1
===========

Version 3.1.0
-----------------------

**Release date:** July 2022

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **Structural Information Model**
    a. MDOF: creating idealized multi-degree-of-freedom models
    b. OpenSees: user-defined OpenSees models
    c. Steel Building Model: automating steel frame design and modeling

#. **Ground Motion Event**
    a. Stochastic Ground Motion: simulating stochastic ground motion recordings
    b. PEER NGA Records: selecting and scaling PEER NGA West2 ground motions
        * :blue:`Adding a surrogate hazard model feature to get target response spectrum from Gaussian Process model`
        * :blue:`A new example is provided for evaluating target response spectrum from GP surrogate for Hayward earthquake in Bay Area`
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
    b. SimCenterUQ

#. **Results**
    a. Summary Data
    b. Data Values

#. **Others**: Improvements to the message area, and minor bug fixes
    * :blue:`Fixing the radio button in Multiple Event (uncheck is now enabled)`

Version 3.0
===========

Version 3.0.0
-----------------------

**Release date:** March. 2022

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **Structural Information Model**
    a. MDOF: creating idealized multi-degree-of-freedom models
    b. OpenSees: user-defined OpenSees models
    c. Steel Building Model: automating steel frame design and modeling

#. **Ground Motion Event**
    a. Stochastic Ground Motion: simulating stochastic ground motion recordings
    b. PEER NGA Records: selecting and scaling PEER NGA West2 ground motions
        * :blue:`Adding a USGS seismic disaggregation feature for given return periods and user-defined IM`
        * :blue:`Computing conditional mean spectrum target (ASCE 7) based on disaggregated mean magnitude and distance`
        * :blue:`Selecting and scaling records to the disaggregation-based target spectrum`
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
    b. :blue:`SimCenterUQ`
        * :blue:`New UQ engine: PLoM - training surrogate model for defined structural model or user-supplied response data matrix`
        * :blue:`Generating new realizations of structural responses from trained surrogate model`
        * :blue:`Including user-defined ground motion intensity measure in the model training`

#. **Results**
    a. Summary Data
    b. Data Values
        * :blue:`New data visualization panel`
        * :blue:`Highlighting data points in the result table`

#. **Others**: Improvements to the message area, and minor bug fixes

Version 2.2
=================

Version 2.2.7
-----------------------

**Release date:** Jan. 2022

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

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

#. **Results**
    a. Summary Data
    b. Data Values

Version 2.2.6
--------------

**Release date:** Dec. 22nd, 2021

*Current Availability* (New features and fixes in this release are denoted with a blue font color in the following list of features.)

#. **Structural Information Model**
    a. MDOF: creating idealized multi-degree-of-freedom models
    b. OpenSees: user-defined OpenSees models
    c. Steel Building Model: automating steel frame design and modeling

#. **Ground Motion Event**
    a. Stochastic Ground Motion: simulating stochastic ground motion recordings
    b. PEER NGA Records: selecting and scaling PEER NGA West2 ground motions
        * :blue:`Specifying the fault type, pulse-like feature, and duration filter in ground motion selection`
        * :blue:`Adding the option of "Geometric" suite average for the PEER NGA West2 ground motion selection`
    c. Site Response: propagating rock motions to the surface
    d. Multiple PEER: using multiple PEER recordings
    e. Multiple SimCenter: using multiple SimCenter-format recordings
    f. User Specified Database: selecting and scaling ground motions from the user-specified flatfile

#. **Finite Element Application**
    a. OpenSees: Open System for Earthquake Engineering Simulation

#. **Engineering Demand Parameter Generator**
    a. Standard Earthquake: maximum story drift ratio, lateral story displacement, peak floor acceleration
    b. User Defined: user-specified EDP
        * :blue:`Fixing the bug of using user-specified EDP names`

#. **Uncertainty Quantification**
    a. Dakota
        - Forward Propagation
        - Sensitivity Analysis
        - Reliability Analysis

#. **Results**
    a. Summary Data
    b. Data Values
        * :blue:`Fixing the bug of exporting ground motion names in the "Save Data"`


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

Version 3.1.0
----------------

**Release plan**: June 2022

*Planned features*

#. UQ: New surrogate modeling methods (e.g., SAF-IDA)
#. EVT: Invoking OpenQuake to generate scenario-based or classical PSHA ground motion spectral targets
#. FEM: invoking OpenSeesPy
#. ...\*

\*: Users are welcome to contact us on `forum <http://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0>`_ for new feature requests.
