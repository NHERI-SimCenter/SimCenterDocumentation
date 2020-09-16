.. _lbl-usage:

**********
User Guide
**********

The |app|, as will be discussed in :ref:`lblArchitecture`, is a scientific workflow application that creates workflows and runs them in the background. These workflows can involve multiple different backend applications. Once the |app| is started, the user is presented with the user interface (UI) shown in |figGenericUI|. It is in this UI where the user selects the applications to run in a workflow, inputs the necessary parameters for each of these applications, starts the workflow either locally or
remotely, and finally views the simulation results. The main window of the UI is divided into several separate areas:

.. only:: quoFEM_app

   .. _figGenericUI-QUOFEM:

   .. figure:: figures/quoFEM.png
	    :align: center
	    :figclass: align-center

	    The |app| user interface.

.. only:: PBE_app

   .. _figGenericUI-PBE:
    
   .. figure:: figures/pbePanel.png
      :align: center
      :figclass: align-center
 
      The |app| user interface.

.. only:: EEUQ_app

   .. _figGenericUI-EE:

   .. figure:: figures/eePanel.png
      :align: center
      :figclass: align-center

      The |app| user interface.

.. only:: WEUQ_app

   .. _figGenericUI-WE:

   .. figure:: figures/wePanel.png
	    :align: center
	    :figclass: align-center

	    The |app| user interface.


1. Login Button: 

The **Login** button is at the top right of the user interface. Before the user can launch any jobs on DesignSafe, they must first login to DesignSafe using their DesignSafe login and password. Pressing the login button will open up the login window for users to enter this information. Users can register for an account on the `DesignSafe-CI <https://www.designsafe-ci.org/account/register>`_ website.

2. Message Area: 

The message area is located in the top center of the UI and displays status and error messages for a running background application. 


3. Input Panel Selection: 

The ribbon on the left side provides the user with a selection of buttons to choose from (e.g. **UQ**, **RV**, **FEM**, **RES**). Selecting any of these buttons will change what is displayed in the central input panel. Each panel, with exception of **RV** and **QoI** panels,  will present the user with an option for which application to choose for that part of the workflow, and will then present the users for inputs for that application.

4. Input Panel: 

The input panel is the large central area of the UI where the user provides input for the application chosen and where they can view the results. For example, if the user had selected **RV** in the input panel selection, it is in this panel that the user would provide details on the distributions associated with each random variable. In the following sections each of the panels that is presented to the user when the buttons in the input panel selection are reviewed:

.. toctree-filt::
   :maxdepth: 1

   UQ
   :earthquake:GI
   :wind:GI
   :earthquake:SIM
   :wind:SIM
   :earthquake:earthquake/earthquakeEvents
   :wind:wind/WindEvents
   :earthquake:FEM
   :wind:FEM
   :quoFEM:quoFEM/FEM
   :EEUQ:response/EDP
   :WEUQ:response/EDP
   RV
   :quoFEM:quoFEM/QuantitiesOfInterest
   :PBE:PBE/DL
   :EEUQ:response/resEE
   :WEUQ:response/resEE
   :quoFEM:quoFEM/resQUO
   :PBE:PBE/resPBE


5. Push Buttons:

This is the area near the bottom of the UI in which 4 buttons are contained:

     * **RUN**: Run the simulation locally on the user’s desktop machine.
     * **RUN at DesignSafe**: Process the information, and send to DesignSafe. The simulation will be run there on a supercomputer, and results will be stored in the user's DesignSafe jobs folder.
     * **GET from DesignSafe**: Obtain the list of jobs for the user from DesignSafe and select a job to download from that list.
     * **Exit**: Exit the application.

