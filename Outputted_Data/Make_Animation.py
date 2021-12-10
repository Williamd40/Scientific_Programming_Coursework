
#####################
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import matplotlib.animation as animation

for file in os.listdir():
    if file.endswith("npz"):
        New_Forest_Simulation = file

with np.load(New_Forest_Simulation) as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]

# Set up the initial figure and axes
fig, ax = plt.subplots(constrained_layout=True)
ax.axis("off")
cmap = ListedColormap(["#964B00", "#006400","#FF0000"])
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
#####################
# Create an animation object which:
# - animate the Figure, `fig`
# - using the function `animate`
# - for len(cells) number of frames
# - where each frame lasts 100 milliseconds
anim = FuncAnimation(fig, animate, frames=len(New_Forest_Sim), interval=20)
# Display the animation in the notebook
# HTML(anim.to_jshtml())
#####################


Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=4000)
anim.save(f'Animation_Of_.mp4', writer=writer)


#####################
