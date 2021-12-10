import numpy as np
import os

CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)
for file in os.listdir(CurrentDirectory):
    if file.endswith("npz"):
        New_Forest_Simulation = file

with np.load(New_Forest_Simulation) as f:
    Cell_Types = f["state"]

# print(Cell_Types[0,0])

#####################
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Set up the initial figure and axes
fig, ax = plt.subplots(constrained_layout=True)
ax.axis("off")
cmap = ListedColormap(["#964B00", "#006400","#FF0000"])

# Plot the initial grid
array_plot = ax.imshow(
    Cell_Types[0],  # Make our data 2-D
    vmin=Cell_Types.min(),
    vmax=Cell_Types.max(),
    animated=True,
    cmap=cmap
)

#####################
def animate(i):
    array_plot.set_array(Cell_Types[i])
    return [array_plot]

#####################

from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Create an animation object which:
# - animate the Figure, `fig`
# - using the function `animate`
# - for len(cells) number of frames
# - where each frame lasts 100 milliseconds
anim = FuncAnimation(fig, animate, frames=len(Cell_Types), interval=100)

# Display the animation in the notebook
HTML(anim.to_jshtml())

#####################