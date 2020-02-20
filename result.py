
# number of libraries

# id_lib nb_book
# book_id book_id book_id

def kw(f, line):
    f.write("%s\n" % line)

class Result:

    def __init__(self):
        self.library_list = []


    def output(self, file):
        with open("result/%s" % file, "w") as f:
            kw(f, len(self.library_list))
            for library in self.library_list:
                if library.loaded_books:
                    kw(f, " ".join([str(library.id), str(len(library.loaded_books))]))
                    kw(f,  " ".join([str(b.id) for b in library.loaded_books]))





