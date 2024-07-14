import logging
import unittest
import random
import string
from modules_for_testing import library_module


def generate_random_book():
    """Function generates random book title, author name,
     page number and ISBN"""
    rnd_book_title = ''.join(random.choices(string.ascii_letters + ' ', k=20))
    rnd_author_name = ''.join(random.choices(string.ascii_letters + ' ', k=20))
    rnd_page_number = ''.join(random.choices(string.digits, k=3))
    rnd_isbn = ''.join(random.choices(string.digits, k=6))
    return [rnd_book_title, rnd_author_name, rnd_page_number, rnd_isbn]


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class UserTakeABook(unittest.TestCase):
    """User takes a book"""

    @classmethod
    def setUpClass(cls):
        logger.info(f"Setting up the test class {cls.__name__}")
        cls.book_1 = library_module.Book(*generate_random_book())
        cls.reader_1 = library_module.Reader("Reader_1")
        cls.reader_2 = library_module.Reader("Reader_2")

    def setUp(self):
        logger.info(f"Setting up the test method for {self}")
        self.book_1.status = "Available"
        self.book_1.taken_by = None
        self.book_1.reserved_by = None

    def test_user_take_unreserved_book(self):
        """User is able to take a book if it's not reserved and
        not taken by other users"""
        logger.info("Testing if user can take an unreserved book")
        self.assertTrue(self.reader_1.take_book(self.book_1))
        logger.info("Test completed")

    def test_user_takes_book_when_its_already_taken(self):
        """User is able to take a book if it's not reserved and
        not taken by other users"""
        logger.info("Testing if user can't take a book "
                    "that is already taken by another user")
        self.reader_1.take_book(self.book_1)
        self.assertFalse(self.reader_2.take_book(self.book_1))
        logger.info("Test completed")

    def test_take_self_reserved_book(self):
        """User is able to take a book if it's reserved by him/herself"""
        logger.info("Testing if user can take a book he/she reserved")
        self.reader_2.reserve_book(self.book_1)
        self.assertTrue(self.reader_2.take_book(self.book_1))
        logger.info("Test completed")

    def test_take_another_user_reserved_book(self):
        """User is not able to take a book if it's reserved by
        another user"""
        logger.info("Testing if user can't take a book another user reserved")
        self.reader_1.reserve_book(self.book_1)
        self.assertFalse(self.reader_2.take_book(self.book_1))
        logger.info("Test completed")


class UserReturnsABook(unittest.TestCase):
    """User returns a book"""

    @classmethod
    def setUpClass(cls):
        logger.info(f"Setting up the test class {cls.__name__}")
        cls.book_2 = library_module.Book(*generate_random_book())
        cls.reader_3 = library_module.Reader("Reader_3")
        cls.reader_4 = library_module.Reader("Reader_4")

    def setUp(self):
        logger.info(f"Setting up the test method for {self}")
        self.book_2.status = "Available"
        self.book_2.taken_by = None
        self.book_2.reserved_by = None

    def test_user_returns_a_book_he_have(self):
        """User is able to return a book previously taken by that user"""
        logger.info("Testing if user can take an unreserved book")
        self.reader_3.take_book(self.book_2)
        self.assertTrue(self.reader_3.return_book(self.book_2))
        logger.info("Test completed")

    def test_user_returns_a_book_he_doesnt_have(self):
        """User is not able to return a book that have
        not taken status"""
        logger.info("Testing if user can return book he doesn't have")
        self.assertFalse(self.reader_3.return_book(self.book_2))
        logger.info("Test completed")

    def test_user_returns_a_book_taken_by_another_user(self):
        """User is not able to return a book that was
        taken by other user"""
        logger.info("Testing if user can return book taken by other user")
        self.reader_4.take_book(self.book_2)
        self.assertFalse(self.reader_3.return_book(self.book_2))
        logger.info("Test completed")


class UserReservesABook(unittest.TestCase):
    """User returns a book"""

    @classmethod
    def setUpClass(cls):
        logger.info(f"Setting up the test class {cls.__name__}")
        cls.book_3 = library_module.Book(*generate_random_book())
        cls.reader_5 = library_module.Reader("Reader_5")
        cls.reader_6 = library_module.Reader("Reader_6")

    def setUp(self):
        logger.info(f"Setting up the test method for {self}")
        self.book_3.status = "Available"
        self.book_3.taken_by = None
        self.book_3.reserved_by = None

    def test_user_reserves_a_book_not_reserved(self):
        """User is able to reserve a book
        that is not reserved by anyone"""
        logger.info("Testing if user can reserve unreserved book")
        self.assertTrue(self.reader_5.reserve_book(self.book_3))
        logger.info("Test completed")

    def test_user_reserves_a_book_reserved_by_other_user(self):
        """User is not able to reserve a book
        that is reserved by another user"""
        logger.info("Testing if user can reserve reserved book")
        self.reader_5.reserve_book(self.book_3)
        self.assertFalse(self.reader_6.reserve_book(self.book_3))
        logger.info("Test completed")
