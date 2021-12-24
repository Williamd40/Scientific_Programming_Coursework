#!/usr/bin/python

import numpy as np
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


Command_Line_Arguments = sys.argv[1:]
File_Name = str(Command_Line_Arguments[0])


os.chdir(File_Name)
for file in os.listdir(File_Name):
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

 
OrignalFileName = New_Forest_Simulation.split(".")[0]
Simulation_And_Percentage_Per_Variable_Dataframe.to_csv("Percentages_For_Simulation.csv",index=False, sep='\t', encoding='utf-16')

plt.figure(facecolor='grey')
ax = plt.axes()
ax.set_facecolor("black")
plt.plot(Simulation_Number, Empty_Cells_Log_Percentage, label = "Total Empty Cells In Simulation", linewidth=0.5, color='pink')
plt.plot(Simulation_Number, Trees_Log_Percentage, label = "Total Trees In Simulation", linewidth=0.5, color='cyan')
plt.plot(Simulation_Number, Trees_On_Fire_Log_Percentage, label = "Total Trees On Fire In Simulation", linewidth=0.5, color='violet')
plt.xlabel('Simulation Number')
plt.ylabel('Percentage (%)')
plt.title('How the percentage of each cell type changes at each simulation.')
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={"size":8})
plt.setp(legend.get_texts(), color='w')
frame = legend.get_frame()
frame.set_facecolor('black')
frame.set_edgecolor('black')
plt.savefig(f'Graph_Of_Percentages_{OrignalFileName}', dpi=1200,bbox_inches="tight", pad_inches=0.2,backend=None,)







# Set up the initial figure and axes
fig, ax = plt.subplots(constrained_layout=True)
ax.axis("off")
cmap = ListedColormap(["#964B00", "#FF0000","#FF0000"])
# Plot the initial grid
array_plot = ax.imshow(
    New_Forest_Sim[0],  # Make our data 2-D
    vmin=New_Forest_Sim.min(),
    vmax=New_Forest_Sim.max(),
    animated=True,
    cmap=cmap
)
#####################
def animate(i):
    array_plot.set_array(New_Forest_Sim[i])
    return [array_plot]



anim = FuncAnimation(fig, animate, frames=len(New_Forest_Sim), interval=150)


Writer = animation.writers['ffmpeg']
writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=2000)
anim.save(f'Animation_Of_{OrignalFileName}.mp4', writer=writer)


#####################
