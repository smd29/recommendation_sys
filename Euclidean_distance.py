from math import sqrt
import random
import numpy as np
import pandas as pd
import itertools
import csv

from google.colab import files
uploaded=files.upload()


#generating random user ratings
user_rating=[]
for i in range(1,5):
  user= random.randint(0,5)
  user_rating.append(user)

print(user_rating)

#opening the csv file containg data on the existing user
f = open('rating.csv')
csv_f = csv.reader(f)
price=[]
location=[]
mode_of_sharing=[]
flat_type=[]


#storing each attribute values in different values for later use
for column in csv_f:
  price.append(column[1])
  location.append(column[2])
  mode_of_sharing.append(column[3])
  flat_type.append(column[4])
  
print(price)
print(location)
print(mode_of_sharing)
print(flat_type)

price.remove('Price')
location.remove('Location')
mode_of_sharing.remove('Mode_of_Sharing')
flat_type.remove('Flat_type')

existing_user=[]
for i in range(0,100):
  existing_user.append([price[i],location[i],mode_of_sharing[i],flat_type[i]])

print(existing_user)


#measuring the euclidean distance

euclidean_dist=[]
user_id=[]
for idx,val in enumerate(existing_user):
  dist = np.linalg.norm(np.array(pd.to_numeric(existing_user[idx]))- np.array(pd.to_numeric(user_rating)))
  euclidean_dist.append(dist)
  user_id.append(idx)

print(euclidean_dist)

mean= np.mean(euclidean_dist)

print(mean)

#finding out similar user indexes

similar_user=[]
user_idx=0
for dist in euclidean_dist:
  user_idx=user_idx+1
  if(dist<mean):
    similar_user.append(user_idx)

print(similar_user)
