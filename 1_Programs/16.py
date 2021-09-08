#PES Python Assignments SET 1
#16 Python program Basics
#Python program Basics	-
##Write program to perform following:
##     i) Check whether given number is prime or not.
##    ii) Generate all the prime numbers between 1 to N where N is given number.


#Manoj Dixit - 20141404
#Python 3.9.0




def prime(a):
    count=0
    for i in range(2,int(a**0.5+1)): #iteratering only till square root of number to optimize time complexity
            if a%i==0:
                count+=1
            if count>=1:
                break
    if count>=1:
        return False
    else:
        return True


a=input('Please enter an integer : ')
try:
    a=int(a)
except:
    print('not an integer')
else:
    if a==1:
        print('1 is niether prime nor non prime')
    elif a==0:
        print('0 is niether prime nor non prime')
    else:
        if prime(a):
            print(a,'is a prime number')
        else:
            print(a,'is not a prime number')
    b=int(input('Enter a range to for all prime numbers to be printed: '))
    for j in range(2,b):
        if prime(j):
            print(j,end=' ')


##Result:
##    Please enter an integer : 9
##    9 is not a prime number
##    Enter a range to for all prime numbers to be printed: 111
##    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 
    
