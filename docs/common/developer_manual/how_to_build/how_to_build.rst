
************
How to Build
************

To build the tool, follow the below instructions:

#. Download this repository from `Github <https://github.com/NHERI-SimCenter/PBE>`_.

#. Download the `SimCenterCommon repository <https://github.com/NHERI-SimCenter/SimCenterCommon>`_. Place the SimCenterCommon Repo in the same directory that you placed the PBE repo (note: not inside the PBE directory itself, but directory above it, i.e. SimCenterCommon and PBE directories both exist in same folder).

#. Download the `EE-UQ repo <https://github.com/NHERI-SimCenter/EE-UQ>`_. Place the EE-UQ Repo in the same directory that you placed the PBE repo.

#. Download the `s3hark repo <https://github.com/NHERI-SimCenter/s3hark>`_. Also place this repo in the same directory that you placed the PBE repo.

#. Download the `GroundMotionUtilities repo <https://github.com/NHERI-SimCenter/GroundMotionUtilities>`_. Again placing this repo in the same directory that you placed the PBE repo.

#. Install `Qt <https://www.qt.io/>`_. Qt is free for open source developers. Download it and start the Qt Creator application. From Qt Creator open the quoFEM.pro file located in the directory the quoFEM repo was downloaded into and select build to build it. For detailed instructions on using Qt, browse their website.

#. To run locally you will need to install and build the `SimCenterBackendApplications repo <https://github.com/NHERI-SimCenter/SimCenterBackendApplications>`_. SimCenterBackendApplications contains a number of applications written in C++, C and Python. Follow the build instructions on the SimCenterBackendApplications githib page to build them. Once built inside the PBE applicationss preferences set the applications directory entry to point to the applications folder that the build process creates for BackendAPpplications.