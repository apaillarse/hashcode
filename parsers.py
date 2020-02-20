import os
from pprint import pprint
from model.book import *
from model.library import *
from result import Result

DIRECTORY = "data"
FILE = "a_example.txt"


def read_input(file):
    """ Red input
    Args:
        file_number (int): complete filename from the current working directory (ie: directory/file.txt)
    Returns:
        tuple: first the list of args as list of str, second list of lists with elements of each line
    """
    filename = os.path.join(DIRECTORY, file)
    with open(filename, "r") as file:
        data = file.read()
        elements = []
        for row in data.split("\n"):
            line = row.split()
            if len(line) > 0:
                elements.append(line)
        return elements


def parse_input(file):
    book_builder = BookBuilder()
    library_builder = LibraryBuilder()

    books = {}
    libraries = {}
    lines = read_input(file)

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

    for file in [
        "a_example.txt",
        "b_read_on.txt",
        "c_incunabula.txt",
        "d_tough_choices.txt",
        "e_so_many_books.txt",
        "f_libraries_of_the_world.txt"
    ]:

        books, libraries, nb_days = parse_input(file)

        for _, book in books.items():
            # print(book)
            pass

        for _, lib in libraries.items():
            # print(lib)
            pass
            for book in lib.books:
                # print(book)
                pass
        nbdays_to_process_lib = 0
        start_day_now = 0
        result = Result()
        for k, library in libraries.items():
            library.loaded_books = list(library.books.values())

            # nbdays_to_process_lib += int(library.nb_days_to_signup) + (len(library.books) / int(library.nb_books_per_day))
            nbdays_to_process_lib = start_day_now + int(library.nb_days_to_signup) + (
                    len(library.books) / int(library.nb_books_per_day))
            # if nbdays_to_process_lib < int(nb_days):
            #     start_day_now += int(library.nb_days_to_signup)
            #     result.library_list.append(library)
            # else:
            start_day_now += int(library.nb_days_to_signup)
            available_days = int(nb_days) - int(start_day_now)
            selected_books = []
            books_list = list(library.books.values())
            i = 0

            while i < len(books_list) and available_days > 0:
                if available_days > 0:
                    for j in range(int(library.nb_books_per_day)):
                        if i + j < len(books_list):
                            selected_books.append(books_list[i + j])
                i += int(library.nb_books_per_day)
                available_days -= 1
            library.loaded_books = selected_books
            # print(selected_books)

            result.library_list.append(library)

        # result.library_list = libraries.values()
        result.output(file)
