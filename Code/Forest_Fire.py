import numpy as np
import random

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





def UPDATE_CELL_TYPE(Previous_Forest):

    ## Making an empty array to store the new array
    New_Forest_SINGLE = np.empty_like(Previous_Forest)

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

        ## Generating the new row to add to the new array later
        New_Row = np.zeros_like(Actual_Row)

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
                New_Row[Actual_Cell_Index] = "E"



            ## Next seeing if the cell is a tree
            ## Giving there a 1 in 5 chance of a Lightening (thus becoming a fire cell)
            elif Actual_Cell_Type == "T":
                Chance_Lightening = random.randint(1,6)
                if Cell_Above == "F" or Cell_Below == "F" or Cell_To_Left == "F" or Cell_To_Right == "F" or Chance_Lightening == 1:
                    New_Row[Actual_Cell_Index] = "F"
                else:
                    New_Row[Actual_Cell_Index] = "T"



            ## Next seeing if the cell is empty
            ## Giving there a 1 in 5 chance of a tree appearing
            elif Actual_Cell_Type == "E":
                Chance_Tree = random.randint(1,2)
                if Chance_Tree == 1:
                    New_Row[Actual_Cell_Index] = "T"
                else:
                    New_Row[Actual_Cell_Index] = "E"

            Actual_Cell_Index += 1 


        New_Forest_SINGLE[Row_Number] = New_Row
    return New_Forest_SINGLE
                    
# ['T', 'E', 'E', 'T', 'E', 'T'],
#  ['E', 'T', 'T', 'T', 'T', 'T'],
#  ['E', 'E', 'E', 'T', 'E', 'T'],
#  ['T', 'T', 'E', 'E', 'E', 'E'],
#  ['T', 'E', 'E', 'T', 'E', 'T'],
#  ['T', 'T', 'E', 'T', 'E', 'T']
#  ])

            




Initial_Forest_Array = np.array([
['T', 'E', 'E', 'T', 'E', 'T'],
 ['E', 'T', 'T', 'T', 'T', 'T'],
 ['E', 'E', 'E', 'T', 'E', 'T'],
 ['T', 'T', 'E', 'E', 'E', 'E'],
 ['T', 'E', 'E', 'T', 'E', 'T'],
 ['T', 'T', 'E', 'T', 'E', 'T']
 ])


NUMBER_OF_STEPS = 4

Empty_Array_List = GETTNG_EMPTY_STORAGE_ARRAY(STEP_NUMBER=NUMBER_OF_STEPS, INITIAL_ARRAY=Initial_Forest_Array)


def SIMULATE_FIRE(New_Forest, Step_Amount):
    for Iteration in range(1, Step_Amount):
        New_Forest[Iteration] = UPDATE_CELL_TYPE(New_Forest[Iteration-1])
    return New_Forest


New_Forest_simulated = SIMULATE_FIRE(Empty_Array_List, NUMBER_OF_STEPS)
for i in range(len(New_Forest_simulated)):
    print(" ")
    print(New_Forest_simulated[i])
    print(" ")



