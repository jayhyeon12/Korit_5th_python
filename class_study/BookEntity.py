class Book:

    def __init__(self, bookId = 0, bookName = "", author = "", publisher = "", isbn = ""):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        return f"""Book[
bookId: {self.bookId},
bookName: {self.bookName},
author: {self.author}
publisher: {self.publisher}]"""
        # return "Book[bookId: {0}, bookName: {1}]".format(self.bookId, self.bookName)

        # return "Book[bookId: %d, bookName: %s]" % (self.bookId, self.bookName)