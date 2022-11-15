# sumsqr=0
# sumcube=0
# print("please enter the 10 numbers")
# for i in range(1,11):
#     num=int(input("number%d= "%i))
#     square=i*i
#     sumsqr=sumsqr+square
#     avgsqr=sumsqr/10
#     cube=i*i*i
#     sumcube=sumcube+cube
#     avgcube=sumcube/10
# print("the square of numbers= ",square)
# print("the sum of square of numbers= ",sumsqr)
# print("the average of squared numbers= ",avgsqr)
# print("the cube of numbers ",cube)
# print("sum of cube of numbers= ",sumcube)
# print("average of cubed numbers= ",avgcube)
i=0
sumsqr=0
sumcube=0
n=10
print(f"number square cube")
while i<n:
    i=int(input("number %d= "%i))
    square=i*i
    cube=i*i*i
    sumsqr=sumsqr+square
    sumcube=sumcube+cube
    avgsqr=sumsqr/10
    avgcube=sumcube/10
    print(f" {square}    {cube}")
    print("sum of square of 10 numbers= ",sumsqr)
    print("sum of cube of 10 numbers= ",sumcube)
    print("average of square= ",avgsqr)
    print("average of cube=",avgcube)

