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
printf "\n${No_Colour}Now running simulation... \n"

python3 Forest_Fire_Functioned_NUMBERS.py $ARRAY_SIZE $STEP_NUM

printf "Done \n"

## Moving the outputted .npz file to a seperate folder
## Folder created is based on 
printf "Moving .npz file generated... \n"

File_Name_Full=$(find . -type f -name *.npz)

IFS='/' read -ra File_Name_Full_BROKEN <<< "$File_Name_Full"

File_Name=${File_Name_Full_BROKEN[1]}



IFS='.' read -ra DIR_NAME_TO_MAKE <<< ${File_Name_Full_BROKEN[1]}
DIR_NAME_TO_MAKE=${DIR_NAME_TO_MAKE[0]}

mkdir -p "$WHOLE_REPO_cwd/Outputted_Data/$DIR_NAME_TO_MAKE/"{NPZ_File,Graphs,Dataframes}

mv $File_Name "$WHOLE_REPO_cwd/Outputted_Data"

#/$DIR_NAME_TO_MAKE/NPZ_File

cd "$WHOLE_REPO_cwd/Outputted_Data"

printf "Ruining data visualisation \n"
python3 Data_Visualisation.py "$WHOLE_REPO_cwd/Outputted_Data"

printf "Visulaisation complete\n"
printf "Moving files...\n"


mv $File_Name "$DIR_NAME_TO_MAKE/NPZ_File"

mv Graph* "$DIR_NAME_TO_MAKE/Graphs"

mv Percentages_For_* "$DIR_NAME_TO_MAKE/Dataframes"

printf "Done \n"
printf "\n"
printf "${Green}Three output directories have been created\n"
printf "One contains the .npz file generated from the original simulation\n"
printf "Another contains the graph generated from analysing how the \npercentages of each cell type change over time\n"
printf "The final directory contains the data used to plot the graph.\n"

printf \n