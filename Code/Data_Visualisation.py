import numpy as np
import os

## Setting current working directory to script location
CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)

with np.load("New_Forest_Simulation.npz") as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]

print(New_Forest_Sim)