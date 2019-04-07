import eucledian_distance
import users_rating
# # from math import sqrt
import random
# # import matching_similarity
# import user_preference_data
# import word_similarity
# import itertools
import csv
import heapq

# consider location is the 1st attribute, flat_type is 2nd and flat_furnishing is 3rd
if __name__ == '__main__':
    Assigned_house = open(r"C:\Users\nEW u\Desktop\Recommendation system\Implementation\DataSet\Assigned_houses_updated.csv")
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
    for i in range(0,100): #as of now 100 is hard coded
        existing_users_rating.append([price_rating[i],location_rating[i],mode_of_sharing_rating[i],flat_type_rating[i]])


    preferred_choices = []
    for i in range(0,100):#as of now 100 is hard coded
        #preferred_choices.append([user_id[i],location[i],price[i],size[i],flat_type[i],flat_id[i]])
        preferred_choices.append([price[i],location[i],size[i],flat_type[i],flat_id[i]])
    print(preferred_choices)

    users = len(user_id)
    attributes = 4
    #print(users)


    #existing_users_rating = users_rating.existingUser(users, attributes)
    new_user_rating = users_rating.newUser(attributes)
    sorted_index_of_newUser_rating = heapq.nlargest(4, range(len(new_user_rating)), key=new_user_rating.__getitem__)
    print(sorted_index_of_newUser_rating)

    location = ['Amanora Park Town', 'Magarpatta City', 'Hadapsar', 'Mundhwa']
    flat_type = ['1BHK', '2BHK', '3BHK', '4BHK']
    flat_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']
    price = ['below 20k','20k-40k','40k-60k','60k-80k','80k-100k','more than 100k']

    new_user_pref = []
    new_user_pref.append(random.sample(price, 1))
    new_user_pref.append(random.sample(location,1))
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
    top_ten_sim_user_list = sorted_sim_user_list[:10]
    #print("Top 10 similar users are:\n"+str(top_ten_sim_user_list))

################################################

    for i in range(0,attributes):
        print(new_user_pref[sorted_index_of_newUser_rating[i]][0])
    #     #check if this value is similar for similar users or not

    for i in range(0,len(top_ten_sim_user_list)):
        print(preferred_choices[top_ten_sim_user_list[i]])

    final_recommendation=[]

    # for i in range(0,attributes):
    #     for j in range(0,len(top_ten_sim_user_list)):
    #         if(new_user_pref[sorted_index_of_newUser_rating[i]][0] == preferred_choices[top_ten_sim_user_list[j]]):
    #             final_recommendation.append(preferred_choices[top_ten_sim_user_list[j]][-1])

    print("Final recommendation generation")
    for i in range(0,attributes):
        for j in range(0,len(top_ten_sim_user_list)):
            if(new_user_pref[sorted_index_of_newUser_rating[i]][0] in preferred_choices[top_ten_sim_user_list[j]]):
                value = preferred_choices[top_ten_sim_user_list[j]][-1]
                if(value not in final_recommendation):
                    final_recommendation.append(value)
                #final_recommendation.append(preferred_choices[top_ten_sim_user_list[j]][-1])

    print(final_recommendation)
