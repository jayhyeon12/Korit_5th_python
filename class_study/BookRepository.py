import pymysql
import pymysql.cursors

class BookRepository:

    host = ""
    port = 3306
    user = ""
    password = ""
    database = ""

    @classmethod
    def saveBook(cls, book = None):
        connection = pymysql.connect(
            host = cls.host,
            port = cls.port,
            user = cls.user,
            password = cls.password,
            database = cls.database)
        
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            insert into book_tb
            values(0, 
                %s,
                %s,
                %s,
                %s,
                1,
                4,
                "http://test.com/test.png",
                now(),
                now()
            )
        '''
        cursor.execute(sql, (book.bookName, book.author, book.publisher, book.isbn))
        connection.commit()

        pass