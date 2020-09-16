import csv
import logging
import json
import xml.etree.ElementTree as ET



def transactions():
    f = open('Transactions2014.csv')
    csv_f = csv.reader(f)

    v = input("Please type List All or List [Account]: ")

    amount = {}
    tran = []
    next(csv_f)
    for row in csv_f:
        logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)


        if v == "List All":
            try:
                d = int(float(row[4]) * 100)

                amount[row[1]] = (amount.get(row[1], 0) - d)

                amount[row[2]] = (amount.get(row[2], 0) + d)

                tran.append(row)

            except:
                logging.error('Error Occurence')
                logging.warning("Error while processing")



        elif v == "List[Todd]":
            if row[1] == "Todd" or row[2] == "Todd":
                    #print(row[1])

            print("Transaction Date: ", row[0], ', ', "Account name: ", row[1], ', ', "Narrative: ", row[3])


        for name, balance in amount.items():
            print(name + ' = ' + str(balance / 100))

print(transactions())


def chooseFile():
    t = input("Please enter the file name you would like to view: ")
    #Opening a JSON File
    if t == "Transactions2013.json":
        with open('Transactions2013.json', 'r') as openFile:

            #Read from JSON file
            json_object = json.load(openFile)

            print(json_object)
            print(type(json_object))

    elif t == "Dodgy Transactions 2015.csv":
        CSVFile = open('DodgyTransactions2015.csv')
        csv_o = csv.reader(CSVFile)

        for line in csv_o:
         print(line)

print(chooseFile())

tree = ET.parse('Transactions2012.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)


















#with open('Transactions2014.csv') as csvfile:
    #fileReader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    #for row in fileReader:
        #for row in fileReader:
            #nameFrom = row['Narrative']
            #print(nameFrom)