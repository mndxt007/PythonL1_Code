#PES Python Assignments SET 1
#19 Python program Basics
#Python program Basics	-
##Using loop structures print even numbers between 1 to 100.  
##a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
##    i) Break the loop if the value is 50
##    ii) Use continue for the values 10,20,30,40,50
##      b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
##      i) Break the loop if the value is 90
##      ii) Use continue for the values 60,70,80,90



#Manoj Dixit - 20141404
#Python 3.9.0

print('Using for loop')
for i in range(1,101):
    if i==50:
        break
    elif i in (10,20,30,40,50):
        continue
    else:
        if i%2==0:
            print(i,end=' ')
        else:
            pass

a=iter(range(1,101))
print('\nUsing while loop')
while True:
    i=next(a)
    if i==90:
        break
    elif i in (60,70,80,90):
        continue
    else:
        if i%2==0:
            print(i,end=' ')
        else:
            pass

##Result:
        ##Using for loop
        ##2 4 6 8 12 14 16 18 22 24 26 28 32 34 36 38 42 44 46 48 
        ##Using while loop
        ##2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 62 64 66 68 72 74 76 78 82 84 86 88 
