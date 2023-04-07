from random import *
def main():
    length = randint(5, 10)
    x = [0]*length
    Sum = 0
    print('Length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print(x[i], end = " ")
        Sum += x[i]
    average = Sum/length
    print(f'\nAverage: {average:.2f}')
    print('Values less than average: ', end = ' ')
    for i in range(length):
        if x[i]<average:
            print(x[i], end = ' ')
    print('\nValues greater than average: ', end = ' ')
    for i in range(length):
        if x[i]>average:
            print(x[i], end = ' ')
    print()
main()

def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i], end = ' ')
    print()
    for i in range(length-1):
        if x[i]>x[i+1]:
            print(f'{x[i]} is greater than {x[i+1]}')
        else:
            print(f'{x[i]} is less than {x[i+1]}')
main()

#Compare all elements with their left and right neighbors and if element is larger from left neighbor and smaller than
#right neighbor, print element is in order otherwise print element is out of order             
        
def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i], end = ' ')
    print()
    for i in range(1, length-1):
        if x[i]<x[i+1] and x[i]>x[i-1]:
            print(f'{x[i]} is in order')
        else:
            print(f'{x[i]} is out of order')
main()

#For all adjacent pairs if first element is larger than second element swap them
def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(10, 500)
        print(x[i], end = ' ')
    print()
    for i in range(length-1):
        if x[i]>x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
    for i in range(length):
        print(x[i], end = ' ')

main()

#Write bubble sort code by swapping first larger element in the pair with its right neighbor
def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(10, 500)
        print(x[i], end = ' ')
    print()
    for j in range(length-1):
        for i in range(length-1):
            if x[i]>x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        print()
        for i in range(length):
            print(x[i], end = ' ')
    print()

main()
def find_min_element(x):
    for i in range(len(x)):
        if i == 0:
            min_element = x[0]
        elif min_element > x[i]:
            min_element = x[i]
    return min_element
def find_min_index(x):
    for i in range(len(x)):
        if i == 0:
            min_index = 0
        elif x[min_index]>x[i]:
            min_index = i
    return min_index

def find_min_index2(x, start, end):
    for i in range(start, end):
        if i == start:
            min_index = start
        elif x[min_index] > x[i]:
            min_index = i
    return min_index

def find_max_index2(x, start, end):
    for i in range(start, end):
        if i == start:
            max_index = start
        elif x[max_index] < x[i]:
            max_index = i
    return max_index   
         
def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i], end = ' ')
    print('\nPosition of minimum element is: ', find_min_index(x), 'and the minimum element is: ', find_min_element(x))

main()  

def main():
    length = 10
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i], end = ' ')
    print('\nminimum index is: ', find_min_element(x))
    print()

main()  

def main():
    length = 20
    x = [0]*length
    for i in range(length):
        x[i] = randint(10, 50)
        print(x[i], end = ' ')
    print('\nminimum index from index 0 to 5: ', find_min_index2(x, 0, 5))
    print('\nminimum index from index 6 to 10: ', find_min_index2(x, 6, 10))
    print('\nminimum index from index 11 to 15: ', find_min_index2(x, 11, 15))
    print('\nminimum index from index 16 to 20: ', find_min_index2(x, 16, 20))
    print('\nminimum index from the array: ', find_min_index(x))
main()

###########Selection Sort#################
def main():
    length = 25
    x = [0]*length
    for i in range(length):
        x[i] = randint(10, 90)
        print(x[i], end = ' ')
    print()
    for i in range(length-1):
        for j in range(length-1):
            min_index = find_min_index2(x, j, length)
            x[j], x[min_index] = x[min_index], x[j]
    for i in range(length):
        print(x[i], end = ' ')
main()

def main():
    length = 25
    x = [0]*length
    for i in range(length):
        x[i] = randint(10, 90)
        print(x[i], end = ' ')
    print()
    for i in range(length-1):
        for j in range(length-1, 0, -1):
            max_index = find_max_index2(x, 0, j+1)
            x[j], x[max_index] = x[max_index], x[j]
    for i in range(length):
        print(x[i], end = ' ')
    print()
main()


