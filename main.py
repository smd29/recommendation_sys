import eucledian_distance
import users_rating
# # from math import sqrt
import random
# # import matching_similarity
# import user_preference_data
# import word_similarity
# import itertools
import csv

# consider location is the 1st attribute, flat_type is 2nd and flat_furnishing is 3rd
if __name__ == '__main__':
    Assigned_house = open(r"C:\Users\nEW u\Desktop\Recommendation system\Implementation\DataSet\Assigned_houses.csv")
    csv_f = csv.reader(Assigned_house)

    rating_dataset =  open(r"C:\Users\nEW u\Desktop\Recommendation system\Implementation\DataSet\rating.csv")
    csv_rating = csv.reader(rating_dataset)

    user_id = []
    price = []
    location = []
    size = []
    flat_type = []
    flat_id = []
    # users = sum(1 for row in Assigned_house)
    # print(users)
    for column in csv_f:
        user_id.append(column[0])
        location.append(column[1])
        price.append(column[2])
        size.append(column[3])
        flat_type.append(column[4])
        flat_id.append(column[5])
    # print(size)
    price.remove('Price')
    location.remove('Location ')
    size.remove('Size')
    flat_type.remove('type')
    flat_id.remove('Flat id')
    user_id.remove('User')

    userID_rating = []
    price_rating = []
    location_rating = []
    mode_of_sharing_rating = []
    flat_type_rating = []

    for column in csv_rating:
        #userID_rating.append(column[0])
        price_rating.append(column[1])
        location_rating.append(column[2])
        mode_of_sharing_rating.append(column[3])
        flat_type_rating.append(column[4])
    price_rating.remove('Price')
    location_rating.remove('Location')
    mode_of_sharing_rating.remove('Mode_of_Sharing')
    flat_type_rating.remove('Flat_type')

    existing_users_rating = []
    for i in range(0,100):
        existing_users_rating.append([price_rating[i],location_rating[i],mode_of_sharing_rating[i],flat_type_rating[i]])
    


    users = len(user_id)
    attributes = 4
    #print(users)


    #existing_users_rating = users_rating.existingUser(users, attributes)
    new_user_rating = users_rating.newUser(attributes)

    location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
    flat_type = ['1BHK', '2BHK', '3BHK', '4BHK']
    flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']

    new_user_pref = []
    new_user_pref.append(random.sample(location, 1))
    new_user_pref.append(random.randint(7000,150000))
    new_user_pref.append(random.sample(flat_type, 1))
    new_user_pref.append(random.sample(flat_furnishing, 1))

    print("\nThe preferred choices for the new user is:\n" + str(new_user_pref) + "\n")

        # calculate eucledian distance and mean
    eucledian_distance_list, mean, user_id = eucledian_distance.eucledian(existing_users_rating, new_user_rating)
    #
    #     # find the similar user profiles
    #
    #     # for debug Purpose
    #     # similar_user_id_list = eucledian_distance.simUser(eucledian_distance_list,mean)
    #
    #     # sorted similar user list
    sorted_sim_user_list = eucledian_distance.sortedSimUser(eucledian_distance_list, mean)
    #
    #     # users preference list
    #     ########THIS IS FOR GENRATING THE USER PREFEREENCES SO THAT WE CAN ASSIGN THE TRAINING USERS TO A FLAT################
    # print("\nPreferred choices or selcted choice of the existing users:\n")
    # location_list = user_preference_data.locationList(location, users)
    # flat_type_list = user_preference_data.flatType(flat_type, users)
    # flat_furnishing_list = user_preference_data.flatFurnishing(flat_furnishing, users)