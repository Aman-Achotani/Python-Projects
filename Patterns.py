print("Enter the number of rows you want !!!")
one = int(input())
print("Enter 1 for normal pattern \nEnter 0 for reverse pattern \n")
two = int(input())
three = bool(two)

if three == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

elif three==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()



