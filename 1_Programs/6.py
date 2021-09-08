#PES Python Assignments SET 1
#6 Python program Basics
#Python program -
##Write a program to read string and print each character separately.
##    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
##    b) Repeat the string 100 times using repeat operator *
##    c) Read string 2 and concatenate with other string using + operator.

#Manoj Dixit - 20141404
#Python 3.9.0

while True:

    string=input('please input a string - ')
    print('This is first 5 chars : ',string[:5])
    print('This is 5 chars from 3rd position : ',string[2:7])
    print('This is string reversed:',string[::-1])
    print('This is string multiplied to itself 3 times : ',string*3)
    print('This is concantination using + operator : ',string+input('Enter another string - '))


##please input a string - Robotics
##This is first 5 chars :  Robot
##This is 5 chars from 3rd position :  botic
##This is string reversed: scitoboR
##This is string multiplied to itself 3 times :  RoboticsRoboticsRobotics
##Enter another string -  Engineer
##This is concantination using + operator :  Robotics Engineer


