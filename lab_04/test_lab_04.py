import pytest
from rpn_modules import Converter, Calculator

def test_simple():
    c = Converter()
    calc = Calculator()
    rpn = c.to_rpn("2 + 2")
    assert calc.calculate(rpn) == 4

def test_priority():
    c = Converter()
    calc = Calculator()
    rpn = c.to_rpn("2 + 2 * 2")
    assert calc.calculate(rpn) == 6

def test_lab_example():
    c = Converter()
    calc = Calculator()
    expr = "3 + 4 * 2 / (1 - 5) ^ 2"
    rpn = c.to_rpn(expr)

    expected_rpn = ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+']
    assert rpn == expected_rpn

    assert calc.calculate(rpn) == 3.5