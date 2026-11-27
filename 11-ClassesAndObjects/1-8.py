# 1-8: Book - add price to object
# NOTE: Original book.py was not provided; this is an independent implementation.
class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.year})")
        print(f"Price: {self.price:.2f} PLN")

book = Book("The Hobbit", "J. R. R. Tolkien", 1937, 48)
book.display_info()
