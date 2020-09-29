File format for user-provided input of building vibration modes
-----------------------

The entries “freq_nub”, “node_nub” and “elem_nub” denote the number of frequencies, nodes and elements. They take an integer input. Their format is
keyword + spacing + $input value;

The entry “geometry” is a list of vectors storing the coordinates of nodes. Its format is

.. code::

    keyword + spacing + “List<vector>”

    $number of nodes

    (

    (0 0 0)

    (0 0 3)

    …

    (0 0 60)

    );


The entry “frequency” is a list of scalars storing values of frequencies. Its format is

.. code::

    keyword + spacing + “List<scalar>”

    $number of frequencies

    (

    1

    2

    …

    3

    );


The entry “mass” is a list of six-dimensional vectors storing the mass and rotational inertial at all nodes. Its format is

.. code::

    keyword + spacing + “List<vector>”

    $number of nodes

    (

    (1500 1500 1500 0 0 0)

    (3000 3000 3000 0 0 0)

    ...

    (3000 3000 3000 0 0 0)

    );



The entry “mode1” is a list of six-dimensional vectors storing modal shapes of the first mode. Its format is

.. code::

    keyword + spacing + “List<vector>”

    $number of nodes

    (

    (0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00)

    (3.2530E-05 -1.2910E-05 1.2870E-17 8.5080E-06 2.1430E-05 0.0000E+00)

    (1.2710E-04 -5.0440E-05 5.9790E-19 1.6410E-05 4.1340E-05 0.0000E+00)

    ...

    (4.8390E-04 -1.9210E-04 -5.8930E-17 3.0400E-05 7.6600E-05 0.0000E+00)

    );


The entry “mode2” is similar to “mode1” but stores the information of the second mode.

