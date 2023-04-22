

# import csv
#
# # read the data with csv into list 'pop'
# pop = []
# with open ('Walmart.csv', 'r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#
#     for row in csv_reader:
#         pop.append(row)
#
# # print the first 5 rows of the table (5 first elements of the list)
# for row in range(0,5):
#     print(pop[row])


import csv

with open('Walmart.csv', "r") as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    maxVal = []
    for i in data:
        maxVal.append(i[:])
print(max(maxVal))


# using pandas
import pandas as pd
df=pd.read_csv("Walmart.csv")
p1=df.max()
print(p1)