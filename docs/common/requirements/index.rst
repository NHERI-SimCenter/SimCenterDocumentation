Requirements Traceability Matrix
================================

The Requirements Traceability Matrix (RTM) is presented as tables linking requirements with project deliverables. The software requirements are many. For ease of presentation they are broken into three groups:

#. Regional Scale - Activities to allow researchers to examine the resilience of a community to natural hazard events.
#. Building Scale - Activities to allow researchers to improve on methods related to response assessment and performance based design of individual buildings subject to the impact of a natural hazard.
#. Education - software development activities related to education of researchers and practicing engineers.

Within each group, software requirements are provided for the different software applications that SimCenter provides. As a result, some may be duplicated across applications.


The requirements for the SimCenter have been obtained from a number of sources:

#. GC: Grand challenges in hazard engineering are the problems, barriers, and bottlenecks that hinder the ideal of a nation resilient from the effects of natural hazards. The vision documents referenced in the solicitation [2, 3, 5, 6] outline the grand challenges for wind and earthquake hazards. These documents all present a list of research and educational advances needed that can contribute knowledge and innovation to overcome the grand challenges. The advances summarized in the vision documents were identified through specially formed committees and workshops comprising researchers and practicing engineers. They identified both the grand challenges faced and also identified what was needed to address these challenges. The software needs identified in these reports that are applicable to research in natural hazards as permitted under the NSF NHERI program were identified in these reports. Those tasks that the NHERI SimCenter identified as pertaining to aiding NHERI researchers perform their research and those which would aid practicing engineers utilize this research in their work are identified here.
#. SP: From the senior personnel on the SimCenter project. The vision documents outline general needs without going into the specifics. From these general needs the senior personnel on the project  identified specific requirements  that would provided a foundation to allow research.
#. UF: SimCenter workshops, boot camps and direct user feedback. As the SimCenter develops and releases tools, feedback from researchers using these tools is obtained at the tool training workshops, programmer boot-camps,  in one-on-one discussions, via direct email, and through online user feedback surveys. 



   


Regional Scale Applications
---------------------------

For regional scale, the requirements are broken down into 3 clasees. AI related requirements in BRAILS, backend workflow requirements in rWhale, and fronmt end user interface requirements in RDT.

.. toctree-filt::
   :caption: Regional Scale 
   :maxdepth: 1
   :numbered: 4
	     
   BRAILS
   pelicun
   rWhale
   RDT 

.. include:: ./bigRequirements.rst


Building Scale Applications
---------------------------

For building scale simulations, the requirements are broken down by SimCenter application. There are a number of applications under development for each of the hazards. Many of the requirements related to UQ and nonlinear analysis are repeated amongst the different applications under the assumption that if they are beneficial to engineers dealing with one hazard, they will be beneficial to engineers dealing with other hazards.

.. toctree-filt::
   :caption: Building Scale
   :maxdepth: 1
   :numbered: 4
	     
   WEUQ
   EEUQ   


quoFEM
------

The following are the requirements are being for the quoFEM application. quoFEM is an application proving UQ and Optimization methods to existing FEM applications. uqFEM has a lower level interface to UQ and Optimization methods than the other applications (WE-UQ, EE-UQ, and PBE). It is thus a more powerful tool providing more capabilities for researchers. All requirements in this section are related to work in WBS 1.3.8.

.. include:: QUOFEM.rst



Performance Based Engineering
-----------------------------

The following are the requirements for application(s) related to performance based engineering of a single structure related to natural hazards such as earthquake and hurricane . The requirements are being met by the PBE application. All requirements in this section are related to work in WBS 1.3.9.

.. include:: PBE.rst

Educational Software
--------------------

The following are educational activities obtained that are related to software development.

.. include :: edRequirements.tex

Contact
=======
Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
