from pathlib import Path
BASE = Path(__file__).resolve().parent

# Section 4, item 13: save books by genre, using functions.
import csv

GENRE_FILES = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt',
}

def load_books(file_name):
    with (BASE / file_name).open('r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))

def save_books_for_genre(books, genre, file_name):
    with (BASE / file_name).open('w', encoding='utf-8') as file:
        for book in books:
            if book['Genre'] == genre:
                file.write(f"{book['Title']},{book['Author']},{book['Genre']}\n")

books = load_books('books.csv')
for genre, target in GENRE_FILES.items():
    save_books_for_genre(books, genre, target)
    print('Saved:', target)
