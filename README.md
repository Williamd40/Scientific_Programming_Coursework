
<p align=centre>
  <img src = "README_Media/Overall_Burning_Tree.png" width="500">
</p>
<head>
</head>

<main>


<body>



<h1>
 Scientific Programming Forest Fire Simulation Coursework 2021
</h1>
<i>
<p1  style = "text-indent:30%; color:grey;">
All code written here is my own work
<br>By <b>William D'Alessandro<b></i>
</p1>
<hr>


<article>
<h2>
    How to run this project
</h2>

<h3>
    Setting up
</h3>

<p1>
    To run this code, simply set your working directory to '~\Scientific_Programming_Coursework\Scripts'. <br>
    Next, using Ubuntu, turn your terminal to one which can interpret BASH scripts, this is often done by simply typing BASH into the cmd terminal itself.
    You will then see green and blue text, in place of the white text. You may be missing some of the required packages, to install them simply follow the on screen sudo commands, as BASH will tell you the prompts to install these.
</p1>
<h3>
Running the simulation
</h3>
<p2>
    This project is designed to be as user-friendly as possible, and as such
    a single BASH command will not only run both simulations together, but will also carry out all the data analysis. The outputted files will then be time stamped and stored in a specific output folder. You will get one output directory per full run through, containing one sub-directory per simulation. Each of these sub-directories will then contain four output folders. The output folders are as follows:
<dl>
<dt>Animation</dt>
<dd>The animation of this simulation.</dd>

<dt>Dataframes</dt>
<dd>A .csv file containing the percentages of each cell type at each time step</dd>

<dt>Graphs</dt>
<dd>The graph plotted for the simulation</dd>

<dt>NPZ_File</dt>
<dd>The dataframe in a .npz format</dd>

</dl>

Now to actually run these simulation, you have two optional parameters. These specify, in order, the array size, and the amount oif time steps. These are specified after the command to run the simulations, as such:<br><strong>bash Simulation_Generation.sh 'Array Size' 'Time Steps'</strong><br>Please note, you will not type Array Size or Time Steps, simply enter numerical values. For example, <strong>bash Simulation_Generation.sh 100 2000</strong> will make an array with the dimensions 100*100, ands then perform 2000 time steps. However, if you choose to not enter values, the project will default to an array of 50*50, and 1000 time steps.
</p2>



</article>



</body>

</main>
