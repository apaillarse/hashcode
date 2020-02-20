import numpy as np


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

    def get_nb_books(self):
        self.nb_books = len(self.books)

    def score_signup(self):
        """Only account for time to signup

        """
        self.books_score = np.sum([v.score for v in self.books.values()])
        return self.books_score / self.nb_days_to_signup

    def score_signup_scan(self):
        """Signup + scan
        """
        signup = self.score_signup()
        self.get_nb_books()
        scan = self.books_score * self.nb_books_per_day / self.nb_books
        return signup + scan


class LibraryBuilder:
    def __init__(self):
        self.id = 0

    def build(self, nb_days_to_signup, nb_books_per_day):
        self.id += 1
        return Library(self.id - 1, nb_days_to_signup, nb_books_per_day)
