.. _lbl-usage:

Usage
================
Once the application is started the user is presented with the user interface (UI) shown in :numref:`fig-generic-ui`. It is in this UI that the user selects the applications to run, inputs the necessary
parameters for each application, starts the workflow either locally or
remotely, and finally views the simulation results. The UI contains several separate areas:

.. _fig-generic-ui:

.. only:: PBE_app

   .. figure:: figures/pbePanel.png
	:align: center
	:figclass: align-center

	The User Interface

.. only:: EEUQ_app

   .. figure:: figures/eePanel.png
	       :align: center
	       :figclass: align-center

	       The User Interface

.. only:: WEUQ_app

   .. figure:: figures/wePanel.png
	:align: center
	:figclass: align-center

	The User Interface


1. Login Button: 

The ``Login`` Button is at the top right of the UI. Before the user can launch any jobs on DesignSafe, they must first login to DesignSafe using their DesignSafe login and password. Pressing the login button will open up the login window for users to enter this information. Users can register for an account on the `DesignSafe <https://www.designsafe-ci.org/account/register>`_.

2. Message Area: 

In the top center of the UI there is an area in which, while the application is running, error and status messages will be displayed. 


3. Push Buttons:

This is the area near the bottom of the UI in which 4 buttons are contained:

     * ``RUN`` – Run the simulation locally on the user’s desktop machine.
     * ``RUN at DesignSafe`` – Process the information, and send to DesignSafe. The simulation will be run there on a supercomputer, and results will be stored in the user's DesignSafe jobs folder.
     * ``GET from DesignSafe`` – Obtain the list of jobs for the user from DesignSafe and select a job to download from that list.
     * ``Exit``: Exit the application.


3. Input Panel Selection: 

This area on the left side provides the user with a selection of buttons to choose from, e.g. ``UQ``, ``GI``, ``SI``, ``EVT``, ``RV``, ``FEM``, ``RES``. Selecting any of these buttons will change what is displayed in the central input panel.

4. Input Panel: 

This is the large central area of the UI where the  user provides input for the application chosen and where thay can view the results. For example, if the user had selected RV in the input panel  selection, it is in this panel that the user would provide details on the distributions associated with each random variable. In the following sections each of the panels that is presented to the user when the buttons in the input panel selection are reviewed:

.. toctree-filt::
	:maxdepth: 2

	UQ
	GI
	SIM
	EVT
	FEM
	:PBE:DL
	:EEUQ:EDP
	:WEUQ:EDP
	RES
