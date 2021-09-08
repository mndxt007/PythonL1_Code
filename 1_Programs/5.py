#PES Python Assignments SET 1
#5 Python program Basics
#Python program -
##    Write a program to receive 5 command line arguments and print each argument separately.
##Example: >> python test.py arg1 arg2 arg3 arg4 arg5
##a) From the above statement your program should receive arguments and print them each of them. 
##b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

#Manoj Dixit - 20141404
#Python 3.9.0

from sys import argv

#reusing prog2 for greatest among 3

def checknum(num):
    if num.isnumeric() or num.replace('.','',1).isdigit():
        return True
    else:
        return False

def checkgreat():
    a=argv[1];b=argv[2];c=argv[3]
    if checknum(a) and checknum(b) and checknum(c):
        a=eval(a);b=eval(b);c=eval(c)
        if a>b:
            if a>c:
               print(a,'is greater than first 3 arguments')
            else:
                print(c, 'is greater than first 3 arguments')
        else:
            if b>c:
               print(b,'is greater than first 3 arguments')
            else:
                print(c, 'is greater than first 3 arguments')
    else:
        print('invalid arguments')

for i in range(1,len(argv)):
    print(argv[i])

checkgreat()

##Result:
##    C:\Users\mndxt\OneDrive\Study\Python\Topgear\SET1>python 5.py 23 25 33 43 50
##23
##25
##33
##43
##50
##33 is greater than first 3 arguments
##
##C:\Users\mndxt\OneDrive\Study\Python\Topgear\SET1>python 5.py 45 gttc 56 43 1111
##45
##gttc
##56
##43
##1111
##invalid arguments
##
##C:\Users\mndxt\OneDrive\Study\Python\Topgear\SET1>python 5.py 45 99 102.13 gttc python
##45
##99
##102.13
##gttc
##python
##102.13 is greater than first 3 arguments
