class Ebook:
    def __init__(self, title, author, total_pages):
        if total_pages < 1:
            raise ValueError('Book must have at least one page')
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if not self.is_open:
            print('Book is closed')
        elif self.current_page < self.total_pages:
            self.current_page += 1

    def previous_page(self):
        if not self.is_open:
            print('Book is closed')
        elif self.current_page > 1:
            self.current_page -= 1

    def show_status(self):
        print(f'{self.title} by {self.author}; page {self.current_page}/{self.total_pages}; open={self.is_open}')
