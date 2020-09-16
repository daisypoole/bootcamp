def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        if num % 17 == 0:
            return 'BuzzFezzFizz'
        else:
            return 'FizzFezzBuzz'

    elif num % 7 == 0 and num % 5 == 0 and num % 3 == 0:
        if num % 17 == 0:
            return 'BangFezzFizz'
        else:
            return "FizzFezzBang"

    elif num % 7 == 0:
        if num % 17:
            return "BangFezz"
        else:
            return 'FezzBang'

    elif num % 11 == 0:
        if num % 17 == 0:
            return 'BongFezz'
        else:
            return 'FezzBong'

    elif num % 13 == 0:
        return 'Fezz'

    elif num % 5 == 0:
        if num % 17 == 0:
            return "BuzzFezz"
        else:
            return 'FezzBuzz'

    elif num % 5 == 0 and num % 13 == 0:
        if num % 17 == 0:
            return 'BuzzFezz'
        else:
            return 'FezzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    else:
        return num


if __name__ == "__main__":

    print ('Please Enter Number')
    x = input(int)
    x = int(x)
    for x in range (1,x):
        print(fizz_buzz(x))


    #for n in range(1, 300):
        #print(fizz_buzz(n))


    #for n in range(1,300):
        #print(fizz_buzz(n))