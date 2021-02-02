################################
Requirements Traceability Matrix
################################

++++++++++++
Introduction
++++++++++++

The requirements for the SimCenter have been obtained from a number of sources:

#. GC: Grand challenges in hazard engineering are the problems, barriers, and bottlenecks that hinder the ideal of a nation resilient from the effects of natural hazards. The vision documents referenced in the solicitation [2, 3, 5, 6] outline the grand challenges for wind and earthquake hazards. These documents all present a list of research and educational advances needed that can contribute knowledge and innovation to overcome the grand challenges. The advances summarized in the vision documents were identified through specially formed committees and workshops comprising researchers and practicing engineers. They identified both the grand challenges faced and also identified what was needed to address these challenges. The software needs identified in these reports that are applicable to research in natural hazards as permitted under the NSF NHERI program were identified in these reports. Those tasks that the NHERI SimCenter identified as pertaining to aiding NHERI researchers perform their research and those which would aid practicing engineers utilize this research in their work are identified here.
#. SP: From the senior personnel on the SimCenter project. The vision documents outline general needs without going into the specifics. From these general needs the senior personnel on the project  identified specific requirements  that would provided a foundation to allow research.
#. UF: SimCenter workshops, boot camps and direct user feedback. As the SimCenter develops and releases tools, feedback from researchers using these tools is obtained at the tool training workshops, programmer boot-camps,  in one-on-one discussions, via direct email, and through online user feedback surveys. 

The Requirements Traceability Matrix (RTM) is presented as tables linking requirements with project deliverables. The software requirements are many. For ease of presentation they are broken into three groups: 1) Building Scale Applications, 2) Regional Scale Applications, and 3) Education and Outreach Activities.


+++++++++++++++++++++++++++
Building Scale Applications
+++++++++++++++++++++++++++

Applications to allow researchers to improve on methods related to determining on the response assessment and performance based design of individual buildings subject to the impact of a natural hazard. For building scale simulations, the requirements are broken down by SimCenter application. There are a number of applications under development for each of the hazards. Many of the requirements related to UQ and nonlinear analysis are repeated amongst the different applications under the assumption that if they are beneficial to engineers dealing with one hazard, they will be beneficial to engineers dealing with other hazards.

.. toctree-filt::
   :caption: Building Scale
   :maxdepth: 1
   :numbered: 4

   QUOFEM
   WE-UQ
   EE-UQ
   HydroUQ
   PBER


+++++++++++++++++++++++++++
Regional Scale Applications
+++++++++++++++++++++++++++

For regional scale, the requirements are broken down into four classes. AI related requirements in **BRAILS**, damage and loss prediction in **pelicun**, backend workflow requirements in **rWhale**, and front end user interface requirements in **R2D**.

.. toctree-filt::
   :caption: Regional Scale 
   :maxdepth: 1
   :numbered: 4
	     
   BRAILS
   pelicun
   rWhale
   R2D
   testbeds


++++++++++++++++++++
Educational Software
++++++++++++++++++++

The following are educational activities obtained that are related to software development.

.. toctree-filt::
   :caption: Education
   :maxdepth: 1
   :numbered: 4

   edRequirements

Contact
=======
Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu
