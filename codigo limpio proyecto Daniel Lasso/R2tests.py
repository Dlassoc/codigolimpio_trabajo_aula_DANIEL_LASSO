import unittest
from payment_plan import PaymentPlan

class TestPaymentPlan(unittest.TestCase):
    import unittest
from payment_plan import PaymentPlan

class TestPaymentPlan(unittest.TestCase):

    def test_calculate_installment_interest(self):
        # Caso normal
        payment_plan = PaymentPlan(
            card_number="Bancolombia 556677",
            purchase_date="2023-08-04",
            purchase_amount=200000,
            payment_date=None,
            payment_amount=None,
            interest_amount=None,
            capital_amount=None,
            balance=200000,
        )

        monthly_installment, total_interest = payment_plan.calculate_installment_interest(annual_interest_rate=37, num_installments=36)

        # Redondear los valores a la cantidad de decimales necesarios
        monthly_installment = round(monthly_installment, 4)
        total_interest = round(total_interest, 2)

        self.assertAlmostEqual(monthly_installment, 9275.0216, places=4)
        self.assertAlmostEqual(total_interest, 133900.78, places=2)

    def test_savings_plan1(self):
        # Caso normal
        purchase_amount = 200000.00  # Valor de compra
        annual_interest_rate = 0.90  # Tasa de interés anual
        expected_monthly_savings = 6528.817139  # Cuota a ahorrar mensualmente
        num_months_saving = 28  # Número de meses ahorrando

        # Crear una instancia de PaymentPlan
        payment_plan = PaymentPlan(
            card_number=None,
            purchase_date=None,
            purchase_amount=purchase_amount,
            payment_date=None,
            payment_amount=None,
            interest_amount=None,
            capital_amount=None,
            balance=None,
        )

        # Calcular el plan de ahorro programado
        total_savings_needed, monthly_savings = payment_plan.calculate_savings_plan(
            annual_interest_rate, num_months_saving)

        # Verificar si las salidas coinciden con los valores esperados
        self.assertAlmostEqual(monthly_savings, expected_monthly_savings, places=4)

    """def test_suggest_savings_plan(self):
        # Crear una instancia de PaymentPlan con los valores de entrada del R2
        payment_plan = PaymentPlan(
            card_number="Bancolombia 556677",
            purchase_date="2023-08-04",
            purchase_amount=200000,
            payment_date=None,
            payment_amount=None,
            interest_amount=None,
            capital_amount=None,
            balance=200000,
        )

        # Parámetros para el cálculo del plan de ahorro (R3) con tasa de interés del 37%
        annual_interest_rate = 37
        num_installments = 36

        # Calcular y obtener la sugerencia de plan de ahorro
        savings_suggestion = payment_plan.suggest_savings_plan(annual_interest_rate, num_installments)

        # Valores esperados redondeados a 2 decimales
        expected_savings_suggestion = "Para evitar pagar 133900.78 en intereses, le sugerimos ahorrar $3719.47 mensuales y comprar de contado."

        # Verificar si la sugerencia coincide con el valor esperado
        self.assertEqual(savings_suggestion, expected_savings_suggestion)
"""
if __name__ == '__main__':
    unittest.main()
