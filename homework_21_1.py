"""HOMEWORK 21_1"""

import logging
from decimal import Decimal
import pytest
from modules_for_testing import bank_module

formatter = logging.Formatter(
    '\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@pytest.fixture(scope="module")
def bank_instance():
    """Test bank instance"""
    return bank_module.Bank("test_bank_instance_1", 0.10)


@pytest.fixture(scope="module")
def client_1():
    """Test client 1"""
    return bank_module.Client("test_client_1", 100, bank_module.eur)


@pytest.fixture(scope="module")
def client_2():
    """Test client 2"""
    return bank_module.Client("test_client_2", 0, bank_module.byn)


@pytest.fixture(scope="module")
def client_3():
    """Test client 3"""
    return bank_module.Client("test_client_3", 25, bank_module.usd)


@pytest.fixture(scope="module")
def client_4():
    """Test client 4"""
    return bank_module.Client("test_client_4", -100, bank_module.usd)


def test_deposit_with_valid_values(bank_instance, client_1):
    """Positive test for deposit method"""
    result = bank_instance.deposit(client_1, 1)
    assert result == Decimal('110.47')
    logger.info("Test passed")


def test_deposit_with_zero_money(bank_instance, client_2):
    """Deposit method returns correct result when amount of money is zero"""
    with pytest.raises(ValueError):
        result = bank_instance.deposit(client_2, 2)
        logger.info("result: %s", result)
    logger.info("Test passed")


def test_deposit_with_megative_money_amount(bank_instance, client_4):
    """Deposit method returns correct result
    when amount of money is negative"""
    with pytest.raises(ValueError):
        result = bank_instance.deposit(client_4, 2)
        logger.info("result: %s", result)
    logger.info("Test passed")


def test_deposit_with_zero_years(bank_instance, client_3):
    """Deposit method returns correct result when amount of years is zero"""
    with pytest.raises(ValueError):
        result = bank_instance.deposit(client_3, 0)
        logger.info("result: %s", result)
    logger.info("Test passed")


def test_deposit_with_negative_years_amount(bank_instance, client_3):
    """Deposit method returns correct result when amount of years is zero"""
    with pytest.raises(ValueError):
        result = bank_instance.deposit(client_3, -1)
        logger.info("result: %s", result)
    logger.info("Test passed")


def test_float_years_value(bank_instance, client_1):
    """TypeError is raised when amount of years is not integer"""
    with pytest.raises(TypeError):
        result = bank_instance.deposit(client_1, 9.99)
        logger.info("result: %s", result)
    logger.info("Test passed")
