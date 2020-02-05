
import pandas as pd
import re
import csv

df = pd.read_csv('sample_email.csv', encoding='latin1')
list_number = []
list_email = []
for a in df.iterrows():
    email_str = "first_name: {0},last_name: {1}, company_name: {2},address:{3},city: {4},county: {5},state: {6},zip: {7},phone1: {8},phone: {9},email: {10},subject: {11},Email Boby: {12}"
    temp = a[1]
    email_str = email_str.format(temp['first_name'], temp['last_name'], temp['company_name'], temp['address'],
                                 temp['city'], temp['county'], temp['state'], temp['zip'], temp['phone1'],
                                 temp['phone'], temp['email'], temp['subject'], temp['Email Boby'] + '.')
    temp_number = re.findall('(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})',
                             temp['Email Boby'])
    if temp_number:
        list_number.append(temp_number[0])
    temp_email = re.findall('\S+@\S+', temp['Email Boby'])
    if temp_email:
        list_email.append(temp_email[0])

with open('number.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list_number)
with open('email.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list_email)
