"""BANK MODULE"""

from decimal import Decimal
import logging

formatter = logging.Formatter(
    '\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# 1. Банковский вклад¶

class Bank:
    """Class bank that allows to create a new bank
    with attribute 'Bank_name'. Contains method 'deposit'
    that allows user to create a deposit of N money for R years."""

    def __init__(self, bank_name, annual_rate):
        self.bank_name = bank_name
        self.annual_rate = annual_rate

    def deposit(self, person, years):
        """Calculates the final amount after the specified number of years
            with monthly interest growth."""

        money = Decimal(str(person.money_amount))
        annual_rate = Decimal(str(self.annual_rate))
        monthly_rate = Decimal(annual_rate / 12)

        if money <= 0:
            raise ValueError

        if years <= 0:
            raise ValueError

        for _month in range(years * 12):
            money = money + Decimal(monthly_rate) * money
            round(money, 2)
        logger.warning("\nЧерез %s лет клиент %s будет "
                       "иметь на счету в банке %s %s",
                       years, person.name, self.bank_name,
                       round(money, 2))
        return round(money, 2)


class Client:
    """Class Client describes a person that can come to bank
     to exchange money or to make a deposit."""

    def __init__(self, name, money_amount):
        self.name = name
        self.money_amount = money_amount

    def go_to_work(self):
        """It's easy. If you want more money - you go to work."""
        self.money_amount += 10


client_socrates = Client("Сократ", 10)
bank_pko = Bank("PKO Bank", 0.15)
print(bank_pko.deposit(client_socrates, 5))
assert bank_pko.deposit(client_socrates, 5) == Decimal("21.07")