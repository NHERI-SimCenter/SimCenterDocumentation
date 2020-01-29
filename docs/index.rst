|full tool name|
=====================================================================

The intended audience for the |full tool name| (|short tool name|) are researchers and practitioners interested in predicting the seismic performance of buildings.

.. only:: PBE_app

   This is an open-source research application that can be used to predict the performance of a building subjected to earthquake events. The application is focused on quantifying building performance given the that the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 

.. only:: EEUQ_app

   This is an open-source research application that can be used to predict the response of a building subjected to earthquake events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, earthquake loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 


.. only:: WEUQ_app

   This is an open-source research application that can be used to predict the response of a building subjected to wind loading events. The application is focused on quantifying the uncertainties in the predicted response, given the that the uncertainties in models, wind loads, and analysis. The computations are performed in a workflow application that will run on either the users local machine or on a high performance computer made available by |DesignSafe|. 


This document covers Version |tool version|  of the tool. Users are encouraged to comment on what additional features and capabilities
they would like to see in this application through the |messageBoard|.


.. _lbl-user-manual:

.. toctree-filt::
   :caption: User Manual
   :maxdepth: 1
   :numbered: 4

   :EEUQ:common/aboutEE
   :PBE:common/aboutPBE
   common/license
   common/user_manual/installation/installation
   common/user_manual/usage/usage
   common/user_manual/troubleshooting/troubleshooting
   common/user_manual/examples/examples
   common/bugs

#   common/user_manual/requirements/requirements




.. _lbl-technical-manual:

.. toctree::
   :caption: Technical Manual
   :maxdepth: 2
   :numbered: 2

   common/technical_manual/technical_manual


.. _lbl-developer-manual:

.. toctree::
   :caption: Developer Manual
   :maxdepth: 2
   :numbered: 2

   common/developer_manual/how_to_build/how_to_build
   common/developer_manual/architecture/architecture
   common/developer_manual/how_to_extend/how_to_extend
   common/developer_manual/verification/verification
   common/developer_manual/coding_style/coding_style

#   common/developer_manual/API/API


Developers
==========

Adam Zsarnóczay 

Frank McKenna

Wael Elhaddad

Chaofeng Wang

Michael Gardner

Acknowledgement
===============

This material is based upon work supported by the National Science Foundation under Grant No. 1612843. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

Contact
=======
Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu