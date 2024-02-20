#2588
int1 = int(input())
int2 = int(input())

cal1 = int1*(int2%10)
cal2 = int1*((int2%100)/10)
cal3 = int1*(int2)/100
print(cal1)
print(cal2)
print(cal3)
print(cal1+cal2*10+cal3*100)