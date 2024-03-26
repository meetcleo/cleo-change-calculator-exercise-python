import unittest

from vending_machine.sources.change_calculator import ChangeCalculator

class ChangeCalculatorTests(unittest.TestCase):
    def test_can_be_instantiated(self):
        change_calculator = ChangeCalculator
        