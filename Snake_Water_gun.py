import random
print("\t WELCOME TO SNAKE , WATER , GUN GAME")
p_name = input("Please enter your name :\n")
c_win = 0
c = ["Snake","Water","Gun"]
p_win = 0
rounds = 1
ties =  0
print("This game will have 5 rounds")
print("Lets start the game",p_name)
while (rounds!= 6):
        c_choice = random.choice(c)
        p_choice = input("For snake enter : 's'\nFor Water enter : 'w'\nFor Gun enter : 'g' \n")
     
        print("Round ",rounds)
        if p_choice == "s":
            if c_choice == "Snake":
                print(p_name,"choice is Snake and computer also choosed Snake ")
                print("Round tied")
                rounds = rounds+1
                ties = ties +1
            elif c_choice == "Water":
                print(p_name,"choice is Snake and computer choosed Water")
                print(p_name,"Won!!!")
                rounds = rounds+1
                p_win = p_win+1
            elif c_choice == "Gun":
                print(p_name,"choice is Snake and computer  choosed Gun ")
                print("Computer won")
                rounds = rounds+1
                c_win = c_win+1

        elif p_choice == "w":
            if c_choice == "Water":
                print(p_name,"choice is Water and computer also choosed Water ")
                print("Round tied")
                rounds = rounds+1
                ties = ties +1
            elif c_choice == "Gun":
                print(p_name,"choice is Water and computer choosed Gun")
                print(p_name,"Won!!!")
                rounds = rounds+1
                p_win = p_win+1
            elif c_choice == "Snake":
                print(p_name,"choice is Water and computer  choosed Snake ")
                print("Computer won")
                rounds = rounds+1
                c_win = c_win+1
                
        
        elif p_choice == "g":
            if c_choice == "Gun":
                print(p_name,"choice is Gun and computer also choosed Gun ")
                print("Round tied")
                rounds = rounds+1
                ties = ties +1
            elif c_choice == "Snake":
                print(p_name,"choice is Gun and computer choosed Snake")
                print(p_name,"Won!!!")
                rounds = rounds+1
                p_win = p_win+1
            elif c_choice == "Water":
                print(p_name,"choice is Gun and computer choosed Water ")
                print("Computer won")
                rounds = rounds+1
                c_win = c_win+1
        else :
            print("Invalid choice")        
      
print()
print("Results:")
print(p_name,"won",p_win,"rounds")
print("Computer won",c_win,"rounds")
print("Rounds tied :",ties)
if p_win>c_win:
    print("Congrats",p_name,"you won the match!!!")
elif p_win<c_win:
    print("Computer won the match!!!")
elif  p_win == c_win:
    print("Match tied !!!")    

print("***Thank you for playing this game",p_name,"***")