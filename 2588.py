#2588
int1 = int(input())
int2 = int(input())

cal1 = int((int2%10)*int1)
cal2 = int(int((int2%100)/10)*int1)
cal3 = int(int((int2)/100)*int1)
print(cal1)
print(cal2)
print(cal3)
print(cal1+cal2*10+cal3*100)

#11382
A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

print(A+B+C)

#10171
print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

#10172
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')