#PES Python Assignments SET 1
#8 Python program Basics
#Python program -
##Repeat program 7 with Tuples (Take example from Tutorial)


#Manoj Dixit - 20141404
#Python 3.9.0

print('This is Tuple 1')
tup1=('tuple','is','Not mutable','Heterogeneous','can','be indexed',123,55.5,True)

for item in tup1:
    print(item)

tup2=tup1[5:]
print('\n*********************\nThis is Tuple 2 with slicing Tuple 1[:7]')
for item in tup2:
    print(item)

print('\n*********************\nThis is Tuple multiplied 2\n',tup1*2)

tup3=tup1+tup2
print('\n*********************\nThis is concatination of Tuple1 and Tuple2\n',tup3)

input('Press any key to continue')

##Result:
##    This is Tuple 1
##    tuple
##    is
##    Not mutable
##    Heterogeneous
##    can
##    be indexed
##    123
##    55.5
##    True
##
##    *********************
##    This is Tuple 2 with slicing Tuple 1[:7]
##    be indexed
##    123
##    55.5
##    True
##
##    *********************
##    This is Tuple multiplied 2
##     ('tuple', 'is', 'Not mutable', 'Heterogeneous', 'can', 'be indexed', 123, 55.5, True, 'tuple', 'is', 'Not mutable', 'Heterogeneous', 'can', 'be indexed', 123, 55.5, True)
##
##    *********************
##    This is concatination of Tuple1 and Tuple2
##     ('tuple', 'is', 'Not mutable', 'Heterogeneous', 'can', 'be indexed', 123, 55.5, True, 'be indexed', 123, 55.5, True)
##    Press any key to continue
