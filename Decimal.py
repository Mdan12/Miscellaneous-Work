def octal():

    while True:
        try:
            number = int(input("Please enter a number: \n"))
        except ValueError:
            print("Please only use numbers. Thank you.\n")
        else:
            break
    list = []

    while (number != int(number/8)):
        list.append(number%8)
        number = int(number/8)
        if number - int(number/8) == 0:
            break

    list.reverse()
    list_correct = (''.join(map(str,list)))
    return list_correct

print (octal())
