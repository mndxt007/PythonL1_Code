#PES Python Assignments SET 1
#15 Python program Basics
#Python program Basics	-
##Create a list of 5 names and check given name exist in the List.
##        a) Use membership operator (IN) to check the presence of an element.
##        b) Perform above task without using membership operator.
##        c) Print the elements of the list in reverse direction.
##


#Manoj Dixit - 20141404
#Python 3.9.0

a = ['Suraj','Manoj','Sai','Ranajit','Swati']

print('Below is the list\n',a)

b=input('Please enter a string to check whether it exists in list : ')

if b in a:
    print(b,'Exists in the list (via IN operator)')
else:
    print(b,'Does not exist in the list')

b=input('Please enter a string to check whether it exists in list : ')

for i in range(len(a)):
    if a[i]==b:
        print(b,'Exists in the list (without membership operator)')
        break

a.reverse()
print('This is list reversed\n',a)

##Result:
##    Below is the list
##     ['Suraj', 'Manoj', 'Sai', 'Ranajit', 'Swati']
##    Please enter a string to check whether it exists in list : Manoj
##    Manoj Exists in the list (via IN operator)
##    Please enter a string to check whether it exists in list : Suraj
##    Suraj Exists in the list (without membership operator)
##    This is list reversed
##     ['Swati', 'Ranajit', 'Sai', 'Manoj', 'Suraj']


    
