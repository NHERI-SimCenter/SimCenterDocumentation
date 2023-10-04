Coupled Digital Twin
--------------------

This panel allows users to utilize a coupled OpenFOAM CFD simulation and OpenSeesPy finite element simulation to obtain loads and pressures on the building for subsequent UQ analysis.

.. figure:: coupled/Coupled.png
   :align: center
   :figclass: align-center
    Coupled Event Panel

 
For a coupled event the user is presented with a workflow they must progress through:

            (1) Coupled simulation settings
            (2) OpenSees Model and External Envelope File Upload
            (3) Specification of CFD domain information and initial conditions
            (4) Desired data output specification
            (5) Post processing

(1) Coupled Simulation Settings

Time Step: The coupling timestep for the solution. This value should be selected such that CFD model CFL criterion is satisfied, as well as the required minimum timestep for finite element analysis model stability.

Duration: Coupled simulation duration.

Preload Structure w/ Gravity: Utilize the nodal masses to create a gravity loading in the -Z direction of the OpenSees model. (optional, this could be handled manually within the OpenSees script itself)

Run Preliminary Structural Analysis: Utilize the end state of the OpenSees analysis (if defined in the OpenSees script) as the initial state of structure during the coupled analysis.

   (1.1) Simulation Settings


.. figure:: coupled/Settings.png
   :align: center
   :figclass: align-center
    Settings


   (1.2) OpenFOAM Settings

Adjust Timestep: [Default, No] This setting allows the OpenFOAM analysis to reduce its timestep to a value below that of the coupling timestep. NOT RECOMMENDEDFOR CASES WITH STRUCTURAL DEFORMATION. Subcycling of the CFD model between coupling iterations can result in erroneous force spikes. It is suggested that a constant timestep size is utilized for coupled analyses.

Turbulence: Allow for calculation of turbulence within the CFD model.

Number of Processors: The number of processors the OpenFOAM CFD solution will be calculated with.

Start Event Recording Time: What time the user would like the coupled model to output post-processing data.

   (1.3) OpenCOUPLING Settings

Coupling Scheme: Implicit/Explicit. Implicit is recommended.

Coupling Data Acceleration Method: IQN-ILS is recommended.

Initial Relaxation Factor: The relaxation factor for FSI coupling iterations.

Maximum Coupling Iterations: Default, 100. Keep at a large value, should converge before reaching maximum iterations.

Coupling Iteration Convergence Tolerance: This is a relative convergence measure of the coupling data passed between participants within each coupling timestep. This value should be below 5e-3, but not too small. This is a measure of how much the coupling residuals change from coupling iteration to coupling iteration. Once the values have nearly approached their desired values from the interface acceleration techniques, the coupling convergence tolerance is satisfied.

Data Mapping Scheme: Nearest Neighbor is recommended. Radial-basis-function mapping is available, but is less stable and slower than nearest neighbor.

Output Data from Coupling Iterations: Not recommended. Intended for debugging of coupling iterations for models which are not converging.

Coupling Iteration Output Data Frequency: A large value is recommended.

(2) Specification of OpenSees Model File (must be an OpenSeesPy script) and external surface file for structure (STL file, this is the boundary which will represent the structure within a three-dimensional CFD simulation, which will be coupled to the FEA model)


(2.1) OpenSees Model


.. figure:: coupled/OpenSees.png 
   :align: center
   :figclass: align-center
    OpenSees

 
(3) Specification of CFD model domain and initial conditions.

                                                                                    
(3.1) OpenFOAM Model

Select a NHERI flume facility or specify the flume geometry within the text field boxes provided.
                                                                                                                                                                           
Specify a flume cell size (this is the approximate edge length size of the volumes within the CFD domain for the largest cells). The minimum flume cell size could tentatively be 8 times smaller than this value, due to mesh castellation during automatic meshing routines. Use caution when specifying this value. CFD mesh resolution is increased in the structural near field.



.. figure:: coupled/OpenFOAM.png
   :align: center
   :figclass: align-center
    OpenFOAM

   
(3.2) Specify the flume bathymetry (STL file, or point list of x position, elevation of flume floor at x position).

If there is no bathymetry, please provide points within the point list which are outside of the boundary of the flume, or specify the bottom of the flume as a two point list with your start x location and end x location as the start and end of the flume and the flume elevation at both points as 0.


.. figure:: coupled/bathymetryOF.png
   :align: center
   :figclass: align-center
    Bathymetry

                                                                                                                              
(3.3) Specify the initial conditions of the OpenFOAM model, including the still water level, the initial fluid velocity, and the fluid reference pressure [default, 0 Pa]. If a velocity time history is desired as an inlet boundary condition, upload a CSV file containing the times and velocities desired at the inlet at those times.
                                                                                                                                                                                                                                       
.. figure:: coupled/initialOF.png
    :align: center
    :figclass: align-center
     Initial Conditions


(3.4) Specify the turbulence initial conditions. The reference length, turbulence intensity, and the reference velocity of the turbulence.

.. figure:: coupled/turbulanceOF.png
    :align: center
    :figclass: align-center
     Turbulence 

                                                                                                                            
(3.5) Specify the wave generation techniques for the CFD model, if waves are desired.                                                                                                                                                                                                                            
Paddle Generated Waves: Upload a CSV of times, displacements of the paddle at the inlet. This will create a paddle generated wave through motion of the CFD boundary at the minimum X boundary of the model.

                                                                                                                                                                                                                            
Periodic Waves: Specify the wave properties to apply a periodic wave inlet boundary condition to the CFD model.
                                                                                                                                                                                                                           
No Waves: Steady state flow or flows without waves.

.. figure:: coupled/waveOF.png
    :align: center
    :figclass: align-center
     Wave Generation 


(4) Outputs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
A variety of outputs from the coupled model can be obtained through specification of the output settings.
 
- Output VTK - Output a VTK file of the OpenSees and OpenFOAM models at the specified time interval.

- Free surface probes - function as wave gauges within the CFD model

- Field Probes - sample various fields from the CFD model for postprocessing (pressure, velocity, phase fraction)
  
- Section cuts - sample various fields as a section cut of the CFD model - specify origin point and normal of the section cut, as well as the fields of interest

.. figure:: coupled/Outputs.png
   :align: center
   :figclass: align-center
    Outputs
   

Field Probes

.. figure:: coupled/OutputFieldProbes.png
   :align: center
   :figclass: align-center
    Field Probes


Surface Probes  

.. figure:: coupled/OutputSuraceProbes.png 
   :align: center
   :figclass: align-center
    Surface Probes

Section Cuts 

.. figure:: coupled/OutputCuts.png
   :align: center
   :figclass: align-center
    Section Cuts

