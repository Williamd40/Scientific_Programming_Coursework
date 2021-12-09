import numpy as np
import os
import seaborn as sns
from concurrent.futures import ProcessPoolExecutor




## Setting current working directory to script location
CurrentDirectory = os.path.dirname(__file__)
os.chdir(CurrentDirectory)
for file in os.listdir(CurrentDirectory):
    if file.endswith("npz"):
        New_Forest_Simulation = file

with np.load(New_Forest_Simulation) as Forest_Sim:
    New_Forest_Sim = Forest_Sim["state"]


Trees_On_Fire_Log=[]
Trees_Log=[]
Empty_Cells_Log=[]
Trees_On_Fire_Log_Percentage = []

Total_Cells = []


for Simulation in New_Forest_Sim:
    Empty_Cells_Log.append(np.count_nonzero(Simulation == 0))
    Trees_Log.append(np.count_nonzero(Simulation == 1))
    Trees_On_Fire_Log.append(np.count_nonzero(Simulation == 2))
    
for i in range(len(Trees_On_Fire_Log)):
    Total_Cells.append(len(New_Forest_Sim[0])*len(New_Forest_Sim[0]))


# if __name__ == "__main__":
#     with ProcessPoolExecutor() as pool:

#         Result_Empty_Cells_Log_Percentage = pool.map(CONVERT_TO_PERCENTAGE, Total_Cells, Empty_Cells_Log)


#         Result_Trees_Log_Percentage = pool.map(CONVERT_TO_PERCENTAGE, Total_Cells, Trees_Log)


#         Result_Trees_On_Fire_Log_Percentage = pool.map(CONVERT_TO_PERCENTAGE, Total_Cells, Trees_On_Fire_Log)


#         Empty_Cells_Log_Percentage = []
#         for r in Result_Empty_Cells_Log_Percentage:
#             Empty_Cells_Log_Percentage.append(r)


#         Trees_Log_Percentage = []
#         for r in Result_Trees_Log_Percentage:
#             Trees_Log_Percentage.append(r)


#         Trees_On_Fire_Log_Percentage = []
#         for r in Result_Trees_On_Fire_Log_Percentage:
#             Trees_On_Fire_Log_Percentage.append(r)



#         print(Empty_Cells_Log_Percentage)
#         print(Trees_Log_Percentage)
#         print(Trees_On_Fire_Log_Percentage)






# sns.displot(data=(tips), x="total_bill", hue="time", kind="kde", common_norm=False)


# for i in range(len(New_Forest_Sim)):
#     print(New_Forest_Sim[i])
#     print(f"For simulation {i}")
#     print(Empty_Cells_Log[i])
#     print(Trees_Log[i])
#     print(Trees_On_Fire_Log[i])

