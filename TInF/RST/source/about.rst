About TInF
===========

The intended audience for this tool is researchers and practitioners
interested in predicting the response of a structure to earthquake
events.

This open-source research application, the source code of which is
available at the https://github.com/NHERI-SimCenter/TInF
Github page, provides an application that can be used to predict the
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

Whether running locally or remotely, the computations are performed,
as will be discussed in Chapter :ref:`chap_theory`, in a workflow
application. That is, the numerical simulations are actually performed
by a number of different applications. The TInF backend software runs
these different applications for the user, taking the outputs from
some programs and providing them as inputs to others. The design of
the TInF application is such that researchers are able to modify the
backend application to utilize their own application in the workflow
computations. This will ensure researchers are not limited to using
the default applications we provide and will be enthused to provide
their own applications for others to use.

This document covers Version
\getsoftwareversion{}
of the tool. Users are
encouraged to comment on what additional features and capabilities
they would like to see in this application. These requests and
feedback can be submitted through an anonymous
\insertsurveylink{user survey};
we greatly appreciate any input you have. If there are
features you want, chances are many of your colleagues also would
benefit from them. Users are encouraged to review
Chapter :ref:`chap_requirements` to see what features are planned for this
application.

