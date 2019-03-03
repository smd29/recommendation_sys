import user_preference_data
import readCSV
import numpy as np
from users_rating import existingUser


user_id = 0
users = int(input("Print number of users: "))


location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
flat_type = ['1BHK', '2BHK', '3BHK', '4BHK']
flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']

attributes_list = ['location','flat_type','flat_furnishing']
attributes = len(attributes_list)

print("\nPreferred choices or selcted choice of the existing users:\n")
location_list = user_preference_data.locationList(location,users)
flat_type_list = user_preference_data.flatType(flat_type,users)
flat_furnishing_list = user_preference_data.flatFurnishing(flat_furnishing,users)

ratingData = existingUser(users,attributes)
print("\nExisting user rating is: "+str(ratingData))

for i in range(len(ratingData)):
    #print(ratingData[i])
    prefOrder = np.argsort(ratingData[i])
    print(prefOrder)

#the last element of the prefOrder list is the index of the highest rated attribute

index = -1
counter = 0
while(counter<attributes):
#print(attributes_list[prefOrder[-3]])
    attributes_list[prefOrder[index]]
    index-=1
    counter+=1
    if(attributes_list[prefOrder[index]]=='location'):
        locatrion_list[counter][0]
    elif (attributes_list[prefOrder[index]] == 'flat_type'):
        flat_type_list[counter][0]
    elif (attributes_list[prefOrder[index]] == 'flat_furnishing'):
        flat_furnishing_list[counter][0]

# if(attributes_list[prefOrder[-1]]=='location'):
#     print(location_list[0][0])
# elif(attributes_list[prefOrder[-1]]=='flat_furnishing'):
#     print(flat_furnishing_list[0][0])
# elif(attributes_list[prefOrder[-1]]=='flat_type'):
#     print(flat_type_list[0][0])