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

## Taking the current file to be analysed, given from the BASH script
Command_Line_Arguments = sys.argv[1:]
File_Name = str(Command_Line_Arguments[0])


## Changing working directory to where the file is
os.chdir(File_Name)

## finding the .npz file and loading it
for file in os.listdir(File_Name):
    if file.endswith("npz"):
        New_Forest_Simulation = file
with np.load(New_Forest_Simulation) as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]


## Pre-allocating lists to each cell type
Trees_On_Fire_Log=[]
Trees_Log=[]
Empty_Cells_Log=[]

## Counting each cell type at each time point
for Simulation in New_Forest_Sim:
    Empty_Cells_Log.append(np.count_nonzero(Simulation == 0))
    Trees_Log.append(np.count_nonzero(Simulation == 1))
    Trees_On_Fire_Log.append(np.count_nonzero(Simulation == 2))
    
## List comprehension to get the simulation number
Simulation_Number = [num for num in range(len(New_Forest_Sim))]

## Further list comprehensions to  get the total cells and total of each cell types at each time point.
## This is achieved through maping a lambda function to each cell type list, then using a list comprehension to return the results
## Please note, I originally had this running in parallel using `concurrent.futures.ProcessPoolExecutor()`
## However, I found this to work at more or less the same speed as the single core variant, so decided to stay with the single core variant
## due to ease of debugging.
        
Total_Cells_Per_Simulation = [len(New_Forest_Sim[0])*len(New_Forest_Sim[0]) for Simulation in Simulation_Number]

Empty_Cells_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Empty_Cells_Log)]

Trees_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Trees_Log)]

Trees_On_Fire_Log_Percentage = [(Result) for Result in map(lambda Total_Cell_List, Cell_List_In_Question: (Cell_List_In_Question/Total_Cell_List)*100,Total_Cells_Per_Simulation,Trees_On_Fire_Log)]


## Making a pandas dataframe to store the cell types at each time point.
Simulation_And_Percentage_Per_Variable_Dataframe = pd.DataFrame({'Simulation Number':Simulation_Number,'Total Cells Percentage':Total_Cells_Per_Simulation,'Total Empty Cells Percentage':Empty_Cells_Log_Percentage,'Total Trees Percentage':Trees_Log_Percentage,'Total Trees On Fire Percentage':Trees_On_Fire_Log_Percentage})

## Saving out the dataframe for the user as an excel spreadsheet, using the original file name.
OriginalFileName = New_Forest_Simulation.split(".")[0]
Simulation_And_Percentage_Per_Variable_Dataframe.to_csv("Percentages_For_Simulation.csv",index=False, sep='\t', encoding='utf-16')

##################
## Graph making ##
##################


## PLotting the graph of the results, and saving this out.

## Extracting the axes part of the graph for further customization.
ax = plt.axes()

## Setting the axes colour to black.
ax.set_facecolor("black")

## Plotting three lines, one per cell type. Also naming these and giving them unique colours.
plt.plot(Simulation_Number, Empty_Cells_Log_Percentage, label = "Total Empty Cells In Simulation", linewidth=0.5, color='pink')
plt.plot(Simulation_Number, Trees_Log_Percentage, label = "Total Trees In Simulation", linewidth=0.5, color='cyan')
plt.plot(Simulation_Number, Trees_On_Fire_Log_Percentage, label = "Total Trees On Fire In Simulation", linewidth=0.5, color='violet')

## Labelling the graph axes.
plt.xlabel('Simulation Number')
plt.ylabel('Percentage (%)')

## Setting the graph title.
plt.title('How the percentage of each cell type changes at each simulation.')

## Moving the legend to the right side of the graph.
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={"size":8})

## Setting the legend font colour.
plt.setp(legend.get_texts(), color='w')

## Setting the legend backdrop colour and edge colour.
frame = legend.get_frame()
frame.set_facecolor('black')
frame.set_edgecolor('black')

## Saving the graph out, and setting the saving parameters.
plt.savefig(f'Graph_Of_Percentages_{OriginalFileName}', dpi=1200,bbox_inches="tight", pad_inches=0.2,backend=None,)



######################
## Animation Making ##
######################



## Setting up the initial figure and axes.
fig, ax = plt.subplots(constrained_layout=True)
ax.axis("off")

## Making the three colours to be used in the animation, one per cell.
Colour_Map = ListedColormap(["#964B00", "#006400","#FF0000"])

## Making the array to be plotted.
array_plot = ax.imshow(
    ## Making the data 2D.
    New_Forest_Sim[0],  
    ## Setting the minimum and maximum values.
    vmin=New_Forest_Sim.min(),
    vmax=New_Forest_Sim.max(),

    ## Telling Python it will be animated.
    animated=True,

    ## Setting the colour map.
    cmap=Colour_Map
)


## Defining the function to animate the actual animation.
def animate(i):
    array_plot.set_array(New_Forest_Sim[i])
    return [array_plot]


## Making the animation.
anim = FuncAnimation(fig, animate, frames=len(New_Forest_Sim), blit=True)

## Setting the writer to save out the animation.
writervideo = animation.FFMpegWriter(fps=10)

## Saving out the animation
anim.save(f'Animation_Of_{OriginalFileName}.mp4', writer=writervideo)



