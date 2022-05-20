#!/usr/bin/python

## The above line sets the environment when this script is run in bash

## Importing required packages
import numpy as np
import random, sys
from datetime import datetime 


#############################################################################################################################################################################################
## for reference, these are the cell types:
#0 = Empty cell
#1 = Tree cell
#2 = Fire cell
#############################################################################################################################################################################################


def GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER, INITIAL_ARRAY):
    """
    This function generates an empty storage array, to store the array generated at each time step.

    Args:
        STEP_NUMBER: The amount of time steps that will be performed, and therefore the amount of storage arrays needed.
        INITIAL_ARRAY: The initial time step of the simulation, thus time step zero/how the simuation starts.
        

    Returns:
        ARRAY_LIST: A storage array with the first entry being how the simulation starts. The length is equal to the total time steps.

    Examples:
        >>> STEP_NUMBER=2, INITIAL_ARRAY = [1,0
                                            0,1]
            
        >[1,0
          0,1],
          [,],
          [,]
    """
    ## Generating an empty array, that is the same size as the INITIAL_ARRAY
    ## This uses a list comprehension for every time step in the range of STEP_NUMBER, thus iterating once per time step requested
    ARRAY_LIST=[np.empty_like(INITIAL_ARRAY) for i in range(STEP_NUMBER)]

    ## Setting the initial array to equal INITIAL_ARRAY 
    ARRAY_LIST[0] = INITIAL_ARRAY

    ## Returning the new array generated
    return ARRAY_LIST


#############################################################################################################################################################################################


def RANDOM_GRID_GENERATION(N):

    """
    This function generates an array that is random filled with 0 and 1, thus has a random selection of cells that are either 0=Empty, or 1=Tree

    Args:
        N: The side length of the array, the array will have uniform side lengths.
        

    Returns:
        Generated_Array:  An array with side lengths N, containing 0s and 1s.

    Examples:
        >>> N=2
            
        >[1,0
          0,1]
    """

    ## Generating an array full of 0s with rows N and columns N, with the datatype of 'uint8'
    Generated_Array = np.zeros((N, N), dtype="uint8")

    ## Now iterating over each now of the array
    for i in range(len(Generated_Array)):

        ## Now iterating over each entry in the actual array, using a nested for loop
        for j in range(len(Generated_Array[i])):

            ## Making the individual array entry be either a 0 or a 1 randomly 
            Generated_Array[i][j] = random.choice([0,1],)

    ## Returning the randomly generated array
    return Generated_Array


#############################################################################################################################################################################################


def GET_NEW_CHAR(Row_To_Analyse,Row_Above_List,Row_Below_List):

    """
    This function generates the new row per time step, per sequence. Using a set of rules and random chances.

    Args:
        Row_To_Analyse: The current row being analysed
        Row_Above_List: The row above the current row being analysed
        Row_Below_List: The row below the current row being analysed
        

    Returns:
        New_Row: The newly generated row, with the correct new charcters.

    Examples:
        >>> Row_Above_List = [1,2,2]
            Row_To_Analyse = [0,0,1]
            Row_Below_List = [2,2,1]

            
        >[1,0,2]
    """

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
        ## this has a 1 in 4 chance
        if Actual_Cell_Type == 2:
            Chance_Rain = random.randint(1,4)
            if Chance_Rain == 1:
                New_Row[Actual_Cell_Index] = 1
            else:
                New_Row[Actual_Cell_Index] = 0



        ## Next seeing if the cell is a tree
        ## Giving there a 1 in 6 chance of a Lightening (thus becoming a fire cell)
        elif Actual_Cell_Type == 1:
            Chance_Lightening = random.randint(1,6)
            if Cell_Above == 2 or Cell_Below == 2 or Cell_To_Left == 2 or Cell_To_Right == 2 or Chance_Lightening == 1:
                New_Row[Actual_Cell_Index] = 2
            else:
                New_Row[Actual_Cell_Index] = 1







        ## Next seeing if the cell is empty
        ## Giving there a 1 in 2 chance of a tree appearing
        elif Actual_Cell_Type == 0:
            Chance_Tree = random.randint(1,2)
            if Chance_Tree == 1:
                New_Row[Actual_Cell_Index] = 1
            else:
                New_Row[Actual_Cell_Index] = 0

        Actual_Cell_Index += 1

    return New_Row


#############################################################################################################################################################################################



def GET_NEW_ROW(Previous_Forest_GNR,Previous_Forest_List_Rows_GNR,New_Forest_SINGLE_GNR):

    """
    This function gets the row being analysed, passes it to GET_NEW_CHAR and returns the new row.

    Args:
        Previous_Forest_GNR: The whole array of rows for the previous time step.
        Previous_Forest_List_Rows_GNR: The rows from the previous time step.
        New_Forest_SINGLE_GNR: An empty array that gets filled with  the new rows
        

    Returns:
        New_Forest_SINGLE_GNR: The newly generated array, with new rows.

    Examples:
        >>> New_Forest_SINGLE_GNR:[[]
                               []]
            Previous_Forest_GNR: [[1,0]
                                  [1,2]]
            Previous_Forest_List_Rows_GNR: [[1,0],[2,1]]

        
        >[1,1
          2,0]
    """

    ## Iterating over every row in the Previous_Forest_List_Rows value
    for Row_Number in range(len(Previous_Forest_List_Rows_GNR)):


        ## Getting the index position of the above row
        ## Also checking this to see if this exceeds the length
        Row_Above_Index = Row_Number - 1

        if Row_Above_Index < 0:
            Row_Above = Previous_Forest_GNR[Row_Number]
        else:
            Row_Above = Previous_Forest_GNR[Row_Above_Index]


        ## Getting the index position of the Below row
        ## Also checking this to see if this exceeds the length
        Row_Below_Index = Row_Number + 1
        if Row_Below_Index > len(Previous_Forest_List_Rows_GNR)-1:
            Row_Below = Previous_Forest_GNR[Row_Number]
        else:
            Row_Below = Previous_Forest_GNR[Row_Below_Index]


        ## Getting the actual row
        Actual_Row =  Previous_Forest_GNR[Row_Number]

        ## MAYBE SEE IF WE CAN REMOVE THE NEED FOR STORAGE VALUES

        ## Converting the rows to lists, to make them iterable
        Actual_Row_Above_As_List = Row_Above.tolist()
        Actual_Row_As_List = Actual_Row.tolist()
        Actual_Row_Below_As_List = Row_Below.tolist()

        New_Row = GET_NEW_CHAR(Actual_Row_As_List,Actual_Row_Above_As_List,Actual_Row_Below_As_List)

        New_Forest_SINGLE_GNR[Row_Number] = New_Row

    return New_Forest_SINGLE_GNR


#############################################################################################################################################################################################


def UPDATE_CELL_TYPE(Previous_Forest_UCT):

    """
    This function generates a new and empty array of zeros, and then  uses a list comprehension to get the rows of the 
    last time step. These variables and the original time step as an array are then passed to the GET_NEW_ROW function, 
    which then returns the new row for this time step. 

    Args:
        Previous_Forest_UCT: The whole array of rows for the previous time step.
        

    Returns:
        New_Forest_SINGLE: The newly generated array, with new rows.

    Examples:
        >>> New_Forest_SINGLE:[[]
                               []]
            Previous_Forest_List_Rows: [[1,0]
                                    [1,2]]
            Previous_Forest_List_Rows: [[1,0],[2,1]]

            
        >[1,1
          2,0]
    """

    ## Making an empty array to store the new array
    New_Forest_SINGLE = np.empty_like(Previous_Forest_UCT)

    ## Making the previous array into a list of rows
    Previous_Forest_List_Rows = [Row for Row in Previous_Forest_UCT]

    GET_NEW_ROW(Previous_Forest_UCT,Previous_Forest_List_Rows,New_Forest_SINGLE)

    return New_Forest_SINGLE


#############################################################################################################################################################################################


def SIMULATE_FIRE(New_Forest, Step_Amount):

    """
    This function begins the whole simulation
    Args:
        New_Forest: The whole array that the simulation will be run on
        Step_Amount: The amount of time steps tom perform
        

    Returns:
        New_Forest_SINGLE: The newly generated array, with new rows.

    Examples:
        >>> Too big to show
            
        > Too big to show

    """

    for Iteration in range(1, Step_Amount):
        New_Forest[Iteration] = UPDATE_CELL_TYPE(New_Forest[Iteration-1])
    return New_Forest


#############################################################################################################################################################################################

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



## Getting the exact date and time, so each simulation can be time-stamped
Current_Time = datetime.now()

## setting the date format
Date = Current_Time.strftime("%d_%m_%Y__%H_%M_%S")

## actually running the simulation
New_Forest_Simulated = SIMULATE_FIRE(Empty_Array_List, NUMBER_OF_STEPS)

## saving out the simulation
np.savez_compressed(f"New_Forest_Simulation_With_Rain", state=New_Forest_Simulated)