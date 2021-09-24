print("Health management system!!!")
list_1  ={"Harry":1,"Rohan":2,"Hameed":3}
print("Enter '1' for Harry\nEnter '2' for Rohan\nEnter '3' for hameed")
name = int(input())
if name == 1:
    print("You Have selected client : Harry")

elif name == 2:
    print("You Have selected client : Rohan")


elif name == 3:
    print("You Have selected client : Hameed")



else:
    print("Invalid number")

def gettime():
    import datetime
    return datetime.datetime.now()





if name==1:
    print("Hello client Harry!!!")
    print("Enter 1 for Exercise \nOr\nEnter 2 for Diet")
    exr_h = int(input())
    if exr_h ==1:
        print("You selected Exercise for client Harry")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("harry_Exr.txt", "a")
          data = input("Enter the exercises that harry has done \n")
          f.write(str([str(gettime())]) + "  " + data + "\n")
          print("Log added succesfully")


          f.close()
        elif l_r==2:
            f = open("harry_Exr.txt", "r")

            print(f.readlines())
            f.close()


    elif exr_h==2:
        print("You selected Diet for client Harry")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("harry_Diet.txt", "a")
          data = input("Enter what  Harry has Eaten?\n")
          f.write(str([str(gettime())]) + "  " + data +"\n")
          print("Log added succesfully")

          f.close()

        elif l_r==2:

            f = open("harry_Diet.txt", "r")

            print(f.readlines())

            f.close()

if name==2:
    print("Hello client Rohan!!!")
    print("Enter 1 for Exercise \nOr\nEnter 2 for Diet")
    exr_r = int(input())
    if exr_r ==1:
        print("You selected Exercise for client Rohan")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("rohan_exr.txt", "a")
          data = input("Enter the exercises that rohan has done \n")
          f.write(str([str(gettime())]) + "  " + data + "\n")
          print("Log added succesfully")

          f.close()
        elif l_r==2:
            f = open("rohan_exr.txt", "r")

            print(f.readlines())
            f.close()
    elif exr_r==2:
        print("You selected Diet for client Rohan")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("rohan_Diet.txt", "a")
          data = input("Enter what  Rohan has Eaten?\n")
          f.write(str([str(gettime())]) + "  " + data +"\n")
          print("Log added succesfully")

          f.close()

        elif l_r==2:

            f = open("rohan_Diet.txt", "r")

            print(f.readlines())


            f.close()




if name==3:
    print("Hello client Hameed!!!")
    print("Enter 1 for Exercise \nOr\nEnter 2 for Diet")
    exr_ha = int(input())
    if exr_ha ==1:
        print("You selected Exercise for client Hameed")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("hameed.Exr.txt", "a")
          data = input("Enter the exercises that hameed has done \n")
          f.write(str([str(gettime())]) + "  " + data + "\n")
          print("Log added succesfully")
          f.close()
        elif l_r==2:
            f = open("hameed.Exr.txt", "r")

            print(f.readlines())

            f.close()
    elif exr_ha==2:
        print("You selected Diet for client Hameed")
        print("Enter 1 to log\nOr\nEnter 2 for retrive")
        l_r = int(input())
        if l_r==1:
          f = open("hameed.Diet.txt", "a")
          data = input("Enter what  Hameed has Eaten?\n")
          f.write(str([str(gettime())]) + "  " + data +"\n")
          print("Log added succesfully")

          f.close()

        elif l_r==2:

            f = open("hameed.Diet.txt", "r")

            print(f.readlines())


            f.close()




print("Bye!!! Stay safe and stay healthy!!!!")