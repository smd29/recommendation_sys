import random


def locationList(location,users):
    #location = ['Amanora Park Town','Magarpatta City','Hadapsar','Mundhwa']  #this is in main
    location_list = []
    #users = int(input("Print number of users: "))
    #location_list = []
    for x in range(users):
        location_list.append(random.sample(location,1)) ##1 denotes no f preferred locations
    print(location_list)


def flatType(flat_type,users):
    #flat_type = ['1BHK','2BHK', '3BHK', '4BHK']  #this is in main
    flat_type_list = []
    for x in range(users):
        flat_type_list.append(random.sample(flat_type,1))  ##1 denotes no of preferred flat types
    print(flat_type_list)
#flat_furnishing = ['Unfurnished','Semi-Furnished','Furnished']

def flatFurnishing(flat_furnishing,users):
    flat_furnishing_list = []
    for x in range(users):
        flat_furnishing_list.append(random.sample(flat_furnishing,1))
    print(flat_furnishing_list)
#print(location_list)
#print(flat_type_list)
#print(flat_furnishing_list)