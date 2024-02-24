class Book:
    def __init__(self, book_name,author, release_year, genre):
        self.book_name=book_name
        self.author = author
        self.release_year = release_year
        self.genre = genre

# Create a list to store Book objects
books_list = []

# Get the number of entries from the user
num_entries = int(input("Enter the number of book entries: "))

# Collect information for each book entry
for _ in range(num_entries):
    book_name = input("Enter book name: ")
    author_name = input("Enter author: ")
    release_year = int(input("Enter the year: "))
    genre = input("Enter the genre: ")

    # Instantiate the Book class and append it to the list
    books_list.append(Book(book_name=book_name,author=author_name, release_year=release_year, genre=genre))

# Display the list of books
print("\nList of Books:")
for i, book in enumerate(books_list, start=1):
    print(f"{i}. {book.book_name} by {book.author}")

# Get user input to choose multiple books
selected_books_indices_str = input("\nEnter the numbers of the books you want to view (separated by spaces): ")
selected_books_indices = [int(index) - 1 for index in selected_books_indices_str.split()]

# Display details for selected books
print("\nDetails for Selected Books:")
for index in selected_books_indices:
    if 0 <= index < len(books_list):
        selected_book = books_list[index]
        print(f"\nDetails of {selected_book.book_name} by {selected_book.author}:")
        print(f"Released in {selected_book.release_year} in the genre {selected_book.genre}")
    else:
        print(f"Invalid book selection: {index + 1}")
