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

import pickle, math

#Opens the data stored as pickle object
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print(enron_data)
print(len(enron_data)) #Finds the number of people, we have the data for.
print(enron_data['METTS MARK'])
poi_counter = 0


for key,value in enron_data.iteritems(): #Finds the number of 'PoIs'.
    if enron_data[key]["poi"] == 1:
        poi_counter = poi_counter + 1

print("The number of POIs are" + " " + str(poi_counter))

poi_nan_counter = 0

for key,value in enron_data.iteritems(): #Finds the number of 'PoIs' that do not have total payments data in the dataset.
    if (enron_data[key]["poi"] == 1 and enron_data[key]["total_payments"] == 'NaN'):
        poi_nan_counter = poi_nan_counter + 1

print("The number of POIs with no total payments data are" + " " + str(poi_nan_counter))

salary_counter = 0

for k, v in enron_data.iteritems(): #Finds number of people with salary data in the dataset.
    if enron_data[k]['salary'] != 'NaN':
        salary_counter = salary_counter + 1

print("The number of guys with a defined salary are" + " " + str(salary_counter))

email_counter = 0

for k, v in enron_data.iteritems(): #Finds number of people with email data in the dataset
    if enron_data[k]['email_address'] != 'NaN':
        email_counter = email_counter + 1

print("The number of guys with a defined email address are" + " " + str(email_counter))

total_payments_counter = 0

for k, v in enron_data.iteritems(): #Finds number of people that do not have total payments data in the dataset.
    if enron_data[k]['total_payments'] == 'NaN':
        total_payments_counter = total_payments_counter + 1

print("The number of guys with invalid total payments data are" + " " + str(total_payments_counter))

print(poi_counter)
print(enron_data.keys())
print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])
