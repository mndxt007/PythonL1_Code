#PES Python Assignments SET 1
#16 Python program Basics
#Python program Basics	-
##Write program to find the biggest and Smallest of N numbers.
##      PS: Use the functions to find biggest and smallest numbers. 

#Manoj Dixit - 20141404
#Python 3.9.0

a=input('Provide numbers delimated by space:\n\t')

b=a.rsplit(' ')
for i in range(len(b)):
    if b[i].isnumeric() or b[i].replace('.','',1).isdigit():
        b[i]=eval(b[i])
    else:
        print(b[i],'is not a number')
b.sort()

print('Smallest number is',b[0])
print('Biggest number is',b[len(b)-1])

##Result:
##    Provide numbers delimated by space:
##	10 10.1 9.9 15 25 32.1
##    Smallest number is 9.9
##    Biggest number is 32.1
