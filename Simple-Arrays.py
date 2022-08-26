# 1 Find the largest and the smallest number in a given array.
#  2 Find the second largest number in the integer array.
#  3 Print array in reverse order.
#  4 Insert an element at the end of an array.
#  5 Merge two sorted arrays into a single sorted array.


array = [1, 2, 6, 3, 7, 1, 3]
array2 = [5, 6, 3, 6]

def largeSmall():
    array.sort()
    return array[0], array[-1]

def secondnumb():
    array.sort()
    return array[-2]

def reversed():
    array.reverse()
    return array

def elementAdd():
    while True:
        try:
            number = int(input("Please enter a number: \n"))
        except ValueError:
            print("Please only use numbers. Thank you.\n")
        else:
            break
    number = str(number)
    array.insert(len(array), number)
    array1 = list(map(int, array))
    return array1

def sorting():
    for i in array2:
        array.append(i)

    return array
