from managers.admin import Admin

class OperationsManager:

    def __init__(self):
        self.admin = Admin()

    def print_menu(self):

        print("\n========== Library Management System ==========")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Add User")
        print("5. Display Users")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Display Borrowed Books")
        print("9. Exit")

    def get_choice(self):

      choice = int(input("\nEnter your choice: "))
      return choice
    def run(self):

        while True:


          self.print_menu()

          choice = self.get_choice()

          if choice == 1:

            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            quantity = int(input("Enter Quantity: "))


            self.admin.add_book(book_id, title, quantity)
            input("\nPress Enter to continue...")

          elif choice == 2:

            self.admin.display_books()
            input("\nPress Enter to continue...")

          elif choice == 3:

            title = input("Enter Book Title: ")

            book = self.admin.search_book(title)
            input("\nPress Enter to continue...")

            if book is None:
                print("Book not found.")
                
            else:
                print(book)
            input("\nPress Enter to continue...")

          elif choice == 4:

            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")

            self.admin.add_user(user_id, name)
            input("\nPress Enter to continue...")

          elif choice == 5:

            self.admin.display_users()
            input("\nPress Enter to continue...")

          elif choice == 6:

            user_id = int(input("Enter User ID: "))
            title = input("Enter Book Title: ")

            self.admin.borrow_book(user_id, title)
            input("\nPress Enter to continue...")

          elif choice == 7:

            user_id = int(input("Enter User ID: "))
            title = input("Enter Book Title: ")

            self.admin.return_book(user_id, title)
            input("\nPress Enter to continue...")

          elif choice == 8:

            self.admin.display_borrowed_books()
            input("\nPress Enter to continue...")
          

          elif choice == 9:

            print("Thank you for using Library Management System.")
            break

          else:
           
           print("Invalid choice.")


