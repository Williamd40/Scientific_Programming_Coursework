#!/usr/bin/bash
Red='\033[0;31m'
Purple='\033[0;35m'
No_Colour='\033[0m'
Green='\033[0;32m'




                                                                                                                                                                                                                                                                                                                                                                   
printf "${Red}           

                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                      
FFFFFFFFFFFFFFFFFFFFFF                                                                                tttt               FFFFFFFFFFFFFFFFFFFFFF  iiii                                                 SSSSSSSSSSSSSSS   iiii                          
F::::::::::::::::::::F                                                                             ttt:::t               F::::::::::::::::::::F i::::i                                              SS:::::::::::::::S i::::i                         
F::::::::::::::::::::F                                                                             t:::::t               F::::::::::::::::::::F  iiii                                              S:::::SSSSSS::::::S  iiii                          
FF::::::FFFFFFFFF::::F                                                                             t:::::t               FF::::::FFFFFFFFF::::F                                                    S:::::S     SSSSSSS                                
  F:::::F       FFFFFFooooooooooo   rrrrr   rrrrrrrrr       eeeeeeeeeeee        ssssssssss   ttttttt:::::ttttttt           F:::::F       FFFFFFiiiiiiirrrrr   rrrrrrrrr       eeeeeeeeeeee         S:::::S            iiiiiii    mmmmmmm    mmmmmmm   
  F:::::F           oo:::::::::::oo r::::rrr:::::::::r    ee::::::::::::ee    ss::::::::::s  t:::::::::::::::::t           F:::::F             i:::::ir::::rrr:::::::::r    ee::::::::::::ee       S:::::S            i:::::i  mm:::::::m  m:::::::mm 
  F::::::FFFFFFFFFFo:::::::::::::::or:::::::::::::::::r  e::::::eeeee:::::eess:::::::::::::s t:::::::::::::::::t           F::::::FFFFFFFFFF    i::::ir:::::::::::::::::r  e::::::eeeee:::::ee      S::::SSSS          i::::i m::::::::::mm::::::::::m
  F:::::::::::::::Fo:::::ooooo:::::orr::::::rrrrr::::::re::::::e     e:::::es::::::ssss:::::stttttt:::::::tttttt           F:::::::::::::::F    i::::irr::::::rrrrr::::::re::::::e     e:::::e       SS::::::SSSSS     i::::i m::::::::::::::::::::::m
  F:::::::::::::::Fo::::o     o::::o r:::::r     r:::::re:::::::eeeee::::::e s:::::s  ssssss       t:::::t                 F:::::::::::::::F    i::::i r:::::r     r:::::re:::::::eeeee::::::e         SSS::::::::SS   i::::i m:::::mmm::::::mmm:::::m
  F::::::FFFFFFFFFFo::::o     o::::o r:::::r     rrrrrrre:::::::::::::::::e    s::::::s            t:::::t                 F::::::FFFFFFFFFF    i::::i r:::::r     rrrrrrre:::::::::::::::::e             SSSSSS::::S  i::::i m::::m   m::::m   m::::m
  F:::::F          o::::o     o::::o r:::::r            e::::::eeeeeeeeeee        s::::::s         t:::::t                 F:::::F              i::::i r:::::r            e::::::eeeeeeeeeee                   S:::::S i::::i m::::m   m::::m   m::::m
  F:::::F          o::::o     o::::o r:::::r            e:::::::e           ssssss   s:::::s       t:::::t    tttttt       F:::::F              i::::i r:::::r            e:::::::e                            S:::::S i::::i m::::m   m::::m   m::::m
FF:::::::FF        o:::::ooooo:::::o r:::::r            e::::::::e          s:::::ssss::::::s      t::::::tttt:::::t     FF:::::::FF           i::::::ir:::::r            e::::::::e               SSSSSSS     S:::::Si::::::im::::m   m::::m   m::::m
F::::::::FF        o:::::::::::::::o r:::::r             e::::::::eeeeeeee  s::::::::::::::s       tt::::::::::::::t     F::::::::FF           i::::::ir:::::r             e::::::::eeeeeeee       S::::::SSSSSS:::::Si::::::im::::m   m::::m   m::::m
F::::::::FF         oo:::::::::::oo  r:::::r              ee:::::::::::::e   s:::::::::::ss          tt:::::::::::tt     F::::::::FF           i::::::ir:::::r              ee:::::::::::::e       S:::::::::::::::SS i::::::im::::m   m::::m   m::::m
FFFFFFFFFFF           ooooooooooo    rrrrrrr                eeeeeeeeeeeeee    sssssssssss              ttttttttttt       FFFFFFFFFFF           iiiiiiiirrrrrrr                eeeeeeeeeeeeee        SSSSSSSSSSSSSSS   iiiiiiiimmmmmm   mmmmmm   mmmmmm
                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
Data Analysis will be run automatically.

Don't forget you can specify the array parameter lengths, and the time step count! Try:
'bash Simulation_Generation.sh 50 1000' to generate arrays which are 50*50, and where each simulation has 1000 time steps
The generic command is:
'bash Simulation_Generation.sh <Array_Size> <Time_Steps>'

If no user inputs are found, the simulation will default to:
ARRAY_SIZE=50
STEP_NUM=1000

This script needs to following packages installed into ubuntu to run properly:
    > ffmpeg
    > pip to install ipython
    > matplotlib
    > numpy
    > seaborn
    > pandas
    > sys
    > random

When run correctly you will see one created parent dirctory per simulation pair.
Within this directory there will then be two sub-directories, one per simulation:
    > One simulation with the added effect 'Rain'
    > One without this effect

Then, within each of these directories, a further four directories will be found:
    > 'Animation' will hold an mp4 file of the simulation in action
    > 'Dataframes' will contain the percentage of each cell type, at each time step
    > 'Graphs' will contain a graph showing the results of the generated dataframe
    > 'NPZ_File' will contain the generated .npz from each simulation


Please note: two simulations run with the same array size, and step number will never be the same
This simulation randomly generates the initial array, and then further random factors will influence the 
outcome of each time step. In theory, two simulations will therefore never be the same!
${No_Colour}"                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                   
Join() {
  local IFS="$1"
  shift
  echo "$*"
}



## Saving the various directory paths for later reference
SCRIPT_cwd="$(pwd)"
cd ..
WHOLE_REPO_cwd="$(pwd)"

## sets the cd to the working directory of the bash script
cd $SCRIPT_cwd

## Taking the array size and amount of steps from the cmd line
ARRAY_SIZE=$1
STEP_NUM=$2

## Testing to check if the user specified requirements for
## the array size and step amount

## If nothing was entered then the program will
## default to these default values

if [ -z "$ARRAY_SIZE" ]
then
    ARRAY_SIZE=50
    printf "\nArray size set to default: "$ARRAY_SIZE 
else
    printf "\nArray size set to user designated value: "$ARRAY_SIZE
fi

if [ -z "$STEP_NUM" ]
then
    STEP_NUM=1000

    printf "\nStep number set to default: "$STEP_NUM
else
    printf "\nStep number set to user designated value: "$STEP_NUM
fi

## Running the simulation and telling the user what is happening
printf "\n${No_Colour}Now running simulations... \n"

python3 Forest_Fire_Simulation_Base.py $ARRAY_SIZE $STEP_NUM

python3 Forest_Fire_Simulation_Additional.py $ARRAY_SIZE $STEP_NUM

printf "Done \n"


## Getting the exact date and time to create a parent directory
## to store the outputs of both simulations
IFS='.' read -ra Date_Broken <<< "$(date)"
Date=$(Join "_" $Date_Broken)
IFS=':' read -ra Date_Broken <<< "$Date"
Date=$(Join "_" ${Date_Broken[@]})


for file in *.npz
do
    cd $SCRIPT_cwd
    ## Moving the outputted .npz file to a seperate folder
    ## Folder created is based on 
    printf "Moving $file... \n"

    File_Name=$file

    IFS='.' read -ra File_Name_Full_BROKEN <<< "$file"

    DIR_NAME_TO_MAKE=${File_Name_Full_BROKEN[0]}


    mkdir -p "$WHOLE_REPO_cwd/Outputted_Data/Simulation_$Date/$DIR_NAME_TO_MAKE/"{NPZ_File,Graphs,Dataframes,Animation}

    mv $File_Name "$WHOLE_REPO_cwd/Outputted_Data"

    cd "$WHOLE_REPO_cwd/Outputted_Data"

    printf "Running data visualisation \n"

    python3 Data_Visualisation.py "$WHOLE_REPO_cwd/Outputted_Data" 2>/dev/null

    printf "Visualisation complete
Moving files...\n"


    mv $File_Name "Simulation_$Date/$DIR_NAME_TO_MAKE/NPZ_File"

    mv Graph* "Simulation_$Date/$DIR_NAME_TO_MAKE/Graphs"

    mv Percentages_For_* "Simulation_$Date/$DIR_NAME_TO_MAKE/Dataframes"

    mv Animation* "Simulation_$Date/$DIR_NAME_TO_MAKE/Animation"
done

printf "${Green}All done!
${No_Colour}Three output directories have been created"
echo