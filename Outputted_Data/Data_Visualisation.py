import numpy as np
import os

## Setting current working directory to script location
CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)

with np.load("New_Forest_Simulation.npz") as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]


import pandas as pd

summary = pd.DataFrame({"number_infected": number_infected})
summary.index.name = "Time step"
summary.plot()