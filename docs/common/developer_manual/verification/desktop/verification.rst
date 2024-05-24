.. _lblVerification:

************
Verification
************

.. only:: notR2D

   This chapter collects carefully designed verification exercises that we use to test the correctness of the implementation of the |app|.	  
	  
   .. toctree-filt::
     :maxdepth: 1
     
     :PBE:PBE/verificationPBE
     :EEUQ:EEUQ/PortalFrameEarthquake
     :EEUQ:EEUQ/ResponseSpectrum
     :EEUQ:EEUQ/SiteResponse
     :EEUQ:quoFEM/DakotaSensitivity
     :WEUQ:WEUQ/PowerSpectralDensity
     :WEUQ:WEUQ/TinFverification
     :quoFEM:quoFEM/InterpointDistances
     :quoFEM:quoFEM/DakotaSensitivity
     :Hydro:HydroUQ/DakotaSensitivity


.. only:: R2D_app
   
   Verification for |app| is performed as part of the `testbed work <file:///Users/fmckenna/release/SimCenterDocumentation/build/R2DTool/html/common/testbeds/atlantic_city/sample_results.html>`_. For each tesbed manual evaluation of randomly selected buildings from th testbed is performed by hand calculation to ensure the results for that building match the output results from the software.
