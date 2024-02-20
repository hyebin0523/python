#2557
print("Hello World!")

#1000
A,B =input().split()
A = int(A)
B = int(B)

if A < 0 or B > 10:
    print('Invalid number')
else:
    print(A+B)