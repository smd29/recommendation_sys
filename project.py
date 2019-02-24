from math import sqrt
import random
import numpy as np
import itertools


if __name__=='__main__':
    # plot1 = [1,3]
    # print(plot1)
    # plot2 = [2,5]
    # eucledian_dist = sqrt((plot1[0]-plot2[0])**2+(plot1[1]-plot2[1])**2)
    # print(numpy.linalg.norm(plot1-plot2))
    # print(eucledian_dist)
    users = int(input("Print number of users: "))
    attributes = int(input("Enter number of attributes: "))
    existing_user = [ [] for i in range(users)]
    for i in existing_user:
        for x in range(attributes):
            i.append(random.randint(0,5))
    print("The preference factors for the existing users are: "+str(existing_user)) ##this user_list is the list of list
    new_user = []
    for x in range(attributes):
        new_user.append(random.randint(0,5))
    print("The preference factors for the new user are: "+str(new_user))  ##new_user holds the preference ratings for the new user against the attributes

    eucledian_distance = []
    user_id = []

    for idx,val in enumerate(existing_user):
        #print("abc"+str(np.array(existing_user[idx])))
        #print(existing_user[val])
        #print("elem is "+str(idx))
        dist = np.linalg.norm(np.array(existing_user[idx])- np.array(new_user))
        eucledian_distance.append(dist)
        user_id.append(idx)
    print("User_id:"+str(user_id))
    #lesser eucledian distance means more similar
    print(eucledian_distance)

    ##mean calculation
    mean = np.mean(eucledian_distance)
    print(mean)

    similar_user_id_list = []
    for i in range(len(eucledian_distance)):
        #print(np.array(existing_user[i]))
        if ((eucledian_distance[i]) > mean):
            similar_user_id_list.append(i)
    print(similar_user_id_list)

    #if no similar user is found, it will consider the ratings of the user and perform accordingly
    if(not similar_user_id_list):
        #print("\nNo similar user is found")


