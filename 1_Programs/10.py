#PES Python Assignments SET 1
#10 Python program Basics
#Python program Basics	-
##Using assignment operators, perform following operations
#Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations

#Manoj Dixit - 20141404
#Python 3.9.0

while True:
    a=input('Enter number 1- ')
    if a.isnumeric() or a.replace('.','',1).isdigit(): #for checking if its a valid number
        b=input('Enter number 2- ')
        if b.isnumeric() or b.lstrip('-').replace('.','',1).isdigit():
            a=eval(a)
            b=eval(b)
            print('Addition of',a,'and',b,'=',a+b)
            print('Substraction of',a,'and',b,'=',a-b)
            print('Multiplication of',a,'and',b,'=',a*b)
            print('Division of',a,'and',b,'=',a/b)
            print('Modulus of',a,'and',b,'=',a%b)
            print('Exponent of',a,'and',b,'=',a**b)
            print('Floor division of',a,'and',b,'=',a//b)
        else:
            print('Invalid number')
    else:
        print('Invalid number')


##Result
##    Enter number 1- 7.0
##    Enter number 2- 2.0
##    Addition of 7.0 and 2.0 = 9.0
##    Substraction of 7.0 and 2.0 = 5.0
##    Multiplication of 7.0 and 2.0 = 14.0
##    Division of 7.0 and 2.0 = 3.5
##    Modulus of 7.0 and 2.0 = 1.0
##    Exponent of 7.0 and 2.0 = 49.0
##    Floor division of 7.0 and 2.0 = 3.0
##    Enter number 1- 7
##    Enter number 2- 2
##    Addition of 7 and 2 = 9
##    Substraction of 7 and 2 = 5
##    Multiplication of 7 and 2 = 14
##    Division of 7 and 2 = 3.5
##    Modulus of 7 and 2 = 1
##    Exponent of 7 and 2 = 49
##    Floor division of 7 and 2 = 3
