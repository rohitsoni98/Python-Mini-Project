"""

create a library class
display book
lend book
add book
return book
Rohit's Library = Library(list of books, library name)
dictionary (book-name of person)

"""


class Library:
    def __init__(self,a,b):
        self.booklist = a
        self.name = b
        self.lenddict = {}

    def displaybook(self):
        print(f"We have the following given books below: {self.name} ")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now!")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book has beed added in the book list !")

    def returnbook(self, book):
        self.lenddict.pop(book)



if __name__ == '__main__':
    Rohit = Library(["Python", "Harry Potter", "Avengers", "Superman", "My Life My Rules"], "Rohit's Library")

    while True:
        print(f"Welcome to the {Rohit.name}. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice == 1:
            Rohit.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            Rohit.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Rohit.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Rohit.returnbook(book)

        else:
            print("not a valid option , select again")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()

            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue





