
# number of libraries

# id_lib nb_book
# book_id book_id book_id

def kw(f, line):
    f.write("%s\n" % line)


class Result:

    def __init__(self):
        self.library_list = []

    def output(self, file):
        f = open("result/%s" % file, "w")
        i = 0
        for l in self.library_list:
            if l.loaded_books:
                i += 1
        kw(f, i)
        for library in self.library_list:
            print(library)
            if library.loaded_books:
                kw(f, " ".join([str(library.id), str(len(library.loaded_books))]))
                kw(f,  " ".join([str(b.id) for b in library.loaded_books]))
        f.close()

