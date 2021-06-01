####################################################################
# Import necessary packages for user-solver class
# We are creating a child class (i.e. usersolver) 
# of the parent class (i.e. solver) that is used by default
####################################################################
import numpy as np
import pandas as pd
import os
import shutil
from GeoClawOpenFOAM import swcfdinter # Import the parent class
from GenUtilities import genUtilities # General utilities

class userswsolver(swcfdinter):

    ####################################################################
    # Read the bathymetry files
    ####################################################################
    def readbathymetry(self,data):

        print("This function is used to read the bathymetry files")
        # data: Data from the dakota.json file
        # Add your method statements here
        # If you do not want to create this method use
        # parent.dircreate() or super().dircreate() 

    ####################################################################
    # Read the sw-cfd interface data
    ####################################################################
    def interface(self,data):

        print("This function is used to read the sw-cfd interface data")
        # data: Data from the dakota.json file
        # Add your method statements here
        # If you do not want to create this method use
        # parent.geometry(data) or super().geometry(data)

    ####################################################################
    # Read solutions
    ####################################################################
    def readsolutions(self,data):

        print("This function is used to create mesh, if required")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.meshing(data) or super().meshing(data)

    ####################################################################
    # Convert SW solutions to boundary condition on the patch
    ####################################################################
    def swtoboundary(self,data):

        print("This function is used to convert the depth averaged velocity to 3D velocity and set them as boundary condition")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.meshing(data) or super().meshing(data)

    ####################################################################
    # Convert SW solutions to initial condition 
    ####################################################################
    def swtoinitialalpha(self,data):

        print("This function is used to read the water depth and set that as initial condition for the alpha field")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.meshing(data) or super().meshing(data)

    