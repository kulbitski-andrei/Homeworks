"""HOMEWORK 20_1"""

import unittest
from modules_for_testing import bank_module


class ExchangeRatesToBynTesting(unittest.TestCase):
    """Testing the conversion from every currency to BYN"""

    @classmethod
    def setUpClass(cls):
        """Setting up Test Class: create test bank instance and
        test client instances with EUR and USD currencies"""
        cls.bank_instance = bank_module.Bank("pko_to_byn", 0.15)
        cls.client_1 = bank_module.Client("test_client_1", 100, bank_module.eur)
        cls.client_2 = bank_module.Client("test_client_2", 100, bank_module.usd)

    def test_eur_to_byn_rate(self):
        """EUR to BYN conversion"""
        self.bank_instance.exchange_currency(self.client_1)
        self.assertEqual(self.client_1.money_amount, 400.0)

    def test_usd_to_byn_rate(self):
        """USD to BYN conversion"""
        self.bank_instance.exchange_currency(self.client_2)
        self.assertEqual(self.client_2.money_amount, 300.0)


class ExchangeRatesToEurTesting(unittest.TestCase):
    """Testing the conversion from every currency to EUR"""

    @classmethod
    def setUpClass(cls):
        """Setting up Test Class: create test bank instance and
        test client instances with EUR and USD currencies"""
        cls.bank_instance = bank_module.Bank("bsb_to_eur", 0.15)
        cls.client_3 = bank_module.Client("test_client_2", 100, bank_module.usd)
        cls.client_4 = bank_module.Client("test_client_3", 100, bank_module.byn)

    def test_usd_to_eur_rate(self):
        """USD to EUR conversion"""
        self.bank_instance.exchange_currency(self.client_3, bank_module.eur)
        self.assertEqual(self.client_3.money_amount, 75.0)

    def test_byn_to_eur_rate(self):
        """BYN to EUR conversion"""
        self.bank_instance.exchange_currency(self.client_4, bank_module.eur)
        self.assertEqual(self.client_4.money_amount, 25.0)


class ExchangeRatesToUsdTesting(unittest.TestCase):
    """Testing the conversion from every currency to USD"""

    @classmethod
    def setUpClass(cls):
        """Setting up Test Class: create test bank instance and
        test client instances with EUR and USD currencies"""
        cls.bank_instance = bank_module.Bank("alfa_to_usd", 0.15)
        cls.client_5 = bank_module.Client("test_client_5", 100, bank_module.eur)
        cls.client_6 = bank_module.Client("test_client_6", 100, bank_module.byn)

    def test_usd_to_eur_rate(self):
        """USD to EUR conversion"""
        self.bank_instance.exchange_currency(self.client_5, bank_module.usd)
        self.assertEqual(self.client_5.money_amount, 133.33333333333334)

    def test_byn_to_eur_rate(self):
        """BYN to EUR conversion"""
        self.bank_instance.exchange_currency(self.client_6, bank_module.usd)
        self.assertEqual(self.client_6.money_amount, 33.333333333333336)


class UnexistingCurrency (unittest.TestCase):
    """Testing the conversion to unexisting currency"""
    @classmethod
    def setUpClass(cls):
        cls.bank_instance = bank_module.Bank("neg_test", 0.15)
        cls.client_7 = bank_module.Client("test_client_7", 100, bank_module.byn)

    def test_to_aud(self):
        """Test conversion to the currency that doesn't exist in a system:
        australian dollars (AUD)"""
        with self.assertRaises(AttributeError):
            self.bank_instance.exchange_currency(self.client_7, bank_module.aud)  # pylint: disable=no-member
