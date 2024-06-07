.. raw:: latex

    \begin{landscape}


################################
Requirements Traceability Matrix
################################

++++++++++++
Introduction
++++++++++++

.. note::
   The contents of this document are also available online at https://nheri-simcenter.github.io/RTM-Documentation/index.html. It might be more up-to-date and easier to review than this PDF version.


The SimCenter has relied on community input to drive application and educational activities. We track these inputs as requirements in our Requirements Traceability Matrix (RTM). This is a living document, which is updated at least yearly. In this document is listed the general requirements for each tool and for each tool, there is also listed the requirements for each component that is used to build up the tool. The components are as shown in the figure below, for example, EE-UQ has components of Cloud (CLD), Reliability (UQR), Sensitivity (UQS), Sampling (UQF), Modelling (MOD), Earthquake Loading (EL), and Analysis (ANA).

.. _figRTM:

.. figure:: figures/RTM.png
   :align: center
   :width: 60%
   :figclass: align-center

   Application & Component Abbreviations for RTM

Each requirement in the RTM has the following entry fields:

   #. A unique identifier, which is a combination of an abbreviation of a tool or component name, plus one or more numbers; with the sequence of numbers indicating a hierarchy in the requirements.

   #. A brief description of the requirement.

   #. A source for the requirement indicating where the requirement originated. That can be one of three:
      
      #. GC: Grand challenges in hazard engineering are the problems, barriers, and bottlenecks that hinder the ideal of a nation resilient from the effects of natural hazards. The vision documents referenced in the solicitation ([NSTC2006]_, [NSB2007]_, [NEHRP2008]_, [Fenves2011]_, [NIST2014]_) outline the grand challenges for wind and earthquake hazards. These documents all present a list of research and educational advances needed that can contribute knowledge and innovation to overcome the grand challenges. The advances summarized in the vision documents were identified through specially formed committees and workshops comprising researchers and practicing engineers. They identified both the grand challenges faced and also identified what was needed to address these challenges. The software needs that were identified in these reports that apply to research in natural hazards as permitted under the NSF NHERI program were identified in these reports. Those tasks that the NHERI SimCenter identified as pertaining to aiding NHERI researchers perform their research and those that would aid practicing engineers utilize this research in their work are identified here.
	 
      #. SP: From the senior personnel on the SimCenter project. The vision documents outline general needs without going into the specifics. From these general needs the senior personnel on the project identified specific requirements that would provide basic functionality to allow research.
    
      #. UF: SimCenter workshops, boot camps, and direct user feedback. As the SimCenter develops and releases tools, feedback from researchers using these tools is obtained at the tool training workshops, programmer boot camps, in one-on-one discussions, via direct email, and through online user feedback surveys. For the feedback related to what additional functionality to include, entries are added to the RTM. For other feedback, related to simple tasks related to the operation of tool and UI, entries are placed in our Jira system.

   #. A designation determined by the management group indicating the importance of the requirement, which again has 3 possible values:
     #.   M - Mandatory: This requirement must be satisfied 
     #.   D - Desirable: It would be desirable to implement the functionality as it would aid research. If time and resources permit it should be.
     #.   P - Possible: Such an activity is possible within the SimCenter Framework. SimCenter could work to include it or work with NHERI researchers to do so.

  #. A column indicating whether the requirement has been implemented and is available to users.

  #. A column indicating which examples are provided that can be used to test the features.


.. toctree-filt::
   :caption: All Requirements
   :maxdepth: 1
   :numbered: 4

   All-Requirements_allCols

   
Contact
=======
Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu

References
==========

.. [Fenves2011]
   Fenves, G. L., Poland, C. D., Crewe, A. J., Eguchi, R., T., Hajjar, J. F., Lynch, J. P., and Nakashima, M. (2011). Grand Challenges in Earthquake Engineering, National Research Council, National Academies Press, Washington, D.C., 90 pp.

.. [NEHRP2008]
   Strategic Plan for the National Earthquake Hazards Reduction Program, Fiscal Years 2009-2013, National Earthquake Hazards Reduction Program. http://www.nehrp.gov/pdf/strategic_plan_2008.pdf.

.. [NIST2014] Measurement Science R&D Roadmap for Windstorm and Coastal Inundation Impact Reduction
NIST GCR 14-973-13 http://www.nist.gov/customcf/get_pdf.cfm?pub_id=915541.

.. [NRC2011] National Earthquake Resilience: Research, Implementation, and Outreach.National Research Council. Washington, DC. The National Academies Press, https://www.nap.edu/catalog/13092/national-earthquake-resilience-research-implementation-and-outreach 

.. [NSB2007] Hurricane Warning-The Critical Need for a National Hurricane Research Initiative. National Science Board. https://www.nsf.gov/nsb/publications/landing/nsb06115.jsp?org=NSF.

.. [NSTC2006] Windstorm Impact Reduction Implementation Plan, National Science and Technology Council. https://www.preventionweb.net/publications/view/1559


.. raw:: latex

    \end{landscape}
	     
