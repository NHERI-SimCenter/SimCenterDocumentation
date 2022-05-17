# SimCenter Example Index

This page summarizes the examples provided for all of the tools.

Adding a new example to the documentation consists of two steps:

1. add the directory name for the example to `examples.yaml`. An
   example should contain the following files at the root of its
   directory:
   - `input.json` - This is an input file that defines the app's
     configuration when running the example.
   - `README.rst` - This file is what will be rendered in the
     documentation.
   - `meta.yaml` - This file provides extra metadata about the
     example. This should at least have a `summary` field, which
     will be displayed on the example gallery page.

2. rebuild the example index by running `make <app-name> examples`


<!--

## quoFEM Examples

```yaml
quoFEM:
  - id: quo-01
    title: Forward Propagation - OpenSees/Tcl
    files: ['TrussModel.tcl', 'TrussPost.tcl']
    synopsis: This example uses quoFEM to estimate the first and second central moments of a FE model's response, given the marginal distributions of various random parameters.
  - id: quo-02
    title: Forward Propagation - OpenSeesPy
    files: ['TrussModel.py', 'TrussParams.py']
    synopsis: This example illustrates how quoFEM interacts with OpenSeesPy. A simple forward propagation procedure is run to estimate the first and second central moments of a FE model's response, given the marginal distributions of various random parameters.
  - id: quo-03
    title: Reliability Analysis
    files: ['TrussModel.tcl', 'TrussPost.tcl']
    synopsis: This example uses quoFEM to perform a second-order reliability analysis (SORM) of an OpenSees FE model.
  - id: quo-04
    title: Sensitivity Analysis
    files: ['TrussModel.tcl', 'TrussPost.tcl']
    synopsis: This example uses quoFEM to perform a global sensitivity analysis of an OpenSees FE model.
  - id: quo-05
    title: Basic modeling with Python
    files: ['Rosen.py', 'RosenParams.py']
    synopsis: This example illustrates how Python scripting can be used with quoFEM to express general mathematical models without the use of a dedicated finite element analysis engine. 
  - id: quo-06
    title: Optimization
    files: ['Rosen.py', 'RosenParams.py']
    synopsis: In this example, a **parameter estimation** routine is used to solve a classical optimization problem for which an analytic solution is known.
  - id: quo-07
    title: Conventional Calibration - Steel Frame
    files: ['Frame2FEM.tcl']
    synopsis: In this example, a parameter estimation routine is used to estimate column stiffnesses of a simple steel frame, given data about it's mode shapes and mass distribution.
  - id: quo-08
    title: Bayesian Calibration - Steel Frame
    files: ['Frame2FEM.tcl']
    synopsis: In this example, Bayesian estimation is used to estimate column stiffnesses of a simple steel frame, given data about it's mode shapes and mass distribution.
  - id: quo-09
  - id: quo-10
    title: Forward Propagation - FEAP
``` 

## EE-UQ Examples

```yaml
EEUQ:
  - id: eeuq-01
    title: Basic Shear Building Procedure
    files: [*'frame_model_tcl']
    synopsis: In this example, the EE-UQ application is used to estimate means and standard deviations of a structural model's displacement response when subjected to earthquake excitations.
```

## PBE Examples

```yaml
PBE:
  - id: pbe-01
    title: pbe-01
    files: [*frame_model_tcl]
```

## WE-UQ Examples

```yaml
WEUQ:
  - id: weuq-01
    title: "9 Story Frame - Basic Sampling"
  - id: weuq-02
    title: "9 Story Frame - Sampling with Select EDPs"
  - id: weuq-03
    title: "9 Story Frame - Reliability Analysis"
  - id: weuq-04
    title: "50 Story Building - Stochastic Loading"
  - id: weuq-05
    title: "50 Story Building - Basic CFD Loading"
  - id: weuq-06
    title: "50 Story Building - Expert CFD loading"
  - id: weuq-07
    title: "3 Story Building - Sensitivity, LowRiseTPU"
  - id: weuq-08
    title: "30-Story Frame - Sensitivity"
```
-->
