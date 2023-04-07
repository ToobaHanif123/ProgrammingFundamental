from random import *

###Task 01: Declare a list of 10 elements. Initialize elements at random (with any range of your choice). 
#Print elements in single line. Find and print average. Subtract all element from average. Print elements 
#again in single line. Next, count and print number of negative elements and number of positive elements.

def main():
    length = 10
    x = [0]*length
    print('Length: ', length)
    sum = 0
    for i in range(length):
        x[i] = randint(1, 50)
        print(x[i], end = ' ')
        sum = sum+x[i]
    average = sum/length
    print(f'\nAverage:{average:.2f}')
    for i in range(length):
        x[i] = x[i]-average
        print(f'{x[i]:.2f}', end = ' ')
    print()

    count1 = 0
    count2 = 0
    for i in range(length):
        if x[i] < 0:
            count1 = count1+1
        elif x[i] >= 0:
            count2 = count2+1
    print('Count of positive values: ', count2)
    print('Count of negative values: ', count1)
    
main()

###Task 02: Declare a list of 30 elements to store marks of 30 students of a class. Initialize elements at 
#random in range 1-100. The management is interested to divide students in three categories i.e. 
#failures, above average and below average. For this purpose, calculate average of passed students only. 
#Do following tasks in steps:
#- Initialize marks and print in single line
#- Print marks in a single line
#- count number of pass students (students with 50 or more marks are pass)
#- sum number of pass students
#- calculate and print average of pass students
#- Next, print marks of fail students in single line
#- Next, print marks of students with above averag

def main():
    length = 30
    marks = [0]*30
    print("Length: ", length)
    for i in range(length):
        marks[i] = randint(1, 100)
        print(marks[i], end = ' ')
    print()
    count = 0
    sum = 0
    print('Marks of passed students: ', end = ' ')
    for i in range(length):
        if marks[i] >= 50:
            count = count+1
            print(marks[i], end = ' ')
            sum = sum+marks[i]
    average = sum/count
    print('\nAverage: ', average)
    print('Marks of fail students: ', end = ' ')
    for i in range(length):
        if marks[i]<50:
            print(marks[i], end = ' ')
    print()
    print("Marks of Students with above average: ", end = ' ')
    for i in range(length):
        if marks[i]>average:
            print(marks[i], end = ' ')
    print()
    print("Marks of Students with below average: ", end = ' ')
    for i in range(length):
        if marks[i]<average:
            print(marks[i], end = ' ')
main()
        
        
    
