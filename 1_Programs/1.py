#PES Python Assignments SET 1
#1 Python program Basics
#Python program Basics	Write a program to Add, Subtract, Multiply, and Divide 2 numbers
#Manoj Dixit - 20141404
#Python 3.9.0


while True:
    a=input("Please enter the first number/or complete expression in the format a+b  - ")
    if not (a.isnumeric() or a.replace('.','',1).isdigit()): #for checking whether its a valid number
        if (a.find('+')>0) or (a.find('-')>0) or (a.find('*')>0) or (a.find('/')>0):
            try:
                print(eval(a))
            except Exception as msg:
                print(msg)
                continue
        else:
            print('Expression not supported')
            continue
    else:
        b=input("Please enter operator - ")
        if b in {'+','-','*','/'}:
            oper=a+b+input("Please enter 2nd number - ")
            try:
                print(eval(oper))
            except Exception as msg:
                print(msg)
                continue
        else:
            print('Operator invalid')
            continue

## Results
        #Supports both int and float as arguments
        #Supports expression input or operand and operator input one by one
        #Exceptions handled
        
#***********Integer operation*************************************
##Please enter the first number/or complete expression in the format a+b  - 22
##Please enter operator - +
##Please enter 2nd number - 2
##24
##Please enter the first number/or complete expression in the format a+b  - 22
##Please enter operator - -
##Please enter 2nd number - 2
##20
##Please enter the first number/or complete expression in the format a+b  - 22
##Please enter operator - *
##Please enter 2nd number - 2
##44
##Please enter the first number/or complete expression in the format a+b  - 22
##Please enter operator - /
##Please enter 2nd number - 2
##11.0
        
#***********Float operation*************************************
##Please enter the first number/or complete expression in the format a+b  - 22.2
##Please enter operator - /
##Please enter 2nd number - 2
##11.1
        
#***********Expression input*************************************
##Please enter the first number/or complete expression in the format a+b  - 22.2+2
##24.2
##Please enter the first number/or complete expression in the format a+b  - 22*0.2
##4.4
##Please enter the first number/or complete expression in the format a+b  - -3.4+2
##-1.4
        
#***********Exception Handling*************************************
##Please enter the first number/or complete expression in the format a+b  - 22.2,2
##Expression not supported
##Please enter the first number/or complete expression in the format a+b  - 34
##Please enter operator - &
##Operator invalid
