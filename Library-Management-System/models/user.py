class User:

    def __init__(self, user_id, name):

        self.id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):

        return f"ID: {self.id} | Name: {self.name}"