import unittest
from ddd.main import Payment


class TestAddClass(unittest.TestCase):
    def setUp(self):
        self.payment_sum = Payment(0, 10000)
        self.payment_incorrect = Payment(0, -10000)
        self.payment_zero = Payment(0, 0)

    def test_add_balance(self):
        self.assertEqual(self.payment_sum.sumer(), 10000, 'Неверный код')

    def test_add_zero_balance(self):
        self.assertEqual(self.payment_zero.sumer(), 0, '0')

    def test_add_incorrect_balance(self):
        self.assertEqual(self.payment_incorrect.sumer(), 'неверная сумма', 'loh')
