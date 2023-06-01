
class Bond():
    def __init__(self, principle, year, interest_rate=15.0):
        self.principle = principle
        self.interest_rate = interest_rate
        self.year = year

    def get_principle():
        enter_principle = input(
            'How much money do you require for your bond?: ')
        float_principle = float(enter_principle)
        return float_principle

    def get_year():
        enter_year = input(
            'Over how many years would you like to repay the bond?: ')
        year_float = float(enter_year)
        return year_float

    def calculate_bond(self):
        self.total_repayments = self.year * 12
        self.total_monthly_interest = self.interest_rate / 100 / 12
        self.total_monthly_payment = (self.total_monthly_interest * self.principle) / (
            1 - ((1 + self.total_monthly_interest) ** (-self.total_repayments)))
        self.total_calculated_payment = self.total_repayments * self.total_monthly_payment

        monthly_payment_formatted = round(self.total_monthly_payment, 2)
        calculated_payment_formatted = round(self.total_calculated_payment, 2)

        return 'Your monthly installment is going to be R{monthly:.2f}. Your bond will be payable over {months}. Total repayment is calculated at R{total:.2f}'.format(
            monthly=monthly_payment_formatted, months=self.total_repayments, total=calculated_payment_formatted)


def main():
    principle = Bond.get_principle()
    year = Bond.get_year()
    my_bond = Bond(principle, year)
    result = my_bond.calculate_bond()
    print(result)


if __name__ == '__main__':
    main()
