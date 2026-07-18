class Transaction:
    def __init__(self, title, amount, transaction_type, note=""):
        self.title = title
        self.amount = amount
        self.type = transaction_type
        self.note = note

    def display_info(self):
        return (
            f"Transaction:\n"
            f"Title: {self.title}\n"
            f"Amount: {self.amount}\n"
            f"Type: {self.type}\n"
            f"Note: {self.note}"
        )


class Bank:
    def __init__(self):
        self.wallet = []

    # Add
    def add_transaction(self, transaction):
        self.wallet.append(transaction)
        return "Transaction Added Successfully!"

    # Remove
    def del_transaction(self, title):
        for trans in self.wallet:
            if trans.title.lower() == title.lower():
                self.wallet.remove(trans)
                return f"{title} has been removed!"

        return "Transaction not found!"

    # Display All
    def display(self):
        if not self.wallet:
            return "No transactions available in your wallet."

        return "\n\n".join(
            [transaction.display_info() for transaction in self.wallet]
        )

    # Search
    def search_wallet(self, query):
        found = [
            trans
            for trans in self.wallet
            if query.lower() in trans.title.lower()
            or query.lower() in trans.type.lower()
        ]

        if not found:
            return "No Transactions!"

        return "\n\n".join(
            [transaction.display_info() for transaction in found]
        )


def main():
    bank = Bank()

    while True:
        print("\n Personal Banking System : ")
        print("1. Add a Transaction")
        print("2. Remove a Transaction")
        print("3. Display all Transactions")
        print("4. Search for a Transaction")
        print("5. Exit")

        choice = input("Enter your choice (1-5) : ")

        if choice == "1":
            title = input("Enter Title: ")
            amount = float(input("Enter Amount: "))
            transaction_type = input("Enter Type (Income/Expense): ")
            note = input("Enter Note: ")

            transaction = Transaction(
                title,
                amount,
                transaction_type,
                note
            )

            print(bank.add_transaction(transaction))

        elif choice == "2":
            title = input("Enter Transaction Title: ")
            print(bank.del_transaction(title))

        elif choice == "3":
            print(bank.display())

        elif choice == "4":
            query = input("Search: ")
            print(bank.search_wallet(query))

        elif choice == "5":
            print("Good Bye!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()