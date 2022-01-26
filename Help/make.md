# `Makefile`


When `make <app-name> html` is invoked, the following steps
are carried out from make::

1. The `SIMDOC_APP` environment variable is exported with the
   name of the application.

2. The `html` target is invoked, executing the following steps:
   1. Build requirement CSV files from JSON (read more [here](requirements.md).
   2. Invoke Sphinx. At this point, control is passed from the Makefile to `conf.py`.

