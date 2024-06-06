# 1.  Библиотека¶
# Создайте класс book с именем книги, автором, кол-м страниц,
# ISBN, флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь который может брать книгу,
# возвращать, бронировать. Если другой пользователь хочет
# взять зарезервированную книгу
# (или которую уже кто-то читает - надо ему про это сказать).
#
class Book:

    def add_book(self, title, author, pages, isbn):

        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

        self.is_reserved = False
        self.reserved_by = None
        self.is_taken = False
        self.taken_by = None

        print(f"В библиотеку добавлена книга '{self.title}', автор: {self.author}")

    def reserve_book(self):
        pass


class Reader:

    def add_reader(self, name):

        self.name = name
        print(f"В библиотеку записался новый читатель: {self.name}")

    def reserve_book(self, book):

        if book.is_reserved == True and book.reserved_by != self.name:
            print(f"Книга '{book.title}' уже зарезервирована другим читателем!")
            return None
        elif book.is_taken:
            print(f"Книгу '{book.title}' уже кто-то читает!")
            return None
        book.is_reserved = True
        book.reserved_by = self.name

    def take_book(self, book):

        if book.is_reserved == True and book.reserved_by != self.name:
            print(f"Книга '{book.title}' уже зарезервирована другим читателем!")
            return None
        elif book.is_taken:
            print(f"Книгу '{book.title}' уже кто-то читает!")
            return None
        book.is_taken = True
        book.taken_by = self.name
        book.is_reserved = False
        book.reserved_by = None


    def return_book(self, book):

        if book.taken_by != self.name:
            print("1", book.is_taken)
            print("2", self.name)
            print("Нельзя вернуть то, чего у вас нет!")
            return None
        book.is_taken = False
        book.taken_by = None
        book.is_reserved = False
        book.reserved_by = None



book_1 = Book()
book_2 = Book()
book_1.add_book("Foundation", "Isaac Asimov", 725, 220180)
book_2.add_book("Solaris", "Stanislaw Lem", 344, 531240)

reader_finn = Reader()
reader_jake = Reader()
reader_finn.add_reader("Finn the Human")
reader_jake.add_reader("Jake the Dog")

reader_jake.reserve_book(book_1)
print(book_1.is_reserved)
print(book_1.reserved_by)

reader_finn.reserve_book(book_1)
reader_finn.take_book(book_1)

reader_jake.reserve_book(book_1)
reader_jake.take_book(book_1)
print(book_1.is_reserved)
print(book_1.reserved_by)
print(book_1.is_taken)
print(book_1.taken_by)

reader_jake.return_book(book_1)
reader_finn.take_book(book_1)
print(book_1.is_taken)
print(book_1.is_reserved)
print(book_1.taken_by)