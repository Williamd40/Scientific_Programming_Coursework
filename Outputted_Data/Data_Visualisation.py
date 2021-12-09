import numpy as np
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Setting current working directory to script location
CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)
for file in os.listdir(CurrentDirectory):
    if file.endswith("npz"):
        New_Forest_Simulation = file

with np.load(New_Forest_Simulation) as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]


Trees_On_Fire_Log=[]
Trees_Log=[]
Empty_Cells_Log=[]

for Simulation in New_Forest_Sim:
    Empty_Cells_Log.append(np.count_nonzero(Simulation == 0))
    Trees_Log.append(np.count_nonzero(Simulation == 1))
    Trees_On_Fire_Log.append(np.count_nonzero(Simulation == 2))
    
Simulation_Number = [num for num in range(len(New_Forest_Sim))]



Total_Cells_Per_Simulation = [len(New_Forest_Sim[0])*len(New_Forest_Sim[0]) for Simulation in Simulation_Number]

Empty_Cells_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Empty_Cells_Log)]

Trees_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Trees_Log)]

Trees_On_Fire_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Trees_On_Fire_Log)]




Simulation_And_Percentage_Per_Variable_Dataframe = pd.DataFrame({'Simulation Number':Simulation_Number,'Total Cells Percentage':Total_Cells_Per_Simulation,'Total Empty Cells Percentage':Empty_Cells_Log_Percentage,'Total Trees Percentage':Trees_Log_Percentage,'Total Trees On Fire Percentage':Trees_On_Fire_Log_Percentage})

 
OrignalFileName = (os.path.basename(file)).split(".")[0]


plt.plot(Simulation_Number, Total_Cells_Per_Simulation, label = "Total Cells In Simulation")
plt.plot(Simulation_Number, Empty_Cells_Log_Percentage, label = "Total Empty Cells In Simulation")
plt.plot(Simulation_Number, Trees_Log_Percentage, label = "Total Trees In Simulation")
plt.plot(Simulation_Number, Trees_On_Fire_Log_Percentage, label = "Total Trees On Fire In Simulation")
plt.xlabel('Simulation Number')
# Set the y axis label of the current axis.
plt.ylabel('Percentage')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Display a figure.
plt.show()