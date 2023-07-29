import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 2, 3) == -1

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 8) == 40

    def test_division(self):
        assert self.calc.division(self, 15, 3) == 5

    def teardown(self):
        print("Выполнение метода Teardown")
