class PaymentPlan:
    def __init__(self, card_number, purchase_date, purchase_amount, payment_date, payment_amount, interest_amount, capital_amount, balance):
        self.card_number = card_number
        self.purchase_date = purchase_date
        self.purchase_amount = purchase_amount
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.interest_amount = interest_amount
        self.capital_amount = capital_amount
        self.balance = balance

    def calculate_installment_interest(self, annual_interest_rate, num_installments):
        monthly_interest_rate = annual_interest_rate / 12 / 100
        monthly_installment = (self.purchase_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_installments)
        total_interest = (monthly_installment * num_installments) - self.purchase_amount
        return monthly_installment, total_interest

    def calculate_savings_plan(self, annual_interest_rate, num_installments):
            total_interest = self.calculate_installment_interest(annual_interest_rate, num_installments)[1]
            total_savings_needed = total_interest

            # Calcular la cantidad mensual de ahorro requerida
            monthly_savings = total_savings_needed / num_installments

            return total_savings_needed, monthly_savings

    def suggest_savings_plan(self, annual_interest_rate, num_installments):
        total_savings_needed, monthly_savings = self.calculate_savings_plan(annual_interest_rate, num_installments)
        suggestion = f"Para evitar pagar {total_savings_needed:.2f} en intereses, le sugerimos ahorrar ${monthly_savings:.2f} mensuales y comprar de contado."
        return suggestion
