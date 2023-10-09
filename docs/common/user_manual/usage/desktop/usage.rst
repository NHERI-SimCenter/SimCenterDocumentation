.. _lbl-usage:

**************
User Interface
**************


The |app| is a scientific workflow application that creates workflows and runs them in the background. These workflows can involve multiple different workflow applications (see more information the backend and workflows under :ref:`lblArchitecture`). Once the |app| is started, the user is presented with the user interface (UI) shown in |figGenericUI|. This interface allows the user to select the applications to run in a workflow, input the controlling parameters for each of these applications, start the workflow either locally or remotely, and finally view the results of the simulation.

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

The main window of the UI is made up from the following areas:

#. **Login Button**

   | This button is at the top right of the user interface. You can only launch jobs on DesignSafe after logging in using your DesignSafe login and password. Pressing this button will open up the login window to enter this information. You can register for an account on the `DesignSafe-CI <https://www.designsafe-ci.org/account/register>`_ website [#]_.

   .. note::

      For more help on external services provided by DesignSafe-CI, such as creating an account, we encourage users to explore their `documentation <https://www.designsafe-ci.org/rw/user-guides/>`_ or consider `submitting a ticket <https://www.designsafe-ci.org/help/new-ticket/>`_.

#. **Message Area**

   | The message area displays the status and error messages for a running background application. The message area is a dockable window: it can be resized, moved, and closed as needed. Its visibility can be toggled by clicking on the menu item **View** -> **Program Output**.

#. **Input Panel Selection Ribbon**

   | The ribbon on the left side provides buttons that represent each step of the simulation workflow (e.g., **EVT: Event Description**, **SIM: Structural Model**, **RES: Results**). Clicking on one of these buttons shows the Input Panel for the workflow applications that correspond to the selected step.

   This user guide describes each of the steps presented in this ribbon and the corresponding workflow applications as follows:

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
      :PBE:GI
      :Hydro:GI

      :EEUQ:SIM
      :WEUQ:SIM
      :Hydro:SIM
      :PBE:SIM
      
      :wind:Assets
      
      :EEUQ:earthquake/earthquakeEvents.rst
      :PBE:earthquake/earthquakeEvents.rst
      :wind:wind/WindEvents
      :Hydro:hydro/EVT.rst
      
      :wind:FEM
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

#. **Input Panel**

   | The input panel is the large central area of the user-interface where the user configures the workflow applications. You can select a workflow application using the drop-down menu at the top of each input panel. Each panel collects input parameters and paths to files with input data for the selected workflow application. The RES (results) panel is different; it shows the results after a simulation is completed.
   
#. **Push Buttons**

   | This is the area near the bottom of the UI with the following four buttons:

   * **RUN**: Run the simulation locally on your computer.
   * **RUN at DesignSafe**: Process the input information and send the data to DesignSafe. The simulation will be run there on a supercomputer and the results will be stored in your DesignSafe jobs folder.
   * **GET from DesignSafe**: Obtain the list of jobs you ran on DesignSafe. You can select a job to download its results to your computer.
   * **Exit**: Close the application.


**Running Jobs Remotely**

.. only:: notR2D

   Clicking on the **RUN at DesignSafe** button will show the remote job submission dialog shown below (:numref:`figRemJobPanel-notR2D`)

   .. _figRemJobPanel-notR2D:

   .. figure:: figures/RemoteJobPanel_sWHALE.png
      :align: center
      :scale: 25%
      :figclass: align-center

      Remote job submission dialog.


.. only:: R2D_app

   Clicking on the **RUN at DesignSafe** button will show the remote job submission dialog shown below (:numref:`figRemJobPanel-R2D`)

   .. _figRemJobPanel-R2D:

   .. figure:: figures/RemoteJobPanel_rWHALE.png
      :align: center
      :figclass: align-center

      Remote job submission dialog.


Descriptions and guidelines for each input are given below:

* **Job Name** 
   
   | An easy to remember and meaningful name to differentiate this job from others.

* **Number of Nodes**

   | Number of compute nodes requested. Each node includes several cores and each core can run one thread of a parallel calculation.

   .. note:: 

      The number of nodes requested affects the time it takes for the job to start. Jobs are queued by a so-called scheduler on the supercomputer that optimizes its performance. Jobs that use 1-2 nodes typically start almost immediately, while a larger number of nodes (e.g., more than 10) may stay in the queue for several hours.

* **Number of processes per Node**

   | Number of processors that will be utilized on each node. It is advantageous to use all available processors of a node when the memory demand of a job is small. When a job is memory intensive, e.g., large finite element models, utilizing all available processors may overwhelm the memory cache of a core and the computation will slow down. Currently, we use the CLX compute nodes on the Frontera computer at TACC. Each of these nodes have 56 cores, that is, the maximum number of processors is 56 and the minimum is 1.

.. only:: R2D_app

   * **Number of Buildings per Task**

      | Number of buildings per task.

      .. note:: 

         Tasks will run in parallel on their own processors. The number of tasks is equal to the number of nodes multiplied by the number of processes per node. Since it takes time to assign buildings to a task and spool up the computation, it may be advantageous to assign a batch of buildings to a task when the individual building analyses are expected to have a short runtime. A good approach is to estimate the total number of buildings to be analyzed and then select the **Number of Nodes**, **Number of processors per Node**, and **Number of Buildings per Task** so that the buildings can be strategically distributed across all processors. This is so that all processors are effectively utilized and do not sit idle.


* **Save Intermediate Results**

   | Save intermediate results to a compressed folder. This is only recommended for debugging purposes because intermediate results will use a substantial amount of disk space.

* **Max Run Time**

   | The maximum time a job will run on the DesignSafe computer, in the format of Hours:Min:Sec. The job will be terminated and the intermediate results will be lost if the run time exceeds this threshold. The maximum runtime allowed for a job on DesignSafe is 48 hours.

   .. note:: 

      You can check the status of a remote run by clicking on the **GET from DesignSafe** button. If the analysis status shows FAILED, log into your DesignSafe account to view the detailed output of the run. First, log in with your credentials on the `DesignSafe <https://www.designsafe-ci.org/help/new-ticket/>`_ webpage. Next, use the menu to navigate to **Workspace** -> **Tools & Applications** -> **Job Status** and then select a job and click on **More info** to view the status of that job.

     
.. only:: R2D_app

   #. **Main Menu**

      | The main menu, which contains the typical pull down options found in almost all desktop applications, contains three additional options **Examples**, **Tools** and **GIS Map**. The **Examples** pull down provides a way to download and then load the examples described in this manual. The **Tools** pull down provide a number of options for generating inputs and additional attributed for the various input widgets of the tool, e.g. a user can use the Ground motion selection tool to create a set of ground motions using OpenSHA, PEER, etc., which can be subsequently used in the **HAZ** part of the workflow. The **GIS Map** pulldown provides access to the standard **QGIS** options, e.g. adding layers, maps, plugins.

      .. include:: R2DTool/tools.rst
