import random

def existingUser(users,attributes):
    existing_users_rating = [[] for i in range(users)]
    for i in existing_users_rating:
        for x in range(attributes):
            i.append(random.randint(0, 5))
    print("The preference factors for the existing users are: " + str(existing_users_rating))  ##this user_list is the list of list
    return existing_users_rating

def newUser(attributes):
    new_user_rating = []
    for x in range(attributes):
        new_user_rating.append(random.randint(0, 5))
    print("The preference factors for the new user are: " + str(new_user_rating))
    return new_user_rating