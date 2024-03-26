import unittest

from vending_machine.sources.change_calculator import ChangeCalculator

class ChangeCalculatorTests(unittest.TestCase):
    def test_returns_empty_list_when_amount_requested_is_zero(self):
        change_calculator = ChangeCalculator()
        self.assertEqual([], change_calculator.coins_needed(0))

    def test_returns_exactly_one_coin_of_correct_denomination(self):
        change_calculator = ChangeCalculator()
        for denomination in [1, 2, 5, 10, 20, 50, 100, 200]:
            with self.subTest(denomination=denomination):
                self.assertEqual([denomination], change_calculator.coins_needed(denomination))

    def test_combines_coins_to_build_requested_amount(self):
        change_calculator = ChangeCalculator()
        expected_outputs_for_inputs = {
            163: [100, 50, 10, 2, 1],
            37: [20, 10, 5, 2],
            15: [10, 5],
            202: [200, 2],
        }

        for amount, expected_output in expected_outputs_for_inputs.items():
            with self.subTest(amount=amount):
                self.assertEqual(expected_output, change_calculator.coins_needed(amount))
