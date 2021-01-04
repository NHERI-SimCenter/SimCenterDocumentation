.. _lblEventApp:

Event Applications
==================

The **event application** takes the event(s) selected for a building site, associates each one with a simulation, and creates EVENT files containing the event intensity measures. It obtains the name of the event from the :ref:`BIM file <lblBuildingApp>` and the intensity measure information from the input :ref:`event files <lblUserDefInputs>`.
This input information is saved in an "EVENT.json" file, located in its corresponding **simulation working directory**.

.. _figContext:

.. figure:: _static/images/backendapps_Events.png
   :align: center
   :figclass: align-center

The following options for event applications vary in the type of event, event properties, and format of the event file which it processes.

.. only:: WEUQ_app

    .. raw:: html
       :file: _static/html/WE-UQ/createEVENT.html


.. only:: EEUQ_app

    .. raw:: html
       :file: _static/html/EE-UQ/createEVENT.html


.. only:: RDT_app

    .. raw:: html
       :file: _static/html/RDT/createEVENT.html
 

