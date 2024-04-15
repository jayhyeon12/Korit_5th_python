from BookEntity import Book
from BookService import BookService

class BookController:

    @classmethod
    def addBookRequest():
        book = Book(bookName = "임시 책", 
                    author = "frec", 
                    publisher = "dream",
                    isbn = "3f36uh5")
        BookService.addBook(book)