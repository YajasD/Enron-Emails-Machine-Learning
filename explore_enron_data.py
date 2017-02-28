#!/usr/bin/python

""" 
    Code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

#Opens the data stored as pickle object
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print(enron_data)
print(len(enron_data)) #Finds the number of people, we have the data for.
print(enron_data['METTS MARK'])
poi_counter = 0

for key,value in enron_data.iteritems(): #Finds the number of 'PoIs'
    if enron_data[key]["poi"] == 1:
        poi_counter = poi_counter + 1


print(poi_counter)
#print(enron_data['COLWELL WESLEY']['poi'])
