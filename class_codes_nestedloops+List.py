def main():
    x = [23, 19, 10, 28, 50]
    print('lenght: ', len(x))
    print(x[0], end = ' ')
    print(x[1], end = ' ')
    print(x[2], end = ' ')
    print(x[3], end = ' ')
    print(x[4], end = ' ')
    print(x[5]) #error index out of range

def main():
    x = [23, 19, 10, 28, 50]
    print('lenght: ', len(x))
    print(x[0], end = ' ')
    print(x[1], end = ' ')
    print(x[2], end = ' ')
    print(x[3], end = ' ')
    print(x[4], end = ' ')
    x[5] = 65 #error index out of range

from random import *
def main():
    x = [1]*10
    print('Length: ', len(x))
    for i in range(len(x)):
        x[i] = randint(10, 99)
        print(x[i], end = ' ')
    print()


main()

def main():
    length = int(input("Enter array length: "))
    x = [0]*length
    print('length: ', length)
    for i in range(length):
        x[i] = input('Enter any number:  ')
        print(x[i], end = ' ')
    print()

def main():
    length = randint(5, 10)
    x = [0]*length
    print('length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print(x[i], end = ' ')
    print()

main()

def main():
    length = randint(5, 10)
    x = [0]*length
    print('length: ', length)
    sum = 0
    for i in range(length):
        x[i] = randint(10, 99)
        print(x[i], end = ' ')
        sum = sum+x[i]
    average = sum/length
    print(f'\nAverage: {average:.2f}')
    for i in range(length):
        if x[i]>average:
            print(f'{x[i]} is greater than average')
        else:
            print(f'{x[i]} is less than equal to average')
main()

def main():
    length = randint(5, 10)
    x = [0]*length
    print('length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print(x[i], end = ' ')
        if i == 0:
            max = min = x[i]
        elif max<x[i]:
            max = x[i]
        elif min>x[i]:
            min = x[i]
    print(f'\nMax: {max}\t\tMin: {min}')
    for i in range(length):
            print(f'{x[i]} is {max-x[i]} less than max and {x[i]} is {x[i]-min} more than minimum')
main()
def main():
    length = randint(5, 10)
    x = [0]*length
    print ('Length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print (x[i], end = ' ')
        if i==0:            max = min = x[i];
        elif max < x[i]:    max = x[i];
        elif min > x[i]:    min = x[i];
    print(f'\nMax: {max}\t\tMin: {min}')
    for i in range(length):
        print (f'{x[i]} is {max-x[i]} less than max and {x[i]-min} more than min')
def main():
    length = randint(5,10)
    x = [0]*length
    print('Length: ', length)
    sum = 0
    for i in range(length):
        x[i] = randint(10, 99)
        print(x[i], end = ' ')
        sum = sum+x[i]
    average = sum/length
    print(f'\nAverage: {average:.2f}')
    sum = 0
    for i in range(length):
        sum = sum + (x[i] - average)**2
    print(f'Variance: {sum/length}')
    print(f'Standard Deviation: {(sum/length)**0.5}')

main()
            
