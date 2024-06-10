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
    def deposit(money, years):
        """Calculates the final amount after the specified number of years
            with monthly interest growth."""

        annual_rate = Decimal("0.10")
        monthly_rate = Decimal(annual_rate / 12)

        for _month in range(years * 12):
            money = money + Decimal(monthly_rate) * money
        print(f"Через {years} лет клиент будет "
              f"иметь на счету {round(money, 2)} рублей")
        return round(money, 2)


pko_bank = Bank("PKO")
bsb_bank = Bank("BSB")
assert pko_bank.deposit(1000, 5) == Decimal("1645.31")
assert bsb_bank.deposit(2000, 2) == Decimal("2440.78")
