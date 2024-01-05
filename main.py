#define a main function
def main():

 #Initialize a book list
  Listbook = []
  books = []
 
 

  #While loop allows users to navigate through menu options. 
  #The user must select 1-4, otherwise selecting 5 will quit the program
  #The condition is checked before each execution
  choice = 0
  while choice != 5 :
    print("*** Welcome to Melanin's Bookstore. \n Kindly select from the options displayed by entering the numbers ")
    print("1) Add a Book")
    print("2) Lookup a Book")
    print("3) Select a Book")
    print("4) Display Books")
    print("5) Quit")

    #Captures user input
    choice = int(input())

    #conditional statement for the choice entry equals to 1
    if choice == 1:
        print("Adding a Book...")
        name_book = input("Enter the name of the book>>>")
        author_book = input("Enter the name of the author>>>")
        pages_book = input("Enter the number of the pages of the book>>>")
        #Adding the user input to the list of books using the append method
        Listbook.append([name_book, author_book, pages_book])
        books.append({'bookname': name_book, 'author': author_book, 'pages':pages_book})
        print(books)

     
     #conditional statement for the subsequent choices if the previous entry is 1
    elif choice == 2:
        print("Looking up a book......")
        #user input to search by assigning a variable
        keyword = input("Enter search Term:")
        for books in Listbook:
         if keyword in books[0] or keyword in books[1] or keyword in books[2]:
           print(books)
   
   
    #conditional statement for selecting a book when the condition is true: entry is 3
    elif choice == 3:
        print("Selecting a book....")
        print(books)
        print("Book has been selected successfully")

    

    #Elif statement for displaying all books when the condition is true: entry is 4
    elif choice == 4:
      print("Displaying books.....")
      for book in Listbook:
        print(book)
 
    
    #Elif statement for quitting the application when the condition is true: entry is 5
    elif choice == 5:
      print("Quitting the application....")
      print("Program Terminated")



#it executes the main function if the name of the file correlates with the name of the main function
if __name__ == "__main__":
     main()


    
