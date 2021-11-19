.. _lbl-usage:

**********
User Guide
**********


The |app|, as will be discussed in :ref:`lblArchitecture`, is a scientific workflow application that creates workflows and runs them in the background. These workflows can involve multiple different backend applications. Once the |app| is started, the user is presented with the user interface shown in |figGenericUI|. It is in this UI where the user selects the applications to run in a workflow, inputs the necessary parameters for each of these applications, starts the workflow either locally or
remotely, and finally views the simulation results. The main window of the UI is divided into several separate areas:

.. only:: quoFEM_app

   .. _figGenericUI-quoFEM:

   .. figure:: figures/quoFEMPanel.png
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


.. only:: Hydro

	  
   .. _figGenericUI-Hydro:

   .. figure:: figures/HydroPanel.png
	   :align: center
	   :figclass: align-center

	   The |app| user interface.
   

.. only:: R2D_app

	  
   .. _figGenericUI-R2D:

   .. figure:: figures/R2DPanel.png
	   :align: center
	   :figclass: align-center

	   The |app| user interface.


1. Login Button:

   The **Login** button is at the top right of the user interface. Before the user can launch any jobs on DesignSafe, they must first login to DesignSafe using their DesignSafe login and password. Pressing the login button will open up the login window for users to enter this information. Users can register for an account on the `DesignSafe-CI <https://www.designsafe-ci.org/account/register>`_ website [#]_. 

2. Input Panel: 

   The input panel is the large central area of the user-interface where the user provides input for the various applications, and also where they can view the results. 

3. Input Panel Selection Ribbon: 

   The ribbon on the left side provides the user with a selection of buttons to choose from (e.g. **RV: Random Variables**, **RES: Results**). Selecting any of these buttons will change what is displayed in the central input panel. Each panel will present the user with an option for which application to choose for that part of the workflow, and will then allow a user to provide inputs for that application. In the following sections, each of the panels in the input panel selection ribbon are reviewed:

   .. toctree-filt::
      :maxdepth: 1

      :R2D:R2DTool/VIZ
      :R2D:R2DTool/GI
      :R2D:R2DTool/HAZ
      :R2D:R2DTool/ASD
      :R2D:R2DTool/HTA
      :R2D:R2DTool/MOD
      :R2D:R2DTool/ANA
      :R2D:R2DTool/DL
      UQ
      :EEUQ:GI
      :WEUQ:GI
      :Hydro:GI 
      :EEUQ:SIM
      :WEUQ:SIM
      :Hydro:SIM
      :PBE:SIM
      :wind:Assets
      :EEUQ:earthquake/earthquakeEvents.rst
      :PBE:earthquake/earthquakeEvents.rst	 	 
      :wind:wind/WindEvents
      :wind:FEM
      :Hydro:hydro/EVT.rst
      :EEUQ:FEM
      :Hydro:FEM
      :PBE:FEM	 
      :quoFEM:quoFEM/FEM
      RV
      :EEUQ:response/EDP
      :WEUQ:response/EDP
      :Hydro:response/EDP
      :quoFEM:quoFEM/QuantitiesOfInterest
      :PBE:PBE/DL
      :EEUQ:response/resEE
      :WEUQ:response/resEE
      :quoFEM:quoFEM/resQUO
      :PBE:PBE/resPBE
      :R2D:R2DTool/RES
      :Hydro:hydro/resHydro

4. Push Buttons:

   
   This is the area near the bottom of the UI in which 4 buttons are contained:

     * **RUN**: Run the simulation locally on the user’s desktop machine.
     * **RUN at DesignSafe**: Process the information, and send to DesignSafe. The simulation will be run there on a supercomputer, and results will be stored in the user's DesignSafe jobs folder.
     * **GET from DesignSafe**: Obtain the list of jobs for the user from DesignSafe and select a job to download from that list.
     * **Exit**: Exit the application.
   
   Clicking on the **RUN at DesignSafe** button will show the remote job submission dialog, given in :numref:`figRemJobPanel`.
   
   .. _figRemJobPanel:

   .. figure:: figures/RemoteJobPanel.png
	   :align: center
	   :figclass: align-center

	   Remote job submission dialog.

   Descriptions and guidelines for each input are given below: 
   
   	* **Job Name**: An easy to remember and meaningful name to differentiate this job from others.
   	* **Number of Nodes**: Number of compute nodes requested. Each node has many cores, and each core typically contains several processors/threads.
	
	.. note:: If a large number of nodes are requested (e.g., more than 10), the job may stay longer in the queue before it starts.
	
   	* **Number of processors per Node**: Number of processors that will be utilized on each node. Typically, it is advantageous to use all available processors of a node when the memory demand of a job is small. When a job is memory intensive, e.g., large finite element models, utilizing all available processors may overwhelm the memory cache of a core and the computation will slow down. Currently, the maximum number of processors is 48 and the minimum is 1.
   	* **Number of Buildings per Task**: Number of buildings per task.
	
	.. note:: Each task will run in parallel on its own processor. The number of tasks is equal to the number of nodes multiplied by the number of processors per node. Since it takes time to assign buildings to a task and spool up the computation, it may be advantageous to assign a batch of buildings to a task when the individual building analyses are expected to have a short runtime. A good approach is to estimate the total number of buildings to be analyzed and then select the **Number of Nodes**, **Number of processors per Node**, and **Number of Buildings per Task** so that the buildings can be strategically distributed across all processors. This is so that all processors are effectively utilized and do not sit idle. 
	
   	* **Save Intermediate Results**: Save intermediate results to a compressed folder. This is typically not recommended as this as this will use up disk space.
   	* **Max Run Time**: The maximum time a job will run on the DesignSafe computer, in the format of Hours:Min:Sec. Job will stop if the run time exceeds this threshold. 

   .. note:: A user can check the status of a remote run by clicking on the **GET from DesignSafe** button. If the analysis status shows FAILED, users are encouraged to log into their DesignSafe account to view the detailed output of the run. To view the detailed output of a run go to the `DesignSafe <https://www.designsafe-ci.org/help/new-ticket/>`_ webpage and log in with your credentials. Next, click on the menus **Workspace** -> **Tools & Applications** -> **Job Status** and then select **More info** to view the status of a job.
	
5. Message Area: 


   The message area is located in the bottom of the UI and displays the status and error messages for a running background application. The message area is a dockable dialog which can be resized, moved, and closed as needed. The dialog visibility can be toggled by clicking on the menu item **View** -> **Program Output**. If moved from its default location, the status dialog can be restored to the bottom of the UI by dragging the dialog back to the bottom of the UI and hovering over the area. 


   .. [#] For more help on external services provided by DesignSafe-CI, such as creating an account, we encourage users to explore their `documentation <https://www.designsafe-ci.org/rw/user-guides/>`_ or consider `submitting a ticket <https://www.designsafe-ci.org/help/new-ticket/>`_.
