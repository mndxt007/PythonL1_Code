#PES Python Assignments SET 1
#2 Python program Basics
#Python program Basics	- Write a program to find the biggest of 3 numbers (Use If Condition)
#Manoj Dixit - 20141404
#Python 3.9.0

while True:
    a=input('Enter number 1- ')
    if a.isnumeric() or a.replace('.','',1).isdigit(): #for checking if its a valid number
        b=input('Enter number 2- ')
        if b.isnumeric() or b.replace('.','',1).isdigit():
            c=input('Enter number 3- ')
            if c.isnumeric() or c.replace('.','',1).isdigit():
                if a>b:
                    if a>c:
                       print(a,'is greater than all')
                    else:
                        print(c, 'is greater than all')
                else:
                    if b>c:
                       print(b,'is greater than all')
                    else:
                        print(c, 'is greater than all')
            else:
                print('invalid number')
                continue
        else:
            print('invalid number')
            continue
    else:
        print('invalid number')
        continue
                    
##Results
##    Support comparision of both int and float values
##
##Enter number 1- 5
##Enter number 2- 6
##Enter number 3- 3
##6 is greater than all
##Enter number 1- 3
##Enter number 2- 3.1
##Enter number 3- 2
##3.1 is greater than all
##Enter number 1- 2
##Enter number 2- 2
##Enter number 3- 2
##2 is greater than all
##Enter number 1- 3
##Enter number 2- 6
##Enter number 3- 4
##6 is greater than all
        
    
