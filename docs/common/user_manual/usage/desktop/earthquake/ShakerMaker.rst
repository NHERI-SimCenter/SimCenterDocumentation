.. _ShakerMakertools:

ShakerMaker
===========
ShakerMaker is designed to assist both earthquake engineers and seismologists by providing an easy-to-use tool for generating and exploring ground motions using the frequency-wavenumber (FK) method on 1-D crustal models. This innovative tool allows users to create realistic, physics-based waveforms for various earthquake scenarios, which can then be analyzed using the Domain Reduction Method (DRM).

The DRM facilitates the simulation of how soil and structures respond to ground motions during earthquakes by connecting large regional earthquake simulations with smaller local soil-structure models without losing critical details. This method significantly improves the accuracy of ground-motion simulations.

Despite its advantages, the DRM has seen limited use due to challenges in handling large, complex datasets, which require specialized tools for creation. ShakerMaker addresses these issues by offering a straightforward solution for generating DRM-compatible motions and an accessible format for working with extensive datasets, making it easier for researchers and practitioners to leverage this powerful method in their analyses.

ShakerMaker is a Python library designed for generating and analyzing seismic wave motions. Its core functionality is built upon the FK method, which is implemented in Fortran. This allows ShakerMaker to leverage the high-performance capabilities of Fortran while providing a user-friendly interface through Python.

**ShakerMaker tool** is a graphical user interface within the EEUQ framework that allows users to create ShakerMaker models easily. This tool simplifies the process of modeling seismic events by providing a visual platform for users to define and manipulate various parameters related to faults, crustal layers and stations. Users can load available fault models and select the type of station they wish to use based on the crustal model. The ShakerMaker tool then generates the necessary input files for the ShakerMaker engine and runs the simulation, providing users with the resulting ground motions for further analysis.

.. The ShakerMaker tool is designed to create a simple and user-friendly interface to load available fault models and based on the crustal models type of station they choose, and then
