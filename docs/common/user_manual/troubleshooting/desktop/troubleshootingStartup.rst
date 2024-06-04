.. _lblTroubleshootingStartup:

Startup Issues
--------------

When initiating any SimCenter desktop application on Windows, you may encounter an error indicating a missing Visual C/C++ runtime library, as depicted in |figMissingCRT|. This issue arises due to the absence of necessary runtime components that the application depends on for execution.

To resolve this, install the Visual C/C++ redistributable package by executing **vc_redist.x64.exe**, which is provided within the application's installation directory. This step ensures that all required runtime libraries are available, allowing the application to start without errors.

.. only:: PBE_app

   .. _figMissingCRT-PBE:

   .. figure:: figures/PBE-MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.

.. only:: EEUQ_app

   .. _figMissingCRT-EE:

   .. figure:: figures/EE-UQ-MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.

.. only:: WEUQ_app

   .. _figMissingCRT-WE:

   .. figure:: figures/WE-UQ-MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.

.. only:: HydroUQ_app

   .. _figMissingCRT-HydroUQ:

   .. figure:: figures/MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.

.. only:: R2D_app

   .. _figMissingCRT:

   .. figure:: figures/MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.

.. only:: quoFEM_app

   .. _figMissingCRT:

   .. figure:: figures/MissingCRT.png
      :align: center
      :figclass: align-center

      Error message indicating a missing Visual C/C++ runtime library.
