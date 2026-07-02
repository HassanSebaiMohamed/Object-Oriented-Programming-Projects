class Book:

    def __init__(self, book_id, title, quantity):

        self.id = book_id
        self.title = title
        self.quantity = quantity

    def __str__(self):

        return f"ID: {self.id} | Title: {self.title} | Quantity: {self.quantity}"