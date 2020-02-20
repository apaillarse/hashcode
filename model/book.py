class Book:
    def __init__(self, id, score):
        self.id = int(id)
        self.score = int(score)

    def __str__(self):
        return f'Book #{self.id} with score {self.score}'


class BookBuilder:
    def __init__(self):
        self.id = 0

    def build(self, score):
        self.id += 1
        return Book(self.id - 1, score)
