print("calculator")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
ch=int(input("enter choic(1-4):"))
if ch==1:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a+b
    print("sum = ",c)
elif ch==2:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a-b
    print("difference = ",c)
elif ch==3:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a*b
    print("product = ",c)
elif ch==4:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a/b
    print("quotient = ",c)
else:
    print("invalid choice")