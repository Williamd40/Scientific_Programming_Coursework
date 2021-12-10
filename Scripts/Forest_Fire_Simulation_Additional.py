#!/usr/bin/python

import numpy as np
import random
import sys
from datetime import datetime 


#############################################################################################################################################################################################


def GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER, INITIAL_ARRAY):
    ARRAY_LIST=[np.empty_like(INITIAL_ARRAY) for i in range(STEP_NUMBER)]
    ARRAY_LIST[0] = INITIAL_ARRAY
    return ARRAY_LIST


#############################################################################################################################################################################################


def RANDOM_GRID_GENERATION(N):
    Generated_Array = np.zeros((N, N), dtype="uint8")
    for i in range(len(Generated_Array)):
        for j in range(len(Generated_Array[i])):
            Generated_Array[i][j] = random.choice([0,1],)
    return Generated_Array


#############################################################################################################################################################################################


def GET_NEW_CHAR(Row_To_Analyse,Row_Above_List,Row_Below_List):
    ## Generating the new row to add to the new array later
    New_Row = np.zeros_like(Row_To_Analyse)

    ## Setting the index to 0, as this will iterate over the loop
    Actual_Cell_Index = 0

     ## Getting the actual cell types
    for Actual_Cell_Type in Row_To_Analyse:

        Right_Cell_Index = 0
        ## Getting the cell type of the above cell
        Cell_Above = Row_Above_List[Actual_Cell_Index]

        ## Getting the cell type of the below cell
        Cell_Below = Row_Below_List[Actual_Cell_Index]


        # Getting the value of the cell to the right
        Right_Cell_Index = Actual_Cell_Index + 1
        if Right_Cell_Index > len(Row_To_Analyse)-1:
            Right_Cell_Index-=1
            Cell_To_Right = Row_To_Analyse[Right_Cell_Index]
        else:
            Cell_To_Right = Row_To_Analyse[Right_Cell_Index]



        # Getting the value of the cell to the left
        Left_Cell_Index = Actual_Cell_Index - 1
        if Left_Cell_Index < 0:
            Left_Cell_Index+=1
            Cell_To_Left = Row_To_Analyse[Left_Cell_Index]
        else:
            Cell_To_Left = Row_To_Analyse[Left_Cell_Index]


        ## Changing cell depending on rules
        ## First seeing if the cell is on fire, if so skipping to end
        ## and setting it to "E" for empty.
        ## Now added the chance of rain, thus making a 2 -> 1
        ## I.E fire to tree
        if Actual_Cell_Type == 2:
            Chance_Rain = random.randint(1,4)
            if Chance_Rain == 1:
                New_Row[Actual_Cell_Index] = 1
            else:
                New_Row[Actual_Cell_Index] = 0



        ## Next seeing if the cell is a tree
        ## Giving there a 1 in 5 chance of a Lightening (thus becoming a fire cell)
        elif Actual_Cell_Type == 1:
            Chance_Lightening = random.randint(1,6)
            if Cell_Above == 2 or Cell_Below == 2 or Cell_To_Left == 2 or Cell_To_Right == 2 or Chance_Lightening == 1:
                New_Row[Actual_Cell_Index] = 2
            else:
                New_Row[Actual_Cell_Index] = 1







        ## Next seeing if the cell is empty
        ## Giving there a 1 in 5 chance of a tree appearing
        elif Actual_Cell_Type == 0:
            Chance_Tree = random.randint(1,2)
            if Chance_Tree == 1:
                New_Row[Actual_Cell_Index] = 1
            else:
                New_Row[Actual_Cell_Index] = 0

        Actual_Cell_Index += 1

    return New_Row


#############################################################################################################################################################################################


def GET_NEW_ROW(Previous_Forest,Previous_Forest_List_Rows,New_Forest_SINGLE):

    for Row_Number in range(len(Previous_Forest_List_Rows)):


        ## Getting the index position of the above row
        ## Also checking this to see if this exceeds the length
        Row_Above_Index = Row_Number - 1

        if Row_Above_Index < 0:
            Row_Above = Previous_Forest[Row_Number]
        else:
            Row_Above = Previous_Forest[Row_Above_Index]


        ## Getting the index position of the Below row
        ## Also checking this to see if this exceeds the length
        Row_Below_Index = Row_Number + 1
        if Row_Below_Index > len(Previous_Forest_List_Rows)-1:
            Row_Below = Previous_Forest[Row_Number]
        else:
            Row_Below = Previous_Forest[Row_Below_Index]


        ## Getting the actual row
        Actual_Row =  Previous_Forest[Row_Number]

        ## Converting the rows to lists, to make them iterable
        Actual_Row_Above_As_List = Row_Above.tolist()
        Actual_Row_As_List = Actual_Row.tolist()
        Actual_Row_Below_As_List = Row_Below.tolist()

        New_Row = GET_NEW_CHAR(Actual_Row_As_List,Actual_Row_Above_As_List,Actual_Row_Below_As_List)

        New_Forest_SINGLE[Row_Number] = New_Row

    return New_Forest_SINGLE


#############################################################################################################################################################################################


def UPDATE_CELL_TYPE(Previous_Forest):
    ## Making an empty array to store the new array
    New_Forest_SINGLE = np.empty_like(Previous_Forest)

    ## Making the previous array into a list of rows
    Previous_Forest_List_Rows = [Row for Row in Previous_Forest]

    GET_NEW_ROW(Previous_Forest,Previous_Forest_List_Rows,New_Forest_SINGLE)

    return New_Forest_SINGLE

## Taking command line arguments for the array dimensions
## and the number of steps to perform
Command_Line_Arguments = sys.argv[1:]
Array_Size = int(Command_Line_Arguments[0])
NUMBER_OF_STEPS = int(Command_Line_Arguments[1])

## Generating the initial random grid of "T" and "E"
Initial_Forest_Array = RANDOM_GRID_GENERATION(Array_Size)






## Generating the list of empty arrays that is equal to the length of steps
## I.E one array slot for each new array generated
Empty_Array_List = GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER=NUMBER_OF_STEPS, INITIAL_ARRAY=Initial_Forest_Array)


def SIMULATE_FIRE(New_Forest, Step_Amount):
    for Iteration in range(1, Step_Amount):
        New_Forest[Iteration] = UPDATE_CELL_TYPE(New_Forest[Iteration-1])
    return New_Forest


Current_Time = datetime.now()
Date = Current_Time.strftime("%d_%m_%Y__%H_%M_%S")
New_Forest_Simulated = SIMULATE_FIRE(Empty_Array_List, NUMBER_OF_STEPS)
np.savez_compressed(f"New_Forest_Simulation_With_Rain", state=New_Forest_Simulated)

# for I in range(len(New_Forest_Simulated)):
#     print(" ")
#     print(New_Forest_Simulated[I])
#     print(" ")
#0 = E
#1 = T
#2 = F
