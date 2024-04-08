Physics Based Ground Motions
----------------------------

This panel allows users to use the results of previously run physics based earthquake rupture simulations that generated suites of ground motions for the
areas studied. As more datasets are made available, more options will be added to the options in the pull down menu.

M9 Dataset
==========

With funding support from the National Science Foundation, a United States Geological Survey and University of Washington team studied the impacts of
large magnitude, megathrust earthquakes on the Cascadia subduction zone as part of the `M9 Project <https://sites.uw.edu/pnet/m9-simulations/about-m9-simulations/>`_ . The researchers used physics-based simulations to generate possible ground motions for the entire Pacific Northwest region during a magnitude-9 (M9) event. Broadband ground motions were developed from these M9 simulations for seven grids (A, B, C, D, E, Y and Z), each corresponding to a particular combination of region and/or `grid resolution <https://sites.uw.edu/pnet/m9-simulations/about-m9-simulations/extent-of-model/>`_

It is these motions developed as part of the `https://sites.uw.edu/pnet/m9-simulations/about-m9-simulations/>`_ that are made available through this option.

The use the dataset the user inputs a number of options, **latitude** and **longitude** being the locations for which the motions are sought, and **numMotions** for the number of motions desired, and the **grid type**.  The location in the users computer that the motions will be downloaded to is specified by the user in **tmp Directory**, by default it is in the users **Documents/EE-UQ/LocalWorkDir** directory. 

Once the user has entered the inputs they press the ``Get Motions`` button. This will start the download process in the background. This process is painfully slow, a few minutes per ground motion. While the motions are downloading the user can work on other parts of the interface. If the user attempts to run a simulation before motions are downloaded, pop ups will appear informing the user that the run should be cancelled.

.. figure:: figures/M9.png
      :align: center
      :figclass: align-center
      :width: 75%

      M9 Interface

.. .. bibliography:: ../../../../references.bib
