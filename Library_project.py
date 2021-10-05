#  My library project


class Library:

    def __init__(self,Book,Library) :
        self.book_name = Book
        self.library_name = Library

        print("\t\t***Welcome to ",self.library_name,"***")

    def display(self):
        print()
        print()
        print("Books avaiable are : ")
        for items in self.book_name:
            print(items)  

    def lend(self):
        print()
        name = input("Enter your name : ")
        ch1 = input("Enter the name of the book you want to lend : ")
        if ch1 in self.book_name:
            self.book_name.remove(ch1)
            print(ch1,"book lended to you succesfully")
            f = open("Library_Record.txt","a")
            f.writelines(f"{name} lended {ch1} book\n")

        else:
            print()
            print("This type of book is not available  ")          
           

    def donate(self):
        print()
        name2 = input("Donator please enter your name : ")
        ch2 = input("Please enter the name of book you want to donate : ")
        self.book_name.append(ch2)
        f = open("Library_Record.txt","a")
        f.writelines(f"{name2} donated {ch2} book\n")
        print("Thank you ",name2,"for donating",ch2,"book!!!")

        
    def return_book(self):
        print()
        name3 = input("Please enter your name : ")
        ch3 = input("Please enter the name of book you want to return : ")
        self.book_name.append(ch3)
        f = open("Library_Record.txt","a")
        f.writelines(f"{name3} returned {ch3} book\n")
        print("Thank you ",name3,"for returning",ch3,"book!!!")

    def arrange(self):
        a = True
        while a== True:
            self.display()
            print()
            print("Enter 1 to lend a book")
            print("Enter 2 to donate a book")
            print("Enter 3 to return a book")
            print("Enter 4 to exit\n")  
            ch4 = input()
            if ch4 == '1':
                self.lend()
            elif ch4 == '2':
                self.donate()
            elif ch4 == '3':
                self.return_book()
  
            elif ch4 == '4':
                break
            else:
                print("Invalid input")




Aman = Library(["Harry Potter","Tales of shivaji","Annabella returns","The fall of troy","Panchatantra"],"Aman's Library")
Aman.display()
print()
Aman.arrange()       