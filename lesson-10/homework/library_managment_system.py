class BookNotFoundException(Exception):
    """Raised when trying to borrow a book that doesn’t exist in the library."""
    pass


class BookAlreadyBorrowedException(Exception):
    """Raised when a book is already borrowed."""
    pass


class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more books than allowed."""
    pass


class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Member:
    """Represents a library member."""

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        return f"{self.name} successfully borrowed {book}."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return f"{self.name} successfully returned {book}."
        return f"{self.name} does not have {book} to return."

    def __str__(self):
        books = ", ".join([str(book) for book in self.borrowed_books]) or "None"
        return f"Member: {self.name}, Borrowed Books: {books}"


class Library:
    """Manages books and members."""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = Book(title, author)
            return f"Book '{title}' by {author} added to the library."
        return f"Book '{title}' already exists in the library."

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
            return f"Member '{name}' added to the library."
        return f"Member '{name}' already exists."

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' does not exist in the library.")
        if member_name not in self.members:
            return f"Member '{member_name}' does not exist in the library."
        member = self.members[member_name]
        book = self.books[book_title]
        return member.borrow_book(book)

    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            return f"Member '{member_name}' does not exist in the library."
        if book_title not in self.books:
            return f"Book '{book_title}' does not exist in the library."
        member = self.members[member_name]
        book = self.books[book_title]
        return member.return_book(book)

    def view_books(self):
        return "\n".join([str(book) + (" (Borrowed)" if book.is_borrowed else "") for book in self.books.values()])

    def view_members(self):
        return "\n".join([str(member) for member in self.members.values()])


# Testing the Library Management System
def main():
    library = Library()

    # Adding books and members
    print(library.add_book("The Great Gatsby", "F. Scott Fitzgerald"))
    print(library.add_book("1984", "George Orwell"))
    print(library.add_book("To Kill a Mockingbird", "Harper Lee"))

    print(library.add_member("Alice"))
    print(library.add_member("Bob"))

    # Borrowing books
    try:
        print(library.borrow_book("Alice", "The Great Gatsby"))
        print(library.borrow_book("Alice", "1984"))
        print(library.borrow_book("Alice", "To Kill a Mockingbird"))
        print(library.borrow_book("Alice", "1984"))  # Exception: Already borrowed
    except Exception as e:
        print(f"Error: {e}")

    # Exceeding member borrowing limit
    try:
        print(library.borrow_book("Bob", "1984"))  # Exception: Already borrowed by Alice
    except Exception as e:
        print(f"Error: {e}")

    # Returning books
    print(library.return_book("Alice", "The Great Gatsby"))
    print(library.return_book("Alice", "The Great Gatsby"))  # Alice does not have it anymore

    # Viewing books and members
    print("\nBooks in the library:")
    print(library.view_books())
    print("\nMembers in the library:")
    print(library.view_members())


if __name__ == "__main__":
    main()