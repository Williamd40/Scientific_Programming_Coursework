#!/usr/bin/bash
Red='\033[0;31m'
Purple='\033[0;35m'
No_Colour='\033[0m'
Green='\033[0;32m'

printf "${Purple}##########################################\n"
printf "##	Forest Fire Simulation          ##\n" 
printf "##########################################\n"
printf "##	Data Analysis run automatically	    ##\n" | column -t
printf "##########################################\n"
printf "##    Don't    forget    you    can     ##\n" 
printf "##########################################\n"
printf "##  specify   the   array  parameter    ##\n" 
printf "##########################################\n"
printf "##  lengths,    and     the     time    ##\n" 
printf "##########################################\n"
printf "##          step         count!         ##\n" 
printf "##########################################\n${No_Colour}"



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
    ARRAY_SIZE=10
    printf "\nArray size set to default: "$ARRAY_SIZE 
else
    printf "\nArray size set to user designated value: "$ARRAY_SIZE
fi

if [ -z "$STEP_NUM" ]
then
    STEP_NUM=5

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


    mkdir -p "$WHOLE_REPO_cwd/Outputted_Data/Simulation_$Date/$DIR_NAME_TO_MAKE/"{NPZ_File,Graphs,Dataframes}

    mv $File_Name "$WHOLE_REPO_cwd/Outputted_Data"

    cd "$WHOLE_REPO_cwd/Outputted_Data"

    printf "Runing data visualisation \n"
    python3 Data_Visualisation.py "$WHOLE_REPO_cwd/Outputted_Data"

    printf "Visulaisation complete\n"
    printf "Moving files...\n"


    mv $File_Name "Simulation_$Date/$DIR_NAME_TO_MAKE/NPZ_File"

    mv Graph* "Simulation_$Date/$DIR_NAME_TO_MAKE/Graphs"

    mv Percentages_For_* "Simulation_$Date/$DIR_NAME_TO_MAKE/Dataframes"
done

printf "Done \n"
printf "\n"
printf "${Green}Three output directories have been created\n"
printf "One contains the .npz file generated from the original simulation\n"
printf "Another contains the graph generated from analysing how the \npercentages of each cell type change over time\n"
printf "The final directory contains the data used to plot the graph.\n"

printf \n