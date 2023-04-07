###Task 01: Write code to print adjacent pairs, which are in order (means first element is smaller than equal second element)
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print (x[i], end = ' ')
    print()
    for i in range(length-1):
        if x[i] <= x[i+1]:
            print('Adjacent Pairs:  ', x[i], x[i+1])
    print()
main()

##Task 02: Create another list of same size with random numbers. Compare corresponding elements of both lists and for each pair print larger element.
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    print('list1: ', end = ' ')
    for i in range(length):
        x[i] = randint(0, 100)
        print (x[i], end = ' ')
    y = [0]*length
    print('\nlist2: ', end = ' ')
    for i in range(length):
        y[i] = randint(0, 100)
        print (y[i], end = ' ')
    print()
    for i in range(length):
        if x[i] > y[i]: 
            print(x[i], end = ' ')
        else:
            print(y[i], end = ' ')
    print()
main()

###Task 03: Extend previous task. Compare corresponding elements of both lists and put smaller element in list 1 and larger elements in list 2 and print both lists again.
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    print('list1: ', end = ' ')
    for i in range(length):
        x[i] = randint(0, 100)
        print (x[i], end = ' ')
    y = [0]*length
    print('\nlist2: ', end = ' ')
    for i in range(length):
        y[i] = randint(0, 100)
        print (y[i], end = ' ')
    print()
    for i in range(length):
        if x[i] > y[i]: 
            x[i], y[i] = y[i], x[i]
    print()
    print('list1: ', end = ' ')
    for i in range(length):
        print (x[i], end = ' ')
    print('\nlist2: ', end = ' ')
    for i in range(length):
        print (y[i], end = ' ')
    print()
    
main()

###Task 04: For the list check and print, whether list is sorted or not. Note, you don’t have to sort, just check adjacent pairs, if all adjacent pairs are in order, the list will be in order.
from random import *
def is_sorted(x):
    sort = all(x[i] <= x[i+1] for i in range(len(x)-1))
    return sort

def main():
    length = randint(5, 15)
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print (x[i], end = ' ')
    print()
    if is_sorted(x):
        print('List is sorted')
    else:
        print('List is not Sorted')
    print()
main()
