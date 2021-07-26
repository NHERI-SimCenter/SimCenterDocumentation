.. _lbl-simcentertopo:

Topography: SimCenter
=======================

One of the primary inputs for a shallow-water solver includes the bathymetric data. In the SimCenter format for the topography files, the surface of water is considered for references as :math:`z=0`.

The data in the SimCenter format allows for both regular and irregular grids and a typical bathymetric data is as shown below.

.. code-block:: latex

    x1 y1 z1
    x2 y2 z2
    ...
    xn yn zn

It should also be noted here that SimCenter format allows for multiple files to be input for the topography. The |app| does a triangulation of the points and stitches multiple files using areas of overlap.