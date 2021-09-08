#PES Python Assignments SET 1
#13 Python program Basics
#Python program Basics	-
##Write a program to find the biggest of 4 numbers.
##   a) Read 4 numbers from user using Input statement.
##   b) extend the above program to find the biggest of 5 numbers.
##(PS: Use IF and IF & Else, If and ELIf, and Nested IF)



#Manoj Dixit - 20141404
#Python 3.9.0

a=input('Please enter 4 numbers delimated by space:\n')
b=a.rsplit(' ')
big=0
#find avg
for item in b:
    if item.isnumeric() or item.replace('.','',1).isdigit(): #to check whether the current number is valid or not
        item=eval(item)
        if item>big:
            big=item
    else:
        print(item,'is invalid')

print(big,'is greater than all given numbers')

a=input('Please enter 5 numbers delimated by space:\n')
b=a.rsplit(' ')
big=0
#find avg
for item in b:
    if item.isnumeric() or item.replace('.','',1).isdigit(): #to check whether the current number is valid or not
        item=eval(item)
        if item>big:
            big=item
    else:
        print(item,'is invalid')

print(big,'is greater than all given numbers')

##Result:
##    Please enter 4 numbers delimated by space:
##    7 8 9 2
##    9 is greater than all given numbers
##    Please enter 5 numbers delimated by space:
##    11.0 6 11.1 22.3 22.2
##    22.3 is greater than all given numbers
