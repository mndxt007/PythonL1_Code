#PES Python Assignments SET 1
#4 Python program Basics
#Python program - Write a program to find the number is Prime or not.
#Manoj Dixit - 20141404
#Python 3.9.0

while True:
    count=0
    a=input('Please enter an integer - ')
    try:
        a=int(a)
    except:
        print('not an integer')
        continue
    if a==1:
        print('1 is niether prime nor non prime')
    elif a==0:
        print('0 is niether prime nor non prime')
    else:
        for i in range(2,int(a**0.5+1)): #iteratering only till square root of number to optimize time complexity
            if a%i==0:
                count+=1
            #print('i',i,'count',count)
            if count>=1:
                break
        if count>=1:
            print(a,'is non prime number')
        else:
            print(a,'is prime number')

##Result:
##Please enter an integer - 0
##0 is niether prime nor non prime
##Please enter an integer - 1
##1 is niether prime nor non prime
##Please enter an integer - 2
##2 is prime number
##Please enter an integer - 3
##3 is prime number
##Please enter an integer - 4
##4 is non prime number
##Please enter an integer - 5
##5 is prime number
##Please enter an integer - 6
##6 is non prime number
##Please enter an integer - 7
##7 is prime number
##Please enter an integer - 8
##8 is non prime number
##Please enter an integer - 9
##9 is non prime number
##Please enter an integer - 10
##10 is non prime number
##Please enter an integer - 11
##11 is prime number
##Please enter an integer - 12
##12 is non prime number
##Please enter an integer - 13
##13 is prime number
##Please enter an integer - 99
##99 is non prime number
##Please enter an integer - 97
##97 is prime number
##Please enter an integer - 55
##55 is non prime number
##Please enter an integer - 57
##57 is non prime number
##Please enter an integer - 59
##59 is prime number
        
            
            
