import csv
import logging
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

class BootCamp:
    def transactionsThree(self, tran):

        v = input("Please type List All, List [Account]: ")

        amount = {}

        for row in tran:
            try:
                d = int(float(row[4]) * 10)
                amount[row[1]] = (amount.get(row[1], 0) - d)
                amount[row[2]] = (amount.get(row[2], 0) + d)
            except:
                logging.error('Error Occurence')
                logging.warning("Error while processing")

        if v == "List All":
            for name, balance in amount.items():
                print(name + ' = ' + str(balance/100))

        elif v == "List[Todd]":
            for row in tran:
                if row[1] == "Todd" or row[2] == "Todd":
                    print("Transaction Date: ", row[0], ', ', "Account name: ", row[1], ', ', "Narrative: ", row[3])

        for name, balance in amount.items():
            print(name + ' = ' + str(balance / 100))


        return(tran)
    #print(transactions(self))


    def transactions(self):
        f = open('Transactions2014.csv')
        csv_f = csv.reader(f)

        v = input("Please type List All, List [Account]: ")

        amount = {}
        tran = []

        next(csv_f)
        for row in csv_f:
            try:
                d = int(float(row[4]) * 10)
                amount[row[1]] = (amount.get(row[1], 0) - d)
                amount[row[2]] = (amount.get(row[2], 0) + d)
                tran.append(row)
            except:
                logging.error('Error Occurence')
                logging.warning("Error while processing")

        if v == "List All":
            for name, balance in amount.items():
                print(name + ' = ' + str(balance/100))

        elif v == "List[Todd]":
            for row in tran:
                if row[1] == "Todd" or row[2] == "Todd":
                    print("Transaction Date: ", row[0], ', ', "Account name: ", row[1], ', ', "Narrative: ", row[3])


        for name, balance in amount.items():
            print(name + ' = ' + str(balance / 100))


        return(tran)
    #print(transactions(self))


    def chooseFile(self):
        t = input("Please enter the file name you would like to view: ")

        #list to store values
        listJ = []
        # Opening a JSON File
        if t == "Transactions2013.json":
            with open('Transactions2013.json', 'r') as openFile:

            #Read from JSON file
                json_object = json.load(openFile)

            for row in json_object:
                jsonRow = [row['date'], row['fromAccount'], row['toAccount'], row['narrative'], row['amount']]
                listJ.append(jsonRow)
                print(listJ)

        elif t == "Dodgy Transactions 2015.csv":
            CSVFile = open('DodgyTransactions2015.csv')
            csv_o = csv.reader(CSVFile)

            for line in csv_o:
                #csvRow = ['Date', line[0], 'From', line[1], 'To', line[2], 'Narrative', line[3], 'Amount', line[4]]
                csvRow = line
                listJ.append(csvRow)
                print(listJ)

        elif t == "Transactions2012.xml":
            tree = ET.parse('Transactions2012.xml')
            root = tree.getroot()

            for transaction in root:
                row = ['', '', '', '', '']

                excelDate = int(transaction.attrib['Date'])
                date = datetime(1900, 1, 1) + timedelta(days=excelDate - 2)
                row[0] = date

                for element in transaction:
                    if element.tag == 'Description':
                        row[3] = element.text

                    elif element.tag == 'Value':
                        row[4] = element.text

                    elif element.tag == 'Parties':
                        for parties in element:
                            if parties.tag == 'From':
                                row[1] = parties.text
                            elif parties.tag == 'To':
                                row[2] = parties.text

                listJ.append(row)

        return(listJ)

bootCamp = BootCamp()
bOne = bootCamp.transactions()
bTwo = bootCamp.chooseFile()

bThree = bOne+bTwo
print(bThree)

bootCamp.transactionsThree(bThree)


















#with open('Transactions2014.csv') as csvfile:
    #fileReader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
    #for row in fileReader:
        #for row in fileReader:
            #nameFrom = row['Narrative']
            #print(nameFrom)