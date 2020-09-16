#
#
import re

myLines = ""
counter = 0
counter2 = 0
with open('TextDoc1.txt', 'rt') as myFile:
    contents = myFile.read()
    for line in contents:
        myLines += line

    for x in range(0, len(myLines)):
        if myLines[x:x+12] == ("@outlook.com"):
            counter = counter+1

    print(counter)


    #for z in range(0, len(myLines)):
    z = re.compile("@softwire.com ")
    z.search(myLines)
    print(len(z.findall(myLines)))

    u = re.compile("@corndel.com ")
    u.search(myLines)
    print(len(u.findall(myLines)))

    myFile.close()

    lib = {}
    with open('TextDoc1.txt', 'rt') as f:
        counter = 0
        counter1 = 0
        counter2 = 0
        for line in f:
            key = line.split(':')
            value = re.findall("@\S+", line)
            print(value)

            for email in value:
                u = lib.get(email, 0)
                lib[email] = u + 1
                print(lib)

                print(lib.get("@gmail.com"))
                print(lib.get("@softwire.com"))
                print(lib.get("@outlook.com"))
                print(lib.get("@kiwimail.co.nz"))
                print(lib.get("@corndel.com"))
                print(lib.get("@yahoo.com"))
                print(lib.get("@swi.re"))
                print(lib.get("@my-email.net"))
                print(lib.get("@facebook.com"))
                print(lib.get("@softwire.comet.net"))
                print(lib.get("@aol.com"))
                print(lib.get("@yandex.ru"))
                print(lib.get("@hotmail.fr"))





























#counter = 0

#x = open("TextDoc1.txt")
#for y in 0 to :
    #print()




#print(x.read())