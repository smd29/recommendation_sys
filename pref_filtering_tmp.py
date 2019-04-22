import random
import csv
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
    choices.append([area[i],pd.to_numeric(rent[i]),pd.to_numeric(bhk[i]),furnishing[i]])

print(choices)
location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
flat_type = ['1', '2', '3', '4']
flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']
upper_budget = [20000,40000,60000,80000,100000,150000]
#tenants = ['Bachelor','Family','Bachelor/Family']


imp_factor = []
total_imp = 0
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
for i in range(len(imp_factor)):
    total_imp+=imp_factor[i]
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
    if(max_location==min_location):
        location_list[i] = (location_list[i] - min_location)
    elif(max_location!=min_location):
        location_list[i] = ((location_list[i]-min_location)/(max_location-min_location))
    price_list[i] = ((max_price-price_list[i])/(max_price-min_price))
    if(max_bhk==min_bhk):
        bhk_list[i] = (bhk_list[i] - min_bhk)
    elif(max_bhk!=min_bhk):
        bhk_list[i] = ((bhk_list[i]-min_bhk)/(max_bhk-min_bhk))
    if(max_furnish==min_furnish):
        furnish_list[i] = (furnish_list[i] - min_furnish)
    elif(max_furnish!=min_furnish):
        furnish_list[i] = ((furnish_list[i]-min_furnish)/(max_furnish-min_furnish))
# print(location_list)
# print(price_list)
# print(bhk_list)
# print(furnish_list)

d_location = []
d_price = []
d_bhk = []
d_furnish = []
for i in range(len(location_list)):
    for j in range(len(location_list)):
        if(location_list[i]-location_list[j]<0):
            d_location.append(0)
        else:
            d_location.append(location_list[i]-location_list[j])
        if(price_list[i]-price_list[j]<0):
            d_price.append(0)
        else:
            d_price.append(price_list[i]-price_list[j])
        if(bhk_list[i]-bhk_list[j]<0):
            d_bhk.append(0)
        else:
            d_bhk.append(bhk_list[i]-bhk_list[j])
        if(furnish_list[i]-furnish_list[j]<0):
            d_furnish.append(0)
        else:
            d_furnish.append(furnish_list[i]-furnish_list[j])

print(d_location)
print(d_price)
print(d_bhk)
print(d_furnish)


############
weighted_location = []
weighted_price = []
weighted_bhk = []
weighted_furnish = []
for i in range(len(d_location)):
    weighted_location.append(imp_factor[0]*d_location[i])
    weighted_price.append(imp_factor[1]*d_price[i])
    weighted_bhk.append(imp_factor[2]*d_bhk[i])
    weighted_furnish.append(imp_factor[3]*d_furnish[i])

no_of_filtered_flats = len(filtered_flats)
print(no_of_filtered_flats)
avg_weight = []
for i in range(len(weighted_furnish)):
    avg_weight.append((weighted_location[i]+weighted_price[i]+weighted_bhk[i]+weighted_furnish[i])/total_imp)
#print(len(avg_weight))
###calculating leaving flow
leaving_vals_out = []
last = 0
while(last<len(avg_weight)):
    leaving_vals_out.append(avg_weight[last:last+(no_of_filtered_flats)])