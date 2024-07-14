"""BANK MODULE"""

import logging
from decimal import Decimal

formatter = logging.Formatter(
    '\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# 1. Банковский вклад¶


class Currency:
    """Class that describes a currency: its name
    and relative value for exchange calculation."""

    def __init__(self, name, relative_value):
        self.name = name
        self.relative_value = relative_value


byn = Currency("BYN", 1)
usd = Currency("USD", 3)
eur = Currency("EUR", 4)


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

        for _month in range(years * 12):
            money = money + Decimal(monthly_rate) * money
            round(money, 2)
        print(f"Через {years} лет клиент {person.name} будет "
              f"иметь на счету в банке {self.bank_name} "
              f"{round(money, 2)} {person.currency}")
        return round(money, 2)

    def exchange_currency(self, person, to_curr=byn):
        """Use amount of money of cpecific currency that person have
        and exchanges it to the selected currency. Relative price of
        any currency is used to calculate exchange rates."""

        absolute_amount = person.money_amount * person.currency.relative_value
        exchanged_amount = absolute_amount / to_curr.relative_value
        old_data = f"{person.money_amount} {person.currency.name}"
        person.money_amount = exchanged_amount
        person.currency = to_curr.name

        logger.info("Клиент %s обменял %s на %s %s в банке %s",
                    person.name, old_data, exchanged_amount,
                    to_curr.name, self.bank_name)
        return exchanged_amount, to_curr.name


class Client:
    """Class Client describes a person that can come to bank
     to exchange money or to make a deposit."""

    def __init__(self, name, money_amount, currency):
        self.name = name
        self.money_amount = money_amount
        self.currency = currency

    def go_to_work(self):
        """It's easy. If you want more money - you go to work."""
        self.money_amount += 10

# client_socrates = Client("Сократ", 10, eur)
# client_plato = Client("Платон", 5, usd)
# client_aristotle = Client("Аристотель", 15, byn)
#
# bank_bsb = Bank("BelSwissBank", 0.10)
# bank_pko = Bank("PKO Bank", 0.15)
#
# bank_bsb.exchange_currency(client_socrates)
# bank_bsb.exchange_currency(client_plato, eur)
# bank_pko.exchange_currency(client_aristotle, usd)
#
# # TEST CASES
# assert (client_socrates.money_amount == 40.0
#         and client_socrates.currency == "BYN")
# assert (client_plato.money_amount == 3.75
#         and client_plato.currency == "EUR")
# assert (client_aristotle.money_amount == 5
#         and client_aristotle.currency == "USD")
#
# # TEST CASES
# assert bank_pko.deposit(client_socrates, 5) == Decimal("84.29")
