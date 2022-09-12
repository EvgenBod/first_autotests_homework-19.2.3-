import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 5, 4) == 1

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 3, 6) == 9