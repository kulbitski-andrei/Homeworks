"""HOMEWORK 20_2"""

import unittest
import random
import string
from log_dir import log_setup
from modules_for_testing import library_module


def generate_random_book():
    """This function generates a random book title, author name,
     page number and ISBN."""
    rnd_book_title = ''.join(random.choices(string.ascii_letters + ' ', k=20))
    rnd_author_name = ''.join(random.choices(string.ascii_letters + ' ', k=20))
    rnd_page_number = ''.join(random.choices(string.digits, k=3))
    rnd_isbn = ''.join(random.choices(string.digits, k=6))
    return [rnd_book_title, rnd_author_name, rnd_page_number, rnd_isbn]


class UserTakeABook(unittest.TestCase):
    """This class tests scenarios where a user takes a book."""

    @classmethod
    def setUpClass(cls):
        log_setup.logger.info("Setting up the test class %s", cls.__name__)
        cls.book_1 = library_module.Book(*generate_random_book())
        cls.reader_1 = library_module.Reader("Reader_1")
        cls.reader_2 = library_module.Reader("Reader_2")

    def setUp(self):
        log_setup.logger.info("Setting up the test method for %s", self)
        self.book_1.status = "Available"
        self.book_1.taken_by = None
        self.book_1.reserved_by = None

    def test_user_take_unreserved_book(self):
        """This test checks if a user can take a book
        that is not reserved and not taken by other users."""
        log_setup.logger.info("Testing if user can take an unreserved book")
        self.assertTrue(self.reader_1.take_book(self.book_1))
        log_setup.logger.info("Test completed")

    def test_user_takes_book_when_its_already_taken(self):
        """This test checks if a user can take a book
        that is already taken by another user."""
        log_setup.logger.info("Testing if user can't take a book "
                              "that is already taken by another user")
        self.reader_1.take_book(self.book_1)
        self.assertFalse(self.reader_2.take_book(self.book_1))
        log_setup.logger.info("Test completed")

    def test_take_self_reserved_book(self):
        """This test checks if a user can take a book
        that he/she has reserved."""
        log_setup.logger.info("Testing if user can take a book he/she reserved")
        self.reader_2.reserve_book(self.book_1)
        self.assertTrue(self.reader_2.take_book(self.book_1))
        log_setup.logger.info("Test completed")

    def test_take_another_user_reserved_book(self):
        """This test checks if a user can take a book
        that is reserved by another user."""
        log_setup.logger.info("Testing if user can't take a book another user reserved")
        self.reader_1.reserve_book(self.book_1)
        self.assertFalse(self.reader_2.take_book(self.book_1))
        log_setup.logger.info("Test completed")


class UserReturnsABook(unittest.TestCase):
    """This class tests scenarios where a user returns a book."""

    @classmethod
    def setUpClass(cls):
        log_setup.logger.info("Setting up the test class %s", cls.__name__)
        cls.book_2 = library_module.Book(*generate_random_book())
        cls.reader_3 = library_module.Reader("Reader_3")
        cls.reader_4 = library_module.Reader("Reader_4")

    def setUp(self):
        log_setup.logger.info("Setting up the test method for %s", self)
        self.book_2.status = "Available"
        self.book_2.taken_by = None
        self.book_2.reserved_by = None

    def test_user_returns_a_book_he_have(self):
        """This test checks if a user can return a book
        that was previously taken by that user."""
        log_setup.logger.info("Testing if user can take an unreserved book")
        self.reader_3.take_book(self.book_2)
        self.assertTrue(self.reader_3.return_book(self.book_2))
        log_setup.logger.info("Test completed")

    def test_user_returns_a_book_he_doesnt_have(self):
        """This test checks if a user can return a book
        that he/she has not taken."""
        log_setup.logger.info("Testing if user can return book he doesn't have")
        self.assertFalse(self.reader_3.return_book(self.book_2))
        log_setup.logger.info("Test completed")

    def test_user_returns_a_book_taken_by_another_user(self):
        """This test checks if a user can return a book
        that was taken by another user."""
        log_setup.logger.info("Testing if user can return book taken by other user")
        self.reader_4.take_book(self.book_2)
        self.assertFalse(self.reader_3.return_book(self.book_2))
        log_setup.logger.info("Test completed")


class UserReservesABook(unittest.TestCase):
    """This class tests scenarios where a user reserves a book."""

    @classmethod
    def setUpClass(cls):
        log_setup.logger.info("Setting up the test class %s", cls.__name__)
        cls.book_3 = library_module.Book(*generate_random_book())
        cls.reader_5 = library_module.Reader("Reader_5")
        cls.reader_6 = library_module.Reader("Reader_6")

    def setUp(self):
        log_setup.logger.info("Setting up the test method for %s", self)
        self.book_3.status = "Available"
        self.book_3.taken_by = None
        self.book_3.reserved_by = None

    def test_user_reserves_a_book_not_reserved(self):
        """This test checks if a user can reserve a book
        that is not reserved by anyone."""
        log_setup.logger.info("Testing if user can reserve unreserved book")
        self.assertTrue(self.reader_5.reserve_book(self.book_3))
        log_setup.logger.info("Test completed")

    def test_user_reserves_a_book_reserved_by_other_user(self):
        """This test checks if a user can reserve a book
        that is reserved by another user."""
        log_setup.logger.info("Testing if user can't reserve reserved book")
        self.reader_5.reserve_book(self.book_3)
        self.assertFalse(self.reader_6.reserve_book(self.book_3))
        log_setup.logger.info("Test completed")
