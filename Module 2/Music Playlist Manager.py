# ---- Book Collection Manager ----

class BookCollection:

    # STEP 1 - Parameterized Constructor
    def __init__(self, collection_name, category):
        self.collection_name = collection_name
        self.category = category
        self.books = []
        print(f"Collection '{self.collection_name}' ({self.category}) has been created!")

    # STEP 2 - Add a book
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book}' added to the collection.")

    # STEP 3 - Remove a book
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' removed from the collection.")
        else:
            print(f"'{book}' was not found.")

    # STEP 4 - Display all books
    def display_books(self):
        print(f"\n--- {self.collection_name} ({self.category}) ---")
        if self.books:
            for i, book in enumerate(self.books, 1):
                print(f"  {i}. {book}")
        else:
            print("  No books available.")

    # STEP 5 - Destructor
    def __del__(self):
        print(f"Collection '{self.collection_name}' has been closed.")

# Object Creation
my_collection = BookCollection("Favorite Reads", "Fiction")

# STEP 6 - Menu-driven program
while True:
    print("\n1. Add Book  2. Remove Book  3. View Collection  4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book title: ")
        my_collection.add_book(book)

    elif choice == "2":
        book = input("Enter book title to remove: ")
        my_collection.remove_book(book)

    elif choice == "3":
        my_collection.display_books()

    elif choice == "4":
        del my_collection
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")