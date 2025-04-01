import pandas as pd
data1 = {"Student_ID": [284,264,754,646,247,938,646,138],
         "Name": ['Lee Cox','Matt Bond','Marcellina Adams','Jill Gates','Joe Malone','Emma Mills','Jill Gates','Raven Adams'],
         "Subject": ['Computer Science','Media Studies','Film Studies','Computer Science','Art and Design','Film Studies','Computer Science','History']}
data2 = {"Grade": [7,9,8,9,3,3,9,4],
         "Retake?":[False,False,False,False,True,True,False,False]}

parad1 = pd.DataFrame(data1)
parad2 = pd.DataFrame(data2)
studentData = parad1.join(parad2)
duplicated_data = studentData.duplicated()
print(duplicated_data)
