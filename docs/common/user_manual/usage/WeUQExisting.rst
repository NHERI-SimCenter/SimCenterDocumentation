
Multiple Existing 
-----------------

This panel is provided for the user to specify multiple existing SimCenter event files.  If more than one event is specified it is done to provide the UQ engine with a discrete set of events to choose from - it is not done with the intention of specifying that one event follows another.  The panel presented to the user is shown in :numref:`fig-SCEventPanel`.

.. _fig-SCEventPanel:
.. figure:: figures/weuqExisting.png
	:align: center
	:figclass: align-center

	Existing (SimCenter) Events

Use the ``Add`` button to add a new event. This adds an empty event to the panel. Pressing the button multiple times will keep adding events to the panel. :numref:`fig-SCEventPanel` shows the state after the button has been pressed twice, and data entered to load the ``Scenario1`` and ``Scenario2`` Events.

The path to the event file can be entered manually, or using the ``Choose`` button for convenience. Pushing the button brings up a typical file search screen. By default, a scale factor of 1.0 is assigned to the event.  The user can change this to another floating point value (DO NOT USE INTEGER), and they can define the scale factor as a random variable by entering a variable name, such as ``factorScenario1`` for the second event
in :numref:`fig-SCEventPanel`. 

Note: the name of the random variable must not start with a number, or contain any spaces or special characters, such as -, +, \%, etc.

The  ``Remove`` button is used to remove events. To remove an event, the user must first select events they wish to remove, which is done by clicking in the small circle at the left side of the event frame. All of the selected events are removed when the ``Remove`` button is pressed.

The ``Load Directory`` button provides a convenient method to load multiple events. All event files shall first be placed into the same folder. We recommend to put the files in a folder of their own, with no other files besides the wind loading events in it. After pressing the ``Load Directory`` button, the user will be able to choose the directory that contains the files, and the application will load all event files (i.e., every file with a ``.json`` extension) into the widget automatically.

Initially, every event will be given a load factor of 1.0. Load factors can be assigned automatically by preparing
a ``Records.txt`` file in the directory with the events. Each line in the ``Records.txt`` shall represent one event file, and contain two comma separated values: the event file name and the desired scale factor. The application will open that file automatically and assign the prescribed load factors to the events. Using a ``Records.txt`` file also allows users to load only a subset of the events from a folder by listing only those in the file. An example ``Records.txt`` is shown below:
::

	Scenario1.json,1.5
	Scenario2.json,2.0

Random Variables: Scale factors can be defined as being random variables by entering a string in the factor field. The variable name entered will appear as a Random Variable in the UQ panel and the user must specify its distribution there. If multiple events are specified,the event itself will be also be treated as a random variable, with each event being part of the discrete set of possible events. For this discrete set the user does not define a distribution as this is done automatically.