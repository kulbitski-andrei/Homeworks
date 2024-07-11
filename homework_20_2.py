"""Unittest test cases for library_module"""

import unittest
from modules_for_testing import library_module


class ExchangeRatesToBynTesting(unittest.TestCase):
    """User take a book"""

    @classmethod
    def setUpClass(cls):
        cls.book_1 = library_module.Book("Foundation", "Isaac Asimov", 725, 220180)
        cls.book_2 = library_module.Book("Solaris", "Stanislaw Lem", 344, 531240)
        cls.reader_finn = library_module.Reader("Finn the Human")
        cls.reader_jake = library_module.Reader("Jake the Dog")

    def test_user_take_unreserved_book(self):
        """User is able to take a book if it's not reserved and
        not taken by other users"""
        self.assertTrue(self.reader_finn.take_book(self.book_1))



# book_1 = Book("Foundation", "Isaac Asimov", 725, 220180)
# book_2 = Book("Solaris", "Stanislaw Lem", 344, 531240)
#
# reader_finn = Reader("Finn the Human")
# reader_jake = Reader("Jake the Dog")
#
# reader_jake.reserve_book(book_1)
# assert not reader_finn.reserve_book(book_1)
# assert not reader_finn.take_book(book_1)