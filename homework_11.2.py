"""HOMEWORK #11.2"""

from decimal import Decimal

# 1. Банковский вклад¶


class Bank:
    """Class bank that allows to create a new bank
    with attribute 'Bank_name'. Contains method 'deposit'
    that allows user to create a deposit of N money for R years"""

    def __init__(self, bank_name):
        self.bank_name = bank_name

    @staticmethod
    def deposit(client_name, money, years):
        """Calculates the final amount after the specified number of years
            with monthly interest growth."""

        client_name = client_name

        annual_rate = Decimal("0.10")
        monthly_rate = Decimal(annual_rate / 12)

        for month in range(years * 12):
            money = money + Decimal(monthly_rate) * money
        print(f"Через {years} лет клиент {client_name} "
              f"будет иметь на счету {round(money, 2)} рублей")


pko_bank = Bank("PKO")
bsb_bank = Bank("BSB")
pko_bank.deposit("John Doe", 1000, 5)
bsb_bank.deposit("Jane Doe", 2000, 2)
