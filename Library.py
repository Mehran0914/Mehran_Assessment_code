library_books = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "status": "available", "ISBN": "9780141199078", "genre": "Classic", "published_year": 1813},
    {"title": "1984", "author": "George Orwell", "status": "available", "ISBN": "9780451524935", "genre": "Dystopian", "published_year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "available", "ISBN": "9780060935467", "genre": "Classic", "published_year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "available", "ISBN": "9780743273565", "genre": "Classic", "published_year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "status": "available", "ISBN": "9780142437247", "genre": "Adventure", "published_year": 1851},
    {"title": "War and Peace", "author": "Leo Tolstoy", "status": "available", "ISBN": "9780199232765", "genre": "Historical", "published_year": 1869},
    {"title": "Jane Eyre", "author": "Charlotte Bronte", "status": "available", "ISBN": "9780142437209", "genre": "Classic", "published_year": 1847},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "status": "available", "ISBN": "9780316769488", "genre": "Classic", "published_year": 1951},
    {"title": "Animal Farm", "author": "George Orwell", "status": "available", "ISBN": "9780451526342", "genre": "Satire", "published_year": 1945},
    {"title": "Brave New World", "author": "Aldous Huxley", "status": "available", "ISBN": "9780060850524", "genre": "Dystopian", "published_year": 1932},
]

def display_books():
    print("\nCurrent Library Collection:")
    for book in library_books:
        print(f"=> {book['title']} by {book['author']} ({book['status']})")
        print(f"   - ISBN: {book['ISBN']}, Genre: {book['genre']}, Published Year: {book['published_year']}")

def search_book(title):
    for book in library_books:
        if book['title'].lower() == title.lower():
            return book
    return None

while True:
    print(""" 
Welcome To Library Management System    

Enter 1 : To View Book List 
Enter 2 : To Add New Book 
Enter 3 : To Search Book 
Enter 4 : To Remove Book 
Enter 5 : To Borrow a Book 
Enter 6 : To Return a Book 
Enter 7 : To Exit
""")
    try:
        user_input = int(input("Please select an option: "))
        
        if user_input == 1:
            display_books()

        elif user_input == 2:
            new_title = input("Enter New Book Title: ").strip().title()
            new_author = input("Enter Author Name: ").strip().title()
            new_isbn = input("Enter ISBN: ").strip()
            new_genre = input("Enter Genre: ").strip().title()
            new_published_year = input("Enter Published Year: ").strip()
            if search_book(new_title):
                print(f"\nThis book '{new_title}' is already in the library collection.")
            else:
                library_books.append({
                    "title": new_title, 
                    "author": new_author, 
                    "status": "available", 
                    "ISBN": new_isbn, 
                    "genre": new_genre, 
                    "published_year": int(new_published_year)
                })
                print(f"\n=> New book '{new_title}' by {new_author} successfully added.\n")
                display_books()

        elif user_input == 3:
            search_title = input("Enter Book Title To Search: ").strip()
            book = search_book(search_title)
            if book:
                print(f"\n=> Found '{book['title']}' by {book['author']} ({book['status']})")
                print(f"   - ISBN: {book['ISBN']}, Genre: {book['genre']}, Published Year: {book['published_year']}")
            else:
                print(f"\n=> No record found for book: {search_title}")

        elif user_input == 4:
            remove_title = input("Enter Book Title To Remove: ").strip()
            book = search_book(remove_title)
            if book:
                if book['status'] == "borrowed":
                    print(f"\nCannot remove '{book['title']}' because it is currently borrowed.")
                else:
                    library_books.remove(book)
                    print(f"\n=> Book '{remove_title}' successfully deleted.\n")
                    display_books()
            else:
                print(f"\n=> No record found for book: {remove_title}")

        elif user_input == 5:  # Borrow a Book
            display_books()
            borrow_title = input("Enter the title of the book you want to borrow: ").strip()
            book = search_book(borrow_title)
            if book:
                if book['status'] == "available":
                    book['status'] = "borrowed"
                    print(f"\n=> You have successfully borrowed '{book['title']}'.")
                else:
                    print(f"\n=> Book '{book['title']}' is already borrowed.")
            else:
                print(f"\n=> Book '{borrow_title}' is not available in the library.")

        elif user_input == 6:  # Return a Book
            print("\nCurrently Borrowed Books:")
            borrowed_books = [book for book in library_books if book['status'] == "borrowed"]
            if borrowed_books:
                for book in borrowed_books:
                    print(f"=> {book['title']} by {book['author']} (ISBN: {book['ISBN']})")
                return_title = input("Enter the title of the book you want to return: ").strip()
                book = search_book(return_title)
                if book and book['status'] == "borrowed":
                    book['status'] = "available"
                    print(f"\n=> Thank you for returning '{book['title']}'.")
                else:
                    print(f"\n=> Book '{return_title}' was not borrowed or does not belong to this library.")
            else:
                print("\nNo books are currently borrowed.")

        elif user_input == 7:
            print("\nThank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Please enter a valid option (1-7).")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    continue_choice = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    if continue_choice not in ["yes", "y"]:
        print("\nThank you for using the Library Management System. Goodbye!")
        break
