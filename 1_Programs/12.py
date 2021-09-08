#PES Python Assignments SET 1
#12 Python program Basics
#Python program Basics	-
##Read 10 numbers from user and find the average of all.
##a) Use comparison operator to check how many numbers are less than average and print them
##b) Check how many numbers are more than average.
##c) How many are equal to average.


#Manoj Dixit - 20141404
#Python 3.9.0

a=input('Please enter 10 numbers delimated by space:\n')
0
b=a.rsplit(' ')
avg=0
#find avg
for item in b:
    if item.isnumeric() or item.replace('.','',1).isdigit(): #to check whether the current number is valid or not
        item=eval(item)
        avg+=item
    else:
        print(item,'is invalid')

avg=avg/len(b)
lta=[]
mta=[]
eta=[]

for item in b:
    if item.isnumeric() or item.lstrip('-').replace('.','',1).isdigit(): #to check whether the current number is valid or not
        item=eval(item)
        if item==avg:
            eta.append(item)
        elif item>avg:
            mta.append(item)
        else:
            lta.append(item)
    else:
        print(item,'is invalid')
print('Average of numbers =',avg)
print('Numbers less than average\n\t',lta)
print('Numbers more than average\n\t',mta)
print('Numbers equal to average\n\t',eta)


##Result:
##    Please enter 10 numbers delimated by space:
##    10 20 30 40 50 60 70 70 80 90
##    Average of numbers = 52.0
##    Numbers less than average
##             [10, 20, 30, 40, 50]
##    Numbers more than average
##             [60, 70, 70, 80, 90]
##    Numbers equal to average
##             []
##    >>> 
##    ======= RESTART: C:/Users/mndxt/OneDrive/Study/Python/Topgear/SET1/12.py =======
##    Please enter 10 numbers delimated by space:
##    10 20 30
##    Average of numbers = 20.0
##    Numbers less than average
##             [10]
##    Numbers more than average
##             [30]
##    Numbers equal to average
##             [20]
##    ======= RESTART: C:/Users/mndxt/OneDrive/Study/Python/Topgear/SET1/12.py =======
##    Please enter 10 numbers delimated by space:
##    10 20 b 30 40 50
##    b is invalid
##    b is invalid
##    Average of numbers = 25.0
##    Numbers less than average
##             [10, 20]
##    Numbers more than average
##             [30, 40, 50]
##    Numbers equal to average
##             []
