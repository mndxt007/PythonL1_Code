#PES Python Assignments SET 1
#16 Python program Basics
#Python program Basics	-
##Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
##a) By using For loop 
##b) By using while loop
##c) Let mystring ="Hello world"
##print each character of mystring in to separate line using appropriate loop structure.

#Manoj Dixit - 20141404
#Python 3.9.0


print('**********Printing 1 to 100 using for loop')
for i in range(100):
    print(i+1,end=' ')

print('\n*********Printing 100 to 1 using for loop')
for i in range(100,0,-1):
    print(i,end=' ')

print('\n*********Printing 1 to 100 using While loop')
a=iter(range(100))
while True:
    try:
        print(next(a)+1,end=' ')
    except Exception:
        break

print('\n*********Printing 100 to 1 using While loop')
a=iter(range(100,0,-1))
while True:
    try:
        print(next(a),end=' ')
    except Exception:
        break
    
mystring ="Hello world"
print('\n**********Printing each charater from mystring variable')
for item in mystring:
    print(item)

##Result:
##    **********Printing 1 to 100 using for loop
##    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 
##    *********Printing 100 to 1 using for loop
##    100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
##    *********Printing 1 to 100 using While loop
##    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 
##    *********Printing 100 to 1 using While loop
##    100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
##    **********Printing each charater from mystring variable
##    H
##    e
##    l
##    l
##    o
##     
##    w
##    o
##    r
##    l
##    d
