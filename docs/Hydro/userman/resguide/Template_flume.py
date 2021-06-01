####################################################################
# Import necessary packages for user-flume class
# We are creating a child class (i.e. userflume) 
# of the parent class (i.e. OSUWaveFlume) that is used by default
####################################################################
import numpy as np
import pandas as pd
import os
import shutil
from Flume import OSUWaveFlume # Import the parent class
from GenUtilities import genUtilities # General utilities

class userflume(OSUWaveFlume):

    ####################################################################
    # Generate the flume geometry
    ####################################################################
    def generateflume(self,data):

        print("This function is used to create the STL files for the flume geometry")
        # Add your method statements here
        # If you do not want to create this method use
        # parent.generateflume() or super().generateflume() 

    ####################################################################
    # Create the wavemaker text file
    ####################################################################
    def GENwavemakerfile(self,dispfilename,heightfilename):

        print("This function is used to create the wavemakerMovement.txt file that has information about the wall movement & water height")
        # dispfilename: File with moving wall displacement with time
        # heightfilename: File with height of water at the moving wall with time
        # Add your method statements here
        # If you do not want to create this method use
        # parent.GENwavemakerfile(data) or
        # super().GENwavemakerfile(data)

