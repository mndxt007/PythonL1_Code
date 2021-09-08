#PES Python Assignments SET 1
#10 Python program Basics
#Python program Basics	-
#Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.
#Manoj Dixit - 20141404
#Python 3.9.0

a=0b11110000
b=0b10101010

print(bin(a),'and',bin(b),'are two binary numbers, or',a,'and',b,'in decimal')

print(bin(a),'&(Binary AND)',bin(b),'=',bin(a&b),'or',a&b,'in decimal')
print(bin(a),'|(Binary OR)',bin(b),'=',bin(a|b),'or',a|b,'in decimal')
print(bin(a),'^(Binary XOR)',bin(b),'=',bin(a^b),'or',a^b,'in decimal')
print(bin(a),'~(Binary Ones Complement)=',bin(~a),'or',~a,'in decimal')
print(bin(a),'<< Binary Left Shift by 1 bit=',bin(a<<1),'or',a<<1,'in decimal')
print(bin(a),'>> Binary Right Shift by 1 bit=',bin(a>>1),'or',a>>1,'in decimal')

input('Press any key to continue')

##Result:
##    0b11110000 and 0b10101010 are two binary numbers, or 240 and 170 in decimal
##    0b11110000 &(Binary AND) 0b10101010 = 0b10100000 or 160 in decimal
##    0b11110000 |(Binary OR) 0b10101010 = 0b11111010 or 250 in decimal
##    0b11110000 ^(Binary XOR) 0b10101010 = 0b1011010 or 90 in decimal
##    0b11110000 ~(Binary Ones Complement)= -0b11110001 or -241 in decimal
##    0b11110000 << Binary Left Shift by 1 bit= 0b111100000 or 480 in decimal
##    0b11110000 >> Binary Right Shift by 1 bit= 0b1111000 or 120 in decimal
