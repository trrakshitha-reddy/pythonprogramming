sumsqr=0
sumcube=0
print("please enter the 10 numbers")
for i in range(1,11):
    num=int(input("number%d= "))
    square=i*i
    sumsqr=sumsqr+square
    avgsqr=sumsqr/10
    cube=i*i*i
    sumcube=sumcube+cube
    avgcube=sumcube/10
print("the square of numbers= ",square)
print("the sum of square of numbers= ",sumsqr)
print("the average of squared numbers= ",avgsqr)
print("the cube of numbers ",cube)
print("sum of cube of numbers= ",sumcube)
print("average of cubed numbers= ",avgcube)