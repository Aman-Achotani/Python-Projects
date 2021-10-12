import random
print("Welcome to random number genrator!!!")
print("Please enter a number till where you want to generate random number :")
num = int(input())

while True:
    ran_num = random.randint(1,num)
    print("Random number is :",ran_num)
    yn = input("Want to generate random number again (y/n) : ")
    if yn =='y':
        continue
    elif yn == 'n':
        break
    else:
        print("Invalid input")


