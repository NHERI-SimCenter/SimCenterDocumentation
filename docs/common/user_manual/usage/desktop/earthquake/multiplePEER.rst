Multiple PEER
-------------


This panel as shown in :numref:`fig-peer-event` is provided for the user to utilize multiple existing 
`PEER <http://peer.berkeley.edu>`_ ground motion acceleration files, *.AT2* files, to create a set of PEER earthquake event. A number of buttons at the top **Add**, **Remove**, and **Load Directory** allow the user to add and remove these PEER events.


.. _fig-peer-event:

.. figure:: figures/multiplePEER.png
	:align: center
	:figclass: align-center

	Multiple PEER events.

The **Add** button is used to add an empty PEER event. For each PEER event the user must input a name for the EVENT, a path to the AT2 file, a direction that the motion acts, and a scale factor. The **+** and **-** buttons within each PEER event allow the user to add or remove AT2 files so that motions can be provided in different directions. Each AT2 file should be specified to operate in a different direction.


The **Remove** button is used to remove events. To remove an event, the user must first select events they wish to remove, which is done by clicking in the small circle at the left side of the event frame. All of the selected events are removed when the **Remove** button is pressed.

The **Load Directory** button provides a convenient method to load multiple events. All event files shall 
first be placed into the same folder. We recommend to put the files in a folder of their own, with no other files besides the earthquake events in it. After pressing the **Load Directory** button, the user will be able to choose the directory that contains the files, and the application will load all event files (i.e., every file with a ``.json`` extension) into the widget automatically. 

Initially, every event will be given a load factor of 1.0. Load factors can be assigned automatically by preparing a *Records.txt* file in the directory with the events. Each line in the *Records.txt* shall represent one event file, and contain two comma separated values: the event file name and the desired scale factor. The application will open that file automatically and assign the prescribed load factors to the events. Using a *Records.txt* file also allows users to load only a subset of the events from a folder by listing only those in the file. An example *Records.txt* is shown below:

.. code-block:: none

   elCentro.AT2,1.5
   Rinaldi228.AT2,2.0
   Rinaldi318.AT2,2.0


.. note::
   **Random Variables**: Scale factors can be defined as being random variables by entering a string in the factor field. The variable name entered will appear as a Random Variable in the **UQ** tab and the user must specify its distribution there. If multiple events are specified, the event itself will be also be treated as a random variable, with each event being part of the discrete set of possible events. For this discrete set the user does not define a distribution as this is done automatically.


