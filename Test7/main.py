
from book import Book

books = {}

while True:
    print("\n----- BOOK MANAGEMENT SYSTEM -----")
    print("1. Add Book")
    print("2. Delete Book by ID")
    print("3. Display All Books")
    print("4. Search Book by ID")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bid = int(input("Enter Book ID: "))

        if bid in books:
            print("Book ID already exists!")
        else:
            name = input("Enter Book Name: ")
            price = float(input("Enter Book Price: "))
            author = input("Enter Book Author: ")

            b = Book(bid, name, price, author)
            books[bid] = b

            print("Book added successfully!")

    elif choice == 2:
        bid = int(input("Enter Book ID to delete: "))

        if bid in books:
            del books[bid]
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    elif choice == 3:
        if len(books) == 0:
            print("No books available!")
        else:
            for bid in books:
                books[bid].display()
                print("-------------------")

    elif choice == 4:
        bid = int(input("Enter Book ID to search: "))

        if bid in books:
            books[bid].display()
        else:
            print("Book not found!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
