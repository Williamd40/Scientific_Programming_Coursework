from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
import string

def GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER, INITIAL_ARRAY):
    ARRAY_LIST=[np.empty_like(INITIAL_ARRAY) for i in range(STEP_NUMBER)]
    ARRAY_LIST[0] = INITIAL_ARRAY
    return ARRAY_LIST

def RANDOM_GRID_GENERATION(N):
    Generated_Array = np.zeros((N, N), dtype=str)
    for i in range(len(Generated_Array)):
        for j in range(len(Generated_Array[i])):
            Generated_Array[i][j] = random.choice(["T","E"],)
    return Generated_Array


Initial_Forest_Array = np.array([
['T', 'E', 'E', 'T', 'E', 'T'],
 ['E', 'T', 'T', 'T', 'T', 'T'],
 ['E', 'E', 'E', 'T', 'E', 'T'],
 ['T', 'T', 'E', 'E', 'E', 'E'],
 ['T', 'E', 'E', 'T', 'E', 'T'],
 ['T', 'T', 'E', 'T', 'E', 'T']
 ])


NUMBER_OF_STEPS = 2

Empty_Array_List = GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER=NUMBER_OF_STEPS, INITIAL_ARRAY=Initial_Forest_Array)



def UPDATE_CELL_TYPE(Previous_Forest):

    ## Making an empty array to store the new array
    New_Forest = np.empty_like(Previous_Forest)

    ## Making the previous array into a list of rows
    Previous_Forest_List_Rows = [Row for Row in Previous_Forest]


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
        # print(" ")
        # print(Row_Above)
        # print(Actual_Row)
        # print(Row_Below)
        # print(" ")

        ## Converting the rows to lists, to make them iterable
        Actual_Row_Above_As_List = Row_Above.tolist()
        Actual_Row_As_List = Actual_Row.tolist()
        Actual_Row_Below_As_List = Row_Below.tolist()

        ## Setting the index to 0, as this will iterate over the loop
        Actual_Cell_Index = 0
        ## Getting the actual cell types
        
        for Actual_Cell_Type in Actual_Row_As_List:
            Right_Cell_Index = 0
            ## Getting the cell type of the above cell
            Cell_Above = Actual_Row_Above_As_List[Actual_Cell_Index]

            ## Getting the cell type of the below cell
            Cell_Below = Actual_Row_Below_As_List[Actual_Cell_Index]

            
            # Getting the value of the cell to the right
            Right_Cell_Index = Actual_Cell_Index + 1
            if Right_Cell_Index > len(Actual_Row_As_List)-1:
                Right_Cell_Index-=1
                Cell_To_Right = Actual_Row_As_List[Right_Cell_Index]
            else:
                Cell_To_Right = Actual_Row_As_List[Right_Cell_Index]
            
            

            # Getting the value of the cell to the left
            Left_Cell_Index = Actual_Cell_Index - 1
            if Left_Cell_Index < 0:
                Left_Cell_Index+=1
                Cell_To_Left = Actual_Row_As_List[Left_Cell_Index]
            else:
                Cell_To_Left = Actual_Row_As_List[Left_Cell_Index]


            ## Changing cell depending on rules
            ## First seeing if the cell is on fire, if so skipping to end
            ## and setting it to "E" for empty.
            if Actual_Cell_Type == "F":
                New_Cell_Type = "E"

            ## Next seeing if the cell is a tree
            elif Actual_Cell_Type == "T":
                if  Cell_Above == "F" or Cell_Below == "F" or Cell_To_Left == "F" or Cell_To_Right == "F":
                    New_Cell_Type== "F"

                



            
            


            


        
# ['T', 'E', 'E', 'T', 'E', 'T'],
#  ['E', 'T', 'T', 'T', 'T', 'T'],
#  ['E', 'E', 'E', 'T', 'E', 'T'],
#  ['T', 'T', 'E', 'E', 'E', 'E'],
#  ['T', 'E', 'E', 'T', 'E', 'T'],
#  ['T', 'T', 'E', 'T', 'E', 'T']
#  ])




            Actual_Cell_Index += 1 
            ## Actual_Row_As_List)
            




def SIMULATE_FIRE(New_Forest, Step_Amount):
    for Iteration in range(1, Step_Amount):
        New_Forest[Iteration] = UPDATE_CELL_TYPE(New_Forest[Iteration-1])


SIMULATE_FIRE(Empty_Array_List, NUMBER_OF_STEPS)

