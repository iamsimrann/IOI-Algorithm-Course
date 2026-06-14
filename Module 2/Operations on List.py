# ---- Library Book Manager ----

# STEP 1 - Create a list of books
books = ["Python Basics", "Data Science", "Machine Learning", "Web Development", "AI Essentials"]
print("Book collection:", books)

# STEP 2 - Access the list
print("Total books:", len(books))
print("First book:", books[0])
print("Last book:", books[-1])
print("First three books:", books[:3])

# STEP 3 - Modify the list
books.append("Cloud Computing")
print("\nAfter adding a book:", books)
books.remove("AI Essentials")
print("After removing a book:", books)
books.sort()
print("Sorted titles:", books)
books.reverse()
print("Reverse order:", books)

# STEP 4 - Create an author dictionary
author = {"name": "John Smith", "genre": "Technology", "books_written": 8}
print("\nAuthor profile:", author)

# STEP 5 - Dictionary operations
print("Genre:", author["genre"])
print("Books Written:", author.get("books_written", "Not found"))
author["books_written"] = 9
author["email"] = "johnsmith@library.com"
author.pop("books_written")
print("Updated author profile:", author)

# STEP 6 - Convert lists to a book directory
book_ids = [101, 102, 103, 104, 105]
book_names = ["Python Basics", "Data Science", "Machine Learning", "Web Development", "Cloud Computing"]
book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:", book_directory)
print("Book with ID 103:", book_directory[103])