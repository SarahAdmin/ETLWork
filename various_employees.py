import pandas as pd
employee_data = {"Name":['Lee Cox','Matt Bond','Raven Adams','Jodie Green','Tammy McGuire','Lemon Jelly','Lee Cox','Raven Adams','Pamela Green'],
                 "Position":['Computer Scientist','Financial Analyst','Accountant','Project Manager','Teacher','Lawyer','Computer Scientist','Accountant','Lawyer']}
dataOne = {"Drive a car?":[True, True, True, False, False, True, True,True,True],
           "Salary":[35000,30000,45000,50000,45000,55000,35000,45000,60000]}
par1 = pd.DataFrame(employee_data)
par2 = pd.DataFrame(dataOne)
employee_df = par1.join(par2)
columntoDelete = ['Drive a car?']
new_employee_df = employee_df.drop(columntoDelete,axis=1)
print(new_employee_df.to_string())
