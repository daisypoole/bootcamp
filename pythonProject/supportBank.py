import csv
import logging
import json




f = open('DodgyTransactions2015.csv')
csv_f = csv.reader(f)

v = input("Please type List All or List [Account]: ")

amount = {}
next(csv_f)
for row in csv_f:
    logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)


    if v == "List All":
        try:
            d = int(float(row[4]) * 100)

            amount[row[1]] = (amount.get(row[1], 0) - d)

            amount[row[2]] = (amount.get(row[2], 0) + d)

        except:
            logging.error('Error Occurence')
            logging.warning("Error while processing")



    elif v == "List[Todd]":
        if row[1] == "Todd" or row[2] == "Todd":
            #print(row[1])

            print("Transaction Date: ", row[0], ', ', "Account name: ", row[1], ', ', "Narrative: ", row[3])


    for name, balance in amount.items():
        print(name + ' = ' + str(balance / 100))














#with open('Transactions2014.csv') as csvfile:
    #fileReader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    #for row in fileReader:
        #for row in fileReader:
            #nameFrom = row['Narrative']
            #print(nameFrom)