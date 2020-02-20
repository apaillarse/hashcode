import numpy as np


class Library:
    def __init__(self, id, nb_days_to_signup, nb_books_per_day):
        self.id = int(id)
        self.nb_days_to_signup = int(nb_days_to_signup)
        self.nb_books_per_day = int(nb_books_per_day)
        self.books = {}
        self.init_date = None
        self.loaded_books = []

    def add_book(self, book):
        self.books[book.id] = book

    def __str__(self):
        return f'Library #{self.id} with nb days to sign up {self.nb_days_to_signup} and nb books per day {self.nb_books_per_day}'

    def get_nb_books(self):
        self.nb_books = len(self.books)

    def get_time_to_scan_books(self):
        return self.nb_books / self.nb_books_per_day

    def sort_score_books(self):
        self.books_score_sorted = np.sort([v.score for v in self.books.values()])

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
        scan = self.books_score / self.get_time_to_scan_books()
        return signup + scan

    def score_time_left(self, time_left):
        if time_left <= self.nb_days_to_signup:
            return 0
        else:
            time_for_scan = time_left - self.nb_days_to_signup
            self.sort_score_books()
            return self.books_score_sorted[0: (time_for_scan * self.nb_books_per_day)]


class LibraryBuilder:
    def __init__(self):
        self.id = 0

    def build(self, nb_days_to_signup, nb_books_per_day):
        self.id += 1
        return Library(self.id - 1, nb_days_to_signup, nb_books_per_day)
