
|full tool name|
=====================================================================

The intended audience for the |full tool name| (|short tool name|) are researchers and practitioners interested in predicting the response of a structure to earthquake events.

This is an open-source research application. The source code at the |tool github link| provides 
an application that can be used to predict the
response of a building subjected to earthquake events. The application
is focused on quantifying the uncertainties in the predicted response,
given the that the properties of the buildings and the earthquake
events are not known exactly, and that both the simulation software
and the user make simplifying assumptions in the numerical modeling of
that structure. In this application, the user is required to
characterize the uncertainties in the input. The application will,
after utilizing the users selected sampling method, provide
information that characterizes the uncertainties in the computed
response measures. As the computations to make these determinations
can be prohibitively expensive to perform on a user's local computer,
the user has the option to perform the computations remotely on the
Stampede2 supercomputer. Stampede2 is located at the Texas Advanced
Computing Center (TACC) and made available to the user through NHERI
DesignSafe, the cyberinfrastructure provider for the distributed NSF
funded Natural Hazards in Engineering Research Infrastructure (NHERI)
facility.


The computations are performed, as discussed in the :ref:`lbl-technical-manual`, in a workflow application. That is, the numerical simulations are performed by a sequence of applications. The |short tool id| backend software runs these applications for the user, taking the outputs from some programs and providing them as inputs to others. The design of the |short tool name| is such that researchers are able to modify the backend application to utilize their own application in the workflow computations. This ensures that researchers are not limited to using the default applications we provide and will be enthused to provide their own applications for others to use.

This is Version |tool version| of the tool. Users are encouraged to comment on what additional features and capabilities they would like to see in this application. These requests and feedback can be submitted through an anonymous |user survey link|. We greatly appreciate any input you have. If there are features you want, chances are many of your colleagues also would benefit from them. Users are encouraged to review the :ref:`lbl-requirements` to see what features are planned for this application.

.. _lbl-user-manual:

.. toctree::
   :caption: User Manual
   :maxdepth: 2
   :numbered: 2

   userManual


.. _lbl-technical-manual:

.. toctree::
   :caption: Technical Manual
   :maxdepth: 2
   :numbered: 2

   technicalManual


.. _lbl-developer-manual:

.. toctree::
   :caption: Developer Manual
   :maxdepth: 2
   :numbered: 2

   developerManual

Developers
==========

Adam Zsarnóczay 

Frank McKenna

Wael Elhaddad

Chaofeng Wang

Michael Gardner

License
=======

The |full tool name| is distributed under the BSD 3-Clause license, see :ref:`lbl-license` for details.

Acknowledgement
===============

This material is based upon work supported by the National Science Foundation under Grant No. 1612843. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

Contact
=======
Adam Zsarnóczay, NHERI SimCenter, Stanford University, adamzs@stanford.edu