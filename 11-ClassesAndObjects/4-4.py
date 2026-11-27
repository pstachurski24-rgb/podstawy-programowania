# 4-4: Ebook class in a separate module
from ebook import Ebook

book = Ebook('Python Basics', 'Jan Kowalski', 120)
book.open_book()
book.show_status()
for _ in range(3):
    book.next_page()
book.show_status()
book.close_book()
book.next_page()
