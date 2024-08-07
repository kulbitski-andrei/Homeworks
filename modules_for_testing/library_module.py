"""LIBRARY MODULE"""

from log_dir import log_setup


class Book:
    """Books in the library are described in this class:
    Title, Author, Pages, ISBN and current status:
    is available, is booked (by whom), is taken (by whom)"""

    def __init__(self, title, author, pages, isbn):
        """When new book is added to the ibrary,
        this method defines such parameters as:
        title, author, pages and isbn."""

        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

        self.status = "Available"
        self.reserved_by = None
        self.taken_by = None


class Reader:
    """Readers that come to the library
    are described in this class.
    They can reserve, take and return books."""

    def __init__(self, name):

        self.name = name
        log_setup.logger.info("В библиотеку записался "
                              "новый читатель: %s", self.name)

    def reserve_book(self, book):
        """Reserving a book to a particular reader
        prevents reserving/taking this book by other reader"""

        if book.status == "Reserved" and book.reserved_by != self.name:
            log_setup.logger.info(
                "Невозможно зарезервировать книгу "
                "'%s' для %s - она уже зарезервирована "
                "другим читателем!", book.title, self.name)
            return False
        if book.status == "Taken":
            log_setup.logger.info(log_setup.logger.info(
                "Невозможно зарезервировать книгу "
                "'%s' для %s - ее уже кто-то читает!",
                book.title, self.name))
            return False
        book.status = "Reserved"
        book.reserved_by = self.name
        log_setup.logger.info(
            "Книга '%s' была зарезервирована читателем %s",
            book.title, self.name)
        return True

    def take_book(self, book):
        """Taking a book by a particular reader
        prevents reserving/taking this book by anyone"""

        if book.status == "Reserved" and book.reserved_by != self.name:
            log_setup.logger.info(
                "Невозможно взять книгу '%s' для %s - "
                "она уже зарезервирована другим читателем!",
                book.title, self.name)

            return False
        if book.status == "Taken":
            log_setup.logger.info(
                "Невозможно взять книгу '%s' для %s - "
                "ее уже взял кто-то другой!",
                book.title, self.name)

            return False

        book.status = "Taken"
        book.taken_by = self.name
        book.reserved_by = None
        log_setup.logger.info(
            "Книга '%s' была взята из библиотеки читателем %s",
            book.title, self.name)

        return True

    def return_book(self, book):
        """Returning a book allows it
        to be reserved/taken by any reader again."""

        if book.taken_by != self.name:
            log_setup.logger.info("Нельзя вернуть то, чего у вас нет!")
            return False
        book.status = "Available"
        book.taken_by = None
        book.reserved_by = None
        log_setup.logger.info("Книга '%s' была возвращена "
                              "в библиотеку", book.title)
        return True


if __name__ == "__main__":
    book_1 = Book("Foundation", "Isaac Asimov", 725, 220180)
    book_2 = Book("Solaris", "Stanislaw Lem", 344, 531240)

    reader_finn = Reader("Finn the Human")
    reader_jake = Reader("Jake the Dog")

    reader_jake.reserve_book(book_1)
    assert not reader_finn.reserve_book(book_1)
    assert not reader_finn.take_book(book_1)

    reader_jake.take_book(book_1)
    assert not reader_finn.reserve_book(book_1)
    assert not reader_finn.take_book(book_1)

    reader_jake.return_book(book_1)
    assert reader_finn.reserve_book(book_1)
    assert reader_finn.take_book(book_1)
