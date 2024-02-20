#2557
print("Hello World!")

#1000
A,B =input().split()
A = int(A)
B = int(B)

if A < 0 or B > 10:
    print('Invalid number')
else:
    print(float(A/B))

#10869
A1,B1 =input().split()
A1 = int(A1)
B1 = int(B1)

if A < 1 or B > 10000:
    print('Invalid number')
else:
    print(A1+B1)
    print(A1-B1)
    print(A1*B1)
    print(int(A1/B1))
    print(A1%B1)