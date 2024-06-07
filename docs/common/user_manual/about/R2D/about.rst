.. _lblAbout:

******
About
******

This open-source research application, which is available at the |tool github link|, is released under the **2-Clause BSD** license (see :ref:`lblLicense`).

The Regional Resilience Determination (R2D) tool is an extensible scientific workflow system that can be used to quantify the effects of hazards on regional communities. The tool incorporates the same workflow components used in the WE-UQ, EE-UQ, and PBE tools, extended to consider multiple asssets and regionally distributed hazards. 



Whether running locally or remotely, the computations are performed by an application called rWHALE, as discussed in the :ref:`lbl-technical-manual`. rWHALE executes the scientific workflow by invoking several applications, taking outputs from some programs, and providing them as inputs to others. The design of the R2D and rWHALE applications allows researchers to incorporate their own applications into the workflow. This flexibility ensures that researchers are not limited to the default applications provided and encourages them to share their custom applications for others to use.

Since computations can be prohibitively expensive to perform on a user's local computer, especially with uncertainty quantification involved, users have the option to perform these computations remotely on the Frontera supercomputer. Frontera is located at the Texas Advanced Computing Center (TACC) and is accessible to users through NHERI DesignSafe, the cyberinfrastructure provider for the NSF-funded Natural Hazards in Engineering Research Infrastructure (NHERI) facility network.

This document covers Version |tool version| of the tool. Users are encouraged to suggest additional features and capabilities they would like to see in this application. Feedback can be submitted through the |messageBoard|, and we greatly appreciate any input. If there are features you desire, it is likely that many of your colleagues would benefit from them as well. Users should also review the |app requirements| to see which features have already been requested.