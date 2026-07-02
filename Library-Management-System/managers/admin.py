from models.book import Book
from models.user import User


class Admin:

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book_id, title, quantity):

        for book in self.books:
            if book.id == book_id:
                print("This book already exists.")
                return

        new_book = Book(book_id, title, quantity)
        self.books.append(new_book)
        print("Book added successfully.")

    def display_books(self):

        if not self.books:
            print("There are no books in the library.")
            return

        for book in self.books:
            print(book)

    def search_book(self, title):

        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def add_user(self, user_id, name):

        for user in self.users:
            if user.id == user_id:
                print("This user already exists.")
                return

        new_user = User(user_id, name)
        self.users.append(new_user)
        print("User added successfully.")

    def display_users(self):

        if not self.users:
            print("There are no users.")
            return

        for user in self.users:
            print(user)

    def search_user(self, user_id):

        for user in self.users:
            if user.id == user_id:
                return user

        return None

    def borrow_book(self, user_id, title):

        book = self.search_book(title)

        if book is None:
            print("Book not found.")
            return

        if book.quantity == 0:
            print("This book is not available.")
            return

        user = self.search_user(user_id)

        if user is None:
            print("User not found.")
            return

        user.borrowed_books.append(book)
        book.quantity -= 1
        print("Book borrowed successfully.")

    def return_book(self, user_id, title):

        book = self.search_book(title)

        if book is None:
            print("Book not found.")
            return

        user = self.search_user(user_id)

        if user is None:
            print("User not found.")
            return

        if book not in user.borrowed_books:
            print("This user didn't borrow this book.")
            return

        user.borrowed_books.remove(book)
        book.quantity += 1
        print("Book returned successfully.")

    def display_borrowed_books(self):

        borrowed = False

        for user in self.users:

            if user.borrowed_books:

                borrowed = True

                print(f"\n{user.name} borrowed:")

                for book in user.borrowed_books:
                    print(f"- {book.title}")

        if not borrowed:
            print("No borrowed books.")