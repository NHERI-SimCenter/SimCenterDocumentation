####################################################################
# Import necessary packages for user-solver class
# We are creating a child class (i.e. usersolver) 
# of the parent class (i.e. solver) that is used by default
####################################################################
import numpy as np
import pandas as pd
import os
import shutil
from OpenFOAM import solver # Import the parent class
from GenUtilities import genUtilities # General utilities

class usersolver(solver):

    ####################################################################
    # Create the solver directories
    ####################################################################
    def dircreate(self):

        print("This function is used to create any solver directories")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.dircreate() or super().dircreate() 

    ####################################################################
    # Geometry related files 
    ####################################################################
    def geometry(self,data):

        print("This function is used to create any geometry files")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.geometry(data) or super().geometry(data)

    ####################################################################
    # Meshing related files 
    ####################################################################
    def meshing(self,data):

        print("This function is used to create mesh, if required")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.meshing(data) or super().meshing(data)

    ####################################################################
    # Material model related files
    ####################################################################
    def matmodel(self,data):

        print("This function is used to create files for material model")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.matmodel(data) or super().matmodel(data)

    ####################################################################
    # Create boundary condition files 
    ####################################################################
    def bccondition(self,data):

        print("This function is used to create files required for boundary condition")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.bccondition(data) or super().bccondition(data)

    ####################################################################
    # Parallelization related files 
    ####################################################################
    def parallel(self,data):

        print("This function is used to create files required for parallelization")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.parallel(data) or super().parallel(data)

    ####################################################################
    # Solver control related files 
    ####################################################################
    def solvecontrol(self,data):

        print("This function is used to create files required to control the solver")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.solvecontrol(data) or super().solvecontrol(data)

    ####################################################################
    # Create any other supplementary files required for the solver
    ####################################################################
    def filecreate(self,data):

        print("This function is used to create any other supplementary files required")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.filecreate(data) or super().filecreate(data)