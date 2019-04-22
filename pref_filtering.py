import random
import csv
import pandas as pd


housing_data = open(r"C:\Users\I355872\Desktop\Thesis\Code\new_housing.csv")
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
    choices.append([area[i],pd.to_numeric(rent[i]),pd.to_numeric(bhk[i]),furnishing[i]])

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
if(not filtered_flats):
    filtered_flats = choices
print(filtered_flats)


######### applying promethee here############

#convert strings to numeric values
for i in range(len(filtered_flats)):
    if(filtered_flats[i][3]=='Unfurnished'):
        filtered_flats[i][3] = 1
    elif (filtered_flats[i][3] == 'Semi-Furnished'):
        filtered_flats[i][3] = 2
    elif (filtered_flats[i][3] == 'Furnished'):
        filtered_flats[i][3] = 3
for i in range(len(filtered_flats)):
    if(new_user_pref[0][0]=='Magarpatta City'):
        if(filtered_flats[i][0]=='Magarpatta City'):
            filtered_flats[i][0] = 4
        elif(filtered_flats[i][0]=='Hadapsar'):
            filtered_flats[i][0] = 2
        elif(filtered_flats[i][0]=='Amanora Park Town'):
            filtered_flats[i][0] = 3
        elif(filtered_flats[i][0]=='Mundhwa'):
            filtered_flats[i][0] = 1
        else:
            filtered_flats[i][0] = 0

    elif (new_user_pref[0][0] == 'Hadapsar'):
        if (filtered_flats[i][0] == 'Magarpatta City'):
            filtered_flats[i][0] = 3
        elif (filtered_flats[i][0] == 'Hadapsar'):
            filtered_flats[i][0] = 4
        elif (filtered_flats[i][0] == 'Amanora Park Town'):
            filtered_flats[i][0] = 2
        elif (filtered_flats[i][0] == 'Mundhwa'):
            filtered_flats[i][0] = 1
        else:
            filtered_flats[i][0] = 0

    elif (new_user_pref[0][0] == 'Amanora Park Town'):
        if (filtered_flats[i][0] == 'Magarpatta City'):
            filtered_flats[i][0] = 3
        elif (filtered_flats[i][0] == 'Hadapsar'):
            filtered_flats[i][0] = 2
        elif (filtered_flats[i][0] == 'Amanora Park Town'):
            filtered_flats[i][0] = 4
        elif (filtered_flats[i][0] == 'Mundhwa'):
            filtered_flats[i][0] = 1
        else:
            filtered_flats[i][0] = 0

    elif (new_user_pref[0][0] == 'Mundhwa'):
        if (filtered_flats[i][0] == 'Magarpatta City'):
            filtered_flats[i][0] = 2
        elif (filtered_flats[i][0] == 'Hadapsar'):
            filtered_flats[i][0] = 1
        elif (filtered_flats[i][0] == 'Amanora Park Town'):
            filtered_flats[i][0] = 3
        elif (filtered_flats[i][0] == 'Mundhwa'):
            filtered_flats[i][0] = 4
        else:
            filtered_flats[i][0] = 0

print(filtered_flats)

#normalize
location_list = []
price_list = []
bhk_list = []
furnish_list = []
for i in range(len(filtered_flats)):
    location_list_val = filtered_flats[i][0]
    price_list_val = filtered_flats[i][1]
    bhk_list_val = filtered_flats[i][2]
    furnish_list_val = filtered_flats[i][3]
    location_list.append(location_list_val)
    price_list.append(price_list_val)
    bhk_list.append(bhk_list_val)
    furnish_list.append(furnish_list_val)
max_location = max(location_list)
min_location = min(location_list)
max_price = max(price_list)
min_price = min(price_list)
max_bhk = max(bhk_list)
min_bhk = min(bhk_list)
max_furnish = max(furnish_list)
min_furnish = min(furnish_list)
#################
for i in range(len(location_list)):
    location_list[i] = ((location_list[i]-min_location)/(max_location-min_location))
    price_list[i] = ((max_price-price_list[i])/(max_price-min_price))
    bhk_list[i] = ((bhk_list[i]-min_bhk)/(max_bhk-min_bhk))
    furnish_list[i] = ((furnish_list[i]-min_furnish)/(max_furnish-min_furnish))
print(location_list)
print(price_list)
print(bhk_list)
print(furnish_list)







