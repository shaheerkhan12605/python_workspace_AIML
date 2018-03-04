import pandas as pd
import numpy as np
data=pd.read_excel('Tehsil Schools.xlsx', index_col=None, header=None)
dataset=np.array(data)
max=dataset[1][12]
max_school=dataset[1][1]
large_scale=0 #header
# Task 1-1
print("Names of all schools for which the number of students passed in 10th Class  Exam is ZERO \n ")

total=0
for data in dataset[1:]:
    if(data[8]==0):
         print(data[1])  # prinitng name of schools
    if(data[6]>50):
        if(max<=data[12]):
            max=data[12]
            max_school=data[1]
        large_scale=large_scale+1
    total=total+1


# Task 1-2
percentage=(float(large_scale)*100)/float(total)
print("**Percentage of large-sized schools w.r.t. student enrollment **")
print (percentage)

#Task 1-3
print("**Name of the school with the highest % dropout **")
print("%s with dropout percentage of %d " %(max_school ,max))