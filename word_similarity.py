import user_preference_data


def locationSimilarity(locationList,new_user_pref):
    for i in range(len(locationList)):#(word_to_be_matched,word_list):
        if (locationList[i]==new_user_pref[0]):
            print(i)
