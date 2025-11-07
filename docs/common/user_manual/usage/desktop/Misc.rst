.. _misc:

====
Misc
====


Analytics
---------

The |app| uses Google Analytics to collect anonymous information about how the application is used.  
This data helps improve both the software and its documentation, and it also supports required usage reporting to the U.S. National Science Foundation.

The information gathered includes: the city and duration of usage, the number of local and remote workflow runs, which example problems are loaded, and errors.

.. note::
   
   No personal or identifying information is collected.

Disabling Analytics
~~~~~~~~~~~~~~~~~~~

You can disable analytics data collection by editing the configuration file, ``config.json``, located in the application's installation directory. If you are on a Mac, this is the |app|/Contents/MacOS directory.

Locate the line:

.. code::

   "GoogleAnalytics": "Yes"

Change the value from ``"Yes"`` to ``"No"`` and save the file.  
After doing so, |app| will no longer share analytics information.


Application Configuration
-------------------------

The ``config.json`` file mentioned above also contains additional settings that allow users to customize the appearance and behavior of the |app| at startup.

1. **Changing the Default Screen Size**

   By default, the application opens in a normal-sized window.  
   To make |app| launch in full-screen mode, edit the line below in ``config.json``:

   .. code::

      "ScreenSize": "Normal"

   Change the value to:

   .. code::

      "ScreenSize": "Full"

2. **Adjusting the Message Area Widget's Location and Size**

   The ``config.json`` file also includes a blank JSON object named ``outputLocation`` that can be customized to control where the output text widget appears and its dimensions.

   You can specify the following keys:

   - ``position`` — where the output widget should appear.  
     Valid options are ``"right"``, ``"left"``, ``"bottom"``, and ``"top"``.
   - ``numPixels`` *(optional)* — the number of pixels to allocate to the widget in the chosen direction.  
     If omitted, Qt assigns a default value.

   **Example:**  
   To place the output widget on the left-hand side of the application with a width of 500 pixels:

   .. code::

      "outputLocation": {
         "position": "left",
         "numPixels": 500
      }
      
   
   


