.. _lblArchitectureOverview:

Overview
========

A Level 1 diagram showing the system context for the SimCenter applications, i.e., how it fits in the world,
is shown in :numref:`architecture figContext`. It shows SimCenter applications (EE-UQ, WE-UQ, HydroUQ, PBE, R2D) as a box in the center surrounded by the user and the user's systems. The SimCenter applications allow a user to create and run scientific workflow applications; the data for the applications may be obtained from the web or DataDepot. The workflow applications are run on either the local desktop or on some HPC at |DesignSafe|.

.. _architecture figContext:

.. figure:: figures/context.png
   :align: center
   :width: 800
   :figclass: align-center

   System context diagram for SimCenter applications.

Given how SimCenter applications fit in with the environment, a level 2 diagram demonstrates how the
SimCenter applications are broken into high-level components. The SimCenter applications are, as shown in
:numref:`architecture figContainer`, split into two components: A front-end UI and a back-end application that runs the workflow. The front-end applications are desktop applications written using the cross-platform `Qt framework <https://www.qt.io/product/framework>`_. The back end is an application that processes the input from the front end, which comes in the form of a JSON file, creates a workflow, and runs it. The workflow applications, written in Python, C, or C++, utilize existing applications where possible and run on either the local desktop machine or on an HPC utilizing resources made available to the NHE community through DesignSafe.

.. _architecture figContainer:

.. figure:: figures/container.png
   :align: center
   :width: 800
   :figclass: align-center

   System container diagram for SimCenter applications.

Two level 3 diagrams are now presented, which break up the two containers into the major building blocks or
components in C4 terminology. In :numref:`architecture figComponentFront`, the component diagram for the front-end UI is presented. It outlines the interaction between the user and the individual graphical elements (widgets) of the UI. Given the jigsaw puzzle analogy, the user selects which piece of the jigsaw puzzle they are working on in the component selection widget. The widget for the jigsaw piece will then be displayed on the desktop. The user for each jigsaw piece then selects which application to run for that piece. For the chosen application, they provide the inputs. When the inputs are all provided, the user can choose to run the simulations locally or remotely. For jobs that run remotely, the user can download and review previously run simulations. As seen, the widgets may subsequently interact with web services through HTTPS requests or with DesignSafe utilizing TAPIS Restful API through the RemoteService container.

.. _architecture figComponentFront:

.. figure:: figures/componentFront.png
   :align: center
   :width: 800
   :figclass: align-center

   Component diagram for front-end UI.

The component diagram for the back-end application shown in :numref:`architecture figComponentBack`, shows that the back-end comprises several component applications. The application ``femUQ.py`` is the application that parses the input from the front end, sets up the workflow by creating a ``workflow_driver`` script and then launches the UQ engine. The choice of UQ Engine and applications to run in the workflow is determined from the data passed from the UI and information contained in a file, ``WorkflowApplication.json``. The ``WorkflowApplication.json`` file is a file that maps the applications specified in the output from the UI with a specific application contained on the users' local machine or at the remote HPC resource, as such it allows the researchers to modify the applications that may be run in the workflow w/o the need to recompile the application. Once the ``workflow_driver`` file is created, control is passed to a UQ engine, which repeatedly runs the ``workflow_driver`` to generate the results. In running the workflow, some of the applications will invoke applications not developed to meet the API. For such applications, pre- and post-processors are provided. The figure shows the back-end application running locally or remotely on an HPC at DesignSafe.

.. _architecture figComponentBack:

.. figure:: figures/componentBack.png
   :align: center
   :width: 800
   :figclass: align-center

   Component diagram for Backend Application.

.. note::
   ``femUQ.py`` is the back-end application for the EE-UQ, WE-UQ, Hydro-UQ, and PBE applications. For R2D, the back-end application is ``R2D_Workflow.py``.

The interaction between the front-end and the back-end is best understood by looking at the sequence of events when the user presses the ``Run`` button. As shown in the figure below, the UI application will first perform several steps:

1. It will create a temporary directory in the Documents folder named ``tmp.SimCenter``, and inside ``tmp.SimCenter`` will create another directory ``templatedir``.

2. It will then run through all the currently selected widgets and invoke the ``copyFiles()`` method, telling these widgets to copy all files needed during the workflow to the ``templatedir`` directory.

3. It will then create a JSON file and will run through the currently selected widgets and on each invokes the methods ``outputToJSON()`` and ``outputAppDataToJSON``, these telling the application to augment the JSON file with the inputs the user has provided in the widget and also the name of the widget.

4. The UI will start the back-end application and spin until the back-end application returns with a completion signal.

Now that the UI has been handed over to the back-end application, the back-end application will perform the following:

5. Open the output file from the UI and parse it to obtain the name of the application to run and the arguments to run the application with. Open up another file, the ``WorkflowApplications.json`` file, contained with the application to determine, given the application name, the full path to the executable to be invoked. It will create in ``templatedir`` a file named ``workflow_driver``. When run by the UQ engine, this file is a script file that will generate a file named ``results.out``. ``results.out`` when the ``workflow_driver`` script has completed will contain a single line of space-separated values, one value for each EDP.
   
6.  It will invoke each application with supplied arguments and an additional command-line argument, ``--getRV``, to inform the application to process the input file and create any additional random variables and input files needed before the workflow runs.

7. It will then launch the UQengine. The UQengine is typically a pre- and post-processor to an existing UQ engine.

8. The pre-processor takes the JSON input file and creates an input file needed by the actual UQ engine.

9. The pre-processor will launch the UQ application. This application will typically run the ``workflow_driver`` many times, passing as input to the workflow a file ``\params`` and obtaining output from the ``workflow_driver`` a file ``results.out``.

10. When done, the engine will output its results.

11. The UQengine will notify the UQpreprocessor that it is done.

12. The UQpreprocessor will notify the femUQ application that it is done.
    
13. The femUQ application will notify the UI that it is done.

14. The UI will read the results and present them to the user.
    

.. _architecture figSequenceLocal:

.. figure:: figures/sequenceLocal.png
   :align: center
   :width: 800
   :figclass: align-center

   Sequence diagram showing what happens when a Workflow runs Locally


That is for the case where the computations are performed on the local computer. When the computations are
performed remotely, the steps are different. The first 8 steps are the same. But now, the UQwrapper will not
start the UQ engine. Instead, control is returned to the UI. The UI will, as shown in the following: (11)
Compress the temporary folder. (12) Send the compressed folder to the remote HPC, shown in
:numref:`architecture figSequenceRemote`. (13) Start an application to perform the computations. All the remote data transfer and application invocation is down through a cloud service. The `TACC tapis <https://tapis-project.org/>`_ interface is used to provide SimCenter users with access to the TACC HPC resources through the DesignSafe portal.


.. _architecture figSequenceRemote:

.. figure:: figures/sequenceRemote.png
   :align: center
   :width: 800
   :figclass: align-center

   Sequence diagram showing what happens when a Workflow runs Remotely

.. only:: R2D_app

   .. include:: R2Dworkflows.rst
