import random
import csv
import numpy as np
import pandas as pd


housing_data = open(r"C:\Users\nEW u\Desktop\Recommendation system\Implementation\DataSet\new_housing.csv")
csv_f = csv.reader(housing_data)
header = next(csv_f)
attributes = header[1:]
#print(attributes)
area = []
rent = []
bhk =[]
furnishing = []
for column in csv_f:

    area.append(column[1])
    rent.append(column[2])
    bhk.append(column[3])
    furnishing.append(column[4])
for i in range(0,30):
  rent[i]=rent[i].replace(',', "")
choices = []
for i in range(0,30):
    choices.append([area[i],rent[i],bhk[i],furnishing[i]])

print(choices)
location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
flat_type = ['1', '2', '3', '4']
flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']
upper_budget = [20000,40000,60000,80000,100000,150000]
#tenants = ['Bachelor','Family','Bachelor/Family']


imp_factor = []
#take user imp_factors for all the attributes
for i in range(len(attributes)):
    imp_factor.append(random.randint(0,5))

#new user preferred choices
new_user_pref = []
new_user_pref.append(random.sample(location,1))
new_user_pref.append(random.sample(upper_budget, 1))
new_user_pref.append(random.sample(flat_type, 1))
new_user_pref.append(random.sample(flat_furnishing, 1))
#new_user_pref.append(random.sample(tenants,1))


print(imp_factor)
#sorted_impFactor_index = np.argsort(imp_factor)
higher_attributes = []
for i in range(len(imp_factor)):
    if(imp_factor[i]>3):
        higher_attributes.append(i)
higher_attributes = sorted(higher_attributes,reverse=True)
print(new_user_pref)
highest_pref_values = []
for i in range(len(higher_attributes)):
    values = new_user_pref[higher_attributes[i]]
    highest_pref_values.append(values)
print(highest_pref_values)

# filter based on this values
filtered_flats = []
filtered_flat_ids = []
for i in range(len(choices)):
    for j in range(len(highest_pref_values)):
        if(highest_pref_values[j][0] in choices[i] and choices[i] not in filtered_flats):
            filtered_flats.append(choices[i])
        if(isinstance(highest_pref_values[j][0],int)):
            if(pd.to_numeric(highest_pref_values[j][0]) >= pd.to_numeric(choices[i][1]) and choices[i] not in filtered_flats):
                filtered_flats.append(choices[i])

print(filtered_flats)





