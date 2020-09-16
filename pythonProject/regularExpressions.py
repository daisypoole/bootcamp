import re

myLines = ""
counter = 0
counter2 = 0
with open('TextDoc1.txt', 'rt') as myFile:
    contents = myFile.read()
    for line in contents:
        myLines += line

    z = re.compile("outlook.com")
    z.findall(myLines)
    print(len(z.findall(myLines)))
