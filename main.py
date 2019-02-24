import eucledian_distance
import users_rating
#from math import sqrt
import random
#import matching_similarity
import user_preference_data
#import word_similarity
#import itertools

#consider location is the 1st attribute, flat_type is 2nd and flat_furnishing is 3rd
if __name__ == '__main__':
    users = int(input("Print number of users: "))
    attributes = 3 #as of now keeping it hard coded
    # existing_users_rating = [ [] for i in range(users)]
    # for i in existing_users_rating:
    #     for x in range(attributes):
    #         i.append(random.randint(0, 5))
    # print("The preference factors for the existing users are: " + str(existing_users_rating))  ##this user_list is the list of list

    # new_user_rating = []
    # for x in range(attributes):
    #     new_user_rating.append(random.randint(0,5))
    # print("The preference factors for the new user are: "+str(new_user_rating))

    existing_users_rating = users_rating.existingUser(users,attributes)
    new_user_rating = users_rating.newUser(attributes)

    location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
    flat_type = ['1BHK', '2BHK', '3BHK', '4BHK']
    flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']

    new_user_pref = []
    new_user_pref.append(random.sample(location,1))
    new_user_pref.append(random.sample(flat_type,1))
    new_user_pref.append(random.sample(flat_furnishing,1))

    print("\nThe preferred choices for the new user is:\n"+str(new_user_pref)+"\n")

    #calculate eucledian distance and mean
    eucledian_distance_list, mean, user_id = eucledian_distance.eucledian(existing_users_rating,new_user_rating)

    #find the similar user profiles

    #for debug Purpose
    #similar_user_id_list = eucledian_distance.simUser(eucledian_distance_list,mean)

    #sorted similar user list
    sorted_sim_user_list = eucledian_distance.sortedSimUser(eucledian_distance_list,mean)



    #users preference list
    # print("\nPreferred choices or selcted choice of the existing users:\n")
    # location_list = user_preference_data.locationList(location,users)
    # flat_type_list = user_preference_data.flatType(flat_type,users)
    # flat_furnishing_list = user_preference_data.flatFurnishing(flat_furnishing,users)



