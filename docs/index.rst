|full tool name|
=====================================================================


.. only:: PBE_app

   The |full tool name| (|app|) is an open-source research application that can be used to predict the performance of a building subjected to earthquake events. The application is focused on quantifying building performance given the that the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 

.. only:: EEUQ_app

   The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to earthquake events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 


.. only:: WEUQ_app

   The |full tool name| (|app|) is an open-source research application that can be used to predict the response of a building subjected to wind loading events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, wind loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 

.. only:: QUOFEM_app
   
   The |full tool name| (|app|) is an open-source research application which focuses on providing uncertainty quantification methods (forward, inverse, reliability, sensitivity and parameter estimation) to researchers in natural hazards who utilize existing simulation software applications, typically Finite Element applications, in their work.

This document covers the features and capabilities of Version |tool version|  of the tool. Users are encouraged to comment on what additional features and capabilities they would like to see in future versions of the application through the |messageBoard|.


.. _lbl-user-manual:

.. toctree-filt::
   :caption: User Manual
   :maxdepth: 1
   :numbered: 4

   common/user_manual/ack
   :EEUQ:common/aboutEE
   :PBE:common/aboutPBE
   :WEUQ:common/aboutWE
   :QUOFEM:common/aboutQUOFEM
   common/user_manual/installation/installation
   common/user_manual/usage/usage
   common/user_manual/troubleshooting/troubleshooting
   common/user_manual/examples/examples
   :EEUQ:common/requirements/EEUQ
   :WEUQ:common/requirements/WEUQ
   :PBE:common/requirements/PBE
   common/bugs
   common/license

.. _lbl-technical-manual:

.. toctree::
   :caption: Technical Manual
   :maxdepth: 1
   :numbered: 2

   common/technical_manual/technical_manual


.. _lbl-developer-manual:

.. toctree::
   :caption: Developer Manual
   :maxdepth: 1
   :numbered: 4

   common/developer_manual/how_to_build/how_to_build
   common/developer_manual/architecture/architecture
   common/developer_manual/how_to_extend/how_to_extend
   common/developer_manual/verification/verification
   common/developer_manual/coding_style/coding_style

#   common/developer_manual/API/API


Developers
==========

.. only:: PBE_app

   | Frank McKenna
   | Adam Zsarnóczay 
   | Wael Elhaddad
   | Chaofeng Wang
   | Michael Gardner

.. only:: EEUQ_app

   | Frank McKenna
   | Wael Elhaddad
   | Chaofeng Wang
   | Michael Gardner


.. only:: WEUQ_app

   | Frank McKenna
   | Jiawei Wan
   | Wael Elhaddad
   | Peter Mackenzie-Helnwein
   | Michael Gardner


Contact
=======
Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu