#PES Python Assignments SET 1
#7 Python program Basics
#Python program -
##Create a list with at least 10 elements having integer values in it;
##       Print all elements
##       Perform slicing operations
##       Perform repetition with * operator
##       Perform concatenation with other list.


#Manoj Dixit - 20141404
#Python 3.9.0

print('This is list 1')
list1=['list','is','Mutable','Heterogeneous','dynamic',"and","Extensible",123,55.5,True]

for item in list1:
    print(item)

list2=list1[5:]
print('\n*********************\nThis is list 2 with slicing list1[:7]')
for item in list2:
    print(item)

print('\n*********************\nThis is list1 multiplied 2\n',list1*2)

list3=list1+list2
print('\n*********************\nThis is concatination of list1 and list2\n',list3)


##This is list 1
##list
##is
##Mutable
##Heterogeneous
##dynamic
##and
##Extensible
##123
##55.5
##True
##
##*********************
##This is list 2 with slicing list1[:7]
##and
##Extensible
##123
##55.5
##True
##
##*********************
##This is list1 multiplied 2
## ['list', 'is', 'Mutable', 'Heterogeneous', 'dynamic', 'and', 'Extensible', 123, 55.5, True, 'list', 'is', 'Mutable', 'Heterogeneous', 'dynamic', 'and', 'Extensible', 123, 55.5, True]
##
##*********************
##This is concatination of list1 and list2
## ['list', 'is', 'Mutable', 'Heterogeneous', 'dynamic', 'and', 'Extensible', 123, 55.5, True, 'and', 'Extensible', 123, 55.5, True]
