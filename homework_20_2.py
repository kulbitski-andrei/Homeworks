import logging
import unittest
from modules_for_testing import library_module

# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создаем обработчик файлов
file_handler = logging.FileHandler('library_module.log')
file_handler.setLevel(logging.INFO)

# Создаем обработчик консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создаем формат логирования
formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class UserTakeABook(unittest.TestCase):
    """User take a book"""

    @classmethod
    def setUpClass(cls):
        logger.info("Setting up the test class")
        cls.book_1 = library_module.Book("Foundation", "Isaac Asimov", 725, 220180)
        cls.book_2 = library_module.Book("Solaris", "Stanislaw Lem", 344, 531240)
        cls.reader_finn = library_module.Reader("Finn the Human")
        cls.reader_jake = library_module.Reader("Jake the Dog")

    def test_user_take_unreserved_book(self):
        """User is able to take a book if it's not reserved and
        not taken by other users"""
        logger.info("Testing if user can take an unreserved book")
        self.assertTrue(self.reader_finn.take_book(self.book_1))
        logger.info("Test completed")

    def test_user_takes_book_when_its_already_taken(self):
        """User is able to take a book if it's not reserved and
        not taken by other users"""
        logger.info("Testing if user can't take a book "
                    "that is already taken by another user")
        self.assertFalse(self.reader_jake.take_book(self.book_1))
        logger.info("Test completed")

    # def setUp(self):
    #     self.reader_finn.return_book(self.book_1)
    #     self.reader_jake.return_book(self.book_1)
    #     self.reader_finn.return_book(self.book_2)
    #     self.reader_jake.return_book(self.book_2)

    def test_take_self_reserved_book(self):
        """User is able to take a book if it's reserved by him/herself"""
        self.reader_finn.return_book(self.book_1)
        self.reader_jake.return_book(self.book_1)
        logger.info("Testing if user can take a book he/she reserved")
        self.reader_jake.reserve_book(self.book_1)
        self.assertTrue(self.reader_jake.take_book(self.book_1))
        logger.info("Test completed")

    def test_take_another_user_reserved_book(self):
        """User is not able to take a book if it's reserved by
        another user"""
        self.reader_finn.return_book(self.book_1)
        self.reader_jake.return_book(self.book_1)
        logger.info("Testing if user can't take a book another user reserved")
        self.reader_finn.reserve_book(self.book_1)
        self.assertFalse(self.reader_jake.take_book(self.book_1))
        logger.info("Test completed")
