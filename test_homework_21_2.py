"""HOMEWORK 21_2"""

import random
import string
import pytest
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


def generate_random_reader_name():
    """This function generates a random name for the library reader"""
    rnd_reader_name = ''.join(random.choices(string.ascii_letters + ' ', k=20))
    return rnd_reader_name


@pytest.fixture(scope="module")
def instances_for_testing():
    """Generating test instances with random parameters"""
    log_setup.logger.info("Generating test instances: "
                          "a random book and two random readers")
    book_1 = library_module.Book(*generate_random_book())
    reader_1 = library_module.Reader(generate_random_reader_name())
    reader_2 = library_module.Reader(generate_random_reader_name())
    return book_1, reader_1, reader_2


@pytest.fixture(scope="function")
def return_book_and_clear_book_status(instances_for_testing):
    """Returning book to the Library.
    Setting book status to Available.
    Setting taken_by and reserved_by to None"""
    yield
    log_setup.logger.info("Returning book to the Library. "
                          "Setting book status to Available. "
                          "Setting taken_by and reserved_by to None")
    instances_for_testing[0].status = "Available"
    instances_for_testing[0].taken_by = None
    instances_for_testing[0].reserved_by = None
    log_setup.logger.info("Book is returned to the library "
                          "and ready for the next test")


def test_user_take_unreserved_book(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can take a book
    that is not reserved and not taken by other users."""
    log_setup.logger.info("Testing if user can take an unreserved book")
    book_1, reader_1, reader_2 = instances_for_testing
    assert reader_1.take_book(book_1)
    log_setup.logger.info("Performed Successfully")


def test_user_takes_book_when_its_already_taken(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can take a book
    that is already taken by another user."""
    log_setup.logger.info("Testing if user can't take a book "
                          "that is already taken by another user")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_1.take_book(book_1)
    assert not reader_2.take_book(book_1)
    log_setup.logger.info("Performed Successfully")


def test_take_self_reserved_book(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can take a book
    that he/she has reserved."""
    log_setup.logger.info("Testing if user can take a book "
                          "he/she reserved")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_1.reserve_book(book_1)
    assert reader_1.take_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_take_another_user_reserved_book(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can take a book
    that is reserved by another user."""
    log_setup.logger.info("Testing if user can't take a book "
                          "another user reserved")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_2.reserve_book(book_1)
    assert not reader_1.take_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_user_returns_a_book_he_have(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can return a book
    that was previously taken by that user."""
    log_setup.logger.info("Testing if user can return a book "
                          "he has taken")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_1.take_book(book_1)
    assert reader_1.return_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_user_returns_a_book_he_doesnt_have(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can return a book
    that he/she has not taken."""
    log_setup.logger.info("Testing if user can return a book "
                          "he doesn't have")
    book_1, reader_1, reader_2 = instances_for_testing
    assert not reader_1.return_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_user_returns_a_book_taken_by_another_user(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can return a book
    that was taken by another user."""
    log_setup.logger.info("Testing if user can return a book "
                          "taken by another user")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_1.take_book(book_1)
    assert not reader_2.return_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_user_reserves_a_book_not_reserved(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can reserve a book
    that is not reserved by anyone."""
    log_setup.logger.info("Testing if user can reserve an unreserved book")
    book_1, reader_1, reader_2 = instances_for_testing
    assert reader_1.reserve_book(book_1)
    log_setup.logger.debug("Performed Successfully")


def test_user_reserves_a_book_reserved_by_other_user(
        instances_for_testing, return_book_and_clear_book_status):
    """This test checks if a user can reserve a book
    that is reserved by another user."""
    log_setup.logger.info("Testing if user can't reserve a book "
                          "reserved by another user")
    book_1, reader_1, reader_2 = instances_for_testing
    reader_1.reserve_book(book_1)
    assert not reader_2.reserve_book(book_1)
    log_setup.logger.debug("Performed Successfully")
