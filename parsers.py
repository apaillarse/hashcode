import os
from pprint import pprint
from model.book import *
from model.library import *


DIRECTORY = "data"
FILE = "a_example.txt"


def read_input():
    """ Red input
    Args:
        file_number (int): complete filename from the current working directory (ie: directory/file.txt)
    Returns:
        tuple: first the list of args as list of str, second list of lists with elements of each line
    """
    filename = os.path.join(DIRECTORY, FILE)
    with open(filename, "r") as file:
        data = file.read()
        elements = []
        for row in data.split("\n"):
            line = row.split()
            if len(line) > 0:
                elements.append(line)
        return elements

def parse_input():
    book_builder = BookBuilder()
    library_builder = LibraryBuilder()

    books = {}
    libraries = {}
    lines = read_input()

    i_line = 0
    for line in lines:
        if i_line == 0:
            nb_books = line[0]
            nb_libraries = line[1]
            nb_days = line[2]
        elif i_line == 1:
            for score in line:
                book = book_builder.build(score)
                books[book.id] = book
        else:
            if i_line % 2:
                for i_book in line:
                    libraries[library.id].add_book(books[int(i_book)])
            else:
                library = library_builder.build(line[1], line[2])
                libraries[library.id] = library
        i_line += 1

    return books, libraries, nb_days


if __name__ == "__main__":
    books, libraries, nb_days = parse_input()

    for _, book in books.items():
        print(book)

    for _, lib in libraries.items():
        print(lib)
        for book in lib.books:
            print(book)

