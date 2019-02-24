from math import sqrt
import random
import numpy as np
import itertools


def eucledian(existing_users_rating,new_user):
    eucledian_distance_list = []
    user_id = []
    for idx,val in enumerate(existing_users_rating):
        #print("abc"+str(np.array(existing_user[idx])))
        #print(existing_user[val])
        #print("elem is "+str(idx))
        dist = np.linalg.norm(np.array(existing_users_rating[idx])- np.array(new_user))
        eucledian_distance_list.append(dist)
        user_id.append(idx)
    print("User_id:"+str(user_id))
    #lesser eucledian distance means more similar
    print(eucledian_distance_list)

    ##mean calculation
    mean = np.mean(eucledian_distance_list)
    print(mean)

    return eucledian_distance_list,mean,user_id

def simUser(eucledian_distance_list,mean):
    #similar users profiles

    similar_user_id_list = []
    for i in range(len(eucledian_distance_list)):
        # print(np.array(existing_user[i]))
        if ((eucledian_distance_list[i]) <mean):
            similar_user_id_list.append(i)
    print("\nSimilar user ids are: "+str(similar_user_id_list))

    # if no similar user is found, it will consider the ratings of the user and perform accordingly
    if (not similar_user_id_list):
        print("\nNo similar user is found")
        ###consider the ratings of the users itself and display the result accordingly

    return similar_user_id_list

def sortedSimUser(eucledian_distance_list,mean):
    sorted_user_list = []
    #new_eucledian_list = sorted(eucledian_distance_list)
    #for i in range(len(similar_user_id_list)):
    sorted_sim_user_list = [i[0] for i in sorted(enumerate(eucledian_distance_list), key=lambda x: x[1])]
    for idx in range(len(sorted_sim_user_list)):
        if(eucledian_distance_list[sorted_sim_user_list[idx]]<mean):
            sorted_user_list.append(sorted_sim_user_list[idx])
    print("\nThe most similar(sorted) user profiles are: "+str(sorted_user_list))
    return sorted_user_list


# print("\nNo similar user is found")


# if __name__=='__main__':
#
#     # users = int(input("Print number of users: "))
#     # attributes = int(input("Enter number of attributes: "))
#     # existing_user = [ [] for i in range(users)]
#     # for i in existing_user:
#     #     for x in range(attributes):
#     #         i.append(random.randint(0,5))
#     # print("The preference factors for the existing users are: "+str(existing_user)) ##this user_list is the list of list
#     # new_user = []
#     # for x in range(attributes):
#     #     new_user.append(random.randint(0,5))
#     # print("The preference factors for the new user are: "+str(new_user))  ##new_user holds the preference ratings for the new user against the attributes
#     #
#     # eucledian_distance = []
#     # user_id = []
#
#     for idx,val in enumerate(existing_user):
#         #print("abc"+str(np.array(existing_user[idx])))
#         #print(existing_user[val])
#         #print("elem is "+str(idx))
#         dist = np.linalg.norm(np.array(existing_user[idx])- np.array(new_user))
#         eucledian_distance.append(dist)
#         user_id.append(idx)
#     print("User_id:"+str(user_id))
#     #lesser eucledian distance means more similar
#     print(eucledian_distance)
#
#     ##mean calculation
#     mean = np.mean(eucledian_distance)
#     print(mean)
#
#     similar_user_id_list = []
#     for i in range(len(eucledian_distance)):
#         #print(np.array(existing_user[i]))
#         if ((eucledian_distance[i]) > mean):
#             similar_user_id_list.append(i)
#     print(similar_user_id_list)
#
#     #if no similar user is found, it will consider the ratings of the user and perform accordingly
#     if(not similar_user_id_list):
#         #print("\nNo similar user is found")


