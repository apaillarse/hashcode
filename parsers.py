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



if __name__ == "__main__":
    book_builder = BookBuilder()
    library_builder = LibraryBuilder()

    book = book_builder.build(1)
    print(book)

    lib = library_builder.build(2, 5)
    print(lib)
    lib.add_book(book)
    print(lib.books[book.id])


    books = []
    libraries = []
    lines = read_input()
    for line in lines:
        pprint(line)



