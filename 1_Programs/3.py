#PES Python Assignments SET 1
#3 Python program Basics
#Python program - Write a program to find given number is odd or Even
#Manoj Dixit - 20141404
#Python 3.9.0

while True:
    a=input('Please enter an integer - ')
    try:
        a=int(a)
    except:
        print('not an integer')
        continue
    if a%2==0:
        print(a,'is an even number')
    else:
        print(a,'is an odd number')
        
        
##Results
##
##Please enter an integer - 4
##4 is an even number
##Please enter an integer - 6
##6 is an even number
##Please enter an integer - 5
##5 is an odd number
##Please enter an integer - 1
##1 is an odd number
##Please enter an integer - 8
##8 is an even number
##Please enter an integer - 0
##0 is an even number
##Please enter an integer - 2
##2 is an even number
##Please enter an integer - 11
##11 is an odd number
##Please enter an integer - 11
##11 is an odd number
##Please enter an integer - 11111
##11111 is an odd number
##Please enter an integer - 1.5
##not an integer
