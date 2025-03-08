import pandas as pd 

myData2 = { 
'Make': ["Toyota","Ford","Volkswagen","Toyota","Ford","Toyota","Vauxhall","Volkswagen","Ford","Volkswagen","Ford"],
'Model':["Yaris","Fiesta","T-Cross","Yaris","Fiesta","Yaris","Corsa","T-Cross","Puma","Polo","Fiesta"], 
'Colour':["Red","Blue","Black","White","Navy Blue","Red","White","Grey","Navy Blue","White","Blue"], 
'No_of_Seats':[5,5,5,5,5,5,5,5,5,5,5], 
'Year':[2019,2024,2020,2019,2024,2019,2024,2022,2023,2024,2024]
}
myD1  = { 
"Type of Petrol": ["Unleaded","Unleaded","Unleaded","Unleaded","Diesel","Unleaded","Unleaded","Diesel","Unleaded","Unleaded","Unleaded"], 
"Manual or Automatic": ["Manual","Manual","Manual","Manual","Manual","Manual","Automatic","Manual","Automatic","Manual","Manual"]          
}
myVar1 = pd.DataFrame(myData2) 
myVar2 = pd.DataFrame(myD1) 
myCars = myVar1.join(myVar2)

carDuplicated = myCars.duplicated()
print(carDuplicated)
