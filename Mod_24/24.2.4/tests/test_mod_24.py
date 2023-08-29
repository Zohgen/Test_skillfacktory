import pytest

from app.calc import Calculator

class TestCalc():
    def setup(self):
        self.calc = Calculator

    def test_adding_success_multiply(self):
        assert self.calc.multiply(self, 5, 8) == 40

    def test_adding_success_division(self):
        assert self.calc.division(self, 36, 6) == 6

    def test_adding_success_subtraction(self):
        assert self.calc.subtraction(self, 13, 6) == 7

    def test_adding_success_adding(self):
        assert self.calc.adding(self, 13, 8) == 21

    def teardown(self):
        print('Выполнение метода teardown')
