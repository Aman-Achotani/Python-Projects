n = 34
g = 5
while (g!=0):
    print("You have ",g,"gusses ")
    g=g-1
    print("Guess your number")
    i = int(input())
    if (i<n):
        print("Guess greater number")
    elif (i>n):
        print("Guess smaller number")
    elif (i==n):
        print("Congratulations you won")
        print("You found the number with ",g,"gusses left")
        break
    if (g==0):
        print("Oops! You lose")
        print("Better luck next time")

        continue
print("")
print("Game over")
print("*** Thanks for playing this game ***")




