
truss:
  truss_model_py: &truss_model_pym >
    This file is a Python script which takes a given realization of the problem's random variables, and runs a finite element analysis of the truss with OpenSeesPy. When this script is invoked by the workflow, it receives the list of the identifiers supplied in the **EDP** tab through the operating system's `stdout` variable, and a set of random variable realizations through the import of the **Parameters File**.

  truss_params_py: &truss_params_py >
