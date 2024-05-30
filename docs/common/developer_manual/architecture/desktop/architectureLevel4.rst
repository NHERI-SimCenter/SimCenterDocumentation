***************************
Four-Level Architecture
***************************

The SimCenter is developing a software framework for building scientific workflow applications to perform computational simulations in the field of NHE at both building level scale and regional scale. It is releasing a number of applications built using this framework. The |app| is one of those applications which has been released (EE-UQ, WE-UQ, PBE). Other applications are under development (R2D). The applications that the SimCenter is developing are limited scientific workflow systems. This chapter presents the software architecture for the framework and the |app| built using it using the C4 model.


Level 1: Context for SimCenter Applications
============================================

A Level 1 diagram showing the system context for the SimCenter applications, i.e., how it fits into the world, is shown in :numref:`figContext`. It shows SimCenter applications (EE-UQ, WE-UQ, PBE, R2D) as a box in the center surrounded by the user and the systems with which it and the user interact. The SimCenter applications allow users to create and run scientific workflow applications; the data for the applications may be obtained from the web or DataDepot, and the workflow applications are run either on the local desktop or on some HPC at |DesignSafe|.

.. _figContext:

.. figure:: figures/context.png
   :align: center
   :figclass: align-center

   System context diagram for SimCenter Applications.


Level 2: Components of a SimCenter Application
================================================

Given how SimCenter applications fit in with the environment, a Level 2 diagram now demonstrates how the SimCenter applications are broken into high-level components. The SimCenter applications are, as shown in :numref:`figContainer`, broken into two components: A front-end UI and a back-end application that runs the workflow. The front-end applications are desktop applications written using the cross-platform Qt framework. The back end is an application that processes the input from the front end, which comes in the form of a JSON file, creates a workflow, and runs it. The workflow applications, written in Python, C, or C++, utilize existing applications where possible and run either on the local desktop machine or on an HPC utilizing resources made available to the NHE community through DesignSafe.

.. _figContainer:

.. figure:: figures/container.png
   :align: center
   :figclass: align-center

   System container diagram for SimCenter applications.

Level 3: Container Diagrams for the Front and Back-End Components
=================================================================

Two Level 3 diagrams are now presented which break up the two containers into the major building blocks or components in C4 terminology. In :numref:`figComponentFront` the component diagram for the front-end UI is presented. It outlines the interaction between the user and the individual graphical elements (widgets) of the UI. Given the analogy of a jigsaw puzzle, the user selects which piece of the jigsaw puzzle they are working on in the component selection widget. The widget for the jigsaw piece will then be displayed on the desktop. The user for each jigsaw piece then selects which application to run for that piece, and for the chosen application, they provide the inputs. When the inputs are all provided, the user can select to run the simulations locally or remotely. For jobs that run remotely, the user can download and review previously run simulations. As seen the widgets may subsequently interact with web services through HTTPS requests or with DesignSafe utilizing TAPIS Restful API through the RemoteService container.

.. _figComponentFront:

.. figure:: figures/componentFront.png
   :align: center
   :figclass: align-center

   Component diagram for the front-end UI.

The component diagram for the backend application shown in :numref:`figComponentBack` shows that the backend is made up of several components, all applications. The application ``femUQ.py`` is responsible for parsing the input from the front end, setting up the workflow, and launching the UQ engine. The specific UQ Engine and applications to run in the workflow are determined from the data passed from the UI and information contained in a WorkflowApplication.json file. This file allows researchers to modify the applications that may be run in the workflow without the need to recompile the application. Control is then passed to a UQ Engine, which repeatedly runs the workflow to generate the results. During the execution of the workflow, some applications may invoke other applications not developed to meet the API. For such applications, pre- and post-processors are provided.

The figure shows the backend application running locally or remotely on an HPC@DesignSafe.

.. _figComponentBack:

.. figure:: figures/componentBack.png
   :align: center
   :figclass: align-center

   Component diagram for the backend application.

Level 4 UML Diagrams
====================

A number of diagrams are presented for the level 4 diagrams. These are mostly UML diagrams showing how the applications are built. The SimCenter releases several front-end applications: EE-UQ shown in :numref:`figUmlEE`, WE-UQ shown in :numref:`figUmlWE`, and PBE shown in :numref:`figUmlPBE`. These applications share code with each other and other SimCenter applications. Consequently, the common code is bundled into several shared packages: EarthquakeEvents shown in :numref:`figUmlEarthquakeEvents`, WindEvents shown in :numref:`figUmlWindEvents`, and SimCenterCommon shown in :numref:`figUmlCommon`. Several packages were chosen instead of placing all common code inside a single package to simplify development efforts for outside programmers (who will mostly be adding new event components) and to reduce the overhead of package management and compile time for SimCenter programmers. UML diagrams are presented for these front-end applications and shared packages. The UML diagrams presented are not exhaustive; they do not show all classes used because it was decided not to show, for example, the myriad of Line edits, labels, spin boxes, etc., that make up the widgets. What is shown is sufficient to present the SimCenter architecture.

While there are various types of UML diagrams, those shown in this document will be limited to class diagrams and sequence diagrams. SimCenter applications are object-oriented. An object-oriented program consists of objects interacting with one another, with each object being of a certain type or class. A class diagram shows the classes, their attributes and methods, and the relationships between the classes. A sequence diagram or event diagram shows the order in which objects interact. To understand the SimCenter framework, it is useful to first present the main() function for a SimCenter application, in this case, EE-UQ, shown in :numref:`codeMainCode`. The code presented is a stripped-down version of the actual code; code for dealing with style sheets, analytics, etc., is not shown as it is not pertinent to understanding the software architecture.


.. _codeMainCode:

.. code-block::

   int main(int argc, char *argv[]) {

     QApplication app(argc, argv);
 
    //                                                                       
    // create a remote interface                                             
    //                                                                       

    QString tenant("designsafe");
    QString storage("agave://designsafe.storage.default/");
    QString dirName("EE-UQ");
    
    //                                                                       
    // create the main window                                                
    // 
    
    WorkflowAppWidget *theInputApp = new WorkflowAppEE_UQ(theRemoteService);
    MainWindowWorkflowApp window(QString("EE-UQ: Response of Building to Earthquake"), theInputApp, theRemoteService);
    
    window.setVersion("Version 1.0.0");


    //                                                                       
    // move the remote interface to a thread                                     
    //                                                                       

    QThread *thread = new QThread();
    theRemoteService->moveToThread(thread); 
    thread->start();

    //                                                                       
    // show the main window, set styles & start the event loop               
    //                                                                       

    window.show(); 
    int res = app.exec();

    //                                                                       
    // once done with the event loop, logout & stop the thread                     
    //                                                                       

    theRemoteService->logout();
    thread->quit();
    
     return res;
   }


As mentioned, front-end UI applications are built using Qt. In a Qt application, the programmer creates a QApplication object, named `app` in this case, and a QMainWindow, named `window` in the example. As shown in :numref:`figUmlCommon`, MainWindowWorkflowApp is a type of QMainWindow used in all SimCenter research applications, handling all application menu items such as File open and close, Help cites, etc. QMainWindowWorkflowApp is a SimCenter class containing a single QWidget of type WorkflowAppWidget. The WorkflowAppWidget object is passed a RemoteService, the remote cloud service with which the application will interact. This RemoteService is placed in its own QThread object so that the UI can respond to user requests while communication with the cloud service is underway. Once the window object is shown, control is passed to the QApplication until the user is done.

.. _lblUmlEE:

UML EE-UQ
---------

EE-UQ is an application to determine the response of a building subjected to an earthquake event. As shown in :numref:`figumlEE`, it comprises a component selection that presents the user with a number of components, jigsaw pieces, which include: earthquake event (EarthquakeEventSelection), UQ engine (UQ Selection), demand parameters of interns (EDP Selection), building information model (BIM Selection), structural analysis model generator (SAM Selection), finite element application (FEM Selection), and RandomVariableContainer. RandomVariableContainer is a widget allowing the user to specify distributions associated with the random variables created by a user. As will be seen in :numref:`figUmlEarthquakeEvents` and :numref:`figUmlCommon`, each component offers the user a number of applications to choose from for that component. Other classes corresponding to widgets presented in the Front-end UI include: UQ Result for displaying the results, Local and Remote Services for running the job locally or remotely, Remote job Manager for monitoring job status and retrieving old jobs, and Login for obtaining credentials from DesignSafe to access and run jobs on the HPC resources. All communication between the applications and DesignSafe-ci is through the Application Service. This is done to allow the applications to switch to other cloud service providers, possibly allowing applications to run at DesignSafe, on Amazon EC-2, IBM's Azure, or elsewhere.

.. _figUmlEE:

.. figure:: figures/umlEE.png
   :align: center
   :figclass: align-center

   UML Diagram for EE-UQ

.. _lblUmlWE:

UML WE-UQ
---------

Similar in construction to EE-UQ is WE-UQ, as shown in figure :numref:`figumlWE`. In fact, the only difference is that Wind Event Selection is present in the component selection, instead of Earthquake Events. The wind event applications, as will be shown in :numref:`figWindEvents`, include stochastic wind models, wind loading from online services such as Vortex-Winds, and applications that take online wind tunnel experimental datasets such as those from Tokyo Polytechnic.

.. _figUmlWE:

.. figure:: figures/umlWE.png
   :align: center
   :figclass: align-center

   UML diagram for WE-UQ.

.. only:: PBE

.. _lblUmlPBE:

UML PBE
-------

PBE is a tool for performance-based engineering. Given a building and an event, it will calculate downtime and loss estimates. As can be seen in :numref:`figumlPBE`, it adds a LossModelSelection to the component Selections available in EE-UQ. The Loss Model applications currently available for selection include a P58 Loss Model and a HAZUS Loss Model. Depending on the selection, different widgets are presented for the user to input the different input arguments needed for the different loss model calculations. Presently, the calculations for both loss models are performed by the same Python script, CalculateDL.py, in the collection of backend applications.

.. _figUmlPBE:

.. figure:: figures/umlPBE.png
   :align: center
   :figclass: align-center

   UML diagram for PBE.

.. _lblUmlEarthquakeEvents:

UML Earthquake Events
--------------------

The Earthquake Events package, as shown in :numref:`figumlEarthquakeEvents`, contains an Earthquake Event selector with several Earthquake Event selections available. The selections include options that interface with the NGA west server directly and options that will collect inputs for stochastic input models of Vlachos et al. or Dabahi and DerKiuerghian, peer NGA records, site response, and our SimCenterEvent format. Each of these widgets corresponds to one application in the backend, e.g., RockOutcrop corresponds to SiteResponse, and it is this application that will run when the workflow runs.

.. _figUmlEarthquakeEvents:

.. figure:: figures/umlEarthquakeEvents.png
   :align: center
   :figclass: align-center

   UML diagram for earthquake events.

.. _lblUmlWindEvents:

UML Wind Events
---------------

Similar to the Earthquake Events package, the wind events package shown in :numref:`figumlWindEvents` contains a Wind Event Selector with a number of Wind Event selections available. The selections include options for stochastically generated wind events, events that obtain wind loading from the vortex-winds server, and options to obtain forces from wind tunnel events, either from the Tokyo Polytechnic University database or a user-supplied file.

.. _figUmlWindEvents:

.. figure:: figures/umlWindEvents.png
   :align: center
   :figclass: align-center

   UML diagram for wind events.

.. _lblSimCenterCommon:

SimCenter Common
----------------

SimCenter Common, shown in :numref:`figUmlCommon`, contains a number of component selections: BIM selection, EDP Selection, SAM Selection, FEM Selection, and UQ Engine Selection. Each contains a number of options. The components and their options are all subclasses of the SimCenterAppWidget class. The SimCenterAppWidget has methods to output and input from a JSON object. SimCenter Common also contains the RandomVariablesContainer class, each object being a container for several RandomVariables. Each RandomVariable has a name and a RandomVariable Distribution associated with it. Types of RandomVariableDistributions include, for example, Normal, Lognormal, Uniform, Beta, and Gumbel.

.. _figUmlCommon:

.. figure:: figures/umlCommon.png
   :align: center
   :figclass: align-center

   UML diagram for SimCenter common.

.. _lblSimCenterBackendApplications:

SimCenter Backend Applications
------------------------------

The Backend Applications are currently all in a single package. These are the applications that perform the numerical computations when the workflow runs. Some of these applications rely on external applications, websites, and external packages. The external applications, web services, and libraries are as shown in :numref:`figAppDiagramBackend`.

.. _figAppDiagramBackend:

.. figure:: figures/appDiagramBackend.png
   :align: center
   :figclass: align-center

   Applications for backend applications.

