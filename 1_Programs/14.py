#PES Python Assignments SET 1
#14 Python program Basics
#Python program Basics	-
##Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
##     a) Print all names on to screen
##     b) Read the index from the  user and print the corresponding name from both list.
##     c) Print the names from 4th position to 9th position
##     d) Print all names from 3rd position till end of the list
##     e) Repeat list elements by specified number of times (N- times, where N is entered by user)
##     f)  Concatenate two lists and print the output.
##     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
##



#Manoj Dixit - 20141404
#Python 3.9.0

A = [1001,1002,1003,2001,2003,3001,3005,3006,3007,3010]
B = ['Suraj','Manoj','Sai','Ranajit','Swati','Amogh','Uday','Vandana','Praveen','Ajay']

def func1(i):
    if i>-1 and i<10:
        print('Emp Id at index',i,'is',A[i],'with name',B[i])
    else:
        print('invalid index')

    print('***********************\n Printing 4th position to 9th position')

    for i in range(3,9):
        print('Index - ',i,',Emp Id - ',A[i],',Emp Name - ',B[i])

    print('***********************\n Printing 3rd position till end of list')

    for i in range(3,len(A)):
        print('Index - ',i,'Emp Name - ',B[i])

    i=int(input('Enter a value to repeat the list : '))

    print(A*i)

    print('A and B lists concatinated using + operator\n',A+B)

    for i in range(len(A)):
        print(A[i],',',B[i])
    

print('Below are all the names')

for item in B:
    print(item)

i=int(input('***************\nplease provide an index to print the Emp Id and Name (0-9) : '))
func1(i)



##Result:
##    Below are all the names
##    Suraj
##    Manoj
##    Sai
##    Ranajit
##    Swati
##    Amogh
##    Uday
##    Vandana
##    Praveen
##    Ajay
##    ***************
##    please provide an index to print the Emp Id and Name (0-9) : 4
##    Emp Id at index 4 is 2003 with name Swati
##    ***********************
##     Printing 4th position to 9th position
##    Index -  3 ,Emp Id -  2001 ,Emp Name -  Ranajit
##    Index -  4 ,Emp Id -  2003 ,Emp Name -  Swati
##    Index -  5 ,Emp Id -  3001 ,Emp Name -  Amogh
##    Index -  6 ,Emp Id -  3005 ,Emp Name -  Uday
##    Index -  7 ,Emp Id -  3006 ,Emp Name -  Vandana
##    Index -  8 ,Emp Id -  3007 ,Emp Name -  Praveen
##    ***********************
##     Printing 3rd position till end of list
##    Index -  3 Emp Name -  Ranajit
##    Index -  4 Emp Name -  Swati
##    Index -  5 Emp Name -  Amogh
##    Index -  6 Emp Name -  Uday
##    Index -  7 Emp Name -  Vandana
##    Index -  8 Emp Name -  Praveen
##    Index -  9 Emp Name -  Ajay
##    Enter a value to repeat the list : 2
##    [1001, 1002, 1003, 2001, 2003, 3001, 3005, 3006, 3007, 3010, 1001, 1002, 1003, 2001, 2003, 3001, 3005, 3006, 3007, 3010]
##    A and B lists concatinated using + operator
##     [1001, 1002, 1003, 2001, 2003, 3001, 3005, 3006, 3007, 3010, 'Suraj', 'Manoj', 'Sai', 'Ranajit', 'Swati', 'Amogh', 'Uday', 'Vandana', 'Praveen', 'Ajay']
##    1001 , Suraj
##    1002 , Manoj
##    1003 , Sai
##    2001 , Ranajit
##    2003 , Swati
##    3001 , Amogh
##    3005 , Uday
##    3006 , Vandana
##    3007 , Praveen
##    3010 , Ajay



      
