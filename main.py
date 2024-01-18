#define a main function
def main():

 #Initialize a book list
 #To store the details of the book
  Listbook = [] 
 #To store the book dictonaries
  books = []
 
 
 
 #In the construction of this code third party code has been used
 #to enhance and debug the program code. The following GitHub repository was used for
 #the next section of the code. The original code and idea can be found at
 # https://github.com/BekBrace/Python_work_flow_CLI_App/blob/main/main.py
 #The code itself provides user input, allows users to lookup and display books.
 #However, I have included the select a book in the options.
 

  #While loop allows users to navigate through menu options. 
  #The user must select 1-4, otherwise selecting 5 will quit the program
  #The condition is checked before each execution
  choice = 0
  while choice != 5 :
    print("*** Welcome to Melanin's Personalized BookShelf. \n Kindly select from the options displayed by entering the numbers: ")
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
        print("Book added successfully!")

     
     #conditional statement for the subsequent choices if the previous entry is 1
    elif choice == 2:
        print("Looking up a book......")
        #user input to search by assigning a variable
        keyword = input("Enter search Term:")
        look_books = [book for book in Listbook if keyword in book[0] or keyword in book[1] or keyword in book[2]]
        if look_books:
              for book in look_books:
                    print(book)
        else:
              print("Book not found.")
   
   
   
    #This section of code was debugged by the generative AI tool: CHATGPT.
    #conditional statement for selecting a book when the condition is true: entry is 3
    elif choice == 3:
     print(Listbook)
     print("Selecting a book....")
     #variable to store user input and converts to a lowercase
     keyword = input("Enter the book to be selected: ").lower()
     #it filters and searches through the List of book and does a comparison of the user input in lower case.
     found_books = [book for book in Listbook if any(keyword in str(value).lower() for value in book)]
    
     if found_books:
        print("Book has been selected successfully:")
        for book in found_books:
            print(f"Title: {book[0]}, Author: {book[1]}, Pages: {book[2]}")
     else:
        print("Book not found.")
    
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


    
