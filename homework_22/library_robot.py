"""LIBRARY MODULE"""

import logging

formatter = logging.Formatter(
    '\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


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

    def reset_status(self):
        """Reset the status of the book to 'Available'
        and clear the reserved_by and taken_by fields."""
        self.status = "Available"
        self.reserved_by = None
        self.taken_by = None


class Reader:
    """Readers that come to the library
    are described in this class.
    They can reserve, take and return books."""

    def __init__(self, name):

        self.name = name
        logger.info("В библиотеку записался "
                    "новый читатель: %s", self.name)

    def reserve_book(self, book):
        """Reserving a book to a particular reader
        prevents reserving/taking this book by other reader"""

        if book.status == "Reserved" and book.reserved_by != self.name:
            logger.info(
                "Невозможно зарезервировать книгу "
                "'%s' для %s - она уже зарезервирована "
                "другим читателем!", book.title, self.name)
            return False
        if book.status == "Taken":
            logger.info(logger.info(
                "Невозможно зарезервировать книгу "
                "'%s' для %s - ее уже кто-то читает!",
                book.title, self.name))
            return False
        book.status = "Reserved"
        book.reserved_by = self.name
        logger.info(
            "Книга '%s' была зарезервирована читателем %s",
            book.title, self.name)
        return True

    def take_book(self, book):
        """Taking a book by a particular reader
        prevents reserving/taking this book by anyone"""

        if book.status == "Reserved" and book.reserved_by != self.name:
            logger.info(
                "Невозможно взять книгу '%s' для %s - "
                "она уже зарезервирована другим читателем!",
                book.title, self.name)
            return False
        if book.status == "Taken":
            logger.info(
                "Невозможно взять книгу '%s' для %s - "
                "ее уже взял кто-то другой!",
                book.title, self.name)
            return False

        book.status = "Taken"
        book.taken_by = self.name
        book.reserved_by = None
        logger.info(
            "Книга '%s' была взята из библиотеки читателем %s",
            book.title, self.name)
        return True

    def return_book(self, book):
        """Returning a book allows it
        to be reserved/taken by any reader again."""

        if book.taken_by != self.name:
            logger.info("Нельзя вернуть то, чего у вас нет!")
            return False
        book.status = "Available"
        book.taken_by = None
        book.reserved_by = None
        logger.info("Книга '%s' была возвращена "
                    "в библиотеку", book.title)
        return True
