class Library:
    def __init__(self, id, nb_days_to_signup, nb_books_per_day):
        self.id = id
        self.nb_days_to_signup = nb_days_to_signup
        self.nb_books_per_day = nb_books_per_day
        self.books = {}

    def add_book(self, book):
        self.books[book.id] = book

    def __str__(self):
        return f'Library #{self.id} with nb days to sign up {self.nb_days_to_signup} and nb books per day {self.nb_books_per_day}'


class LibraryBuilder:
    def __init__(self):
        self.id = 0

    def build(self, nb_days_to_signup, nb_books_per_day):
        self.id += 1
        return Library(self.id - 1, nb_days_to_signup, nb_books_per_day)