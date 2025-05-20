Usage
=====

.. _installation:

Installation
------------

The prerequisites for CelerisAi are standard Python libraries, with Taichi being the most important. You can install these libraries manually:

.. code-block:: console

   $ pip install imageio>=2.36.0 matplotlib>=3.7.2 numpy>=1.24.3 scipy>=1.9.0 taichi>=1.7.0

Alternatively, you can install all required dependencies automatically using the provided requirements file:

.. code-block:: console

   $ pip install -r requirements.txt

Downloading the Source Code
-----------------------------

Clone the repository from GitHub to download the source code:

.. code-block:: console

   $ git clone https://github.com/wrenteria/CelerisAi.git

Running the Examples
--------------------

.. note::
   Make sure to execute these examples from within the CelerisAi directory.


After installing the dependencies and downloading the source, you can verify the installation by running the provided examples.

For a 1D example, execute:

.. code-block:: console

   $ python setrun_1D.py

For a 2D example based on the configuration files created by CelerisWebGPU, execute:

.. code-block:: console

   $ python setrun_web.py

For more details on configuring CelerisWebGPU, please refer to its application at
`CelerisWebGPU <https://plynett.github.io/>`_.

