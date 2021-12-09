#!/usr/bin/bash




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
    echo "Array size set to default: "$ARRAY_SIZE
else
    echo "Array size set to user designated value: "$ARRAY_SIZE
fi

if [ -z "$STEP_NUM" ]
then
    STEP_NUM=5

    echo "Step number set to default: "$STEP_NUM
else
    echo "Step number set to user designated value: "$STEP_NUM
fi

## Running the simulation and telling the user what is happening
printf "Now running simulation... \n"

python3 Forest_Fire_Functioned.py $ARRAY_SIZE $STEP_NUM

printf "Done \n"

## Moving the outputted .npz file to a seperate folder
## Folder created is based on 
printf "Moving .npz file generated... \n"

File_Name_Full=$(find . -type f -name *.npz)

IFS='/' read -ra File_Name_Full_BROKEN <<< "$File_Name_Full"

File_Name=${File_Name_Full_BROKEN[1]}



IFS='.' read -ra DIR_NAME_TO_MAKE <<< ${File_Name_Full_BROKEN[1]}
DIR_NAME_TO_MAKE=${DIR_NAME_TO_MAKE[0]}

mkdir -p "$WHOLE_REPO_cwd/Outputted_Data/$DIR_NAME_TO_MAKE/"{NPZ_File,Graphs}

mv $File_Name "$WHOLE_REPO_cwd/Outputted_Data/$DIR_NAME_TO_MAKE/NPZ_File"

cd "$WHOLE_REPO_cwd/Outputted_Data"


printf "Done \n"


